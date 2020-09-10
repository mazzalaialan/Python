from tkinter import *
from tkinter import messagebox
root=Tk()


#ventana emergente
def infoadic():
    messagebox.showinfo('alan el gil','huele a mono')

barramenu=Menu(root)
root.config(menu=barramenu,width=300, height=300)

archivomenu=Menu(barramenu, tearoff=0)

archivomenu.add_command(label='nuevo')
archivomenu.add_command(label='guardar')
archivomenu.add_command(label='guardar como')
archivomenu.add_separator()
archivomenu.add_command(label='cerrar')
archivomenu.add_command(label='salir')

edicionmenu=Menu(barramenu, tearoff=0)

edicionmenu.add_command(label='copiar')
edicionmenu.add_command(label='cortar')
edicionmenu.add_command(label='pegar')

herramientasmenu=Menu(barramenu, tearoff=0)

ayudamenu=Menu(barramenu, tearoff=0)
ayudamenu.add_command(label='licencia')
ayudamenu.add_command(label='acerca de...', command=infoadic)

barramenu.add_cascade(label='archivo', menu=archivomenu)

barramenu.add_cascade(label='edicion', menu=edicionmenu)

barramenu.add_cascade(label='herramientas', menu=herramientasmenu)

barramenu.add_cascade(label='ayuda', menu=ayudamenu)



root.mainloop()
