import csv

a_list = ['Pedro', 'Florencia', 'Matías', 'Jorge', 'María', 'Inés']
#ruta = 'C:/Users/User/Dropbox/Alan/Programacion/Curso_Python/Estructuras de datos en Python/Modulo2/'
ruta = 'C:\\Users\\Alan\\Dropbox\\Alan\\Programacion\\Curso_Python\\Estructuras de datos en Python\\Modulo2\\'

with open(ruta+'nombres.csv', 'w', newline='') as f: 
    writer = csv.writer(f,delimiter=';', quotechar='|', quoting=csv.QUOTE_MINIMAL) 
    writer.writerow(a_list)

#with open(ruta+'nombres.csv', 'w', newline='') as f: 
#    writer = csv.writer(f,delimiter=';', quotechar='|', quoting=csv.QUOTE_MINIMAL) 
#    writer.writerow(a_list)