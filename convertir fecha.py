#Haz un programa que reciba una fecha en formato:#"4 de enero de 2026" y devuelva 4/01/26
#Haz un programa que reciba una fecha en formato:
#"4 de enero de 2026" y devuelva 4/01/26
def devuelve_dia(fecha):
    dia="" #una cadena donde vamos a construir numero a numero eldia
    cont=0
    longitud=len(fecha)
    while(cont<longitud):
        if(fecha[cont]!=" "):#detectamos si el caracter es o no un espacio
            dia=dia+fecha[cont]
            cont=cont+1
        else:
            cont=longitud
    return(dia)

def devuelve_mes(fecha):
    mes=""
    cont=0
    nespacios=0
    longitud=len(fecha)
    while(cont<longitud):
        if(fecha[cont]==" "):
            nespacios=nespacios+1
        else:
            if(nespacios==2):
                mes=mes+fecha[cont]
        cont=cont+1
    return(mes)  


def fecha():
    #Tiene que leer una fecha (en el formato adecuado)
    fecha=raw_input("Introduce la fecha en el formato: 4 de enero de 2026 ")
    dia=devuelve_dia(fecha)
    mes=devuelve_mes(fecha)
    #anio=devuelve_anio(fecha)
    print(dia)
    print(mes)
   
   
fecha()
    #Tengo que aislar el día, el mes y el año: 4,enero,2026
    #Lo hago con tres funciones devuelve_dia(fecha), devuelve_mes(fecha)
    #devuelve_anio(mes)

    #Transformo el mes en un número: enero->01
   
    #Concateno el día+mes+año, separados por "/"
