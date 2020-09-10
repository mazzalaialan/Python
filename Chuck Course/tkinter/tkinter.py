from tkinter import *
from tkinter import messagebox
import sqlite3

root=Tk()
root.title('BBDD Y TKINTER')


miframe2=Frame(root)
miframe2.pack()

botoncrear=Button(miframe2, text='Create')
botoncrear.grid(row=1, colum=0, sticky='e', padx=10, pady=10)

botonleer=Button(miframe2, text='Read')
botonleer.grid(row=1, colum=1, sticky='e', padx=10, pady=10)

botonactu=Button(miframe2, text='Update')
botonactu.grid(row=1, colum=2, sticky='e', padx=10, pady=10)

botonborrar=Button(miframe2, text='Delete')
botonborrar.grid(row=1, colum=3, sticky='e', padx=10, pady=10)

root.mainloop()
