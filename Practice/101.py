fhand = open('texto.txt')
mails = dict()
for line in fhand:
    if line.startswith('From'):
        lineas = line.split()
        try:
            mails[lineas[1]] = mails.get(lineas[1], 0) + 1
        except:
            continue
print(mails)
lista = list()
for k,v in mails.items():
    lista.append((v,k))
lista.sort(reverse=True)
print(lista)
print(lista[0])
