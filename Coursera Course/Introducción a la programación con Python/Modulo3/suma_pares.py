def suma_pares(rango):
    sumador = 0
    for num in range(2,rango+2,2):
        sumador += num
    print(sumador)

suma_pares(100)