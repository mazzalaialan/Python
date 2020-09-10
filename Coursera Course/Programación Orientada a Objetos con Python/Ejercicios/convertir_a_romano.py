# -*- coding: utf-8 -*-
import unittest

class NumeroRomano(object):

    valores = [1000,900,500,400,100,90,50,40,10,9,5,4,1]
    simbolos = ['M','CM','D','CD','C','XC','L','XL','X','IX','V','IV','I']

    def convertir_a_romano(self,numero):
        resto = numero
        numero_romano = ''
        for i in range(len(self.valores)):
            numero_romano,resto = self.agregar_numero_romano(resto,self.valores[i],self.simbolos[i],numero_romano)
        return numero_romano

    def agregar_numero_romano(self,numero,valor,simbolo,numero_romano):
        resto = numero
        while resto >= valor:
            numero_romano = numero_romano + simbolo
            resto -= valor
        return numero_romano, resto

class NumeroRomanoTestCase(unittest.TestCase):

    def setUp(self):
        self.numero_romano = NumeroRomano()

    def test_convertir_a_romano_1(self):
        numero_romano = self.numero_romano.convertir_a_romano(1)
        self.assertEqual('I',numero_romano)

    def test_convertir_a_romano_4(self):
        numero_romano = self.numero_romano.convertir_a_romano(4)
        self.assertEqual('IV',numero_romano)

    def test_convertir_a_romano_5(self):
        numero_romano = self.numero_romano.convertir_a_romano(5)
        self.assertEqual('V',numero_romano)

    def test_convertir_a_romano_8(self):
        numero_romano = self.numero_romano.convertir_a_romano(8)
        self.assertEqual('VIII',numero_romano)

    def test_convertir_a_romano_9(self):
        numero_romano = self.numero_romano.convertir_a_romano(9)
        self.assertEqual('IX',numero_romano)

    def test_convertir_a_romano_10(self):
        numero_romano = self.numero_romano.convertir_a_romano(10)
        self.assertEqual('X',numero_romano)

    def test_convertir_a_romano_30(self):
        numero_romano = self.numero_romano.convertir_a_romano(30)
        self.assertEqual('XXX',numero_romano)

    def test_convertir_a_romano_40(self):
        numero_romano = self.numero_romano.convertir_a_romano(40)
        self.assertEqual('XL',numero_romano)

    def test_convertir_a_romano_50(self):
        numero_romano = self.numero_romano.convertir_a_romano(50)
        self.assertEqual('L',numero_romano)

    def test_convertir_a_romano_51(self):
        numero_romano = self.numero_romano.convertir_a_romano(51)
        self.assertEqual('LI',numero_romano)

    def test_convertir_a_romano_90(self):
        numero_romano = self.numero_romano.convertir_a_romano(90)
        self.assertEqual('XC',numero_romano)

    def test_convertir_a_romano_100(self):
        numero_romano = self.numero_romano.convertir_a_romano(100)
        self.assertEqual('C',numero_romano)

    def test_convertir_a_romano_400(self):
        numero_romano = self.numero_romano.convertir_a_romano(400)
        self.assertEqual('CD',numero_romano)

    def test_convertir_a_romano_500(self):
        numero_romano = self.numero_romano.convertir_a_romano(500)
        self.assertEqual('D',numero_romano)

    def test_convertir_a_romano_637(self):
        numero_romano = self.numero_romano.convertir_a_romano(637)
        self.assertEqual('DCXXXVII',numero_romano)

    def test_convertir_a_romano_900(self):
        numero_romano = self.numero_romano.convertir_a_romano(900)
        self.assertEqual('CM',numero_romano)

    def test_convertir_a_romano_978(self):
        numero_romano = self.numero_romano.convertir_a_romano(978)
        self.assertEqual('CMLXXVIII',numero_romano)

    def test_convertir_a_romano_1000(self):
        numero_romano = self.numero_romano.convertir_a_romano(1000)
        self.assertEqual('M',numero_romano)

if __name__ == '__main__':
    unittest.main()
