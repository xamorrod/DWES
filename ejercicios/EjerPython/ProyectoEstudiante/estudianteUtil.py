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
    listaEstudianteConservada = []  # Lista para conservar los estudiantes que no se eliminan
    nombre_del = input("Introduce el nombre del estudiante que quieres eliminar: ")
    apellido_del = input("Introduce el apellido del estudiante: ")
    edad_del = input("Introduce la edad del estudiante: ")

    for estudiante in Estudiante.listaEstudiante:
        # Si encontramos al estudiante a eliminar
        if estudiante.nombre == nombre_del and estudiante.apellido == apellido_del and estudiante.edad == edad_del:
            encontrado = True
            print(
                "El estudiante que va a borrarse es ",
                estudiante.nombre, " ", estudiante.apellido, " ", estudiante.edad,
                "\n¿Estás seguro de que deseas borrarlos? (Y/n)",
            )
            confirmBorrado = input()
            if confirmBorrado.lower() == "y":  # Comprobación insensible a mayúsculas
                # Eliminar al estudiante de la lista
                Estudiante.listaEstudiante.remove(estudiante)
                print("El estudiante se ha borrado satisfactoriamente.")
            else:
                print("No se procede al borrado de ningún estudiante.")
                listaEstudianteConservada.append(estudiante)  # Conservar al estudiante

        else:
            listaEstudianteConservada.append(estudiante)  # Conservar el estudiante

    if encontrado:
        with open("registro_estudiantes.txt", "w") as ficheroActualizado:
            for estudiante in listaEstudianteConservada:
                ficheroActualizado.write(f"Nombre: {estudiante.nombre}, Apellido: {estudiante.apellido}, Edad: {estudiante.edad}\n")
    else:
        print("No se ha encontrado ningún estudiante con los datos proporcionados.")

        
def reload():
    with open ("registro_estudiantes.txt" , "r") as fichero:
        #Iteramos en las líneas para encontrar estudiantes y crear objetos de los que haya presentes
        for linea in fichero.readlines():
            partes = linea.split(",")
            nombre = partes[0].split(": ")[1]
            apellido = partes[1].split(": ")[1]
            edad = partes[2].split(": ")[1]
            #Creamos el objeto estudiante
            estudiante = Estudiante(nombre, apellido, edad)
            
