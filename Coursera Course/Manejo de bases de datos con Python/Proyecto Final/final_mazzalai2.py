# -*- coding: utf-8 -*-

"""Sistema para escuelas"""

"""Para este proyecto, realizarás un sistema para una escuela. 
Este sistema permite registrar nuevos alumnos, profesores y cursos.
Un alumno es asignado a un curso y un curso puede tener asociado más de un profesor. 
Los profesores tienen un horario que indica cuando están en cada curso.
El horario asociará un curso y un profesor para un día de la semana (Lunes, Martes, Miércoles, Jueves, Viernes, Sábado, Domingo), una hora desde y una hora hasta.
El sistema permitirá exportar los alumnos que pertenecen a un curso, el horario de cada profesor y el horario del curso."""

import csv
import datetime

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Time, Sequence
from sqlalchemy.orm import sessionmaker

from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.sql import exists

Base = declarative_base()

#Verificar si en el modelo que hizo tu compañero, existe una clase mapeada que representa un curso.
class Curso(Base):
    __tablename__ = 'curso'

    id = Column(Integer, Sequence('curso_id_seq'), primary_key=True)
    nombre = Column(String)

    alumno = relationship('Alumno', order_by='Alumno.id', back_populates='curso')
    curso_horario = relationship('Horario', order_by='Horario.hora_desde', back_populates='curso')

    def __repr__(self):
        return "{} {}".format(self.nombre)

#Verificar si en el modelo que hizo tu compañero, existe una clase mapeada que representa un alumno.
class Alumno(Base):
    __tablename__ = 'alumno'

    id = Column(Integer, Sequence('alumno_id_seq'), primary_key=True)
    nombre = Column(String)
    apellido = Column(String)

    #Verificar si hay una relación uno a muchos entre el alumno y el curso.
    curso_id = Column(Integer, ForeignKey('curso.id'))
    curso = relationship('Curso', back_populates='alumno')

    def __repr__(self):
        return "{} {}".format(self.nombre, self.apellido)

#Verificar si en el modelo que hizo tu compañero, existe una clase mapeada que representa un profesor.
class Profesor(Base):
    __tablename__ = 'profesor'

    id = Column(Integer, Sequence('profesor_id_seq'), primary_key=True)
    nombre = Column(String)
    apellido = Column(String)

    profesor_horario = relationship('Horario', order_by='Horario.hora_desde', back_populates='profesor')

    def __repr__(self):
        return "Prof {} {}".format(self.nombre, self.apellido)

#Verificar si en el modelo que hizo tu compañero, existe una clase mapeada que representa un horario.
class Horario(Base):
    __tablename__ = 'horario'
    
    id = Column(Integer, Sequence('horario_id_seq'), primary_key=True)
    dia = Column(Integer)
    hora_desde = Column(Time)
    hora_hasta = Column(Time)

    #Verificar si hay una relación uno a muchos entre el horario y el curso.
    curso_id = Column(Integer, ForeignKey('curso.id'))
    #Verificar si hay una relación uno a muchos entre el horario y el profesor.
    profesor_id = Column(Integer, ForeignKey('profesor.id'))

    #Verificar si hay una relación uno a muchos entre el horario y el curso.
    curso = relationship('Curso', back_populates='curso_horario')
    #Verificar si hay una relación uno a muchos entre el horario y el profesor.
    profesor = relationship('Profesor', back_populates='profesor_horario')

    def __repr__(self):
        return "dia {} de {} a {}".format(self.dia,self.hora_desde,self.hora_hasta)

class CSVCurso(object):
    #Verificar si se exporta correctamente los alumnos asociados a un curso dado.
    def __init__(self, path):
        self.path = path

    def exportar(self, curso):
        alumnos = curso.alumno
        with open(self.path, 'w', newline='') as archivo:
            writer = csv.writer(archivo)
            writer.writerow(['Nombre y Apellido'])
            for alumno in alumnos:
                writer.writerow([alumno])

