import json

#Ahora tenemos una lista de diccionarios de 3 elementos

def cargar_listaDiccionarios(nombreArchivo):
    try:
        listaDiccionarios = [] 
        with open(nombreArchivo) as fichero:
            
            for elemento in fichero: 
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
    except FileNotFoundError as e:
        print("El fichero no existe")
   



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
    indice = buscar_cancion(listaDiccionarios , nomCancion)
    if indice >= 0:
            listaDiccionarios.pop(indice)
            print(f"Cancion {nomCancion} eliminada con éxito")
    else:
        print("No se ha encontrado la canción buscada")
    
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
        for i , cancion in enumerate(listaDiccionario):
            nombre = cancion["nombre"]
            artista = cancion["artista"]
            genero = cancion["genero"]
            if nomCancion == nombre:
                print(f"Los datos de la canción buscada son {nombre} , {artista} , {genero}")
                return i
        return -1
    except IOError as e:
        print("Ha habido un error con la búsqueda del fichero")
        
def cargarPlaylistJSON(nombreArchivo):
    with open(nombreArchivo ,"r", encoding="utf-8") as data:
        return json.load(data )

def volcarPlaylistJSON(listJson):
    with open("playlistVolcada.json" ,"w") as data:
        json.dump(listJson ,data, indent = 4, ensure_ascii=False)
            
#TEST

# prueba = cargar_listaDiccionarios("playlist.txt")
# pruebaAñadida = agregar_cancion(prueba , "a" ,"b", "c")    
# pruebaEliminada = eliminar_cancion(pruebaAñadida , "a")  
pruebaJson = cargarPlaylistJSON("playlist.json")
volcarPlaylistJSON(pruebaJson)


    