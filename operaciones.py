

def operaciones_complejas():
    while True:
        
        Sum1 = input("dime un numero: ")
        Sum2 = input("dime otro numero: ")

        print "\n--- MENU DE OPERACIONES ---"
        print "1. Sumar"
        print "2. Restar"
        print "3. Multiplicar"
        print "4. Dividir"

        opcion = input("¿Qué deseas hacer (1-4)? ")

        if opcion == 1:
            print str(Sum1) + " + " + str(Sum2) + " = " + str(Sum1 + Sum2)
            break
        elif opcion == 2:
            print str(Sum1) + " - " + str(Sum2) + " = " + str(Sum1 - Sum2)
            break
        elif opcion == 3:
            print str(Sum1) + " * " + str(Sum2) + " = " + str(Sum1 * Sum2)
            break
        elif opcion == 4:
            if Sum2 == 0:
                print " DIVISION ENTRE 0. Introduzca otros numeros.\n"
                continue
            else:
                print str(Sum1) + " / " + str(Sum2) + " = " + str(float(Sum1) / float(Sum2))
                break
        else:
            print " Opcion no válida. Introduzca un numero del 1 al 4.\n"
    
operaciones_complejas()
   
def devuelve_operaciones():
    return(operaciones_complejas)3
devuelve_operaciones()
