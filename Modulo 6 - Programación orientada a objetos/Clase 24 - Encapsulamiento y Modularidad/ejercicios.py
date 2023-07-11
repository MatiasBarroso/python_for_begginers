import unittest

# Actividad: Módulo Utilidades

# Implementa las siguientes funciones en un módulo llamado 'utilidades.py' que se utilizará en este ejercicio.

# Función 1: Obtener el área de un círculo
# Recibe el radio del círculo y devuelve el área calculada utilizando la fórmula: área = pi * radio^2
def obtener_area_circulo(radio):
    pass

# Función 2: Obtener el área de un triángulo
# Recibe la base y la altura del triángulo y devuelve el área calculada utilizando la fórmula: área = (base * altura) / 2
def obtener_area_triangulo(base, altura):
    pass

# Función 3: Obtener el máximo de una lista
# Recibe una lista de números y devuelve el valor máximo de la lista utilizando la función max() de Python.
def obtener_maximo(lista):
    pass


# Tests utilizando el módulo unittest

class TestUtilidades(unittest.TestCase):
    def test_obtener_area_circulo(self):
        self.assertEqual(obtener_area_circulo(5), 78.54)
        self.assertEqual(obtener_area_circulo(2.5), 19.63)

    def test_obtener_area_triangulo(self):
        self.assertEqual(obtener_area_triangulo(4, 5), 10.0)
        self.assertEqual(obtener_area_triangulo(3.5, 2.5), 4.375)

    def test_obtener_maximo(self):
        self.assertEqual(obtener_maximo([2, 5, 9, 1, 7]), 9)
        self.assertEqual(obtener_maximo([-5, -2, -9, -1, -7]), -1)

unittest.main()
