from estudiante import Estudiante
from estudianteUtil import crearEstudiante, eliminarEstudiante, obtenerEstudiantes

# Vamos a realizar un menú que contenga las opciones: Agregar estudiante,  ver lista de estudiantes, Buscar estudiante, Eliminar estudiante o salir del programa
def menu():
    confirmador = True
    while confirmador:
        try:
            opcion = int(
                input(
                    "Introduce el número de la opción que desees:\n1- Agregar estudiante\n2- Ver lista de estudiantes\n3- Buscar estudiante\n4- Eliminar estudiante\n5- Para salir\n"
                )
            )
            match opcion:
                case 1:
                    crearEstudiante()
                case 2:
                    Estudiante.verEstudiantes()
                case 3:
                    obtenerEstudiantes()

                case 4:
                    eliminarEstudiante()
                case 5:
                    confirmador = False
                    print("Saliendo del programa")
                case _:
                    print("Opción no válida, introduce una opción 1-5")
        except ValueError:
            print("Valor de entrada no válido. Por favo introduce un número")