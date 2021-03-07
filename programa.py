from funciones import lecturajson,menu,listar

contenido=lecturajson("coches.json")

menu2=menu()

while menu2!=6:
    if menu2==1:
        print("Estos son los dueños de los vehículos: ")
        for i in listar(contenido):
            print(i.get("duenio").get("nombre"), end=" ")
            print(i.get("duenio").get("apellido"))

    menu2=menu()