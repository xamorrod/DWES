class Estudiante:
    
    #Definimos el atributo global de la clase que será la lista con todas las personas
        
    listaEstudiante  = []    
    
    def __init__(self, nombre, apellido, edad):
        
        #Definimos los atributos de la clase
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        #Llamamos al método dentro del constructor para que se guarde automáticamente
        self.guardar_estudiante()
        #Llamamos al método que escribe los datos creados en un fichero
        self.escribir_estudiante()
        
        
    def guardar_estudiante(self):
        Estudiante.listaEstudiante.append(self)
    
    def escribir_estudiante(self):
        with open ("registro_estudiantes.txt" , "a") as fichero:
            fichero.write(f"Nombre: {self.nombre}, Apellido: {self.apellido}, Edad: {self.edad}")

    #Definimos el método __str__ para hacer la representación de cada estudiante que se llamará cuando queramos ver la lista de estudiantes
    def __str__(self):
        return f"Nombre: {self.nombre}, Apellido: {self.apellido}, Edad: {self.edad}"
    
    #cls implica que se refiere al atributo de la clase
    @classmethod
    def verEstudiantes(cls):
        for estudiante in cls.listaEstudiante:
            print(estudiante)
        
         
        
  
        
        