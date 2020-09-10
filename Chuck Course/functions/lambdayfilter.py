#def area_triangulo(base, altura):
#    return (base*altura)/2
#LAMBA

area_triangulo=lambda base, altura:(base*altura/2)


#FILTER
numeros=[17,22,55,66,99,44,12]


print(list(filter(lambda np: np%2==0, numeros)))


class Empleado:
    def__init__(self, nombre, cargo, salario):
        self.nombre=nombre
        self.cargo=cargo
        self.salario=salario
    def__str__(self):
        return "{} que trabaja como {} tiene un salario de {} $".format(self.nombre, self.cargo, self.salario)

listaempleados=[
Empleado("Juan","director","70000")
Empleado("Lisa","presidenta","80000")
Empleado("Cami","coordinador","30000")
Empleado("Jose","secretario","40000")
]

salarios_altos=filter(lambda Empleado:Empleado.salario>50000, listaempleados)

for es in salarios_altos
    print(es)


def calculo_comision(Empleado):
    Empleado.salario=Empleado*1.03
    return Empleado


#listaempleadoscomi=map(calculo_comision, listaempleados)
listaempleadoscomi=map(lambda Empleado:Empleado.salario*1.03, listaempleados)


for Empleado in listaempleadoscomi:
    print(Empleado)
