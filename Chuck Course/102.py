fhand = open('texto.txt')
horas = dict()
for line in fhand:
    if line.startswith('From'):
        lineas = line.split()
        try:
           horas[lineas[5][:2]] = horas.get(lineas[5][:2], 0) + 1
        except:
            continue
print(horas)
kika = list()
for k,v in horas.items():
    kika.append((k,v))
kika.sort()
print(kika)
