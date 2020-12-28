#Programa que administra una caja registradora
import unittest

class Producto():
    def __init__(self, codigo, nombre, valor,descuento):
        self._codigo = codigo
        self._nombre = nombre
        self._valor = valor
        self._descuento = valor
        
    def precio_con_descuento(self):
       return self._valor * descuento

class ListarProducto():
    def __init__(self):
        self._listar = []
        self._caja = Caja(self._listar)

class ListarPrecio():
    def __init__(self):
        self._lista_Precio = []
        for produc in ListarProducto()._listar:
            self._lista_Precio.append(Producto.precio_con_descuento)

class Caja():
    def __init__ (self, listaProductos):
        self._productos = listaProductos
        self._compra = []

    def agregar_producto(self, codigo):
        for produc in self._productos:
            if(produc._codigo) == (codigo):
                self.cesta.append(produc)
            print("Se ha agregado el siguiente producto: {produc._nombre} ")

    def compra_total(self, descuento):
        sumaTotal=0
        for produc in self._compra:
            sumaTotal += produc.obtenerPrecioConDescuento()
        print("El subtotal de la compra es: " + sumaTotal)
        return sumaTotal

    def compra_final(self, descuento):
        total = 0
        for produc in self._compra:
            total += produc._valor * produc.descuento
        print("El total de la compra es: " + total)
        return total

    def finalizar_compra(self):
        totalCompra = self.compra_final(True)
        print("Compra finalizada")
        return totalCompra

    def realizar_pago(self, total_compra, pago):
        print("Pago confirmado")
        if total_compra > pago:
            print("Error, pago insuficiente")
            return False
        else:
            print("Se ha generado su compra")
            cambio = pago - total_compra
            print("Su vuelto es de: " + cambio)
            return True, cambio

class GerandoPruebas(unittest.TestCase):

    def setUp(self):
        self.ListarProducto = [Producto(100,"Notebook",170000,30),Producto(110,"Impresoras",95000,30)]
        self.caja = Caja(self.ListarProducto)
    
    def realizar_compra(self):
        compra = self.caja
        compra.agregar_producto(100)
        compra.agregar_producto(110)
        self.assertEqual (2,len(compra._compra))

    def realizar_descuento(self):
        compra = self.caja
        compra.agregar_producto(100)
        compra.agregar_producto(110)
        total = Caja.compra_total(True)
        self.assertEqual (130000, total)

    def finalizar_compra(self):
        compra = self.caja
        compra.agregar_producto(100)
        compra.agregar_producto(110)
        total = Caja.finalizar_compra()
        self.assertEqual(130000, total)
    
    def compra_final(self):
        compra = self.caja
        compra.agregar_producto(100)
        compra.agregar_producto(110)
        total = Caja.compra_final()
        self.assertEqual(130000, total)

if __name__ == "__main__":
    unittest.main()