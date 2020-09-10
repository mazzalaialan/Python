
import re
fhand = open('texto.txt')
y=0
c=0
b = list()
for line in fhand:
    line = line.rstrip()
    x = re.findall('^New Revision: ([0-9][0-9]+)',line)
    if len(x) > 0:
        b.append(x[0])
        y= y+1
for elemento in b:
    bn = int(elemento)
    c = c+bn
print('lista',b,'promedio', (c/y))
