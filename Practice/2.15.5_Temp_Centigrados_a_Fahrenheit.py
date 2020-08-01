fah = input('escribi la temperatura')
try:
    fh = int(fah)
    cel = (fh - 32) * 5/9
    print(cel)
except:
    print('ingresa un numero pelotudo')
