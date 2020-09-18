from sqlalchemy import create_enginefrom sqlalchemy.ext.declarative import declarative_basefrom sqlalchemy import Column, Integer, String, Sequence, ForeignKeyfrom sqlalchemy.orm import sessionmaker, relationshipfrom sqlalchemy import Table, TextBase = declarative_base()horario_profesor = Table('horario_profesor', Base.metadata, Column('horario_id', ForeignKey(    'horario.id'), primary_key=True), Column('profesor_id', ForeignKey('profesor.id'), primary_key=True))horario_curso = Table('horario_curso', Base.metadata, Column('horario_id', ForeignKey(    'horario.id'), primary_key=True), Column('curso_id', ForeignKey('curso.id'), primary_key=True))# Definiciones de Clasesclass Horario(Base):    __tablename__ = 'horario'    id = Column(Integer, Sequence('horario_id_seq'), primary_key=True)    dia = Column(String)    hora_inicio = Column(String)    hora_fin = Column(String)    horario_cursos = relationship(        'Curso', secondary=horario_curso, back_populates='curso_horario')    horario_profesores = relationship(        'Profesor', secondary=horario_profesor, back_populates='profesor_horario')    def __repr__(self):        return ' {} - {} - {} '.format(self.dia, self.hora_inicio, self.hora_fin)class Profesor(Base):    __tablename__ = 'profesor'    id = Column(Integer, Sequence('profesor_id_seq'), primary_key=True)    nom_profesor = Column(String)    curso_asig = Column(Integer, ForeignKey('curso.id'))    curso = relationship('Curso', back_populates='profesor')    profesor_horario = relationship(        'Horario', secondary=horario_profesor, back_populates='horario_profesores')    def __repr__(self):        return "{}".format(self.nom_profesor)class Alumno(Base):    __tablename__ = 'alumno'    id = Column(Integer, Sequence('alumno_id_seq'), primary_key=True)    nom_alumno = Column(String)    curso_id = Column(Integer, ForeignKey('curso.id'))    curso = relationship('Curso', back_populates='alumno')    def __repr__(self):        return "{}".format(self.nom_alumno)class Curso(Base):    __tablename__ = 'curso'    id = Column(Integer, Sequence('curso_id_seq'), primary_key=True)    nom_curso = Column(String)    profesor = relationship(        'Profesor', back_populates='curso', cascade='all,delete, delete-orphan')    alumno = relationship('Alumno', back_populates='curso',                          cascade='all, delete, delete-orphan')    curso_horario = relationship(        'Horario', secondary=horario_curso, back_populates='horario_cursos')    def __repr__(self):        return '{}'.format(self.nom_curso)engine = create_engine('sqlite:///:memory:')Base.metadata.create_all(engine)Session = sessionmaker(bind=engine)session = Session()# Menuwhile True:    print("\nSISTEMA REGISTRO ESCOLAR")    print("(1) Alumno")    print("(2) Profesor")    print("(3) Curso")    print("(4) Salir")    opcion = input("\nElija (1,2,3,4): ")    if opcion == "1":        while True:            print("\nMENU ALUMNOS")            print("(1) Insertar")            print("(2) Buscar alumnos por Curso")            print("(3) Alumnos Registrados")            print("(4) Salir")            opcion = input("\nElija (1,2,3,4): ")            if opcion == "1":                curso = session.query(Curso).all()                if curso:                    nombre = input("Nombre del Alumno: ")                    curso_inscrito = input("Curso a inscribir: ")                    curso = session.query(Curso).filter(                        Curso.nom_curso == curso_inscrito).all()                    curso_id = curso[0].id                    alumno = Alumno(nom_alumno=nombre, curso_id=curso_id)                    session.add(alumno)                    print("Alumno insertado correctamente: " +                          nombre + " Curso: " + curso_inscrito)                else:                    print("¡ Primero debe registrar Cursos... !")                    break            elif opcion == "2":                curso = session.query(Curso).all()                if curso:                    curso_buscar = input("Nombre del curso: ")                    curso_encontrado = session.query(Curso).filter(                        Curso.nom_curso == curso_buscar).all()                    if curso_encontrado:                        id_curso = curso_encontrado[0].id                        alumnos = session.query(Alumno).filter(                            Alumno.curso_id == id_curso).all()                        if alumnos:                            print("ALUMNOS MATRICULADOS:")                            for i in range(len(alumnos)):                                print(alumnos[i])                        else:                            print("No existen alumnos matriculados...")                    else:                        print("Curso No registrado")                else:                    print("¡ Primero debe registrar Cursos... !")            elif opcion == "3":                print("\nALUMNOS REGISTRADOS\n")                alumnos = session.query(Alumno).all()                if alumnos:                    for i in range(len(alumnos)):                        curso = session.query(Curso).filter(                            Curso.id == alumnos[i].curso_id)                        print(alumnos[i].nom_alumno +                              "\t" + curso[0].nom_curso)                else:                    print("No existen alumnos registrados...")            elif opcion == "4":                break            else:                print("Debes elegir una opción anterior")    elif opcion == "2":        while True:            print("\nMENU PROFESORES")            print("(1) Insertar")            print("(2) Horario de Profesores")            print("(3) Profesores Registrados")            print("(4) Salir")            opcion = input("\nElija (1,2,3,4): ")            if opcion == "1":                cursos = session.query(Curso).all()                if cursos:                    nombre = input("Nombre Profesor: ")                    curso_asig = input("Curso asignado: ")                    curso = session.query(Curso).filter(                        Curso.nom_curso == curso_asig).all()                    dias = input("HORARIO\nDia[Lunes-Domingo]: ")                    hora_inicio = input("Hora Inicio [HH:MM]: ")                    hora_fin = input("Hora Término [HH:MM]: ")                    curso_id = curso[0].id                    profesor = Profesor(nom_profesor=nombre,                                        curso_asig=curso_id)                    session.add(profesor)                    horario = Horario(                        dia=dias, hora_inicio=hora_inicio, hora_fin=hora_fin)                    horarios = session.add(horario)                    horario.horario_profesores.append(profesor)                    curso = session.query(Curso).get(curso_id)                    horario.horario_cursos.append(curso)                    print("Profesor ingresado correctamente: " +                          nombre + " Curso: " + curso_asig)                else:                    print(" Antes debe registrar algún Curso !!! ")                    break            elif opcion == "2":                horarios = session.query(Horario).all()                if horarios:                    nombre = input("Nombre Profesor: ")                    profesor = session.query(Profesor).filter(                        Profesor.nom_profesor == nombre).all()                    if profesor:                        for horario in session.query(Horario).\                                filter(Horario.horario_profesores.any(Profesor.nom_profesor == nombre)).all():                            print(horario)                    else:                        print(" Profesor no registrado....!")                else:                    print("¡ No existen Profesores registrados... !")            elif opcion == "3":                print("PROFESORES REGISTRADOS")                profesores = session.query(Profesor).all()                if profesores:                    for i in range(len(profesores)):                        print(str(i+1) + "\t"+profesores[i].nom_profesor)                else:                    print("Profesores no registrados...")            elif opcion == "4":                break            else:                print("Debes elegir una opción anterior")    elif opcion == "3":        while True:            print("\nMENU CURSO")            print("(1) Insertar")            print("(2) Horario de Curso")            print("(3) Cursos Registrados")            print("(4) Salir")            opcion = input("\nElija (1,2,3,4): ")            if opcion == "1":                nombre = input("Nombre del Curso: ")                nombre = Curso(nom_curso=nombre)                session.add(nombre)                print("Curso insertado correctamente: " + nombre.nom_curso)            elif opcion == "2":                horarios = session.query(Horario).all()                if horarios:                    nombre = input("Nombre del Curso: ")                    curso = session.query(Curso).filter(                        Curso.nom_curso == nombre).all()                    if curso:                        for horario in session.query(Horario).\                                filter(Horario.horario_cursos.any(Curso.nom_curso == nombre)).all():                            print(horario)                    else:                        print("Curso No Registrado....")                else:                    print("¡ No existen Profesores registrados... !")            elif opcion == "3":                cursos = session.query(Curso).all()                if cursos:                    for i in range(len(cursos)):                        print(str(i+1) + "\t"+cursos[i].nom_curso)                else:                    print("Cursos aún no registrados...")            elif opcion == "4":                break            else:                print("Debes elegir una opción anterior..")    elif opcion == "4":        break    else:        print("Debes elegir una opción anterior") 
