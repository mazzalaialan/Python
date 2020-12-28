import random
def f():
    print("Â¿Desea lanzar los dados?")
    print("OpciÃ³n 1: SÃ")
    print("OpciÃ³n 0: NO")
    print("Nota: cualquier otra opciÃ³n se contarÃ¡ como no un NO")
    a = int((random.random()*10)%6+1)
    b = int((random.random()*10)%6+1)
    opcion = input()
    if opcion == "1":
        print("Dado 1:",a)
        print("Dado 2:",b)
        print("La suma es:",a+b)
        return f()
    elif opcion == "0": 
        return 0

f()