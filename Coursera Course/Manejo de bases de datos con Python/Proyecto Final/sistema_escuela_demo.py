
# -*- coding: utf-8 -*-

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Sequence
from sqlalchemy.orm import sessionmaker

from sqlalchemy import ForeignKey
from sqlalchemy import UniqueConstraint
from sqlalchemy.orm import relationship

from sqlalchemy import Table, Text

engine = create_engine('sqlite:///:memory:')
Base = declarative_base()
    

# Association table
alumno_cursos = Table('alumno_cursos', Base.metadata,
    Column('alumno_id', ForeignKey('alumno.id'), primary_key=True),
    Column('curso_id', ForeignKey('curso.id'), primary_key=True)
)


class Alumno(Base):
    __tablename__ = 'alumno'

    id = Column(Integer, Sequence('alumno_id_seq'), primary_key=True)
    nombres = Column(String)
    apellidos = Column(String)
    genero = Column(String)
    edad = Column(Integer)

    cursos = relationship("Curso", 
                        secondary=alumno_cursos,
                        back_populates="alumnos")

    def __repr__(self):
        return "{} {}".format(self.nombres, self.apellidos)


class Curso(Base):
    __tablename__ = 'curso'
    id = Column(Integer, Sequence('curso_id_seq'), primary_key=True)
    nombre = Column(String)
    totalcreditos = Column(Integer)

    horarioscursoprofesor = relationship("HorarioCursoProfesor", back_populates="cursos")
    alumnos = relationship("Alumno", 
                        secondary=alumno_cursos,
                        back_populates="cursos")

    def __repr__(self):
        return "{}".format(self.nombre)


class Profesor(Base):
    __tablename__ = 'profesor'
    id = Column(Integer, Sequence('profesor_id_seq'), primary_key=True)
    nombres = Column(String)
    apellidos = Column(String)
    genero = Column(String)
    edad = Column(Integer)

    horarioscursoprofesor = relationship("HorarioCursoProfesor", back_populates="profesores")

    def __repr__(self):
        return "{} {}".format(self.nombres, self.apellidos)


class Horario(Base):
    __tablename__ = 'horario'
    id = Column(Integer, Sequence('horario_id_seq'), primary_key=True)
    dia = Column(String)
    horadesde = Column(String)
    horahasta = Column(String)

    horarioscursoprofesor = relationship("HorarioCursoProfesor", back_populates="horarios")

    def __repr__(self):
        return "{} {} {}".format(self.dia, self.horadesde, self.horahasta)


class HorarioCursoProfesor(Base):
    __tablename__ = 'horariocursoprofesor'
    __table_args__ = (UniqueConstraint('curso_id', 'profesor_id', name='unique_cursoprofesor'),)

    id = Column(Integer, Sequence('horariocursoprofesor_id_seq'), primary_key=True)
    curso_id = Column(Integer, ForeignKey('curso.id'))
    profesor_id = Column(Integer, ForeignKey('profesor.id'))
    horario_id = Column(Integer, ForeignKey('horario.id'))
    
    profesores = relationship("Profesor", back_populates="horarioscursoprofesor")
    cursos = relationship("Curso", back_populates="horarioscursoprofesor")
    horarios = relationship("Horario", back_populates="horarioscursoprofesor")

    def __repr__(self):
        return "{} {} {}".format(self.curso_id, self.profesor_id, self.horario_id)


Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

# Registrar Cursos
cur1 = Curso(nombre='BIOLOGÍA', totalcreditos=3)
cur2 = Curso(nombre='MATEMÁTICA FINANCIERA', totalcreditos=4)
cur3 = Curso(nombre='GESTIÓN DEL TALENTO HUMANO', totalcreditos=3)
cur4 = Curso(nombre='ECONOMÍA', totalcreditos=5)
cur5 = Curso(nombre='COMUNICACIÓN 1', totalcreditos=5)

session.add_all([cur1, cur2, cur3, cur4, cur5])


# Registrar Alumnos
alu1 = Alumno(nombres='Roxana', apellidos='Cochachi Cuentas', genero='F', edad=30)
alu2 = Alumno(nombres='Emiliano José', apellidos='Tapia Ruiz', genero='M', edad=19)
alu3 = Alumno(nombres='Gonzalo', apellidos='Olivos Prado', genero='F', edad=27)
alu4 = Alumno(nombres='Cecilia Giovanna', apellidos='Puertas Leon', genero='M', edad=22)


