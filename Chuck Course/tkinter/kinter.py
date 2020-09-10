from tkinter import *

raiz=Tk()

raiz.title('Alan es un tipo medio pelotudo')

raiz.resizable(True,True)

raiz.iconbitmap('papel.ico'
                )
#raiz.geometry('650x350')

raiz.config(bg='green')

miframe=Frame()

miframe.pack(side='right', anchor='s')

miframe.config(bg='red')

miframe.config(width='650', height ='350')

miframe.config(relief='sunken')

miframe.config(bd=35)

miframe.config(cursor='hand2')

raiz.mainloop()
