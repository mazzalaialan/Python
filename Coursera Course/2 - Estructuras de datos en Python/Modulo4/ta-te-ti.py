t=[['_','_','_'],['_','_','_'],['_','_','_']]
s='|'
cont=0
print(s,t[0][0],s,t[0][1],s,t[0][2],s)
print(s,t[1][0],s,t[1][1],s,t[1][2],s)
print(s,t[2][0],s,t[2][1],s,t[2][2],s)
simb=input('Indique con que simbolo quiere jugar (X/O): ')
if simb != 'X' and simb !='O':
    while simb != 'X' and simb !='O':
        print('Los simbolos son la letra X o la letra O, ambas en mayuscula')
        simb=input('Indique con que simbolo quiere jugar (X/O): ')
print('Muy bien, elegiste',simb)

def posicion():
    f=int(input('En que fila quieres colocar la marca? (0,1,2): '))
    if f != 0 and f != 1 and f != 2:
        while f != 0 and f != 1 and f != 2:
            print('Las filas van del cero (0) al dos (2)')
            f=int(input('En que fila quieres colocar la marca? (0,1,2): '))
    c=int(input('En que columna quieres colocar la marca? (0,1,2): '))
    if c != 0 and c != 1 and c != 2:
        while c != 0 and c != 1 and c != 2:
            print('Las columnas van del cero (0) al dos (2)')
            c=int(input('En que columna quieres colocar la marca? (0,1,2): '))
    print('La marca ira en la posicion',f,',',c)
    return(f,c)

def juego_X():
    print('Vamos con las X')
    fx,cx=posicion()
    while t[fx][cx]!='_':
        print('Poscion ocupada por',t[fx][cx])
        fx,cx=posicion()
    t[fx][cx]='X'

def juego_O():
    print('Vamos con las O')
    fo,co=posicion()
    while t[fo][co]!='_':
        print('Poscion ocupada por',t[fo][co])
        fo,co=posicion()
    t[fo][co]='O'

def gen_tateti(cont):
    resultado=""
    while cont<9:
        if cont%2==0:
            juego_X()
        else:
            juego_O()
        cont+=1
        print(s,t[0][0],s,t[0][1],s,t[0][2],s),print(s,t[1][0],s,t[1][1],s,t[1][2],s),print(s,t[2][0],s,t[2][1],s,t[2][2],s)
        if t[0]== ['X','X','X'] or t[1]== ['X','X','X'] or t[2]== ['X','X','X']:
            resultado='Ganó X'
            yield resultado
            break
        elif t[0]== ['O','O','O'] or t[1]== ['O','O','O'] or t[2]== ['O','O','O']:
            resultado='Ganó O'
            yield resultado
            break
        elif t[0][0]==t[1][0]==t[2][0]=='X' or t[0][1]==t[1][1]==t[2][1]=='X' or t[0][2]==t[1][2]==t[2][2]=='X' or t[0][0]==t[1][1]==t[2][2]=='X' or t[0][2]==t[1][1]==t[2][0]=='X':
            resultado='Ganó X'
            yield resultado
            break
        elif t[0][0]==t[1][0]==t[2][0]=='O' or t[0][1]==t[1][1]==t[2][1]=='O' or t[0][2]==t[1][2]==t[2][2]=='O' or t[0][0]==t[1][1]==t[2][2]=='O' or t[0][2]==t[1][1]==t[2][0]=='0':
            resultado='Ganó O'
            yield resultado
            break
        else:
            if cont==9:
                resultado='Empate'
                yield resultado

result=gen_tateti(cont)
for i in result:
    print(i)

