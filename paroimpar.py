def par_impar():
    numero=input("¿Cuantos numeros quieres contar?: ")
    for cont in range(1,numero+1):
        if(cont%2==0):
            print(str(cont)+"PAR")
        if(cont%2==1):
            print(str(cont)+"IMPAR")


par_impar()
