from tkinter import *
from tkinter import messagebox
import sqlite3

#--------------------funciones
def conexionbbdd():
    miconex=sqlite3.connect('Usuarios')
    micursor=miconex.cursor()
    try:
        micursor.execute('''
            CREATE TABLE DATOSUSUARIOS (
            ID INTEGER PRIMARY KEY AUTOINCREMENT,
            NOMBRE_USUARIO VARCHAR(50),
            APELLIDO VARCHAR(50),
            DIRECCION VARCHAR(50),
            CONTRASEÑA VARCHAR(50),
            COMENTARIOS VARCHAR(100))
            ''')
        messagebox.showinfo('BBDD', 'BBDD creada con éxito')
    except:
        messagebox.showwarning('Atención', 'La BBDD ya existe')

def salir():
    sino=messagebox.askquestion('salir', '¿Desea salir?')
    if sino=='yes':
        root.destroy()

def borrarcampo():
    miid.set('')
    minombre.set('')
    miapellido.set('')
    midire.set('')
    mipass.set('')
    textocomen.delete(1.0, END)
#cambio x parametrica
def crear():
    miconex=sqlite3.connect('Usuarios')
    micursor=miconex.cursor()
    datos=minombre.get(), miapellido.get(), midire.get(), mipass.get(), textocomen.get(1.0, END)
    micursor.execute("INSERT INTO DATOSUSUARIOS VALUES(NULL,?,?,?,?,?)",(datos))
#    micursor.execute("INSERT INTO DATOSUSUARIOS VALUES(NULL, '" +minombre.get()+
#        "','" + miapellido.get()+
#        "','" + midire.get()+
#        "','" +mipass.get()+
#        "','" +textocomen.get("1.0", END)+"')")
    miconex.commit()
    messagebox.showinfo("BBDD","Registro insertado con éxito")
#ENCRIPTAR PASSWORDS
def read():
    try:
        miconex=sqlite3.connect('Usuarios')
        micursor=miconex.cursor()
        micursor.execute("SELECT * FROM DATOSUSUARIOS WHERE ID=" + miid.get())
        usuarioleido=micursor.fetchone()
        minombre.set(usuarioleido[1])
        miapellido.set(usuarioleido[2])
        midire.set(usuarioleido[3])
        mipass.set(usuarioleido[4])
        textocomen.delete(1.0, END) #bug corregido
        textocomen.insert(1.0, usuarioleido[5])
    except:
        minombre.set('NO EXISTE EL USUARIO')

#actualiza los campos vacios fixear eso
def update():
    miconex=sqlite3.connect('Usuarios')
    micursor=miconex.cursor()
    datos=minombre.get(), miapellido.get(), midire.get(), mipass.get(), textocomen.get(1.0, END)
    datos2=list()
    for d in datos:
        if d=="":
            datos2.append(None)
        else:
            datos2.append(d)
    print(datos2)

    micursor.execute("UPDATE DATOSUSUARIOS SET NOMBRE_USUARIO=CASE ? WHEN '' then NOMBRE_USUARIO ELSE ? END, APELLIDO=?, DIRECCION=?, CONTRASEÑA=?, COMENTARIOS=? " +
    "WHERE ID=" + miid.get(), datos)
    #micursor.execute("UPDATE DATOSUSUARIOS SET NOMBRE_USUARIO='" + minombre.get() +
    #"', APELLIDO='" + miapellido.get() +
    #"', DIRECCION='" + midire.get() +
    #"', CONTRASEÑA='" + mipass.get() +
    #"', COMENTARIOS='" + textocomen.get(1.0,END) +
    #"'WHERE ID="+ miid.get())
    miconex.commit()
    messagebox.showinfo("BBDD","Registro Actualizado con éxito")
    borrarcampo() #bug corregido

def delete():
    miconex=sqlite3.connect('Usuarios')
    micursor=miconex.cursor()
    micursor.execute("DELETE FROM DATOSUSUARIOS WHERE ID=" + miid.get())
    miconex.commit()
    messagebox.showinfo("BBDD","Registro borrado con éxito")
    borrarcampo() #bug corregido


