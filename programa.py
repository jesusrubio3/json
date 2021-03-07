from funciones import lecturajson,menu,listar,marca,accesorios,propiedad,antiguedad

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
    
    if menu2==4:
        nombre=input("introduce el nombre: ")
        apellido=input("introduce el apellido: ")
        print("Estas son las matriculas a su nombre: ")

        for i in propiedad(nombre,apellido,contenido):
            print(i)
    
    if menu2==5:
        print("Esta es la lista de coches de matriculados de más antiguos a los mas modernos: ")
        h=antiguedad(contenido)
        h=dict(sorted(h.items(), key=lambda item:item[1]))
        for i,j in h.items():
            print("%s matriculado en %d"%(i,j))
    menu2=menu()