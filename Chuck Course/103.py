import string

fh  = open('texto.txt')
texto = fh.read()
texto = texto.lower()
texto = texto.translate(str.maketrans('', '', string.punctuation+string.whitespace+string.digits))
letras = dict()
for x in texto:
    letras[x] = letras.get(x,0)+1
orden = list()
for k,v in letras.items():
    orden.append ((v,k))
orden.sort(reverse=True)
print(orden)
