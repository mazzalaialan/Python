from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Sequence, ForeignKey
from sqlalchemy.orm import sessionmaker

from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.sql import exists

engine = create_engine('sqlite:///:memory:') #La creo en memoria pero también se podría ingresar la ruta a un archivo .sql

Base = declarative_base()

#Creo la clase Profesor, la cuál es hija de la clase Curso. Ya que, según la consigna, un curso puede tener varios profesores.
class Profesor(Base):

    __tablename__ = 'profesor'

    id = Column(Integer, Sequence('profesor_id_seq'), primary_key=True)
    nombre = Column(String)
    apellido = Column(String)
    horario = Column(String) #Le asigno un horario a cada profesor (entendí según la consigna que cada profesor tiene su horario).
    curso_id = Column(Integer, ForeignKey('curso.id'))

    curso = relationship("Curso", back_populates="profesores") #Creo la relación con la clase Curso
                          
    def __repr__(self):
        return "{} {}".format(self.nombre, self.apellido)

#Creo la clase curso, la cuál es padre de la clase Profesor.
class Curso(Base):

    __tablename__ = 'curso'

    id = Column(Integer, Sequence('curso_id_seq'), primary_key=True)
    nombre = Column(String)
    descripcion = Column(String)
    dia = Column(String)

    profesores = relationship("Profesor", order_by="Profesor.id", back_populates='curso',
                            cascade="all, delete, delete-orphan") #Creo la relación con la clase Profesor

    alumnos = relationship("Alumno", order_by="Alumno.id", back_populates='curso',
                            cascade="all, delete, delete-orphan") #Creo la relación con la clase Alumno

    def __repr__(self):
        return "{}".format(self.nombre)

#Creo la clase alumno, la cuál es hija de la clase Curso, ya que un curso puede tener muchos alumnos.
class Alumno(Base):

    __tablename__ = 'alumno'

    id=Column(Integer, Sequence('alumno_id_seq'), primary_key=True)
    nombre = Column(String)
    apellido = Column(String)
    curso_id = Column(Integer, ForeignKey('curso.id'))

    curso = relationship("Curso", back_populates="alumnos") #Creo la relación con la clase Curso

    def __repr__(self):
        return "{} {}".format(self.nombre, self.apellido)

    

Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)

session = Session()

curso_matematica = Curso(nombre='Matemática',
                         descripcion='Curso de Matemática',
                         dia='Jueves') #Creo el curso llamado curso_matemática.

curso_matematica.profesores = [Profesor(nombre='Juan',
                                        apellido='Fernandez',
                                        horario='11 a 13'),
                               Profesor(nombre='Ignacio',
                                        apellido='Martinez',
                                        horario='10 a 12')] #Le asigno dos profesores a dicho curso

curso_matematica.alumnos = [Alumno(nombre='Martin',
                                   apellido='Garcia'),
                            Alumno(nombre='Pablo',
                                   apellido='Gonzalez')] #Le asigno dos alumnos a dicho curso


session.add(curso_matematica)
session.commit()

#Imprimo tanto los alumnos como los profesores de cada curso, que están guardados en una lista. Obviamente esto se podría imprimir de distintas maneras
#(por ejemplo con un ciclo for para mostrar todo de una, o también se podrían imprimir los horarios de cada profesor).
print(curso_matematica.profesores[0], curso_matematica.profesores[1]) 
print(curso_matematica.alumnos[0], curso_matematica.alumnos[1])

#Nota: Hice el proyecto según como interpreté la consigna y logicamente basándome en los videos del curso. La verdad creo que la consigna no es muy específica.




