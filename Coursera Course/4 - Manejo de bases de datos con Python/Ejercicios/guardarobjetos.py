# -*- coding: utf-8 -*-
import sqlite3

DB_PATH = 'C:\\Users\\Alan\\Dropbox\\Alan\\Programacion\\Curso_Python\\Manejo de bases de datos con Python\\Ejercicios\\prueba.db'

class CurrencyDoesNotExists(Exception):
    pass

class CurrencyManager(object):
    def __init__(self,database=None):
        if not database:
            database = ':memory:'
        self.conn = sqlite3.connect(database)
        self.cursor = self.conn.cursor()

    def insert(self,obj):
        query = 'INSERT INTO currency(codigo,nombre,simbolo) VALUES ("{}", "{}", "{}")'.format(obj.code,obj.name,obj.symbol)
        self.cursor.execute(query)
        self.conn.commit()

    def get(self,code):
        query = 'SELECT * FROM currency WHERE codigo="{}"'.format(code)
        self.cursor.execute(query)
        data = self.cursor.fetchone()
        if not data:
            raise CurrencyDoesNotExists("No existe la moneda de codigo {}".format(code))
        return Currency(code=data[1],name=data[2],symbol=data[3])

    def filter(self, **kwargs):
        code = kwargs.get('code')
        name = kwargs.get('name')
        symbol = kwargs.get('symbol')

        condition = ' WHERE '
        add_and = False
        add_condition = False

        if code:
            condition += 'codigo="{}" '.format(code)
            add_condition = True
            add_and = True
        if name:
            if add_and:
                condition += 'AND '
            condition += 'nombre="{}" '.format(name)
            add_condition = True
            add_and = True
        if symbol:
            if add_and:
                condition += 'AND '
            condition += 'simbolo="{}" '.format(symbol)
            add_condition = True
            add_and = True
        
        query = 'SELECT * FROM currency'
        if add_condition:
            query += condition

        self.cursor.execute(query)
        result = self.cursor.fetchall()

        currencies = []
        for data in result:
            currency = Currency(code=data[1],name=data[2],symbol=data[3])
            currencies.append(currency)
        return currencies

    def update(self,old_obj,obj):
        updated = False
        add_comma = False

        query = 'UPDATE currency SET '

        if old_obj.name != obj.name:
            query += 'nombre="{}"'.format(obj.name)
            updated = True
            add_comma = True
        if old_obj.symbol != obj.symbol:
            if add_comma:
                query += ', '
            query += 'simbolo="{}"'.format(obj.symbol)
            updated = True
        
        if updated:
            query += ' WHERE codigo="{}"'.format(obj.code)
            self.cursor.execute(query)
            self.conn.commit()

    def save(self,obj):
        try:
            old_obj = self.get(code=obj.code)
        except CurrencyDoesNotExists:
            self.insert(obj)
        else:
            self.update(old_obj,obj)

    def delete(self,obj):
        query = 'DELETE FROM currency WHERE codigo="{}"'.format(obj.code)
        self.cursor.execute(query)
        self.conn.commit()
            
class Currency(object):
    "Currency Model"
    objects = CurrencyManager(DB_PATH)

    def __init__(self,code,name,symbol):
        self.code = code
        self.name = name
        self.symbol = symbol

    def __repr__(self):
        return u'{}'.format(self.name)

#peso_arg = Currency(code='ARS',name='Pesos Arg',symbol='$')
#dolar = Currency(code='USD',name='Dolar',symbol='U$S')
#euro = Currency(code='EUR',name='Euro',symbol='€')

#Currency.objects.insert(peso_arg)
#Currency.objects.insert(dolar)
#Currency.objects.insert(euro)

#print(Currency.objects.get(code='ARS'))

#print(Currency.objects.filter(code='EUR'))
#print(Currency.objects.filter(name='Dolar'))
#print(Currency.objects.filter(symbol='€'))

#print(Currency.objects.filter())

#pesos_arg = Currency.objects.get(code='ARS')
#Currency.objects.save(pesos_arg)

#pesos_arg = Currency.objects.get(code='ARS')
#print(pesos_arg.code)
#print(pesos_arg.name)
#print(pesos_arg.symbol)

#pesos_arg.name = 'Pesos (ARG)'
#Currency.objects.save(pesos_arg)

#pesos_arg = Currency.objects.get(code='ARS')
#print(pesos_arg.code)
#print(pesos_arg.name)
#print(pesos_arg.symbol)

pesos_uru = Currency(code='UYU',name='Pesos Uruguayos',symbol='$')
Currency.objects.save(pesos_uru)

pesos_uru = Currency.objects.get(code='UYU')
print(pesos_uru.code)
print(pesos_uru.name)
print(pesos_uru.symbol)

Currency.objects.delete(pesos_uru)
pesos_uru = Currency.objects.get(code='UYU')

