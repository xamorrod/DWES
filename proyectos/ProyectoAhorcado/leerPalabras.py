import random

def leerPalabrasUnJugador():
    try:
        with open(
            "palabras.txt",
            "r",
            encoding="utf-8",
        ) as archivo:
            palabras = (
                archivo.read().splitlines()
            ) 
        return random.choice(palabras)  
    except FileNotFoundError:
        print("Error: El archivo 'palabras.txt' no se encontró.")
        return None  
    except Exception as e:
        print(f"Se produjo un error: {e}")
        return None  



