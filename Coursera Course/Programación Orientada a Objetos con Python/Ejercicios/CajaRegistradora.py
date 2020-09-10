import unittest


class CajaCerrada(Exception):
    """
    La caja esta cerrada y no se pueden agregar mas productos
    """
    pass

class DatosProductoIvalidos(Exception):
    """
    Los datos ingresados para crear un producto son invalidos
    """
    pass

class DatosClienteIvalidos(Exception):
    """
    Los datos ingresados para crear un cliente son invalidos
    """
    pass

class CodigoInvalido(Exception):
    """
    No existe un producto con el codigo ingresado
    """
    pass


class MontoInsuficiente(Exception):
    """
    El cliente no dipone de dinero suficiente para realizar la compra
    """
    pass


class Cliente():
    """
    Almacena el monto que tiene disponible para pagar
    
    Atributos:
        monto(int): cantidad de dinero disponible

    Metodos:
        pagar(int): devuelve el monto 
    """
    def __init__(self, monto):
        if monto < 0:
            raise DatosClienteIvalidos
        self.monto = monto

    def pagar(self):
        return self.monto


class Sistema():
    """
    Almacena los productos disponibles para comprar y los descuentos 
    que existen

    Atributos:
        productos(list): lista de productos disponibles
        descuentos(dict): lista de descuentos disponibles

    Metodos:
        agregar_descuento(void): agrega un descuento a "descuentos"
        agregar_producto(void): agrega un producto a "productos"
        obtener_producto_con_codigo(Producto): devuelve el producto que posee determinado codigo
    """

    def __init__(self):
        self.productos = []
        self.descuentos = {}

    def agregar_descuento(self, codigo, descuento):
        try:
            # si existe el producto con ese codigo, creo el descuento
            # sino, capturo la excepcion CodigoInvalido
            self.obtener_producto_con_codigo(codigo)      
            self.descuentos[codigo] = descuento
        except CodigoInvalido:
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
            raise CodigoInvalido

        return producto_a_devolver


class Producto():
    """
    Representa un producto que el cliente puede comprar

    Atributos:
        nombre(str): nombre del producto
        valor(float): valor del producto
        codigo(int): codigo del producto

    Metodos:
        ---
    """
    def __init__(self, nombre, valor, codigo):
        if len(nombre) < 1 or valor < 0 or codigo < 0:
            raise DatosProductoIvalidos
        self.nombre = nombre
        self.valor = valor
        self.codigo = codigo

    def __repr__(self):
        return f"{self.nombre.capitalize()}: Valor: {self.valor}, Codigo: {self.codigo}"


class CajaRegistradora():
    """
    Representa el medio por el que el cliente puede acceder a productos

    Atributos:
        lista_productos(list): productos comprados por el usuario
        sistema(Sistema): Objeto sistema 
        cliente(Cliente): Objeto cliente
        cerrada(boolean): representa si la caja esta cerrada o no

    Metodos:
        escanear_producto(float): llama a agregar_a_lista() si el codigo es valido
        agregar_a_lista(float): agrega un producto a lista_productos
        devolver_subtotal(float): devuelve la suma de valores de los productos en lista_productos
        finalizar_compra(float): cierra la caja, llama a aplicar_descuentos() y devuelve el vuelto
        aplicar_descuentos(void): si existen, aplica los descuentos correspondientes a los productos en lista_productos
        calcular_vuelto(float): calcula el vuelto que se le dara al cliente
    """

    def __init__(self, sistema, cliente):
        self.lista_productos = []
        self.sistema = sistema
        self.cliente = cliente
        self.cerrada = False

    def escanear_producto(self, codigo):
        if self.cerrada:
            raise CajaCerrada 

        try:
            # si el producto existe en el sistema, lo agrego a la lista de productos
            # comprados por el cliente, y luego devuelvo el subtotal
            producto = self.sistema.obtener_producto_con_codigo(codigo)
            return self.agregar_a_lista(producto)
        except CodigoInvalido:
            print("El codigo hace referencia a un producto inexistente!")

    def agregar_a_lista(self, producto):
        print("Se agrego el producto: ", producto)
        self.lista_productos.append(producto)
        return self.devolver_subtotal()

    def devolver_subtotal(self):
        if self.cerrada:
            raise CajaCerrada 

        return sum([producto.valor for producto in self.lista_productos])


    def finalizar_compra(self):
        if self.cerrada:
            raise CajaCerrada 

        self.aplicar_descuentos()
        try:
            # calculo el vuelto que le tengo que dar al cliente, ese sera su nuevo monto
            # si no tiene suficiente se captura una excepcion
            # luego cierro la caja
            vuelto = self.calcular_vuelto(self.cliente.pagar(), self.devolver_subtotal())
            self.cliente.monto = vuelto 
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

    def calcular_vuelto(self, pago_cliente, monto_a_cobrar):
        if (pago_cliente - monto_a_cobrar) < 0:
            raise MontoInsuficiente
        return (pago_cliente - monto_a_cobrar)


