"""Escribe un programa en Python que acepte una cadena de caracteres y cuente el tamaño de la
cadena y cuantas veces aparece la letra A (mayuscula y minúscula)"""

cadena = input("Ingresar la cadena de texto a validar: ")
print("El tamaño de cadena es:", len(cadena), "y la cantidad de A es:", cadena.lower().count('a'))
