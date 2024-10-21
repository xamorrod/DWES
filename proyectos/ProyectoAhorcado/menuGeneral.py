from leerPalabras import leerPalabrasUnJugador
from dibujarAhorcado import *
from menuJuego import menuJuego


# Menú inicial
def menuGeneral():
    confirm = False
    modalidad = int(input("Introduce la modalidad a la que deseas jugar\n1- Modo un jugador\n2- Modo dos jugadores\n"))
    while not confirm:
        if modalidad == 1:
            confirm = True
            palabraElegida = modoUnJugador()
            menuJuego(palabraElegida)
        elif modalidad == 2:
            confirm = True
            palabraElegida = modoDosJugadores()
            menuJuego(palabraElegida)
        else:
            print("Introduce un valor válido")


# Menú en modo un jugador
def modoUnJugador():
    print("Eligiendo palabra aleatoriamente de lista de palabras")
    palabraElegida = leerPalabrasUnJugador()
    return palabraElegida


# Menú en modo dos jugadores
def modoDosJugadores():
    palabraElegida = input("Introduce la palabra para comenzar el juego ").lower()

    # Añadimos cada nueva palabra a la lista de palabras
    with open("palabras.txt", "a", encoding="utf-8") as archivo:
        archivo.write(palabraElegida + "\n")

    return palabraElegida
