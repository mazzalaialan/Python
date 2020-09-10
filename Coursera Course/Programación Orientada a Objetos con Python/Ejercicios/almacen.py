"""
Para este proyecto, deberás programar una caja registradora para una almacén. El sistema debe poder escanear 
un producto (el cajero puede tipear el código del producto), y agregarlo a la lista de productos comprados 
para ese cliente. Además debe mostrar el subtotal. El cajero cuando lo desee puede finalizar la compra y el 
sistema deberá aplicar los descuentos correspondientes a los productos. Luego, el cajero indica con cuánto 
paga el cliente y el sistema debe mostrar el cambio que debe devolver al cliente.
"""

import unittest

class Producto:
    """
    Define un producto con codigo y precio
    """
    def __init__(self, codigo, precio):
        self.codigo = codigo
        self.precio = precio

class CajaRegistradora:
    """
    Define un carrito de compra con cliente y productos
    """
    def __init__(self, cliente, productos):
        self.cliente = cliente
        self.productos = productos

    # Agrega productos en tupla producto-precio
    def agregarProducto(self, producto, precio):
        self.productos.append([producto, precio])
        return self.productos

    # Calcula subtotal recorriendo el carrito de productos y multiplicando precio unitario por cantidad comprada
    def calcularSubtotal(self):
        suma = 0
        for i in range(len(self.productos)):
                suma += self.productos[i][0].precio * self.productos[i][1]
        return suma

    # Finaliza la compra, efectuando un descuento del 5% sobre el total
    def finalizarCompra(self):
        subtotalConDescuentos = self.calcularSubtotal() * 0.95
        return subtotalConDescuentos

    # Paga el subtotal con descuento, devuelvo vuelto
    def pagarYdarVuelto(self, montoRecibido):
        while montoRecibido < self.calcularSubtotal() * 0.95:
            #print("El importe no cubre el total de $", self.calcularSubtotal() * 0.95)
            vuelto = 0
            break
        else:
            vuelto = montoRecibido - self.calcularSubtotal() * 0.95
        return vuelto

class testAlmacen(unittest.TestCase):
    def setUp(self):
        self.carrito = CajaRegistradora("Roberto",[])
        self.producto1 = Producto('0001',105)
        self.producto2 = Producto('0002',230)
        self.producto3 = Producto('0003',580)
        self.carrito.agregarProducto(self.producto1,10)
        self.carrito.agregarProducto(self.producto2,20)
        self.carrito.agregarProducto(self.producto3,8)

    def testProductoCodigo(self):
        prod = self.producto1
        self.assertEqual('0001',prod.codigo)

    def testProductoPrecio(self):
        prod = self.producto2
        self.assertEqual(230,prod.precio)

    def testNuevaCajaRegistradora(self):
        carr = self.carrito
        self.assertEqual('Roberto',carr.cliente)

    def testPrecioAgregarProducto(self):
        agregarProd = self.carrito.agregarProducto(self.producto1,5)
        self.assertEqual(105,self.carrito.productos[0][0].precio)

    def testCantidadAgregarProducto(self):
        agregarProd = self.carrito.agregarProducto(Producto('0004',800),11)
        self.assertEqual(11,self.carrito.productos[-1][1]) 

    def testCalcularSubtotal(self):
        calcularSubtotal = self.carrito.calcularSubtotal()
        self.assertEqual(10290,calcularSubtotal)

    def testFinalizarCompra(self):
        calcularSubtotalConDesc = self.carrito.finalizarCompra()
        self.assertEqual(9775.5,calcularSubtotalConDesc)

    def testPago(self):
        vuelto = self.carrito.pagarYdarVuelto(10000)
        self.assertEqual(224.5,vuelto)

    def testPagoInsuficiente(self):
        vuelto = self.carrito.pagarYdarVuelto(5000)
        self.assertEqual(0,vuelto)


if __name__ == "__main__":
    unittest.main()