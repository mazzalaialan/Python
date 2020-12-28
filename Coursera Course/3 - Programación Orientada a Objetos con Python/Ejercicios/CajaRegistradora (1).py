import unittest

class CompraCerrada(Exception):
    pass

class DatosProductoIvalidos(Exception):
    pass

class DatosClienteIvalidos(Exception):
    pass

class CodigoInexistente(Exception):
    pass


class MontoInsuficiente(Exception):
    pass

class ListaPrecios(object):

    def __init__(self):
        self.productos = []
        self.descuentos = {}

    def agregar_descuento(self, codigo, descuento):
        try:
            self.obtener_producto_con_codigo(codigo)      
            self.descuentos[codigo] = descuento
        except CodigoInexistente:
            print("El codigo hace referencia a un producto inexistente!")

    def agregar_producto(self, nombre, valor, codigo):
        if valor >= 0 and codigo >= 0:
            self.productos.append(Producto(nombre, valor, codigo))

    def obtener_producto_con_codigo(self, codigo):
        producto_a_devolver = None
        for producto in self.productos:
            if producto.codigo == codigo:
                producto_a_devolver = producto
                break
        else:
            raise CodigoInexistente
        return producto_a_devolver

    def obtener_precio_con_descuento(self,codigo):
        return self.productos[codigo]['Valor'] + (self.descuentos[codigo] * self.productos[codigo]['Valor'] / 100 )

    def obtener_precio_sin_descuento(self,codigo):
        return self.productos.get(Producto(valor))

class Producto(object):
    def __init__(self, nombre, valor, codigo):
        if len(nombre) < 1 or valor < 0 or codigo < 0:
            raise DatosProductoIvalidos
        self.nombre = nombre
        self.valor = valor
        self.codigo = codigo

    def __repr__(self):
        return f"{self.nombre.capitalize()}: Valor: {self.valor}, Codigo: {self.codigo}"

class Compra(object):

    def __init__(self, monto):
        if monto < 0:
            raise DatosClienteIvalidos
        self.monto = monto

    def pagar(self):
        return self.monto

class CajaRegistradora(object):

    def __init__(self, compra): #sistema,
        self.lista_productos = []
        #self.sistema = sistema
        self.compra = compra
        self.cerrada = False

    def escanear_producto(self, codigo):
        if self.cerrada:
            raise CompraCerrada 
        try:
            producto = self.sistema.obtener_producto_con_codigo(codigo)
            return self.agregar_a_lista(producto)
        except CodigoInexistente:
            print("El codigo hace referencia a un producto inexistente!")

    def agregar_a_lista(self, producto):
        print("Se agrego el producto: ", producto)
        self.lista_productos.append(producto)
        return self.devolver_subtotal()

    def devolver_subtotal(self):
        if self.cerrada:
            raise CompraCerrada 
        return sum([producto.valor for producto in self.lista_productos])

    def calcular_vuelto(self, pago_cliente, monto_a_cobrar):
        if (pago_cliente - monto_a_cobrar) < 0:
            raise MontoInsuficiente
        return (pago_cliente - monto_a_cobrar)

    def finalizar_compra(self):
        if self.cerrada:
            raise CompraCerrada 
        self.aplicar_descuentos()
        try:
            vuelto = self.calcular_vuelto(self.compra.pagar(), self.devolver_subtotal())
            self.compra.monto = vuelto 
            self.cerrada = True
            return vuelto   
        except MontoInsuficiente:
            print("El cliente no dispone de dinero suficiente")

    def aplicar_descuentos(self):
        # si hay descuentos, recorro todos los productos que compro el cliente
        # y si hay un descuento para ese producto, se lo aplico
        if len(self.sistema.descuentos) > 0:
            for producto in self.lista_productos:
                if producto.codigo in self.sistema.descuentos:
                    producto.valor *= self.sistema.descuentos[producto.codigo]

