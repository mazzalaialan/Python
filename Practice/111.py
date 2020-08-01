import re
fhand = open('texto.txt')
mails = dict()
dato = input('ingrese una expresión')
for line in fhand:
    line = line.rstrip()
    x = re.findall(dato, line)
    for valores in x:
      try:
          mails[valores] = mails.get(valores, 0) + 1
      except:
          continue
print(mails)
