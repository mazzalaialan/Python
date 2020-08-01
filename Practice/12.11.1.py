import socket
dat = input('ingrese url:')
archi = input('ingrese link archivo')
try:
    misock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    misock.connect((dat, 80))
    cmd = 'GET '+archi+' HTTP/1.0\r\n\r\n'.encode()
    misock.send(cmd)
except:
    print('archivo mal ingresado o no encontrado')
    quit()
while True:
    datos = misock.recv(512)
    if len(datos) < 1:
        break
print(datos.decode(),end='')
misock.close()
