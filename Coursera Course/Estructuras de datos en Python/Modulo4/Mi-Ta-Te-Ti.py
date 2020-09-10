def mostrar_tablero(tablero):
    for fila in tablero:
        for i in range(len(fila)):
            if i == len(fila) - 1:
                print('| ' + fila[i] + ' |', end='\n')
            else:
                print('| ' + fila[i], end=' ') 


def movimiento(ficha, posicion, tablero):    
    if posicion == 1:
        tablero[0][0] = ficha
    elif posicion == 2:
        tablero[0][1] = ficha
    elif posicion == 3:
        tablero[0][2] = ficha
    elif posicion == 4:
        tablero[1][0] = ficha
    elif posicion == 5:
        tablero[1][1] = ficha
    elif posicion == 6:
        tablero[1][2] = ficha
    elif posicion == 7:
        tablero[2][0] = ficha
    elif posicion == 8:
        tablero[2][1] = ficha
    elif posicion == 9:
        tablero[2][2] = ficha


def ganador(ficha, tablero):
    if tablero[0][0] == tablero[0][1] == tablero[0][2] == ficha:
        return True
    elif tablero[1][0] == tablero[1][1] == tablero[1][2] == ficha:
        return True
    elif tablero[2][0] == tablero[2][1] == tablero[2][2] == ficha:
        return True
    elif tablero[0][0] == tablero[1][0] == tablero[2][0] == ficha:
        return True
    elif tablero[0][1] == tablero[1][1] == tablero[2][1] == ficha:
        return True
    elif tablero[0][2] == tablero[1][2] == tablero[2][2] == ficha:
        return True
    elif tablero[0][0] == tablero[1][1] == tablero[2][2] == ficha:
        return True
    elif tablero[0][2] == tablero[1][1] == tablero[2][0] == ficha:
        return True
    else:
        return False


def posicion_ocupada(posicion, tablero):
    if posicion == 1:
        if tablero[0][0] == '_':
            pass
        else: 
            return True
    elif posicion == 2:
        if tablero[0][1] == '_':
            pass
        else: 
            return True
    elif posicion == 3:
        if tablero[0][2] == '_':
            pass
        else: 
            return True
    elif posicion == 4:
        if tablero[1][0] == '_':
            pass
        else: 
            return True
    elif posicion == 5:
        if tablero[1][1] == '_':
            pass
        else: 
            return True
    elif posicion == 6:
        if tablero[1][2] == '_':
            pass
        else: 
            return True
    elif posicion == 7:
        if tablero[2][0] == '_':
            pass
        else: 
            return True
    elif posicion == 8:
        if tablero[2][1] == '_':
            pass
        else: 
            return True
    elif posicion == 9:
        if tablero[2][2] == '_':
            pass
        else: 
            return True
    



matriz = [
        ['_', '_', '_'],
        ['_', '_', '_'],
        ['_', '_', '_'],
    ]

matriz_muestra_valores =  [
        ['1', '2', '3'],
        ['4', '5', '6'],
        ['7', '8', '9'],
    ]


print('Bienvenido al juego Ta-Te-Ti hecho por Nicolas Bravo')

ficha_jugador_2 = None
ficha_jugador_1 = str(input('\n Jugador 1 eliga si juega con X o con O(INDIQUE CON LAS LETRAS EN MAYUSCULA):'))
if ficha_jugador_1 == 'X':
    ficha_jugador_2 = 'O'
else:
    ficha_jugador_2 = 'X'

print('A continuacion se muestra una table que indica el numero de cada casillero:')
mostrar_tablero(matriz_muestra_valores)
print('\n')

cant_movimientos = 0
jugador_1 = True

while cant_movimientos <= 9:
    if cant_movimientos == 9:
        print('Hubo empate')
        break
    mostrar_tablero(matriz)

    if jugador_1:
        print('Juega el jugador 1')
        posicion = int(input('Indique el casillero que desea ocupar:'))
        if posicion_ocupada(posicion, matriz):
            print('Esta posicion esta ocupada, intente de nuevo')
        else:    
            movimiento(ficha_jugador_1, posicion, matriz )
            jugador_1 = not jugador_1
            cant_movimientos += 1
    else:
        print('Juega el jugador 2')
        posicion = int(input('Indique el casillero que desea ocupar:'))
        if posicion_ocupada(posicion, matriz):
            print('Esta posicion esta ocupada, intente de nuevo')
        else:
            movimiento(ficha_jugador_2,posicion, matriz)
            jugador_1 = True
            cant_movimientos += 1
    
    if ganador(ficha_jugador_1, matriz):
        print('El Jugador 1 Gano')
        break
    if ganador(ficha_jugador_2, matriz):
        print('El Jugador 2 gano')
        break

