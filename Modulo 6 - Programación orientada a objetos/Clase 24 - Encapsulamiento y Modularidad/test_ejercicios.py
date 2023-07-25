import unittest
from ejercicios import *

# Tests utilizando el módulo unittest

class TestTienda(unittest.TestCase):
    def setUp(self):
        self.producto1 = Producto("iPhone 13", "teléfono", 1200)
        self.producto2 = Producto("MacBook Pro", "computadora", 2500)
        self.producto3 = Producto("Smart TV", "televisor", 800)
        self.producto4 = Producto("iPad Air", "tablet", 700)
        self.producto5 = Producto("Auriculares inalámbricos", "accesorio", 100)

    def test_obtener_productos_por_categoria(self):
        productos = [self.producto1, self.producto2, self.producto3, self.producto4, self.producto5]
        categoria_telefonos = obtener_productos_por_categoria(productos, "teléfono")
        categoria_accesorios = obtener_productos_por_categoria(productos, "accesorio")

        self.assertEqual(len(categoria_telefonos), 1)
        self.assertEqual(categoria_telefonos[0].nombre, "iPhone 13")

        self.assertEqual(len(categoria_accesorios), 1)
        self.assertEqual(categoria_accesorios[0].nombre, "Auriculares inalámbricos")

    def test_calcular_total_compra(self):
        productos = [self.producto1, self.producto2, self.producto3, self.producto4, self.producto5]
        total_compra = calcular_total_compra(productos)

        self.assertEqual(total_compra, 5300)

    def test_obtener_producto_mas_caro(self):
        productos = [self.producto1, self.producto2, self.producto3, self.producto4, self.producto5]
        producto_mas_caro = obtener_producto_mas_caro(productos)

        self.assertEqual(producto_mas_caro.nombre, "MacBook Pro")
        self.assertEqual(producto_mas_caro.precio, 2500)

unittest.main()