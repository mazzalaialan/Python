from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column,Integer,String,Sequence
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import aliased
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy import Table,Text,Time
import csv

Base = declarative_base()

class Alumno(Base):
    __tablename__ = 'alumnos'

    id = Column(Integer,Sequence('alumno_id_seq'),primary_key=True)
    nombre = Column(String)
    apellido = Column(String)
    curso_id = Column(Integer,ForeignKey('curso.id'))

    curso = relationship("Curso",back_populates="alumnos")

    def __repr__(self):
        return "{} {} {}".format(self.nombre,self.apellido,self.curso_id)

class Profesor(Base):
    __tablename__ = 'profesores'

    id = Column(Integer,Sequence('profesor_id_seq'),primary_key=True)
    nombre = Column(String)
    apellido = Column(String)
    
    horarios_profesores = relationship("Horario",back_populates="profesor")

    def __repr__(self):
        return "{} {}".format(self.nombre,self.apellido)

class Curso(Base):
    __tablename__ = 'curso'

    id = Column(Integer,Sequence('curso_id_seq'),primary_key=True)
    nombre = Column(String)

    alumnos = relationship("Alumno",back_populates="curso")
    horarios_cursos = relationship("Horario",back_populates="curso")

    def __repr__(self):
        return "{}".format(self.nombre)

class Horario(Base):
    __tablename__ = 'horarios'
    
    id = Column(Integer,Sequence('horario_id_seq'),primary_key=True)
    hora_in = Column(String)
    hora_out = Column(String)
    dia = Column(String)
    curso_id = Column(Integer,ForeignKey('curso.id'))
    profesor_id = Column(Integer,ForeignKey('profesores.id'))
    
    curso = relationship("Curso",back_populates="horarios_cursos")
    profesor = relationship("Profesor",back_populates="horarios_profesores")

    def __repr__(self):
        return "{} {} {} {} {}".format(self.hora_in,self.hora_out,self.dia,self.curso_id,self.profesor_id)


engine = create_engine('sqlite:///:memory:')

Session = sessionmaker(bind=engine)

session = Session()

Base.metadata.create_all(engine)

#REGISTROS DE PRUEBA

alumno1 = Alumno(nombre='Lucia',apellido='Palomeque',curso_id=2)
alumno2 = Alumno(nombre='Julian',apellido='Viejo',curso_id=1)
alumno3 = Alumno(nombre='Lorenzo',apellido='Marinucci',curso_id=2)
alumno4 = Alumno(nombre='Blas',apellido='Sosa',curso_id=3)
alumno5 = Alumno(nombre='Martin',apellido='Motte',curso_id=4)

profesor1 = Profesor(nombre='Sandra',apellido='Cirimelo')
profesor2 = Profesor(nombre='Leonel',apellido='Guccione')
profesor3 = Profesor(nombre='Guillermo',apellido='Lazurri')
profesor4 = Profesor(nombre='Ivonne',apellido='Gellon')

curso1 = Curso(nombre='Programacion 3')
curso2 = Curso(nombre='Programacion 2')
curso3 = Curso(nombre='Taller de Programacion')
curso4 = Curso(nombre='Programacion 1')
curso5 = Curso(nombre='Computacion')
curso6 = Curso(nombre='Modelos')
curso7 = Curso(nombre='Arquitectura')

horario1 = Horario(hora_in='11:00:00',hora_out='13:00:00',dia='Lunes',curso_id=3,profesor_id=2)
horario2 = Horario(hora_in='17:00:00',hora_out='19:00:00',dia='Miercoles',curso_id=2,profesor_id=1)
horario3 = Horario(hora_in='10:00:00',hora_out='12:00:00',dia='Martes',curso_id=3,profesor_id=4)
horario4 = Horario(hora_in='08:00:00',hora_out='10:00:00',dia='Viernes',curso_id=1,profesor_id=3)
horario5 = Horario(hora_in='10:00:00',hora_out='12:00:00',dia='Lunes',curso_id=3,profesor_id=3)

session.add(alumno1)
session.add(alumno2)
session.add(alumno3)
session.add(alumno4)
session.add(alumno5)

session.add(profesor1)
session.add(profesor2)
session.add(profesor3)
session.add(profesor4)

session.add(curso1)
session.add(curso2)
session.add(curso3)
session.add(curso4)
session.add(curso5)
session.add(curso6)
session.add(curso7)

session.add(horario1)
session.add(horario2)
session.add(horario3)
session.add(horario4)
session.add(horario5)

file1 = open("alumnos_curso.csv",'w')

curso_consulta = 3 #modificar parametro en base al curso a consultar

for alumno in session.query(Alumno).filter(Alumno.curso_id==curso_consulta).all(): 
    row = [alumno.nombre,alumno.apellido]
    csv.writer(file1).writerow(row)

for horario,profesor in session.query(Horario,Profesor).filter(Horario.curso_id == curso_consulta).filter(Profesor.id == Horario.profesor_id).all():
    row = [horario.hora_in,horario.hora_out,horario.dia,profesor.nombre,profesor.apellido]
    csv.writer(file1).writerow(row)

for horario in session.query(Horario).filter(Horario.curso_id == curso_consulta).all():
    row = [horario.hora_in,horario.hora_out,horario.dia]
    csv.writer(file1).writerow(row)

file1.close