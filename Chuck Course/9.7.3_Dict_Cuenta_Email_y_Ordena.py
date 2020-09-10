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
nombre = None
num = 0
for k in mails:
    if mails[k]> num:
        num = mails[k]
        nombre = k
print(nombre, num)
