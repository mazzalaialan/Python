"""Escribe un programa Python que acepte un número entero (n) y calcule el valor de n + nn + nnn"""

numero = input("Ingresar el número entero a calcular: ")
try:
    numeroInt = int(numero)
    print(numeroInt + (numeroInt ** 2) + (numeroInt ** 3))
except TypeError:
    print("Tipo de dato inválido. No ingreso un número:", numero)
except ValueError:
    print("Valor inválido. No ingreso un número correcto:", numero)