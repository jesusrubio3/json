from funciones import lecturajson,menu,listar,marca,accesorios

contenido=lecturajson("coches.json")

menu2=menu()

while menu2!=6:
    if menu2==1:
        print("Estos son los dueños de los vehículos: ")
        for i in listar(contenido):
            print(i.get("duenio").get("nombre"), end=" ")
            print(i.get("duenio").get("apellido"))
    
    if menu2==2:
        print("este es el número de coche que tiene cada marca: ")
        for marca,numero in marca(contenido).items():
            print("%s tiene %d"%(marca,numero))

    if menu2==3:
        matricula=input("introduce la matrícula del vehículo: ")
       
        print("estos son sus accesorios: ")
        for i in accesorios(matricula,contenido):
            print(i)
    menu2=menu()