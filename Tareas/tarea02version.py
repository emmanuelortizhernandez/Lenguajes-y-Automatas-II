with open('file.txt', 'r', encoding="utf-8") as file:
    lista_palabras = str(file.read())
    palabra_arepetir = {}
    for palabras in lista_palabras.split(" "):
        if palabras.isalpha():
            lowerpalabras = palabras.lower()
            if lowerpalabras in palabra_arepetir:
                palabra_arepetir[lowerpalabras] += 1
            else:
                palabra_arepetir[lowerpalabras] = 1
print(palabra_arepetir)
