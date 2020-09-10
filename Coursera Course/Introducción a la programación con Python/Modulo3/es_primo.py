def es_primo(numero):
   cont = 0
   resultado = True

   for divisor in range(2, numero):
       cont += 1
       if (numero % divisor) == 0:

           resultado = False

           break
   #print(cont)
   return resultado


#es_primo(13)

if __name__ == "__main__":
    import sys
    es_primo(int(sys.argv[1]))