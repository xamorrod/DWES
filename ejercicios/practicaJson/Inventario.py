import json


class Inventario:

    def __init__(self):
        self.productos = []

    def agregar_producto(self, producto):
        self.productos.append(producto)

    def listar_producto(self):
        for producto in self.productos:
            producto.mostrar_informacion()

    def guardar_json(self):
        # Guardamos todos los datos del inventario en un json

        with open("productos.json", "w") as fichero:
            listaDiccionarios = []
            for producto in self.productos:
                listaDiccionarios.append(producto.convertir_a_diccionario())
            # Diccionario a cadena JSON
            json.dump(listaDiccionarios, fichero, indent=4)
