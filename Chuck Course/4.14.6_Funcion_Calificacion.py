def calcula_calificacion(calif):
    if calif >= 0.9 :
        return('Sobresaliente')
    elif calif >= 0.8:
         return('Notable')
    elif calif >= 0.7:
         return('Bien')
    elif calif >= 0.6:
         return('Suficiente')
    elif calif < 0.6:
         return('Insuficiente')


punti = input('ingrese calificacion entre 0.0 y 1.0')

try:
    punt = float(punti)
    if punt < 0 or punt >=1:
        print('ingrese un valor valido')

    else:
        print(calcula_calificacion(punt))
except: print('ingrese un valor entre 0.0 y 1.0')
