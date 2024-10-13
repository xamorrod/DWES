from estudiante import Estudiante

# Creamos las funciones a las que llama el match para realizar el CRUD


def crearEstudiante():
    nombre = input("Introduce el nombre del estudiante")
    apellido = input("Introduce el apellido del estudiante")
    edad = int(input("Introduce la edad del estudiante"))
    estudiante = Estudiante(nombre, apellido, edad)


def obtenerEstudiantes():
    encontrado = False
    nombre = input("Introduce el nombre del estudiante que quieres buscar")
    for estudiante in Estudiante.listaEstudiante:
        if estudiante.nombre == nombre:
            print("Los estudiante que coinciden con lo dado son ", estudiante.nombre , " con apellido " ,estudiante.apellido , " y edad " ,estudiante.edad)
            encontrado = True
    if not encontrado:
        print("No se ha encontrado ningún estudiante")


def eliminarEstudiante():
    encontrado = False
    nombre = input("Introduce el nombre del estudiante que quieres eliminar")
    for estudiante in Estudiante.listaEstudiante:
        if estudiante.nombre == nombre:
            encontrado = True
            print(
                "Los estudiante que van a borrarse son ",
                estudiante.nombre,
                "\n¿Estás seguro de que deseas borrarlos? (Y/n)",
            )
            confirmBorrado = input()
            if confirmBorrado == "Y":
                Estudiante.listaEstudiante.remove(estudiante)
                print("El estudiante se ha borrado satisfactoriamente")
            else:
                "No se procede al borrado de ningún estudiante"
    if not encontrado:
        print("No se ha encontrado ningún estudiante")
