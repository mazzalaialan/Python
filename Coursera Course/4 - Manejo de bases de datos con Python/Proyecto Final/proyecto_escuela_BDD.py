#proyecto final - BDD en Python - Fritz, Mariano

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Sequence, ForeignKey, Table, Text
from sqlalchemy.orm import sessionmaker, relationship

#para exportar los datos
import csv

engine = create_engine("sqlite:///:memory:")
Base = declarative_base()

class CursoNoExisteException(Exception):
    pass

class CursoRepetidoException(Exception):
    pass

class OperacionCanceladaException(Exception):
    pass

def cargar_un_curso(s, a, d, cantidad_alumnos=5, cantidad_profes=4):
    un_curso = Curso(anyo=a, division=d)
    
    #cargo los alumnos
    for i in range(cantidad_alumnos):
        un_alumno = Alumno(nombre=f"nombre{i}", apellido=f"apellido{i}")
        un_curso.alumnos.append(un_alumno)
          
    s.add(un_curso)
  
    #cargo los profes
    for i in range(cantidad_profes):
        un_profe = Profesor(nombre=f"{a}{d}_nombre{i}", apellido=f"apellido{i}")
      
        un_horario = Horario(curso_id=un_curso.id, profesor_id=un_profe.id, dia="Lunes", desde=f"hora{i}", hasta=f"hora{i+1}")
        un_profe.cursos.append(un_horario)
        un_curso.profesores.append(un_horario)
        
        s.add(un_profe)


def cargar_datos_ejemplo(s):
    
    for i in range(1,3):
        cargar_un_curso(s, str(i), "a")
        cargar_un_curso(s, str(i), "b")
                
    
class Alumno(Base):
    __tablename__ = 'alumno'
    id = Column(Integer, Sequence('alumno_id_seq'), primary_key=True)
    nombre  = Column(String)
    apellido = Column(String)
    curso_id = Column(Integer, ForeignKey('curso.id'))

    #la relación entre el alumno y el curso
    curso = relationship('Curso', back_populates='alumnos')

    def __repr__(self):
        return f"Estudiante {self.nombre} {self.apellido}"

    def campos_valores(self):
        return ["id","apellido","nombre"],[self.id, self.apellido, self.nombre]


class Profesor(Base):
    __tablename__ = 'profesor'
    id = Column(Integer, Sequence('profesor_id_seq'), primary_key=True)
    nombre  = Column(String)
    apellido = Column(String)

    #la relación muchos a muchos entre profesor - horario - curso
    cursos = relationship('Horario', backref='profesores')
    
    def __repr__(self):
        return f"Prof. {self.nombre} {self.apellido}"

    def campos_valores(self):
        return ["id","apellido","nombre"],[self.id, self.apellido, self.nombre]


class Curso(Base):
    __tablename__ = 'curso'
    id = Column(Integer, Sequence('curso_id_seq'), primary_key=True)
    anyo  = Column(String)
    division = Column(String)

    #la relación muchos a muchos entre curso - horario - profesor
    profesores = relationship('Horario', backref='cursos')
    
    #la relación entre el curso y el alumno
    alumnos = relationship('Alumno', back_populates='curso')
    
    def __repr__(self):
        return f"Curso: {self.anyo} {self.division}"

    def campos_valores(self):
        return ["id","anyo","division"],[self.id, self.anyo, self.division]


#No se usa una tabla secundaria (secondary) sino que se la reemplaza con nueva clase Horario
class Horario(Base):
    __tablename__ = 'horario'
    id = Column(Integer, Sequence('horario_id_seq'), primary_key=True)
    profesor_id = Column(Integer, ForeignKey('profesor.id'))
    curso_id = Column(Integer, ForeignKey('curso.id'))
    dia = Column(String)
    desde = Column(String)
    hasta = Column(String)

    def __repr__(self):
        return f"Horario: {self.dia} de {self.desde} a {self.hasta}"


def preguntar_sino(m):
    opt = input(m).lower()

    while opt not in ["s","n","si", "no"]:
        opt = input(m).lower()

    return opt in ["s", "si"]


