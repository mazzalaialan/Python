def calculo_salario(parametro1,parametro2):
    parametro1f = float(parametro1)
    parametro2f = float(parametro2)
    if parametro1f <=40:
         resultado = (parametro1f*parametro2f)
    else:
         resultado = (( parametro1f - 40)* 0.5 * parametro2f ) + ( parametro1f * parametro2f )
    return resultado

hs = input('ingrese horas >>')
tf = input('ingrese tarifa por hora >>')
try:
    hsi = float(hs)
    tfi = float(tf)
    print('Salario:',calculo_salario(hsi,tf))
except:
    print('Error: Debe ingresar un valor numerico')
