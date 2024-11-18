import json
from Producto import Producto
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

    def cargar_inventario(self, nombreFichero):
        # Cargamos los datos de un JSON y los convertimos en objetos para poder acceder a ellos

        with open(nombreFichero , "r") as fichero:
            productos = json.load(fichero)

            productoMayor  = ([producto["nombre"] for producto in productos if producto["precio"] > 10])
            print(productoMayor)
            for producto in productos:
                productoN = Producto(producto["nombre"] , producto["precio"], producto["cantidad"])
                self.agregar_producto(productoN)

    def ordenar_productos(self):
        # Ordenamos cantidad mayor a menor y cantidad de menor a mayor

        self.productos = sorted(self.productos , key= lambda producto :(-producto.cantidad , producto.precio))

        for producto in self.productos:
            producto.mostrar_informacion()
