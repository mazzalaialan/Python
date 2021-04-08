"""Escribe un programa en Python que muestre la hora actual con una suma de dos horas adicionales"""
import datetime

horaActual = datetime.datetime.now()
dosHoras = horaActual + datetime.timedelta(hours=2)
print(dosHoras.strftime('%H:%M:%S'))