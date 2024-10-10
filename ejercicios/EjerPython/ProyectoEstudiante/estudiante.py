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
        
    def guardar_estudiante(self):
        Estudiante.listaEstudiante.append(self)
    
    def get_nombre(self):
        return self.nombre
        
         
        
  
        
        