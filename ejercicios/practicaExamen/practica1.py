import math

def mayorDeTres(num1 , num2, num3):
    listaOrdenar = [num1 ,num2 , num3]
    listaOrdenar.sort()
    print(listaOrdenar[2])

def mayorDeTresSinLista():

    num1 = int(input("Introduce un número"))
    num2 = int(input("Introduce otro número"))
    num3 = int(input("Introduce otro número"))
    
    tuplaNum = (num1 , num2 ,num3)
    print(max(tuplaNum))
    
def ejerLista():
    enterosList = [ 1 , 5, 12, 2 , 5, 12 ,9]
    nuevaList = []
    for num in enterosList:
        if num % 2 != 0:
            nuevaList.append(num*3)
            

    nuevaList.sort( reverse=True)
    print(nuevaList)


def ejer3():
    nomCiudades = ("Ciudad Juárez" , "Singapur" , "Guanajuato" , "Montevideo" , "Detroit")
    dicCiudades = {}
    for ciudad in nomCiudades:
        dicCiudades[ciudad] = len(ciudad)

    print(dicCiudades)


def ejer4():
    listNum = []
    confirm = True

    while (confirm):
        opcion = int(input("Introduce la opción que desees "))

        match opcion:
            case 1:
                num = int(input("Introduce un número a la lista "))
                listNum.append(num)
                continue
            case 2:
                media = sum(media) / len(media)
                print("La media es " , media)
                continue
            case 3:
                num = int(input("Introduce un número y vamos a ver cuántas veces aparece "))
                print(listNum.count(num))
                continue
            case 4:
                print("Saliendo del programa")
                confirm = False
                continue
            

def ejer5():
    puntaje = {}
    promedio = {}
    with open ("puntaje.txt" , "r") as ficheroNotas:
        for elemento  in ficheroNotas:
            nombre , nota = elemento.strip().split("-")
            nota = float(nota)
            if(nombre in puntaje):
                
                notas = puntaje[nombre]
                notas.append(nota)
                puntaje[nombre] = notas
            else:
                puntaje[nombre] = [nota]
            
            #Calculo de nota media para escribi
    print(puntaje)    
    with open ("promedio.txt" , "w") as ficheroPromedio:
        for elemento , notas in puntaje.items():
            media = sum(notas) / len(notas)
            linea = f"{nombre} - {media}\n"
            ficheroPromedio.write(linea)

ejer5()