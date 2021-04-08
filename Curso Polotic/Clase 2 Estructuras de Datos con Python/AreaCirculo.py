"""Escribe un programa Python que acepte el radio de un círculo del usuario y calcule el área."""

import math

radio = input("Ingresar el radio del circulo: ")
try:
    radioFloat = float(radio)
    print(math.pi * (radioFloat ** 2))
except TypeError:
    print("Tipo de dato inválido. No ingreso un número:", radio)
except ValueError:
    print("Valor inválido. No ingreso un radio correcto:", radio)