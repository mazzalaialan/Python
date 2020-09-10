import unittest

class Producto():
    """Verificar si en el modelo de tu compañero, existe una clase que represente un producto."""
    def __init__(self, codigo, precio, descuento):
        self.codigo = codigo
        self.precio = precio
        self.descuento = descuento

    def obtenerPrecioSinDescuento(self):
        return self.precio

    def obtenerPrecioConDescuento(self):
        return self.precio - (self.precio * self.descuento / 100)

class ListaPrecio():
    """Verificar si en el modelo de tu compañero, existe una clase que represente una lista de precios"""

    def __init__(self):
        self.precios = {}
        self.descuentos = {}

    def actualizar_lista(self,productos):
        for p in productos:
            self.agregar_precio(p)

    def agregar_precio(self,producto):
        self.precios[producto.codigo] = producto.precio
        self.descuentos[producto.codigo] = producto.descuento

    def obtener_precios_sin_descuento(self,producto):
        """Verificar si en el modelo de tu compañero, la clase que representa la lista de precios tiene un método para obtener el precio de un producto sin descuento."""
        return self.precios[producto.codigo]

    def obtener_precios_con_descuento(self,producto):
        """Verificar si en el modelo de tu compañero, la clase que representa la lista de precios tiene un método para obtener el precio de un producto sin descuento."""
        return self.precios[producto.codigo] - (self.descuentos[producto.codigo] * self.precios[producto.codigo] / 100 )

class CajaRegistradora():
    """Verificar si en el modelo que hizo tu compañero, existe una clase que representa la caja registradora"""

    def __init__ (self, listaProductos):
        self.productos = listaProductos
        self.cesta = []

    def agregarProducto(self, codigoprod):
        """Verificar si en el modelo de tu compañero, la clase que representa la caja registradora tiene un método para agregar un producto escaneado a la compra"""
        for producto in self.productos:
            if(producto.codigo) == (codigoprod):
                self.cesta.append(producto)
            print("El procuto {producto.codigo} fue agregado a la cesta")

    def calcular_subtotal(self, descuento):
        """Verificar si en el modelo de tu compañero,  la clase que representa la caja registradora tiene un método para calcular el subtotal de la compra."""
        sumaTotal=0
        for producto in self.cesta:
            if descuento:
                sumaTotal += producto.obtenerPrecioConDescuento()
            else:
                sumaTotal += producto.obtenerPrecioSinDescuento()
        print("El subtotal de la compra es: " + str(sumaTotal))
        return sumaTotal

    def finalizarCompra(self):
        """Verificar si en el modelo de tu compañero, la clase que representa la caja registradora tiene un método para finalizar la compra"""
        totalCompra = self.calcular_total(True)
        print("Compra finalizada")
        return totalCompra

    def calcular_total(self, descuento):
        """Verificar si en el modelo de tu compañero, la clase que representa la caja registradora tiene un método para calcular el total de la compra."""
        total = 0
        for producto in self.cesta:
            total += producto.precio - (producto.precio * producto.descuento / 100)
        print("El total de la compra es: " + str(total))
        return total

    def Pagar(self, compraTotal, pago):
        """Verificar si en el modelo de tu compañero, la clase que representa la caja registradora tiene un método para indicar con cuánto paga el cliente e indica cuánto debe devolverle."""
        print("Pago confirmado... ")
        if compraTotal > pago:
            print("Error, tu pago no fue sufuciente")
            print("Debes para un monto por encima o igual al total")
            return False
        else:
            print("Compra realizada satisfactoriamente")
            cambio = pago - compraTotal
            print("Tu cambio es de: " + str(cambio))
            return True, cambio


class Compra(CajaRegistradora):
    """Verificar si en el modelo de tu compañero, existe una clase que represente la compra."""
    pass

