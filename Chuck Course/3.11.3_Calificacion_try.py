punti = input('ingrese calificacion entre 0.0 y 1.0')

try:
    punt = float(punti)
    if punt < 0 or punt >=1:
        print('ingrese un valor valido')
    elif punt >= 0.9 :
        print('Sobresaliente')
    elif punt >= 0.8:
         print('Notable')
    elif punt >= 0.7:
         print ('Bien')
    elif punt >= 0.6:
         print('Suficiente')
    elif punt< 0.6:
         print('Insuficiente')
except: print('ingrese un valor entre 0.0 y 1.0') 
