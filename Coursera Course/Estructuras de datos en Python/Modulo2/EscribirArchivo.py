import math
factorial_10 = str(math.factorial(10))
with open('C:/Users/User/Dropbox/Alan/Programacion/Curso_Python/Estructuras de datos en Python/Modulo2/factorial.txt', 'w') as a_file:
    a_file.write(factorial_10)