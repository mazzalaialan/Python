archi= input('ingrese archivo')
if archi == 'na na na':
    print('NA NA BOO BOO PARA TI - Te he atrapado!')
try:
    archivo = open(archi)
except:
    print('error de archivo')
    quit()
count = 0
perro = 0
for bab in archivo:
    if bab.startswith('X-DSPAM-Confidence:'):
        count= count + 1
        tultul = bab.find(':')
        numero = float(bab[tultul+1:])
        perro= perro + numero
print('promedio spam Confidence', perro/count)
