class Producto:

    def __init__(self, nombre, precio, cantidad):
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad
    
    # Funciones de la clase
    
    def mostrar_informacion(self):
        print(f"El nombre del producto es {self.nombre} el precio es {self.precio} la cantidad es {self.cantidad}")
    
    #El método convertir a diccionario puede hacerse con el __dict__
    def convertir_a_diccionario(self):
        return {
            "nombre" : self.nombre,
            "precio" : self.precio,
            "cantidad" : self.cantidad
        } 


