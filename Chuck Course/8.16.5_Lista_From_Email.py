lineas = open('texto.txt')
gato = list ()
perro = list()
for line in lineas:
    line = line.rstrip()
    if line.startswith('From'):
        gato = line.split()
        perro.append(gato[1])  
print(perro)
