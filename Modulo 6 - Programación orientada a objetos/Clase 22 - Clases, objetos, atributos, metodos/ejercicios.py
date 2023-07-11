import unittest

# Actividades de Programación Orientada a Objetos - Temática: Figuras Geométricas

# Actividad 1: Clase y objetos
# Completa la definición de la clase 'Rectangulo' con atributos 'base' y 'altura'
# Crea dos objetos 'rectangulo1' y 'rectangulo2' de la clase 'Rectangulo' con diferentes medidas

class Rectangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

# Prueba de la clase Rectangulo
class TestRectangulo(unittest.TestCase):
    def test_rectangulo(self):
        rectangulo1 = Rectangulo(4, 5)
        rectangulo2 = Rectangulo(3, 6)

        self.assertEqual(rectangulo1.base, 4)
        self.assertEqual(rectangulo1.altura, 5)
        self.assertEqual(rectangulo2.base, 3)
        self.assertEqual(rectangulo2.altura, 6)

unittest.main()


# Actividad 2: Atributos y métodos
# Completa el método 'calcular_area' de la clase 'Rectangulo' para calcular el área del rectángulo
# utilizando la fórmula: área = base * altura
# Imprime el área del 'rectangulo1'

class Rectangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def calcular_area(self):
        return self.base * self.altura

# Prueba del método calcular_area
class TestCalcularArea(unittest.TestCase):
    def test_calcular_area(self):
        rectangulo1 = Rectangulo(4, 5)

        self.assertEqual(rectangulo1.calcular_area(), 20)

unittest.main()


# Actividad 3: Métodos adicionales
# Completa el método 'es_cuadrado' de la clase 'Rectangulo' para determinar si el rectángulo es un cuadrado
# El rectángulo es un cuadrado si la base y la altura son iguales
# Imprime 'Es cuadrado' si 'rectangulo2' es un cuadrado, de lo contrario, imprime 'No es cuadrado'

class Rectangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def calcular_area(self):
        # Código anterior

    def es_cuadrado(self):
        return self.base == self.altura

# Prueba del método es_cuadrado
class TestEsCuadrado(unittest.TestCase):
    def test_es_cuadrado(self):
        rectangulo1 = Rectangulo(4, 5)
        rectangulo2 = Rectangulo(6, 6)

        self.assertFalse(rectangulo1.es_cuadrado())
        self.assertTrue(rectangulo2.es_cuadrado())

unittest.main()


# Al ejecutar el archivo, se realizarán las pruebas y se mostrará el resultado de cada una de ellas. 
# Si todas las pruebas pasan sin errores, significa que la implementación es correcta según los criterios establecidos en las pruebas.