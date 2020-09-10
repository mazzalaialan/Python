fhand = open('texto.txt')
mails = dict()
for line in fhand:
    if line.startswith('From'):
        lin = line.split()
        lineas = lin[1].split('@')
        try:
            mails[lineas[1]] = mails.get(lineas[1], 0) + 1
        except:
            continue
print(mails)
