from Inventario import Inventario
from Producto import Producto


def main():
    invent2 = Inventario()
    #producto1 = Producto("Aspiradora", 29.99, 10)
    #producto1.modificar_informacion(nombre="Amador")
    #producto1.mostrar_informacion()

    # invent.agregar_producto(producto1)

    # invent.listar_producto()
    # invent.guardar_json()
    invent2.cargar_inventario("productos.json")
    invent2.ordenar_productos()
    


if __name__ == "__main__":
    main()
