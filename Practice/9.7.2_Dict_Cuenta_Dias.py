fhand = open('texto.txt')
mails = dict()
for line in fhand:
    if line.startswith('From'):
        lineas = line.split()
        try:
            mails[lineas[2]] = mails.get(lineas[2], 0) + 1
        except:
            continue
    #for d in dia:#    
print(mails)
