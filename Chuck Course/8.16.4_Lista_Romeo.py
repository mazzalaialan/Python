texto = open('romeo.txt')
lineas = texto.read()
lista = lineas.split()
nueva = list()
for words in lista:
    if words not in nueva:
        nueva.append(words)
nueva.sort()
print(nueva)
