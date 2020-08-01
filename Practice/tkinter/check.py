from tkinter import *

root=Tk()

root.title('Boton')

playa=IntVar()
montania=IntVar()
turismo=IntVar()

def opciones():
    opcionelegida=''
    if playa.get()==1:
        opcionelegida+='playa\n'
    if montania.get()==1:
        opcionelegida+='montaña\n'
    if turismo.get()==1:
        opcionelegida+='turismo rural'
    final.config(text=opcionelegida)

foto=PhotoImage(file='avion.png')
Label(root, image=foto).pack()

Label(root, text='Viajes').pack()

frame=Frame(root).pack()
Label(frame, text='elige destinos', width=50).pack()

Checkbutton(frame, text='playa', variable=playa, onvalue=1, offvalue=0, command=opciones).pack()
Checkbutton(frame, text='montaña', variable=montania, onvalue=1, offvalue=0, command=opciones).pack()
Checkbutton(frame, text='turismo rural', variable=turismo, onvalue=1, offvalue=0, command=opciones).pack()
botonenvio=Button(frame, text='Enviar')
botonenvio.pack()

#etiqueta=Label(root)
#etiqueta.pack()
final=Label(frame)
final.pack()

root.mainloop()
