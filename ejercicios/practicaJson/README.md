# Gestión de Inventario de Productos

## Descripción

Este programa en Python permite gestionar un inventario de productos para una tienda. Cada producto tiene atributos básicos como nombre, precio y cantidad en stock. Se enfoca en funcionalidades esenciales como agregar y listar productos, manteniendo la persistencia de datos mediante archivos JSON.

---

## Requisitos

### Clases y Métodos

1. **Clase Producto**:

   - **Atributos**:
     - `nombre`: Nombre del producto.
     - `precio`: Precio del producto.
     - `cantidad`: Cantidad disponible en stock.
   - **Métodos**:
     - `mostrar_informacion()`: Devuelve una cadena con la información básica del producto.
     - `convertir_a_diccionario()`: Convierte el producto a un diccionario para su serialización.

2. **Clase Inventario**:
   - **Atributos**:
     - `productos`: Lista de productos en el inventario.
   - **Métodos**:
     - `agregar_producto(producto)`: Agrega un producto al inventario.
     - `listar_productos()`: Lista todos los productos del inventario.
     - `guardar_en_json()`: Guarda los datos del inventario en un archivo JSON.
     - `cargar_desde_json()`: Carga los datos desde un archivo JSON.

---

## Funcionalidades

1. Añadir un nuevo producto al inventario.
2. Listar todos los productos del inventario.
3. Guardar y cargar el inventario desde un archivo JSON.

---
