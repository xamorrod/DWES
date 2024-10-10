from estudiante import Estudiante

estudiante1 = Estudiante("A" , "b" ,22)

#Vamos a realizar un menú que contenga las opciones: Agregar estudiante,  ver lista de estudiantes, Buscar estudiante, Eliminar estudiante o salir del programa

confirmador = True

while(confirmador):
    opcion = int(input("Introduce el número de la opción que desees:\n1- Agregar estudiante\n2-Ver lista de estudiantes\n3- Buscar estudiante\n4- Eliminar estudiante"))    
    match opcion:
        case 1:
            return 
        


print (estudiante1.get_nombre())