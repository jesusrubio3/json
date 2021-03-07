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