class CSVCursoHorario(object):
    #Verificar si se exporta correctamente el horario de un curso dado. Por ejemplo, Día de la semana, hora desde, hora hasta, profesor.
    def __init__(self, path):
        self.path = path

    def exportar(self, curso):
        horarios = curso.curso_horario
        with open(self.path, 'w', newline='') as archivo:
            writer = csv.writer(archivo)
            writer.writerow(['dia', 'hora desde', 'hora hasta', 'profesor'])
            for horario in horarios:
                writer.writerow([horario.dia, horario.hora_desde, horario.hora_hasta, horario.profesor])

class CSVProfesorHorario(object):
    #Verificar si se exporta correctamente el horario de un profesor dado. Por ejemplo, Día de la semana, hora desde, hora hasta, curso.
    def __init__(self, path):
        self.path = path

    def exportar(self, profesor):
        horarios = profesor.profesor_horario
        with open(self.path, 'w', newline='') as archivo:
            writer = csv.writer(archivo)
            writer.writerow(['dia', 'hora desde', 'hora hasta', 'curso'])
            for horario in horarios:
                writer.writerow([horario.dia, horario.hora_desde, horario.hora_hasta, horario.curso.nombre])

def main(*args, **kwargs):
    engine = create_engine('sqlite:///:memory:')
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    curso3a = Curso(nombre='3A')
    curso3b = Curso(nombre='3B')

    alumno1 = Alumno(nombre='Alan', apellido='Mazzalai', curso=curso3a)
    alumno2 = Alumno(nombre='Bruno', apellido='Gonzalez', curso=curso3b)
    alumno3 = Alumno(nombre='Cinthia', apellido='Pardos', curso=curso3a)
    alumno4 = Alumno(nombre='Matias', apellido='Dominguez', curso=curso3a)

    profesor1 = Profesor(nombre='Albert', apellido='Einstein')
    profesor2 = Profesor(nombre='Friedrich', apellido='Nietzsche')

    horario1 = datetime.time(8, 0, 0)
    horario2 = datetime.time(10, 0, 0)
    horario3 = datetime.time(12, 0, 0)

    horario3ap1 = Horario(dia=1, hora_desde=horario1, hora_hasta=horario2, curso=curso3a, profesor=profesor1)
    horario3ap2 = Horario(dia=1, hora_desde=horario2, hora_hasta=horario3, curso=curso3a, profesor=profesor2)
    horario3bp2 = Horario(dia=1, hora_desde=horario1, hora_hasta=horario2, curso=curso3b, profesor=profesor2)
    horario3bp1 = Horario(dia=1, hora_desde=horario2, hora_hasta=horario3, curso=curso3b, profesor=profesor1)
    
    session.add(curso3a)
    session.add(curso3b)

    session.add(alumno1)
    session.add(alumno2)
    session.add(alumno3)
    session.add(alumno4)

    session.add(profesor1)
    session.add(profesor2)

    session.add(horario3ap1)
    session.add(horario3ap2)
    session.add(horario3bp2)
    session.add(horario3bp1)

    session.commit()

    ruta_archivo = 'C:\\Users\\Alan\\Dropbox\\Alan\\Programacion\\Curso_Python\\Manejo de bases de datos con Python\\Proyecto Final\\'

    CSVCurso(ruta_archivo+'Alumnos_Curso_{}.csv'.format(curso3a.nombre)).exportar(curso3a)
    CSVCurso(ruta_archivo+'Alumnos_Curso_{}.csv'.format(curso3b.nombre)).exportar(curso3b)

    CSVCursoHorario(ruta_archivo+'Horario_Curso_{}.csv'.format(curso3a.nombre)).exportar(curso3a)
    CSVCursoHorario(ruta_archivo+'Horario_Curso_{}.csv'.format(curso3b.nombre)).exportar(curso3b)

    CSVProfesorHorario(ruta_archivo+'Horario_Profesor_{}.csv'.format(profesor1)).exportar(profesor1)
    CSVProfesorHorario(ruta_archivo+'Horario_Profesor_{}.csv'.format(profesor2)).exportar(profesor2)

if __name__ == "__main__":
    main()