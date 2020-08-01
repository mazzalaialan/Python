from tkinter import *

root=Tk()

root.title('Boton')
VarOpcion=IntVar()
def imprimir():
    #print(VarOpcion.get())
    if VarOpcion.get()==1:
        etiqueta.config(text='Femenino')
    else:
        etiqueta.config(text='Masculino')

Label(root, text='Género').pack()

Radiobutton(root, text='Femenino', variable=VarOpcion, value=1, command=imprimir).pack()

Radiobutton(root, text='Masculino', variable=VarOpcion, value=2, command=imprimir).pack()

etiqueta=Label(root)
etiqueta.pack()

root.mainloop()
