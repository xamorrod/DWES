import random
#Definimos el atributo global del diccionario de canciones
dicCanciones = {}

#Ahora tenemos una lista de diccionarios

def cargar_listaDiccionarios(nombreArchivo):
    listaDiccionarios = [] 
    with open(nombreArchivo) as fichero:
        
        for elemento in fichero: 
            nombre , artista, genero = elemento.strip().split(" - ")
            cancion = { 
                       "nombre" : nombre,
                       "artista" : artista,
                       "genero" : genero
                       }
            if len(cancion) == 3:
                listaDiccionarios.append(cancion) 
            else: 
                print(f"La línea no está formateada correctamente {nombre}")
                
        print(listaDiccionarios) 
    return listaDiccionarios
   



def agregar_cancion(listaDiccionarios ,nomCancion , nomArtista , nomGenero):
    nuevaLista = []
    
    dicNuevo ={
        "nombre" : nomCancion,
        "artista" : nomArtista,
        "genero" : nomGenero
    } 
    
    listaDiccionarios.append(dicNuevo)
    print(listaDiccionarios)
    return listaDiccionarios



def eliminar_cancion(listaDiccionarios , nomCancion , nomArtista , nomGenero):
   #Proceso de búsqueda de las 3 ocurrencias en cada diccionario
   
    for cancion in listaDiccionarios:
        nombre , artista, genero = cancion.items()
        if nomCancion == cancion["nombre"] and nomArtista == cancion["artista"] and nomGenero == cancion["genero"]:
            print(f"Cancion {nombre} eliminada con éxito")
            listaDiccionarios.remove(cancion)
        
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
            


prueba = cargar_listaDiccionarios("playlist.txt")
pruebaAñadida = agregar_cancion(prueba , "a" ,"b", "c")    
pruebaEliminada = eliminar_cancion(pruebaAñadida , "a" ,"b", "c")  
guardar_cancion("playlist2.txt" ,pruebaEliminada)  
print(pruebaEliminada)
    
    
    
def cargar_lista(nombreArchivo):
    with open(nombreArchivo ,"r") as fichero:
        for elemento in fichero:
            cancion , grupo = elemento.strip().split(" - ")
            dicCanciones[cancion] = grupo
        print(dicCanciones)
    return dicCanciones



def agregar_cancion(nomCancion , nomArtista):
    dicCanciones[nomCancion] = nomArtista

def eliminar_cancion(nomCancion):
    if nomCancion in dicCanciones:
        dicCanciones.pop(nomCancion)
    else:
        print("La canción no está en la playlist")



def contar_canciones():
    contador = 0
    for cancion in dicCanciones:
        contador+=1
    print(contador)


def buscar_por_artista(nomArtista):
    listaCanciones = [] 
    for cancion in dicCanciones:
        if (dicCanciones[cancion] == nomArtista):
            listaCanciones.append(cancion)
    print(listaCanciones)
    return listaCanciones


#Pendiente --Hecho  a posteriori
def ordenar_alfabeticamente():
    tuplaCanciones = sorted(dicCanciones.items())
    return tuplaCanciones

#cargar_lista("playlist.txt")
#print(ordenar_alfabeticamente())

#Pendiente --Hecho  a posteriori
def crear_lista_aleatoria(n):
    #Ajustamos n por si es usuario introduce un número mayor que canciones hay
    n = min(n, len(dicCanciones))
    listRandom = random.sample(list(dicCanciones.keys()), n)
    print(listRandom)
    return  listRandom


#Corregido a posteriori

def guardar_lista(nomArchivo):
    with open(nomArchivo, "w") as fichero:
        for titulo, artista in dicCanciones.items():
            fichero.write(f"{titulo} - {artista}\n")

        
            
