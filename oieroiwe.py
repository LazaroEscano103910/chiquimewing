

def operaciones_complejas():
    continuar = True  

    while continuar:
        Sum1 = input("Dime un numero: ")
        Sum2 = input("Dime otro numero: ")

        while True:
            print "\n--- MENU DE OPERACIONES ---"
            print "1. Sumar"
            print "2. Restar"
            print "3. Multiplicar"
            print "4. Dividir"
            print "5. Cambiar numeros"
            print "6. Salir"

            opcion = input("¿Que deseas hacer (1-6)? ")

            if opcion == 1:
                print str(Sum1) + " + " + str(Sum2) + " = " + str(Sum1 + Sum2)
            elif opcion == 2:
                print str(Sum1) + " - " + str(Sum2) + " = " + str(Sum1 - Sum2)
            elif opcion == 3:
                print str(Sum1) + " * " + str(Sum2) + " = " + str(Sum1 * Sum2)
            elif opcion == 4:
                
                if Sum2 == 0:
                    print " DIVISION ENTRE 0. Introduzca otros numeros.\n"
                    continue
                else:
                    print str(Sum1) + " / " + str(Sum2) + " = " + str(float(Sum1) / float(Sum2))
                    break
            elif opcion == 5:
                
                break
            elif opcion == 6:
                print "Programa finalizado."
                continuar = False 
                break
            else:
                print "️ Opción no válida. Introduzca un número del 1 al 6."

        print "\n-----------------------------------\n"

operaciones_complejas()
