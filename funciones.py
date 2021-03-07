import json

def lecturajson(fichero):
    with open(fichero) as archivo:
        contenido=json.load(archivo)
    return contenido

def menu():
    opcion=int(input("""Elige una opción:
    1 Listar el nombre de los propietarios de los vehículos.
    2 Cuantos coches tiene cada marca.
    3 Introduce un coche para saber sus componentes.
    4 Introduce nombre y apellido de un conductor para saber sus vehiculos.
    5 Mostrar todos los coches, de más antiguo a más moderno.
    6 Salir.
    Opción elegida:"""))

    return opcion

def listar(fichero):
    duenos=fichero.get("coches").get("coche")
    return duenos

def marca(fichero):
    marcas=fichero.get("coches").get("coche")
    lista=[]
    numero={}
    for i in marcas:
        
        lista.append(i.get("marca"))
    for j in lista:
       
        numero[j]=lista.count(j)
        
    return numero

def accesorios(coche,fichero):
    lista=[]
    accesiorio=fichero.get("coches").get("coche")
    for i in accesiorio:
        if i.get("matricula")==coche:
            numero=i.get("accesorios").get("accesorio")
    
    for j in numero:
        j=j.get("nombre")
        lista.append(j)

        
    return lista

def propiedad(nombre,apellido,fichero):
    lista=[]
    x=fichero.get("coches").get("coche")

    for i in x:
        if nombre==i.get("duenio").get("nombre") and apellido==i.get("duenio").get("apellido"):
            coche=i.get("matricula")
            lista.append(coche)
    
    return lista

def antiguedad(fichero):
    dicc={}
    x=fichero.get("coches").get("coche")

    for i in x:
        matricula=i.get("matricula")
        año=int(i.get("anio"))
        dicc[matricula]=año
        

    return dicc
    
