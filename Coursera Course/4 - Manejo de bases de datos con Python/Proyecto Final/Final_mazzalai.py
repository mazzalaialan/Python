# -*- coding: utf-8 -*-

"""Sistema para escuelas"""

"""Para este proyecto, realizarás un sistema para una escuela. 
Este sistema permite registrar nuevos alumnos, profesores y cursos.
Un alumno es asignado a un curso y un curso puede tener asociado más de un profesor. 
Los profesores tienen un horario que indica cuando están en cada curso.
El horario asociará un curso y un profesor para un día de la semana (Lunes, Martes, Miércoles, Jueves, Viernes, Sábado, Domingo), una hora desde y una hora hasta.
El sistema permitirá exportar los alumnos que pertenecen a un curso, el horario de cada profesor y el horario del curso."""

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Sequence, ForeignKey, Table, Text
from sqlalchemy.orm import sessionmaker,relationship

import unittest

engine = create_engine('sqlite:///:memory:')

Base = declarative_base()

#associate table
horario = Table('horario',Base.metadata,
    Column('id_profesor', ForeignKey('profesor.id'),primary_key=True),
    Column('id_curso', ForeignKey('curso.id'),primary_key=True)
)

class Curso(Base):
    __tablename__ = 'curso'

    id = Column(Integer, Sequence('id_curso_seq'), primary_key=True)
    curso = Column(Integer)
    division = Column(String)
    
    alumno = relationship("Alumno", order_by="Alumno.id", back_populates="curso", cascade="all, delete, delete-orphan")
    #horario = relationship("Horario", order_by="Horario.id", back_populates="curso", cascade="all, delete, delete-orphan")
    horarios = relationship('Profesor',secondary=horario,back_populates='horarios')

    def __repr__(self):
        return "{} {}".format(self.curso,self.division)

class Alumno(Base):
    __tablename__ = 'alumno'

    id = Column(Integer, Sequence('id_alumno_seq'), primary_key=True)
    nombre = Column(String)
    apellido = Column(String)
    dni = Column(Integer)
    id_curso = Column(Integer, ForeignKey('curso.id'))

    curso = relationship("Curso",back_populates="alumno")

    def __repr__(self):
        return "{} {} DNI {}".format(self.nombre,self.apellido,self.dni)

class Profesor(Base):
    __tablename__ = 'profesor'

    id = Column(Integer, Sequence('id_profesor_seq'), primary_key=True)
    nombre = Column(String)
    apellido = Column(String)
    dni = Column(Integer)

    #horario = relationship("Horario", order_by="Horario.id", back_populates="profesor", cascade="all, delete, delete-orphan")
    horarios = relationship('Curso',secondary=horario,back_populates='horarios')

    def __repr__(self):
        return "{} {} DNI {}".format(self.nombre,self.apellido,self.dni)


class Horario(Base):
    __tablename__ = 'horario'

    id = Column(Integer, Sequence('id_curso_seq'), primary_key=True)
    dia = Column(String)
    hora_desde = Column(Integer)
    hora_hasta = Column(Integer)    
    id_curso = Column(Integer, ForeignKey('curso.id'))
    curso = relationship("Curso",back_populates="horario")
    id_profesor = Column(Integer, ForeignKey('profesor.id'))
    profesor = relationship("Profesor",back_populates="horario")

    def __repr__(self):
        return "{} de {} a {}".format(self.dia,self.hora_desde,self.hora_hasta)


Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)

session = Session()

curso1a = Curso(curso=3, division='A')
print(curso1a)

curso1a.alumno = [Alumno(nombre='Alan', apellido='Mazzalai', dni=33234124),
                   Alumno(nombre='Cinthia', apellido='Pardo', dni=35023212),
                   Alumno(nombre='Matias', apellido='Dominguez', dni=32742347),
                   Alumno(nombre='Bruno', apellido='Gonzalez', dni=33169545)]

session.add(curso1a)
session.commit()
print(curso1a.alumno)

profesor1 = Profesor(nombre='Albert',apellido='Einstein',dni=15235745)

horario11a = [Horario(dia='Lunes',hora_desde=9,hora_hasta=12)]

profesor1.horarios = 

    curso1a.horarios.


#profesor1.horario = [Horario(dia='Lunes',hora_desde=9,hora_hasta=12)]
#print(profesor1)
#print(profesor1.horario)

#curso1a.horario = profesor1.horario

#print(curso1a)
#print(curso1a.horario)


#print('pre Cant Cursos',session.query(Author).filter_by().count())
#print('pre Cant Alumnnos',session.query(Book).filter().count())