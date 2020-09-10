import random

def tirar_dados(caras):
    "Lanza un dado de la cantidad de digitos recibido por parámetro"
    a = list(random.choices(range(1,caras+1),K=2))
    print("Resultados:",a[0],"y",a[1],"Suma:",a[0]+a[1])    

relanzar = None
while(relanzar not in ('NO','N')):
    tirar_dados(6)
    relanzar = str.upper(input("¿Volver a lanzar? escirba N o No para salir :"))