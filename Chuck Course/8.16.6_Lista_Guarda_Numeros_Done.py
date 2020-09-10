numlista = list()
while True:
    valor = input('ingrese un numero')
    if valor == ('done'):
        break
    try:
        valori = int(valor)
        numlista.append(valori)        
    except:
        print('error')
    
print('max= ', max(numlista),'min= ', min(numlista))
