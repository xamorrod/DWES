from Producto import Producto
from Inventario import Inventario


def main():
    invent = Inventario()
    producto1 = Producto("Aspiradora", 29.99, 10)
    print(producto1.convertir_a_diccionario)
    invent.agregar_producto(producto1)

    invent.listar_producto()
    invent.guardar_json()


if __name__ == "__main__":
    main()
