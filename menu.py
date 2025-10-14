def menu():
    # MENU
    print("Elige una opcion (1-7): ")
    print("1. Contar el numero de letras")
    print("2. Contar el numero de consonantes")
    print("3. Contar el numero de vocales")
    print("4. Contar el numero de palabras")
    print("5. Contar el numero de de veces que aparece la letra o")
    print("6. Encriptar el mensaje")
    print("7. salir")
    

def contar_letras(texto):
    print("Tiene "+str(len(texto))+" caracteres")

def contar_consonantes(texto):
    n_consonantes=0
    vocales="aeiouAEIOU"
    numero="1234567890"
    for letra in texto:
        if(not((letra in vocales) or (letra==" ") or(letra in numero))):
            n_consonantes=n_consonantes+1
    print("Tiene "+str(n_consonantes)+ " consonantes")

def contar_vocales(texto):
    n_vocales=0
    vocales="aeiouAEIOU"
    numero="1234567890"
    for letra in texto:
        if((letra in vocales) or (letra=="") or (letra in numero)):
            n_vocales=n_vocales+1
    print("Tiene "+str(n_vocales)+ " vocales")

def contar_palabras(texto):
    palabras = texto.split()
    num_palabras = len(palabras)
    print(" el numero de palabras son : ", num_palabras)
    
def contar_oes(texto):
    n_oes=0
    Letra_O = "Oo"
    for letra in texto:
        if(letra in Letra_O):
           n_oes=n_oes+1
    print("tiene "+str(n_oes)+ " letras o")

def encriptar(texto):
    encriptada= ""
    for letra in texto:
        if letra.isalpha():
            if letra == 'z':
                encriptada += 'a'
            if letra == 'Z':
                encriptada += 'A'
            else:
                encriptada += chr(ord(letra)+1)
        else:
            encriptada += letra
    print("El mesnaje encriptado es :", encriptada)
    

def contador_total():
    texto = raw_input("Introduce una frase: ")

    while True:
        menu()
        try:
            opcion = int(raw_input("ELIGE UNA OPCIÓN (1-7): "))
        except ValueError:
            print "Por favor, introduce un número válido."
            continue

        if opcion == 1:
            contar_letras(texto)
        elif opcion == 2:
            contar_consonantes(texto)
        elif opcion == 3:
            contar_vocales(texto)
        elif opcion == 4:
            contar_palabras(texto)
        elif opcion == 5:
            contar_oes(texto)
        elif opcion == 6:
            encriptar(texto)
        elif opcion == 7:
            print "¡Hasta luego!"
            break
        else:
            print "Opción no válida, intenta otra vez."



contador_total()
    
