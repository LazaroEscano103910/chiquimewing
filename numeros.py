def mostrar_anteriores_y_posteriores(numero):
    print("Los tres numeros anteriores son:", numero - 3, numero - 2, numero - 1)
    print("Los tres numeros posteriores son:", numero + 1, numero + 2, numero + 3)


n = int(input("Introduce un número: "))
mostrar_anteriores_y_posteriores(n)
def suma_digitos(numero):
    suma = 0
    for digito in str(numero):
        if digito.isdigit():
            suma += int(digito)
    return suma


n = input("Introduce un número: ")
print("La suma de los digitos es:", suma_digitos(n))
suma_digitos(n)




    



        
