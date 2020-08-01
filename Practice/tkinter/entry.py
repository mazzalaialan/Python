from tkinter import *

root=Tk()

miframe=Frame(root, width=1200, height=600)

miframe.pack()

cuadrotxt=Entry(miframe)
cuadrotxt.grid(row=0, column=1)

cuadroapellido=Entry(miframe)
cuadroapellido.grid(row=1, column=1)

cuadrodire=Entry(miframe)
cuadrodire.grid(row=2, column=1)

nombreLabel=Label(miframe, text='Nombre:')
nombreLabel.grid(row=0, column=0, sticky='w')

apellidoLabel=Label(miframe, text='apellido:')
apellidoLabel.grid(row=1, column=0, sticky='w')

direccionLabel=Label(miframe, text='direccion:')
direccionLabel.grid(row=2, column=0, sticky='w')

root.mainloop()
