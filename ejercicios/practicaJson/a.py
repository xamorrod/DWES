import json

with open("productos.json", "r") as fichero:
    list = json.load(fichero)
    
    for producto in list:
    #Código de creación del objeto

#with open("productos.json", "w") as fichero:
    #Obtener lista de diccionarios para escribir
    #lista = []
   # json.dump(lista, fichero, indent=4)
    