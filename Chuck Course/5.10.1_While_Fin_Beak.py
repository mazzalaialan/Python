b = 0
c = 0
while True:
    valor = input('ingrese un numero')
    try:
        valori = int(valor)
        b = b+valori
        c = c+1
    except:
        print('error')
    if valor == ('fin'):
        break
print(b,c,(b/c))
