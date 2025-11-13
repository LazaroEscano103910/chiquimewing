def muestra_anteriores(numero,correlacion):
    for cont in range(0,correlacion):
        cont=cont+1
        print(numero+cont)
    

def muestra_posteriores(numero,correlacion):
    for cont in range(0,correlacion):
        cont=cont+1
        print(numero-cont)


def devuelve_numeros():
    numero=input("dime un numero: ")
    correlacion=input("dime cuantos numeros anteriores y posteriores quieres: ")
    muestra_anteriores(numero,correlacion)
    muestra_posteriores(numero,correlacion)
    suma_digitos(numero)

devuelve_numeros()
