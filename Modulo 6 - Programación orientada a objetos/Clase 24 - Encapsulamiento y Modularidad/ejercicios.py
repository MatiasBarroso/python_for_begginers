import unittest

# Actividad: Módulo Tienda

# Implementa las siguientes funciones en un módulo llamado 'tienda.py' que se utilizará en este ejercicio.

# Clase Producto
# Crea una clase llamada 'Producto' para representar un producto en una tienda de electrónicos.
# Un producto debe tener un nombre, una categoría (como 'teléfono', 'computadora', etc.), y un precio.

class Producto:
    def __init__(self, nombre, categoria, precio):
        self.nombre = nombre
        self.categoria = categoria
        self.precio = precio


# Función 1: Obtener productos por categoría
# Recibe una lista de productos y una categoría. Devuelve una nueva lista con los productos que pertenecen a la categoría especificada.
def obtener_productos_por_categoria(productos, categoria):
    pass

# Función 2: Calcular el total de la compra
# Recibe una lista de productos y devuelve el precio total de la compra.
def calcular_total_compra(productos):
    pass

# Función 3: Producto más caro
# Recibe una lista de productos y devuelve el producto más caro de la lista.
def obtener_producto_mas_caro(productos):
    pass


