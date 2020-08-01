hs = input('ingrese horas')
tf = input('ingrese tarifa por hora')
try:
         hsi = int(hs)
         tfi = int (tf)
         if hsi <=40:
              print('salario',  hsi*tfi)
         else:
              print('salario:',(hsi-40)*0.5*tfi + (hsi*tfi))
except:
        print('ingrese un numero')