root=Tk()
root.title('BBDD Y TKINTER')

barramenu=Menu(root)
root.config(menu=barramenu,width=300, height=300)

bbddmenu=Menu(barramenu, tearoff=0)

bbddmenu.add_command(label='conectar', command=conexionbbdd)
bbddmenu.add_separator()
bbddmenu.add_command(label='salir', command=salir)

bomenu=Menu(barramenu, tearoff=0)

bomenu.add_command(label='Borrar campos', command=borrarcampo)

crudmenu=Menu(barramenu, tearoff=0)
crudmenu.add_command(label='Crear', command=crear)
crudmenu.add_command(label='Leer',command=read)
crudmenu.add_command(label='Actualizar', command=update)
crudmenu.add_command(label='Borrar', command=delete)

ayudamenu=Menu(barramenu, tearoff=0)
ayudamenu.add_command(label='licencia')
ayudamenu.add_command(label='acerca de...')

barramenu.add_cascade(label='BBDD', menu=bbddmenu)
barramenu.add_cascade(label='Borrar', menu=bomenu)
barramenu.add_cascade(label='CRUD', menu=crudmenu)
barramenu.add_cascade(label='Ayuda', menu=ayudamenu)

#entradas

miframe=Frame(root)
miframe.pack()

miid=StringVar()
minombre=StringVar()
miapellido=StringVar()
midire=StringVar()
mipass=StringVar()

cuadroid=Entry(miframe, textvariable=miid)
cuadroid.grid(row=0, column=1, padx=10, pady=10)

cuadroname=Entry(miframe, textvariable=minombre)
cuadroname.grid(row=1, column=1, padx=10, pady=10)
cuadroname.config(fg='blue', justify='right')

cuadroape=Entry(miframe, textvariable=miapellido)
cuadroape.grid(row=2, column=1, padx=10, pady=10)

cuadrodire=Entry(miframe, textvariable=midire)
cuadrodire.grid(row=3, column=1, padx=10, pady=10)

cuadropass=Entry(miframe, textvariable=mipass)
cuadropass.grid(row=4, column=1, padx=10, pady=10)
cuadropass.config(show='*')

textocomen=Text(miframe, width=16, height=5)
textocomen.grid(row=5, column=1, padx=10, pady=10)
scrollvert=Scrollbar(miframe, command=textocomen.yview)
scrollvert.grid(row=5, column=2, sticky='nsew')
textocomen.config(yscrollcommand=scrollvert.set)

#labels

idLabel=Label(miframe, text='id:')
idLabel.grid(row=0, column=0, sticky='e', padx=10, pady=10)

nameLabel=Label(miframe, text='nombre:')
nameLabel.grid(row=1, column=0, sticky='e',padx=10, pady=10)

apeLabel=Label(miframe, text='apellido:')
apeLabel.grid(row=2, column=0, sticky='e',padx=10, pady=10)

direccionLabel=Label(miframe, text='direccion:')
direccionLabel.grid(row=3, column=0, sticky='e',padx=10, pady=10)

contraseñaLabel=Label(miframe, text='contraseña:')
contraseñaLabel.grid(row=4, column=0, sticky='e',padx=10, pady=10)

comenLabel=Label(miframe, text='comentarios:')
comenLabel.grid(row=5, column=0, sticky='e',padx=10, pady=10)

#botones


miframe2=Frame(root)
miframe2.pack()

botoncrear=Button(miframe2, text='Create', command=crear)
botoncrear.grid(row=1, column=0, sticky='e', padx=10, pady=10)

botonleer=Button(miframe2, text='Read', command=read)
botonleer.grid(row=1, column=1, sticky='e', padx=10, pady=10)

botonactu=Button(miframe2, text='Update', command=update)
botonactu.grid(row=1, column=2, sticky='e', padx=10, pady=10)

botonborrar=Button(miframe2, text='Delete', command=delete)
botonborrar.grid(row=1, column=3, sticky='e', padx=10, pady=10)

root.mainloop()
