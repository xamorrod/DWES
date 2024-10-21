from dibujarAhorcado import *

# Menú para el juego dada la palabra
def menuJuego(palabra):

    intento = 0
    print("Iniciando juego...")

    # Añadiendo espacios para que en el modo 2 jugadores no se vea la palabra
    for espacio in range (30):
        print(".")

    # Generamos una cadena del tamaño de la palabra escogida
    cadenaSolucion = "-" * len(palabra)
    letrasUsadas = []

    while intento < 5:

        letra = input("Introduce una letra ").lower()
       
        if letra not in letrasUsadas:
            # Añadimos la letra usada para que se compruebe a posteriori
            letrasUsadas.append(letra)
            # Vemos si la palabra contiene la letra escogida
            if letra[0] in str(palabra):
                
                cadenaSolucion = rellenarEspacios(letra, palabra, cadenaSolucion)
                print(cadenaSolucion)

                if "-" not in cadenaSolucion:
                    print("¡Felicidades! Has adivinado la palabra:", palabra)
                    break
            else:
                intento += 1
                match intento:
                    case 1:
                        dibujarSuelo()
                        print(cadenaSolucion)
                    case 2:
                        dibujarCabeza()
                        print(cadenaSolucion)
                    case 3:
                        dibujarCuerpo()
                        print(cadenaSolucion)
                    case 4:
                        dibujarBrazos()
                        print(cadenaSolucion)
                    case 5:
                        dibujarPiernas()
                        print("Perdiste, la palabra correcta era ..." , palabra)
        else:
            print("No puedes repetir letra\nPor ahora has usado",letrasUsadas)


# Dada una letra , la cadena con los espacios por rellenar con "-" y la palabra objetivo sustituye las ocurrencias
# de la palabra objetivo en la cadenaEmpty
def rellenarEspacios(letra, palabra, cadenaSolucion):
    palabra = str(palabra)
    letra = str(letra)
    cadenaSolucion = str(cadenaSolucion)

    nuevaCadena = cadenaSolucion
    for i in range(len(palabra)):
        if palabra[i] == letra:
            nuevaCadena = nuevaCadena[:i] + letra + nuevaCadena[i + 1 :]

    return nuevaCadena
