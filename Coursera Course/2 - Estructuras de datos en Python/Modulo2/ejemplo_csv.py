import csv

ruta = 'C:/Users/User/Dropbox/Alan/Programacion/Curso_Python/Estructuras de datos en Python/Modulo2/'

with open(ruta+'some1.csv', 'r') as f:
    reader = csv.reader(f)
    for row in reader:
        print('; '.join(row))

with open(ruta+'some1.csv', 'a') as f:
        writer = csv.writer(f)
        writer.writerow(['Pedro','Gont','423112','alan@gmail.com'])