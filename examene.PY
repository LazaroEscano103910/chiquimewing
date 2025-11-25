def CURVI(letra):
    respuesta=0
    lista_curvi="QSCDRGBJUOPÑ"
    if(letra in lista_curvi):
        respuesta=1
    return(respuesta)

def programa_2():
    palabra=raw_input("Introduce una letra: ")
    palabra_a=""
    ronaldo=len(palabra)
    messi=0
    neymar=0
    for neymar in range(0,ronaldo):
        messi=messi+CURVI(palabra[neymar])
        if(CURVI(palabra[neymar])==1):
            palabra_a=palabra_a+"+"
            neymar=neymar+1
    print("La palabra "+palabra+" tiene " +str(messi)+" letras curvis")
    print("la palabra "+palabra_a+"tiene "+str(messi)+" letra_a")
programa_2()




#messi = suma ; ronaldo = longitud ; neymar = cont
