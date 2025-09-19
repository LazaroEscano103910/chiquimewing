def contar_letras():
    palabra=raw_input("introduce una palabra: ")
    longitud=len(palabra)
    print("la palabra "+palabra+" tiene "+str(longitud)+" letras")
    for cont in range(0,longitud):
        print(palabra[cont])
    

contar_letras()