class Pruebas(unittest.TestCase):

    def setUp(self):
        self.cliente = Cliente(1000)
        self.sistema = Sistema()
        self.caja = CajaRegistradora(self.sistema,self.cliente)

    def test_comprar_un_producto(self):
        self.sistema.agregar_producto("Queso", 100, 1)
        self.caja.escanear_producto(1)
        self.assertEqual(100,self.caja.devolver_subtotal())

    def test_intentar_cargar_producto_inexistente(self):
        with self.assertRaises(CodigoInvalido):
            self.sistema.obtener_producto_con_codigo(2)

    def test_creo_un_producto_con_datos_invalidos(self):
        with self.assertRaises(DatosProductoIvalidos):
            Producto("",120,-20)

    def test_comprar_un_producto_existente_y_otro_no(self):
        self.sistema.agregar_producto("Gaseosa", 150, 12)
        self.caja.escanear_producto(12)
        with self.assertRaises(CodigoInvalido):
            self.sistema.obtener_producto_con_codigo(10)
        self.assertEqual(150,self.caja.devolver_subtotal())

    def test_crear_un_cliente_con_datos_invalidos(self):
        with self.assertRaises(DatosClienteIvalidos):
            Cliente(-20)

    def test_comprar_3_productos(self):
        self.sistema.agregar_producto("Gaseosa", 150, 12)
        self.sistema.agregar_producto("Papas fritas", 40, 11)
        self.sistema.agregar_producto("Pizza", 300, 2)
        self.caja.escanear_producto(12)
        self.caja.escanear_producto(11)
        self.caja.escanear_producto(2)

        self.assertEqual(510,self.caja.finalizar_compra())

    def test_comprar_2_productos_sin_suficiente_dinero(self):
        self.sistema.agregar_producto("Lavandina", 110, 5)
        self.sistema.agregar_producto("Cerveza", 600, 14)
        self.caja.escanear_producto(14)
        self.caja.escanear_producto(5)

        self.caja.cliente.monto = 20

        with self.assertRaises(MontoInsuficiente):
            self.caja.calcular_vuelto(self.caja.cliente.monto, self.caja.devolver_subtotal())

    def test_se_cobro_correctamente(self):

        self.sistema.agregar_producto("Mortadela", 100, 25)
        self.sistema.agregar_producto("Cerveza", 600, 14)
        self.caja.escanear_producto(14)
        self.caja.escanear_producto(25)

        self.assertEqual(self.caja.finalizar_compra(),self.caja.cliente.monto)

    def test_la_caja_cierra_correctamente(self):

        self.sistema.agregar_producto("Mortadela", 100, 25)
        self.sistema.agregar_producto("Cerveza", 600, 14)
        self.caja.escanear_producto(14)
        self.caja.escanear_producto(25)

        self.caja.finalizar_compra()

        self.assertEqual(True,self.caja.cerrada)

    def test_luego_de_cerrar_la_caja_no_puedo_escanear_productos(self):

        self.sistema.agregar_producto("Mortadela", 100, 25)
        self.sistema.agregar_producto("Cerveza", 600, 14)
        self.sistema.agregar_producto("Galletitas", 20, 4)
        self.caja.escanear_producto(14)
        self.caja.escanear_producto(25)

        self.caja.finalizar_compra()

        with self.assertRaises(CajaCerrada):
            self.caja.escanear_producto(4)

    def test_no_puedo_cerrar_la_caja_2_veces(self):

        self.sistema.agregar_producto("Mortadela", 100, 25)
        self.sistema.agregar_producto("Cerveza", 600, 14)
        self.sistema.agregar_producto("Galletitas", 20, 4)
        self.caja.escanear_producto(14)
        self.caja.escanear_producto(25)

        self.caja.finalizar_compra()

        with self.assertRaises(CajaCerrada):
            self.caja.finalizar_compra()

    def test_se_aplican_los_descuentos(self):

        self.sistema.agregar_producto("Mortadela", 100, 25)
        self.sistema.agregar_producto("Cerveza", 600, 14)
        self.sistema.agregar_producto("Galletitas", 20, 4)
        self.sistema.agregar_descuento(14,0.5)
        self.caja.escanear_producto(14)
        self.caja.escanear_producto(25)
        self.caja.escanear_producto(4)
        
        self.assertEqual(580,self.caja.finalizar_compra())

    def test_no_puedo_aplicarle_descuento_a_un_producto_inexistente(self):

        self.sistema.agregar_producto("Mortadela", 100, 25)
        self.sistema.agregar_producto("Cerveza", 600, 14)
        self.sistema.agregar_producto("Galletitas", 20, 4)
        self.sistema.agregar_descuento(14,0.5)
        
        with self.assertRaises(CodigoInvalido):
            self.sistema.obtener_producto_con_codigo(220)
            
    
unittest.main()
