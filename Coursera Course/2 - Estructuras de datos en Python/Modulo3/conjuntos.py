frutas = {'manzana','pera','manzana','naranja','naranja','banana','kiwi'}

conjunto = set() #conjunto vacio

a = set('abracadabra') #{'d', 'a', 'c', 'b', 'r'}
b = set('alacazam') #{'a', 'z', 'c', 'm', 'l'}

a-b #{'d', 'b', 'r'}



#conjuntos por comprension
c = {x for x in 'abracadabra' if x not in 'abc'} #{'d', 'r'}