class AlmacenTestCase(unittest.TestCase):

    def setUp(self):
        self.lista = ListaPrecios()
        self.compra = Compra(100)
        self.caja = CajaRegistradora(self.lista,self.compra)

    def test_comprar_un_producto(self):
        self.lista.agregar_producto("Queso", 100, 1)
        self.caja.escanear_producto(1)
        self.assertEqual(100,self.caja.devolver_subtotal())

    def test_intentar_cargar_producto_inexistente(self):
        with self.assertRaises(CodigoInexistente):
            self.lista.obtener_producto_con_codigo(2)

    def test_creo_un_producto_con_datos_invalidos(self):
        with self.assertRaises(DatosProductoIvalidos):
            Producto("",120,-20)

    def test_comprar_un_producto_existente_y_otro_no(self):
        self.lista.agregar_producto("Gaseosa", 150, 12)
        self.caja.escanear_producto(12)
        with self.assertRaises(CodigoInexistente):
            self.lista.obtener_producto_con_codigo(10)
        self.assertEqual(150,self.caja.devolver_subtotal())

    def test_crear_un_cliente_con_datos_invalidos(self):
        with self.assertRaises(DatosClienteIvalidos):
            Compra(-20)

    def test_comprar_3_productos(self):
        self.lista.agregar_producto("Gaseosa", 150, 12)
        self.lista.agregar_producto("Papas fritas", 40, 11)
        self.lista.agregar_producto("Pizza", 300, 2)
        self.caja.escanear_producto(12)
        self.caja.escanear_producto(11)
        self.caja.escanear_producto(2)

        self.assertEqual(510,self.caja.finalizar_compra())

    def test_comprar_2_productos_sin_suficiente_dinero(self):
        self.lista.agregar_producto("Lavandina", 110, 5)
        self.lista.agregar_producto("Cerveza", 600, 14)
        self.caja.escanear_producto(14)
        self.caja.escanear_producto(5)

        self.caja.compra.monto = 20

        with self.assertRaises(MontoInsuficiente):
            self.caja.calcular_vuelto(self.caja.compra.monto, self.caja.devolver_subtotal())

    def test_se_cobro_correctamente(self):

        self.lista.agregar_producto("Mortadela", 100, 25)
        self.lista.agregar_producto("Cerveza", 600, 14)
        self.caja.escanear_producto(14)
        self.caja.escanear_producto(25)

        self.assertEqual(self.caja.finalizar_compra(),self.caja.compra.monto)

    def test_la_caja_cierra_correctamente(self):

        self.lista.agregar_producto("Mortadela", 100, 25)
        self.lista.agregar_producto("Cerveza", 600, 14)
        self.caja.escanear_producto(14)
        self.caja.escanear_producto(25)

        self.caja.finalizar_compra()

        self.assertEqual(True,self.caja.cerrada)

    def test_luego_de_cerrar_la_caja_no_puedo_escanear_productos(self):

        self.lista.agregar_producto("Mortadela", 100, 25)
        self.lista.agregar_producto("Cerveza", 600, 14)
        self.lista.agregar_producto("Galletitas", 20, 4)
        self.caja.escanear_producto(14)
        self.caja.escanear_producto(25)

        self.caja.finalizar_compra()

        with self.assertRaises(CompraCerrada):
            self.caja.escanear_producto(4)

    def test_no_puedo_cerrar_la_caja_2_veces(self):

        self.lista.agregar_producto("Mortadela", 100, 25)
        self.lista.agregar_producto("Cerveza", 600, 14)
        self.lista.agregar_producto("Galletitas", 20, 4)
        self.caja.escanear_producto(14)
        self.caja.escanear_producto(25)

        self.caja.finalizar_compra()

        with self.assertRaises(CompraCerrada):
            self.caja.finalizar_compra()

    def test_se_aplican_los_descuentos(self):

        self.lista.agregar_producto("Mortadela", 100, 25)
        self.lista.agregar_producto("Cerveza", 600, 14)
        self.lista.agregar_producto("Galletitas", 20, 4)
        self.lista.agregar_descuento(14,0.5)
        self.caja.escanear_producto(14)
        self.caja.escanear_producto(25)
        self.caja.escanear_producto(4)
        
        self.assertEqual(580,self.caja.finalizar_compra())

    def test_no_puedo_aplicarle_descuento_a_un_producto_inexistente(self):

        self.lista.agregar_producto("Mortadela", 100, 25)
        self.lista.agregar_producto("Cerveza", 600, 14)
        self.lista.agregar_producto("Galletitas", 20, 4)
        self.lista.agregar_descuento(14,0.5)
        
        with self.assertRaises(CodigoInexistente):
            self.lista.obtener_producto_con_codigo(220)
            
    
unittest.main()
