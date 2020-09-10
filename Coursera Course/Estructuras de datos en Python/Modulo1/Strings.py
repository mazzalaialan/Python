name = "Agustín"
"Hola %s" % name # Resultado: Hola Agustín
"El número es %d" % 5 # Resultado: El número es 5
"El número es %02d" % 5 # Resultado: El número es 005
"El decimal es %f" % 6.5 # Resultado: El número es 6.500000
"El decimal es %.2f" % 6.5 # Resultado: El número es 6.50
"Hola %(name)s" % {'name': name} # Resultado: Hola Agustín