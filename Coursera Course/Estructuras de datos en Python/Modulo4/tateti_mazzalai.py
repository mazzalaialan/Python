#creo la matriz de simbolos y las funciones para generar el tablero
matriz_tateti = [
    [None,None,None],
    [None,None,None],
    [None,None,None]
]
simbolos = {1:'X',0:'O',None:'_'}
simbolos_jugadores = {'X':1,'O':0}

def imprimir_tablero():
    """Imprime el tablero según los datos de la matriz_tateti global"""
    print('')
    print('|',simbolos.get(matriz_tateti[0][0]),'|',simbolos.get(matriz_tateti[0][1]),'|',simbolos.get(matriz_tateti[0][2]),'|',sep='')
    print('|',simbolos.get(matriz_tateti[1][0]),'|',simbolos.get(matriz_tateti[1][1]),'|',simbolos.get(matriz_tateti[1][2]),'|',sep='')
    print('|',simbolos.get(matriz_tateti[2][0]),'|',simbolos.get(matriz_tateti[2][1]),'|',simbolos.get(matriz_tateti[2][2]),'|',sep='')
    print('')

def casillero_libre(fila,columna):
    """Valida si en la matriz_tateti el casillero que seleccionó el jugaador esta libre"""
    if fila < 0 or fila > 2:
        print('Elija una fila entre 1 y 3')
        return False
    if columna < 0 or columna > 2:
        print('Elija una columna entre 1 y 3')
        return False
    if matriz_tateti[fila][columna] == None:
        return True
    else:
        print('Elija un casillero que no este ocupado!')
        return False
    return False

def quien_gano(valor):
    print('Gano el jugador que usaba',simbolos.get(valor))

def hay_ganador():
    """Valida que no se haya hecho linea dentro de la matriz_tateti para ganar el juego"""
    ganador = False
    if matriz_tateti[0][0] != None and matriz_tateti[0][0] == matriz_tateti[0][1] and matriz_tateti[0][1] == matriz_tateti[0][2]:
        ganador = True
        quien_gano(matriz_tateti[0][0])
    elif matriz_tateti[1][0] != None and matriz_tateti[1][0] == matriz_tateti[1][1] and matriz_tateti[1][1] == matriz_tateti[1][2]:
        ganador = True
        quien_gano(matriz_tateti[1][0])
    elif matriz_tateti[2][0] != None and matriz_tateti[2][0] == matriz_tateti[2][1] and matriz_tateti[2][1] == matriz_tateti[2][2]:
        ganador = True
        quien_gano(matriz_tateti[2][0])
    elif matriz_tateti[0][0] != None and matriz_tateti[0][0] == matriz_tateti[1][0] and matriz_tateti[1][0] == matriz_tateti[2][0]:
        ganador = True
        quien_gano(matriz_tateti[0][0])
    elif matriz_tateti[0][0] != None and matriz_tateti[0][0] == matriz_tateti[1][0] and matriz_tateti[1][0] == matriz_tateti[2][0]:
        ganador = True
        quien_gano(matriz_tateti[0][0])
    elif matriz_tateti[0][0] != None and matriz_tateti[0][0] == matriz_tateti[1][0] and matriz_tateti[1][0] == matriz_tateti[2][0]:
        ganador = True
        quien_gano(matriz_tateti[0][0])
    elif matriz_tateti[0][0] != None and matriz_tateti[0][0] == matriz_tateti[1][1] and matriz_tateti[1][1] == matriz_tateti[2][2]:
        ganador = True
        quien_gano(matriz_tateti[0][0])
    elif matriz_tateti[0][2] != None and matriz_tateti[0][2] == matriz_tateti[1][1] and matriz_tateti[1][1] == matriz_tateti[2][0]:
        ganador = True
        quien_gano(matriz_tateti[0][2])
    if ganador:
        return True
    else:
        return False

def juego_incompleto():
    """Valida si en la matriz_tateti quedan casilleros libres para seguir jugando"""
    if hay_ganador(): return False
    sin_rellenar = False
    for x in range(3):
        for y in range(3):
            if matriz_tateti[x][y] == None:
                sin_rellenar = True
    if sin_rellenar == False:
        print('Tenemos un empate!')
    return sin_rellenar

imprimir_tablero()
jugador_actual = None

#asigno simbolos a cada jugador
global simbolo_jugador1,simbolo_jugador2
simbolo_jugador1,simbolo_jugador2 = '',''
while (simbolo_jugador1 not in (simbolos.get(0),simbolos.get(1))):
    simbolo_jugador1 = str.upper(str(input('Elija su simbolo X o O: ')))
if simbolo_jugador1 == simbolos.get(1):
    simbolo_jugador2 = simbolos.get(0)
    jugador_actual = 1
    print('Comienza el jugador 1')
else:
    simbolo_jugador2 = simbolos.get(1)
    jugador_actual = 2
    print('Comienza el jugador 2')

#comienza el juego
def jugar(jugador_actual):
    """Funcion con la estructuraa principal del juego con recursividad"""
    if juego_incompleto():
        if jugador_actual == 1:
            print('Jugador 1 (',simbolo_jugador1,')')
        else:
            print('Jugador 2 (',simbolo_jugador2,')')
        try:
            jugadaf = int(input('elija la fila: '))-1
            jugadac = int(input('elija la columna: '))-1
        except KeyboardInterrupt:
            raise KeyboardInterrupt
        except:
            jugadaf = -1
            jugadac = -1
        if casillero_libre(jugadaf,jugadac):
            if jugador_actual == 1:
                matriz_tateti[jugadaf][jugadac] = simbolos_jugadores.get(simbolo_jugador1)
            elif jugador_actual == 2:
                matriz_tateti[jugadaf][jugadac] = simbolos_jugadores.get(simbolo_jugador2)
            imprimir_tablero()
            if jugador_actual == 2:
                jugar(1)
            else:
                jugar(2)
        else:
            print('vuelva a eligir un casillero.')
            jugar(jugador_actual)


jugar(jugador_actual)


""" while (juego_incompleto() and not hay_ganador):
    jugadaxf = int(input('elija la fila donde colocar la X: '))-1
    jugadaxc = int(input('elija la columna donde colocar la X: '))-1
    if casillero_libre(jugadaxf,jugadaxc):
        matriz_tateti[jugadaxf][jugadaxc] = 1
        imprimir_tablero()
    else:
        print('vuelva a eligir un casillero.')
        continue
    jugadaof = int(input('elija la fila donde colocar la O: '))-1
    jugadaoc = int(input('elija la columna donde colocar la O: '))-1
    if casillero_libre(jugadaxf,jugadaxc):
        matriz_tateti[jugadaxf][jugadaxc] = 1
        imprimir_tablero()
    else:
        print('vuelva a eligir un casillero.')
        continue """

print('Juego Finalizado!')