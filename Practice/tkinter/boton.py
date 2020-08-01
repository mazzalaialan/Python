from tkinter import *

root=Tk()

miframe=Frame(root, width=1200, height=600)

miframe.pack()

minombre=StringVar()

cuadrotxt=Entry(miframe, textvariable=minombre)
cuadrotxt.grid(row=0, column=1, padx=10, pady=10)

cuadroapellido=Entry(miframe)
cuadroapellido.grid(row=1, column=1, padx=10, pady=10)

cuadropass=Entry(miframe)
cuadropass.grid(row=2, column=1, padx=10, pady=10)
cuadropass.config(show='*')

cuadrodire=Entry(miframe)
cuadrodire.grid(row=3, column=1, padx=10, pady=10)

textocoment=Text(miframe, width=16, height=5)
textocoment.grid(row=4, column=1, padx=10, pady=10)

nombreLabel=Label(miframe, text='Nombre:')
nombreLabel.grid(row=0, column=0, sticky='e', padx=10, pady=10)

apellidoLabel=Label(miframe, text='apellido:')
apellidoLabel.grid(row=1, column=0, sticky='e', padx=10, pady=10)

direccionLabel=Label(miframe, text='contraseña:')
direccionLabel.grid(row=2, column=0, sticky='e', padx=10, pady=10)

direccionLabel=Label(miframe, text='direccion:')
direccionLabel.grid(row=3, column=0, sticky='e', padx=10, pady=10)

comentsLabel=Label(miframe, text='comentarios:')
comentsLabel.grid(row=4, column=0, sticky='e', padx=10, pady=10)

def codigoboton():
    minombre.set('Cinthia')

botonenvio=Button(root, text='Enviar', command=codigoboton)
botonenvio.pack()

root.mainloop()
