import random
#Definimos el atributo global del diccionario de canciones
dicCanciones = {}



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

cargar_lista("playlist.txt")
crear_lista_aleatoria(3) 

def guardar_lista(nomArchivo):
    with open(nomArchivo, "w") as fichero:
        for titulo, artista in dicCanciones.items():
            fichero.write(f"{titulo} - {artista}\n")

            
            
 