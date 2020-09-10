# -*- coding: utf-8 -*-
import unittest

class CompraFinalizadaEx(Exception):
    pass

class CompraVaciaEx(Exception):
    pass

class CajaRegistradora(object): 

    def __init__(self):
        self._productos = []
        self.finalizada = False

    def agregar_producto_escaneado(self,elProducto):
        self._productos.append(elProducto)
    
    def calcular_subtotal(self):
        pass

    def finalizar_compra(self):
        if self.finalizada:
            raise CompraFinalizadaEx("La compra ya fué finalizada")
        if not self._productos:
            raise CompraVaciaEx("La compra no tiene productos")
        self.finalizada = True

    def calcular_total(self):
        pass

    def pagar(self,dinero):
        return 0

class Compra(object):
    pass

class Producto(object):
    def __init__(self, codigo):
        self._codigo = codigo

    def codigo(self):
        return self._codigo

class ListaPrecios(object):

    def __init__(self):
        self.precios = {}
        self.descuentos = {}
    
    def cargar_precio_para(self, unproducto, elprecio):
        self.precios[unproducto] = elprecio

    def cargar_descuento_para(self, unproducto, eldescuento):
        self.descuentos[unproducto] = eldescuento

    def obtener_precio_cdescuento(self,elproducto):
        return self.precios[elproducto] + (self.descuentos[elproducto] * self.precios[elproducto] / 100 )

    def obtener_precio_sdescuento(self,elproducto):
        return self.precios[elproducto]

class AlmacenTestCase(unittest.TestCase):

    def setUp(self):        
        self.MiCompra = CajaRegistradora()
        producto1 = Producto('manzana')
        producto2 = Producto('banana')
        producto3 = Producto('kiwi')
        producto4 = Producto('pera')
        self.MiListaProductos = [producto1, producto2, producto3, producto4]
        
        self.MilistaPrecios = ListaPrecios()
        self.MilistaPrecios.cargar_precio_para(producto1, 3.5)
        self.MilistaPrecios.cargar_precio_para(producto2, 4.5)
        self.MilistaPrecios.cargar_precio_para(producto3, 6.0)
        self.MilistaPrecios.cargar_precio_para(producto4, 3.75)
        
        self.MilistaPrecios.cargar_descuento_para(producto1, 10) 
        self.MilistaPrecios.cargar_descuento_para(producto3, 15)


        self.caja = CajaRegistradora(self.Lista, self.Milista)

    def test_comprar_1_producto(self):
        unProducto = self.Compra.agregar_producto_escaneado('banana')
        #pagar = 100-self.micompra.finalizar_compra()
        #self.assertEqual(95.5,pagar)

    """def test_comprar_2_productos_sin_descuento(self):
        self.micompra.agregar_producto_escaneado('banana')
        self.micompra.agregar_producto_escaneado('pera')
        pagar = 100-self.micompra.finalizar_compra()
        self.assertEqual(91.75,pagar)

    def test_comprar_2_productos_con_descuento(self):
        self.micompra.agregar_producto_escaneado('manzana')
        self.micompra.agregar_producto_escaneado('banana')
        pagar = 100-self.micompra.finalizar_compra()
        self.assertEqual(92.35,pagar)

    def test_comprar_5_productos_con_descuento(self):
        self.micompra.agregar_producto_escaneado('manzana')
        self.micompra.agregar_producto_escaneado('banana')
        self.micompra.agregar_producto_escaneado('kiwi')
        self.micompra.agregar_producto_escaneado('pera')
        self.micompra.agregar_producto_escaneado('kiwi')
        pagar = 100-self.micompra.finalizar_compra()
        self.assertEqual(78.4,pagar)

    def test_comprar_1_producto2(self):
        self.micompra.agregar_producto_escaneado('pera') #Compra.productos.get()
        pagar = 100-self.micompra.finalizar_compra()
        self.assertEqual(96.25,pagar)"""


if __name__ == '__main__':
    unittest.main()
