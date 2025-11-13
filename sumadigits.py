def suma_digitos(numero):
    suma = 0
    for digito in str(numero):
        if digito.isdigit():
            suma += int(digito)
    return suma


n = input("Introduce un número: ")
print("La suma de los digitos es:", suma_digitos(n))
suma_digitos(n)