def pedir_datos():
    print("Ingrese los datos: ")
    nombre = input("Nombre: ")    
    apellido = input("Apellido: ")

    return nombre,apellido


def pedir_profesor():
    return pedir_datos()


def pedir_horario():
    print("Ingrese los datos del horario: ")
    dia = input("Dia de la semana: ")
    desde = input("Hora de inicio: ")
    hasta = input("hora de fin: ")

    return Horario(dia=dia, desde=desde, hasta=hasta)


def seleccionar_horario():
    print("Generar un horario para el profesor")
    
    horario = pedir_horario()
    
    return horario


def nuevo_profesor(s):
    print("Nuevo profesor---")
    nombre, apellido = pedir_datos()

    nuevo = Profesor(nombre=nombre, apellido=apellido)
    
    #elijo un curso y un horario
    curso = seleccionar_curso(s, True)
    horario = seleccionar_horario()
   
    #añado las relaciones
    nuevo.cursos.append(horario)
    curso.profesores.append(horario)

    return nuevo


def pedir_alumno():
    return pedir_datos()


def nuevo_alumno(s):
    print("Nuevo alumno---")
    nombre, apellido = pedir_alumno()

    nuevo = Alumno(nombre=nombre, apellido=apellido)
    nuevo.curso = seleccionar_curso(s, True) 

    return nuevo 


def pedir_curso():
    print("Ingrese los datos del curso: ")
    anyo = input("Año: ")
    divis = input("Division:")

    return (anyo, divis)


def seleccionar_curso(s, puede_crear=False):
    print("Seleccionar curso")
    anyo, divis = pedir_curso()

    curso = None

    try:
        curso = s.query(Curso).filter(Curso.anyo==anyo).filter(Curso.division==divis).one()
    
    except Exception:
        if puede_crear:
            rta = preguntar_sino("El curso no existe. ¿Desea crearlo? (s/n)")
            if rta:
                curso = Curso(anyo=anyo, division=divis)
            else:
                raise OperacionCanceladaException("Operación cancelada por el usuario")
        else:
            raise CursoNoExisteException(f"No existe el curso {anyo} {divis}")
    
    return curso
    
        
def nuevo_curso(s):
    print("Nuevo curso---")
    anyo, divis = pedir_curso()
    
    if s.query(Curso).filter(Curso.anyo==anyo).filter(Curso.division==divis).count()==0:
        nuevo = Curso(anyo=anyo, division=divis)

    else:
        raise CursoRepetidoException(f"El curso {anyo} {divis} ya existe")

    return nuevo


def menu():
    opt = "x"

    while opt not in ["1","2","3","4","5","6","7","8","9","0"]:
        print("---- Menú de opciones ----")
        print("1. Nuevo alumno")
        print("2. Nuevo profesor")
        print("3. Nuevo curso")
        print("-"*30)
        print("4. Listar alumnos por curso")
        print("5. Listar horarios por profesor")
        print("6. Listar horarios por curso")
        print("--------------------------")
        print("7. Listar todos los alumnos")
        print("8. Listar todos los profesores")
        print("9. Listar todos los cursos")
        print("--------------------------")
        print("0. Salir")
        opt=input(">")

    return opt


def volcar_csv(ruta, campos, filas):
    with open(ruta, "w", newline="") as csvfile:
        csvw = csv.writer(csvfile)
        csvw.writerow(campos)
        csvw.writerows(filas)

        print(f"Se ha generado el archivo {ruta}")


def mostrar_fila(fila, ancho=12):
    linea = map(lambda x:str(x).center(ancho), fila)
    print("|".join(linea))


def mostrar_filas(filas, ancho=12):
    for f in filas:
        mostrar_fila(f, ancho)

