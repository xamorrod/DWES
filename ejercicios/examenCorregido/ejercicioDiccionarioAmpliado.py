#Ahora tenemos una lista de diccionarios de 3 elementos

def cargar_listaDiccionarios(nombreArchivo):
    listaDiccionarios = [] 
    with open(nombreArchivo) as fichero:
        
        for elemento in fichero: 
            # nombre , artista, genero = elemento.strip().split(" - ")
            # cancion = { 
            #            "nombre" : nombre,
            #            "artista" : artista,
            #            "genero" : genero
            #            }
            # if len(cancion) == 3:
            #     listaDiccionarios.append(cancion) 
            # else: 
            #     print(f"La línea no está formateada correctamente {nombre}")
            values = elemento.strip().split(" - ")
            
            if len(values) == 3:
                cancion = { 
                       "nombre" : values[0],
                       "artista" : values[1],
                       "genero" : values[2]
                       }
                listaDiccionarios.append(cancion) 
            else: 
                print(f"La línea no está formateada correctamente")
        print(listaDiccionarios) 
    return listaDiccionarios
   



def agregar_cancion(listaDiccionarios ,nomCancion , nomArtista , nomGenero):
    nuevaLista = []
    #filtrado 
    dicNuevo ={
        "nombre" : nomCancion,
        "artista" : nomArtista,
        "genero" : nomGenero
    } 
    
    listaDiccionarios.append(dicNuevo)
    print(listaDiccionarios)
    return listaDiccionarios



def eliminar_cancion(listaDiccionarios , nomCancion ):
   #Proceso de búsqueda del nombre en cada diccionario
   
    for cancion in listaDiccionarios:
        if buscar_cancion(listaDiccionarios , nomCancion):
            listaDiccionarios.remove(cancion)
            print(f"Cancion {nomCancion} eliminada con éxito")
            break
        else:
            print("La canción no existe por lo que no puede guardarse")
        
    return listaDiccionarios



def guardar_cancion(nombreArchivo , listaCanciones):
    with open(nombreArchivo ,"w")  as fichero:
        for cancion in listaCanciones:
            nombre = cancion["nombre"]
            artista = cancion["artista"]
            genero = cancion["genero"]
            linea = (f"{nombre} - {artista} - {genero}\n")
            fichero.write(linea)
    return listaCanciones
            
def buscar_cancion(listaDiccionario , nomCancion):
    #Buscamos entendiendo que la clave primaria es el nombre de la canción
    try:
        for cancion in listaDiccionario:
            nombre = cancion["nombre"]
            artista = cancion["artista"]
            genero = cancion["genero"]
            if nomCancion == nombre:
                print(f"Los datos de la canción buscada son {nombre} , {artista} , {genero}")
                return True
        return False
    except IOError as e:
        print("Ha habido un error con la búsqueda del fichero")
        

#TEST

prueba = cargar_listaDiccionarios("playlist.txt")
pruebaAñadida = agregar_cancion(prueba , "a" ,"b", "c")    
pruebaEliminada = eliminar_cancion(pruebaAñadida , "a")  
print(pruebaEliminada)

    