class AlmacenTestCase(unittest.TestCase):
    def setUp(self):
        self.listaProductos = [Producto("Manzana", 10.00, 10),
                            Producto("Banana", 15.00, 15),
                            Producto("Kiwi", 20.00, 0),
                            Producto("Anana", 17.00, 20),
                            Producto("Pera", 12.00, 10),
                            Producto("Palta", 40.00, 0),
                            Producto("Tomate", 25.00, 0)]
        #self.ListaPrecio.actualizar_lista(self.listaProductos)
        self.cajaRegistradora = CajaRegistradora(self.listaProductos)

    def test01_agregar_1_producto_cesta(self):
        """Verificar si en el modelo de tu compañero, hay casos de prueba sobre el método que agrega un producto a la compra."""
        cajaRegistradora = self.cajaRegistradora
        cajaRegistradora.agregarProducto("Manzana")
        self.assertEqual (1, len(cajaRegistradora.cesta))

    def test02_calcular_totalCompra_conDescuento(self):
        """Verificar si en el modelo de tu compañero, hay casos de prueba sobre el método  que calcula el subtotal de la compra."""
        cajaRegistradora = self.cajaRegistradora
        cajaRegistradora.agregarProducto("Manzana")
        cajaRegistradora.agregarProducto("Banana")
        cajaRegistradora.agregarProducto("Kiwi")
        cajaRegistradora.agregarProducto("Anana")
        cajaRegistradora.agregarProducto("Pera")
        total = cajaRegistradora.calcular_subtotal(True)
        self.assertEqual(round(66.15,2), round(total,2))

    def test02_calcular_totalCompra_sinDescuento(self):
        """Verificar si en el modelo de tu compañero, hay casos de prueba sobre el método  que calcula el subtotal de la compra."""
        cajaRegistradora = self.cajaRegistradora
        cajaRegistradora.agregarProducto("Manzana")
        cajaRegistradora.agregarProducto("Banana")
        cajaRegistradora.agregarProducto("Kiwi")
        cajaRegistradora.agregarProducto("Anana")
        cajaRegistradora.agregarProducto("Pera")
        total = cajaRegistradora.calcular_subtotal(False)
        self.assertEqual(round(74.00,2), round(total,2))

    def test03_finalizarCompra(self):
        """Verificar si en el modelo de tu compañero, hay casos de prueba sobre el método que finaliza la compra."""
        cajaRegistradora = self.cajaRegistradora
        cajaRegistradora.agregarProducto("Manzana")
        cajaRegistradora.agregarProducto("Banana")
        cajaRegistradora.agregarProducto("Kiwi")
        cajaRegistradora.agregarProducto("Anana")
        cajaRegistradora.agregarProducto("Pera")
        total = cajaRegistradora.finalizarCompra()
        self.assertEqual(round(66.15,2), round(total,2))

    def test04_compraFinal(self):
        """Verificar si en el modelo de tu compañero, hay casos de prueba sobre el método  que calcula el total de la compra (con los descuentos aplicados)"""
        cajaRegistradora = self.cajaRegistradora
        cajaRegistradora.agregarProducto("Manzana")
        cajaRegistradora.agregarProducto("Banana")
        cajaRegistradora.agregarProducto("Kiwi")
        cajaRegistradora.agregarProducto("Anana")
        cajaRegistradora.agregarProducto("Pera")
        total = cajaRegistradora.calcular_total(True)
        self.assertEqual(round(66.15,2), round(total,2))

    def test05_hacercompra_fallida(self):
        """Verificar si en el modelo de tu compañero, hay casos de prueba sobre el método que calcula el vuelto que se le debe dar al cliente."""
        cajaRegistradora = self.cajaRegistradora
        cajaRegistradora.agregarProducto("Manzana")
        cajaRegistradora.agregarProducto("Banana")
        cajaRegistradora.agregarProducto("Kiwi")
        cajaRegistradora.agregarProducto("Anana")
        cajaRegistradora.agregarProducto("Pera")
        total = cajaRegistradora.finalizarCompra()
        pago = 60.00
        fallo = cajaRegistradora.Pagar(total, pago)
        self.assertFalse(fallo)

    def test06_hacercompra_bien(self):
        """Verificar si en el modelo de tu compañero, hay casos de prueba sobre el método que calcula el vuelto que se le debe dar al cliente."""
        cajaRegistradora = self.cajaRegistradora
        cajaRegistradora.agregarProducto("Manzana")
        cajaRegistradora.agregarProducto("Banana")
        cajaRegistradora.agregarProducto("Kiwi")
        cajaRegistradora.agregarProducto("Anana")
        cajaRegistradora.agregarProducto("Pera")
        total = cajaRegistradora.finalizarCompra()
        pago = 100.00
        satisf, cambio = cajaRegistradora.Pagar(total, pago)
        self.assertTrue(satisf)
        self.assertEqual(round(33.85,2), round(cambio,2))

if __name__== '__main__':
    unittest.main()