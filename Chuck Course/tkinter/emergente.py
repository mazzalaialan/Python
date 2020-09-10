from tkinter import *
from tkinter import messagebox
from tkinter import filedialog

root=Tk()

barramenu=Menu(root)

def abrirfichero():
    fichero=filedialog.askopenfilename(title='abrir',initialdir='c:')
    print(fichero)

def explosivo():
    messagebox.showwarning('AVISO', 'LANZAR MISIL EN 3, 2 , 1\nPRESIONE ENVIAR NUEVAMENTE SI ESTA SEGURO')

botonenvio=Button(root, text='Enviar', command=explosivo)
botonenvio.pack()
Button(root, text='abrir fichero', command=abrirfichero).pack()

root.mainloop()
