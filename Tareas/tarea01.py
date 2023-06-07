with open('file.txt','r', encoding="utf-8") as file:
    #Nos permitira devolver todas las lineas de texto como una lista
    txt = str(file.read())
    for palabras in txt.split(' '):
        if palabras.isalpha():
            print(palabras)