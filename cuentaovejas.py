def cuenta_ovejas():
    n_ovejas=input("¿Cuantas ovejas quieres contar?: ")
    for cont in range(1,n_ovejas+1):
        if(cont==1):
            print(str(cont)+ " oveja")
        
        else:
            print(str(cont)+ " ovejas")
        



cuenta_ovejas()
