with open('file.txt','r', encoding="utf-8") as file:
    # Nos permitira devolver todas las lineas de texto como una lista
    txt = str(file.read())
    palabr = input("Ingrese palabra:")
    count = txt.count(palabr)
    #count=txt.count("prueba")
    print('La palabra se encuentra', count, "veces")
    print('--------------------------------------')
    for palabras in txt.split(' '):
        if palabras.isalpha(): 
            
            print(palabras)
            
