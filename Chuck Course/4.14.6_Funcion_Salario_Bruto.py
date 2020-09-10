hs = input('ingrese horas')
tf = input('ingrese tarifa por hora')
hsi = int(hs)
tfi = int (tf)
def calci(hsi, tfi):
    multi = (hsi*tfi)
    return(multi)
print('salario', calci())
