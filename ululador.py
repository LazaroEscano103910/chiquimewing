#Ejercicio que lee una palabra y sustituye las vocales por 'u'
def ululador():
    frase_entrada=raw_input("Dime algo coherente: ")#Leo una palabra
    frase_salida="" #Creo una cadena vacía
    vocales_minus="aeiou"
    vocales_mayus="AEIOU"
    for cont in range(0,len(frase_entrada)):
        if(frase_entrada[cont] in vocales_minus):#Si la letra que toca es la 'a'  ...
            frase_salida=frase_salida+'u' #...concateno una 'u'
        else:#Si no lo es...
            if(frase_entrada[cont] in vocales_mayus):#Si la letra que toca es la 'a'  ...
                frase_salida=frase_salida+'U' #...concateno una 'u'
            else:
                frase_salida=frase_salida+frase_entrada[cont] #...concateno la letra que toca
    print(frase_salida)

ululador()
