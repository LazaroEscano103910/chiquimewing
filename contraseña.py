def contrasena():
    nombre=raw_input("dime tu nombre: ")
    apellido1=raw_input("dime tu apellido: ")
    apellido2=raw_input("dime tu otro apellido: ")
    ano=raw_input("dime tu ano de nacimiento: ")
    codigo=nombre[:3] + apellido1[:3] + apellido2[:3] + ano[2:4]
    print("tu conrtrasena es: ",codigo)

contrasena()
