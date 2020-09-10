from tkinter import *

raiz=Tk()

raiz.title('CALCULADORA')

miframe=Frame(raiz)

miframe.pack()

operacion=''
reset_pantalla=False
resultado=0

#----------------------------pantalla---------------------------------
numeropantalla=StringVar()


pantalla=Entry(miframe, textvariable=numeropantalla)
pantalla.grid(row=1, column=1, padx=10, pady=10, columnspan=4)
pantalla.config(background='black', fg='#03f941',justify='right')

#-------------funciones
def numeropulsado(num):
    global operacion
    if operacion !='':
        numeropantalla.set(num)
        operacion =''
    else:
        numeropantalla.set(numeropantalla.get()+ num)

def suma(num):
    global operacion
    global resultado
    resultado+=int(num)
    operacion='suma'
    reset_pantalla=True
    numeropantalla.set(resultado)

def elresultado():
    global resultado
    numeropantalla.set(resultado+int(numeropantalla.get()))
    resultado=0

num1=0

contador_resta=0

def resta(num):
	global operacion
	global resultado
	global num1
	global contador_resta
	global reset_pantalla

	if contador_resta==0:

		num1=int(num)

		resultado=num1

	else:

		if contador_resta==1:

			resultado=num1-int(num)

		else:

			resultado=int(resultado)-int(num)

		numeropantalla.set(resultado)

		resultado=numeropantalla.get()


	contador_resta=contador_resta+1
	operacion="resta"
	reset_pantalla=True
#----------------------fila 1-------------------------------------------

buton7=Button(miframe, text='7',width=3, command=lambda:numeropulsado("7"))
buton7.grid(row=2,column=1)
buton8=Button(miframe, text='8',width=3, command=lambda:numeropulsado("8"))
buton8.grid(row=2,column=2)
buton9=Button(miframe, text='9',width=3, command=lambda:numeropulsado("9"))
buton9.grid(row=2,column=3)
butonx=Button(miframe, text='x',width=3, command=lambda:numeropulsado("x"))
butonx.grid(row=2,column=4)

#----------------------fila 2-------------------------------------------

buton4=Button(miframe, text='4',width=3, command=lambda:numeropulsado("4"))
buton4.grid(row=3,column=1)
buton5=Button(miframe, text='5',width=3, command=lambda:numeropulsado("5"))
buton5.grid(row=3,column=2)
buton6=Button(miframe, text='6',width=3, command=lambda:numeropulsado("6"))
buton6.grid(row=3,column=3)
butonr=Button(miframe, text='-',width=3,command=lambda:resta(numeropantalla.get()))
butonr.grid(row=3,column=4)
#----------------------fila 3-------------------------------------------

buton1=Button(miframe, text='1',width=3, command=lambda:numeropulsado("1"))
buton1.grid(row=4,column=1)
buton2=Button(miframe, text='2',width=3, command=lambda:numeropulsado("2"))
buton2.grid(row=4,column=2)
buton3=Button(miframe, text='3',width=3, command=lambda:numeropulsado("3"))
buton3.grid(row=4,column=3)
butons=Button(miframe, text='+',width=3, command=lambda:suma(numeropantalla.get()))
butons.grid(row=4,column=4)
#----------------------fila 4-------------------------------------------
buton0=Button(miframe, text='0',width=3, command=lambda:numeropulsado("0"))
buton0.grid(row=5,column=1)
butonc=Button(miframe, text=',',width=3, command=lambda:numeropulsado(","))
butonc.grid(row=5,column=2)
butond=Button(miframe, text='/',width=3, command=lambda:numeropulsado("/"))
butond.grid(row=5,column=3)
butoni=Button(miframe, text='=',width=3, command=lambda:elresultado())
butoni.grid(row=5,column=4)



raiz.mainloop()
