precios1 = {'manzana':3.5,'banana':4.5,'kiwi':6.0,'pera':3.75}
precios2 = dict(manzana=3.5,banana=4.5,kiwi=6.0,pera=3.75)
precios3 = dict([('manzana',3.5),('banana',4.5),('kiwi',6.0),('pera',3.75)])

#agrego y actualizo
precios1['melon'] = 5.75 
precios1['manzana'] = 3.0

#borro
del precios1['kiwi']

#consulto
precios1.get('manzana')

#consulta o la crea con el valor default
precios1.setdefault('coliflor',3.25)

#actualiza, si no existe, la crea con el valor
precios1.update({'manzana':4.0,'pera':4.0})
precios1.update([('manzana',3.75)])

precios1.keys()
precios1.values()
precios1.items()

precios1.pop('melon',0.00)

#saca elemento LIFO
precios1.popitem()

copia_precios = precios1.copy()

precios1.clear()