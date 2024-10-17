class Estudiante:

    # Definimos el atributo global de la clase que será la lista con todas las personas

    listaEstudiante  = []    

    def __init__(self, nombre, apellido, edad):

        # Definimos los atributos de la clase
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        # Llamamos al método dentro del constructor para que se guarde automáticamente
        self.guardar_estudiante()
        # Llamamos al método que escribe los datos creados en un fichero
        self.escribir_estudiante()

    @classmethod
    def constructor_sin_metodo(cls , nombre, apellido, edad):
        # Esto se efectua para que el método reload no llame a los métodos nativos del constructor
        estudiante = cls.__new__(cls)
        estudiante.nombre = nombre
        estudiante.apellido = apellido
        estudiante.edad = edad
        return estudiante

    def guardar_estudiante(self):
        Estudiante.listaEstudiante.append(self)

    def escribir_estudiante(self):
        with open ("registro_estudiantes.txt" , "a") as fichero:
            fichero.write(f"Nombre: {self.nombre}, Apellido: {self.apellido}, Edad: {self.edad}\n")

    # Definimos el método __str__ para hacer la representación de cada estudiante que se llamará cuando queramos ver la lista de estudiantes
    def __str__(self):
        return f"Nombre: {self.nombre}, Apellido: {self.apellido}, Edad: {self.edad}"

    # cls implica que se refiere al atributo de la clase
    @classmethod
    def verEstudiantes(cls):
        for estudiante in cls.listaEstudiante:
            print(estudiante)

    @classmethod
    def reload(cls):

        # Abrir el archivo y leer los datos de los estudiantes
        try:
            with open("registro_estudiantes.txt", "r") as fichero:
                for linea in fichero.readlines():
                    # Dividir la línea por las comas para obtener las partes
                    partes = linea.strip().split(", ")
                    # Extraer los valores de nombre, apellido y edad
                    nombre = partes[0].split(": ")[1]
                    apellido = partes[1].split(": ")[1]
                    edad = int(partes[2].split(": ")[1])
                    # Crear una instancia de Estudiante con los datos leídos
                    estudiante = Estudiante.constructor_sin_metodo(nombre, apellido, edad)
                    cls.listaEstudiante.append(estudiante)

        except FileNotFoundError:
            print("El archivo 'registro_estudiantes.txt' no existe. No se han cargado estudiantes.")
