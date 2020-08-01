import re
fhand = open('texto.txt')
dato = input('ingrese una expresión')
y = 0
for line in fhand:
    line = line.rstrip()
    x = re.findall(dato, line)
    if len(x) > 0:
        y = y+1
print(dato, y)
print(type(y))
