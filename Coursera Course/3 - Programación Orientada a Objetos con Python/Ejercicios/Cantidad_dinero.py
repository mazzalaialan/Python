class moneda(object):
    def __init__(self,nombre,simbolo,tc):
        self.nombre = nombre
        self.simbolo = simbolo
        self.tc = tc
        
    def __repr__(self):
        return self.nombre

    def convertir_importe_a_moneda_base(self,importe_a_convertir):
        return importe_a_convertir * self.tc

    def convertir_importe_desde_moneda_base(self,importe_a_convertir):
        return importe_a_convertir / self.tc


class dinero(object):
    def __init__(self,importe,moneda):
        self.importe = importe
        self.moneda = moneda

    def importe_moneda_base(self):
        return self.moneda.convertir_importe_a_moneda_base(self.importe)

    def __repr__(self):
        return '{} {}'.format(self.moneda,self.importe)

    def __add__(self,importe_a_sumar):
        importe = self.importe_moneda_base() + importe_a_sumar.importe_moneda_base()
        importe = self.moneda.convertir_importe_desde_moneda_base(importe)
        return dinero(importe,moneda)

    def __sub__(self,importe_a_restar):
        importe = self.importe_moneda_base() - importe_a_restar.importe_moneda_base()
        importe = self.moneda.convertir_importe_desde_moneda_base(importe)
        return dinero(importe,moneda)

    def __mul__(self,cantidad):
        return dinero(self.importe*cantidad,moneda)

    def __truediv__(self,cantidad):
        return dinero(self.importe/cantidad,moneda)

    def no_hacer_nada(self):
        pass

dolar = moneda('dolar USA','U$S',1)
peso = moneda('pesos (Arg)','$',1/78)

one_dollar = dinero(1,dolar)
one_peso = dinero(1,peso)

print('Suma:',one_dollar + one_peso)

print('Resta:',one_dollar - one_peso)

print('Multplicacion:',one_dollar * 10)

print('Division:',one_dollar / 2)

one_dollar / 2