# Asociar un curso por alumno
alu1.cursos.append(cur1)
alu2.cursos.append(cur4)
alu3.cursos.append(cur5)
alu4.cursos.append(cur2)

session.add_all([alu1, alu2, alu3, alu4])


# Registrar Profesores
prof1 = Profesor(nombres='Fernanda', apellidos='Melina Diaz', genero='F', edad=40)
prof2 = Profesor(nombres='Carlos', apellidos='Lore de Mola', genero='M', edad=29)
prof3 = Profesor(nombres='Maria Alejandra', apellidos='Perez Cuellar', genero='F', edad=38)
prof4 = Profesor(nombres='Nestor', apellidos='Sertzen Matheus', genero='M', edad=42)

session.add_all([prof1, prof2, prof3, prof4])


# Registrar Horarios base
hor1 = Horario(dia='Lunes', horadesde='08:00', horahasta='12:00')
hor2 = Horario(dia='Martes', horadesde='08:00', horahasta='12:00')
hor3 = Horario(dia='Miercoles', horadesde='08:00', horahasta='12:00')
hor4 = Horario(dia='Jueves', horadesde='08:00', horahasta='12:00')
hor5 = Horario(dia='Viernes', horadesde='08:00', horahasta='12:00')

session.add_all([hor1, hor2, hor3, hor4, hor5])
session.flush()


#Asociar curso según horario de profesores
asign1 = [HorarioCursoProfesor(curso_id=cur2.id, horario_id=hor1.id, profesor_id=prof2.id),
       HorarioCursoProfesor(curso_id=cur2.id, horario_id=hor2.id, profesor_id=prof4.id),
       HorarioCursoProfesor(curso_id=cur1.id, horario_id=hor3.id, profesor_id=prof3.id)
       ]
        

session.add_all(asign1)


# Confirmar los cambios en base de datos
session.commit()

# Listar todos los alumnos
print(''.rjust(60,'-'))
print("Listado de Alumnos")
print(''.rjust(60,'-'))

for instance in session.query(Alumno).order_by(Alumno.id):
    print(instance.id, instance.nombres, instance.apellidos)

# Listar todos los cursos
print('')
print(''.rjust(60,'-'))
print("Listado de Cursos disponibles")
print(''.rjust(60,'-'))
for instance in session.query(Curso).order_by(Curso.id):
    print(instance.id, instance.nombre, instance.totalcreditos)

# Listar todos los profesores
print('')
print(''.rjust(60,'-'))
print("Listado de Profesores")
print(''.rjust(60,'-'))
for instance in session.query(Profesor).order_by(Profesor.id):
    print(instance.id, instance.nombres, instance.apellidos)


# Exportar los alumnos que pertenecen a un curso
print('')
print(''.rjust(60,'-'))
print("Reporte de alumnos que pertenecen a un determinado curso")
print(''.rjust(60,'-'))

for instance in session.query(Alumno).order_by(Alumno.id):
    print(instance.id, instance.nombres, instance.apellidos, instance.cursos)


# Exportar el horario de cada profesor
print('')
print(''.rjust(60,'-'))
print("Reporte de Horarios de cada profesor")
print(''.rjust(60,'-'))

for instance in session.query(HorarioCursoProfesor.id, Profesor.nombres, Profesor.apellidos, Horario.dia, Horario.horadesde, Horario.horahasta).\
        filter(Profesor.id == HorarioCursoProfesor.profesor_id).\
        filter(HorarioCursoProfesor.horario_id == Horario.id).\
        all():
    print(instance.id, instance.nombres, instance.apellidos, instance.dia, instance.horadesde, instance.horahasta)


# Exportar el horario de cada curso
print('')
print(''.rjust(60,'-'))
print("Reporte de Horarios de cada curso")
print(''.rjust(60,'-'))
for instance in session.query(HorarioCursoProfesor.id, Curso.nombre, Horario.dia, Horario.horadesde, Horario.horahasta).\
        filter(Curso.id == HorarioCursoProfesor.curso_id).\
        filter(HorarioCursoProfesor.horario_id == Horario.id).\
        all():
    print(instance.id, instance.nombre, instance.dia, instance.horadesde, instance.horahasta)