def listar_alumnos_por_curso(s):
    #busca los alumnos de un curso
    
    #ruta por defecto
    ruta = "informe.csv"
    anyo, divis = pedir_curso()

    print(f"Alumnos de {anyo} {divis}")

    campos = ["Apellido","Nombre","Anyo","Curso"]
    registros = s.query(Alumno.apellido, Alumno.nombre, Curso.anyo, Curso.division).join(Curso).filter(Curso.anyo==anyo).filter(Curso.division==divis).all()
    mostrar_fila(campos)
    mostrar_filas(registros)
    
    print(f"{len(registros)} registros")
    if preguntar_sino(f"¿Generar {ruta}? s/n"):
        volcar_csv(ruta, campos, registros)



def listar_horarios_por_curso(s):
    #busca los horarios de un curso
    
    #ruta por defecto
    ruta = "informe.csv"
    
    curso = seleccionar_curso(s)
    
    print(f"Horarios de {curso.anyo} {curso.division}")

    campos = ["Anyo", "Division", "Dia", "Desde", "Hasta", "Apellido", "Nombre"]
    registros = s.query(Curso.anyo, Curso.division, Horario.dia, Horario.desde, Horario.hasta, Profesor.apellido, Profesor.nombre).join(Horario, Curso.id==Horario.curso_id).join(Profesor, Horario.profesor_id==Profesor.id).filter(Curso.anyo==curso.anyo).filter(Curso.division==curso.division).all()
   
    mostrar_fila(campos)
    mostrar_filas(registros)
  
    print(f"{len(registros)} registros")
    if preguntar_sino(f"¿Generar {ruta}? s/n"):
        volcar_csv(ruta, campos, registros)



def listar_horarios_por_profesor(s):
    #busca los horarios de un profesor

    ruta = "informe.csv"
    nombre, apellido = pedir_profesor()

    campos = ["Dia","Desde","Hasta","Anyo", "Division"]    
    registros = s.query(Horario.dia, Horario.desde, Horario.hasta, Curso.anyo, Curso.division).join(Curso).join(Profesor).filter(Profesor.nombre==nombre).filter(Profesor.apellido==apellido).all()

    mostrar_fila(campos)
    mostrar_filas(registros)

    print(f"{len(registros)} registros")
    if preguntar_sino(f"¿Generar {ruta}? s/n"):
        volcar_csv(ruta, campos, registros)


def listado_completo(s, obj):
    ruta = "informe.csv"
    
    print(f"Listado completo {obj.__tablename__}")   
    registros_crudos = s.query(obj).all()

    registros = []

    for r in registros_crudos:
        campos, valores = r.campos_valores()
        registros.append(valores)

    mostrar_fila(campos)
    mostrar_filas(registros)

    print(f"{len(registros)} registros")
    if preguntar_sino(f"¿Generar {ruta}? s/n"):
        volcar_csv(ruta, campos, registros)


def listar_todos_los_alumnos(s):
    listado_completo(s, Alumno)


def listar_todos_los_profesores(s):
    listado_completo(s, Profesor)


def listar_todos_los_cursos(s):
    listado_completo(s, Curso)
    

def principal(s):
    opt = menu()

    while opt != "0":
        if opt == "1":
            try:
                a = nuevo_alumno(s)
                s.add(a)
            except OperacionCanceladaException as ex:
                print(ex)
            
        elif opt == "2":
            try:
                p = nuevo_profesor(s)
                s.add(p)
            except OperacionCanceladaException as ex:
                print(ex)

        elif opt == "3":
            try:
                c = nuevo_curso(s)
                s.add(c)
            except CursoRepetidoException as ex:
                print(ex)

        elif opt == "4":
            try:
                listar_alumnos_por_curso(s)
            except CursoNoExisteException as ex:
                print(ex)
        
        elif opt == "5":
            listar_horarios_por_profesor(s)

        elif opt == "6":
            try:
                listar_horarios_por_curso(s)
            except CursoNoExisteException as ex:
                print(ex)
                
        elif opt == "7":
            listar_todos_los_alumnos(s)
        
        elif opt == "8":
            listar_todos_los_profesores(s)
        
        elif opt == "9":
            listar_todos_los_cursos(s)

        opt = menu()

    s.commit()
    print("Programa terminado")


Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
sesion = Session()

cargar_datos_ejemplo(sesion)

principal(sesion)