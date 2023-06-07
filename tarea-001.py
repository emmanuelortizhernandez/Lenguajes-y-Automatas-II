## Modificar este codigo para leer las palabras del archivo " file.txt"
## imprimirlas de manera que solo imprima palabras validas, validas se 
## refiere a palabras que solo tengan caracteres del abecedario
##
##  Ejemplo: Si lee el siguiente texto " Esta es una1 oraci0n de prueba algoritmica."
##  
##  Resultado "se perados por ,": Esta,es,de,prueba
##
##  Esto debera estar en su github


file = open('file.txt', 'r')
 
while 1:
     
    # read by character
    char = file.read(1)         
    if not char: # if char is false, finish the while
        break
         
    print(char)
 
file.close()