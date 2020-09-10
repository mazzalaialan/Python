def decoradori(func_parametro):
    def f_c(*args,**kwargs):
        #acciones adicionales que agregan txt
        print("realizando calculos")
        func_parametro(*args, **kwargs)
        #+acciones
        print("Calculo terminado")
    return f_c



@decoradori
def suma(num1, num2):
    print(num1 + num2)

@decoradori
def resta(num1, num2):
    print(num1 - num2)

@decoradori
def potencia(base, exponente):
    print(pow(base, exponente))

suma(5,7)
resta(9,3)


potencia(base=5, exponente=3)