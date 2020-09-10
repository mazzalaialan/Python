import json

ruta = 'C:/Users/User/Dropbox/Alan/Programacion/Curso_Python/Estructuras de datos en Python/Modulo2/'

#deserializa un objeto
json.dumps('[1,2,3]')

with open(ruta+'json_example.txt','w') as a_file:
    json.dump([1,2,3,4],a_file)

with open(ruta+'json_example.txt','r') as a_file:
    a_list = json.load(a_file)
    print(a_list)