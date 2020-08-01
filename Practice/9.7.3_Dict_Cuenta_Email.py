fhand = open('text.txt')
palabras = dict()
lista = list()
for line in fhand:
    lista = line.split()
    for palabra in lista:
        palabras[palabra] = 1
print(palabras)
