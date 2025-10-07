def superprograma():
    frase = raw_input("Dime una frase jefe: ")
    print("El texto tiene " + str(len(frase)) + " caracteres")

    vocales = "aeiouAEIOU"
    consonantes = "bcdfghjklmnñpqrstvwxyzBCDFGHJKLMNÑPQRSTVWXYZ"
    letraO = "oO"

    cont_vocales = 0
    cont_consonantes = 0
    cont_o = 0
    cont_letras = 0

    
    for letra in frase:
        if letra.isalpha():  
            cont_letras += 1
            print("Numero de letras:", cont_letras)
            if letra in vocales:
                cont_vocales += 1
                print("Numero de vocales:", cont_vocales)
            elif letra in consonantes:
                cont_consonantes += 1
                print("Numero de consonantes:", cont_consonantes)
            if letra in letraO:
                cont_o += 1
                print("Numero de veces que aparece la letra 'o':", cont_o)

    
    palabras = frase.split()
    num_palabras = len(palabras)

    
    print("Numero de palabras:", num_palabras)
    

   
    encriptada = ""
    for letra in frase:
        if letra.isalpha():
            if letra == 'z':
                encriptada += 'a'
            elif letra == 'Z':
                encriptada += 'A'
            else:
                encriptada += chr(ord(letra) + 1)
        else:
            encriptada += letra

    print("Mensaje encriptado:", encriptada)



superprograma()
