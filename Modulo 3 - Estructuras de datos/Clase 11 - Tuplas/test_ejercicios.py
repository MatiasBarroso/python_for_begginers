import unittest
from ejercicios import *

# Prueba del Ejercicio 1
class TestCrearTupla(unittest.TestCase):
    def test_crear_tupla(self):
        resultado = crear_tupla()
        self.assertEqual(resultado, ('rojo', 'verde', 'azul'))


# Prueba del Ejercicio 2
class TestObtenerElemento(unittest.TestCase):
    def test_obtener_elemento(self):
        tupla = ('manzana', 'naranja', 'plátano')
        resultado1 = obtener_elemento(tupla, 1)
        resultado2 = obtener_elemento(tupla, 3)
        self.assertEqual(resultado1, 'naranja')
        self.assertEqual(resultado2, None)


# Prueba del Ejercicio 3
class TestObtenerLongitud(unittest.TestCase):
    def test_obtener_longitud(self):
        tupla = (1, 2, 3, 4, 5)
        resultado = obtener_longitud(tupla)
        self.assertEqual(resultado, 5)


# Prueba del Ejercicio 4
class TestConcatenarTuplas(unittest.TestCase):
    def test_concatenar_tuplas(self):
        tupla1 = ('a', 'b')
        tupla2 = ('c', 'd')
        resultado = concatenar_tuplas(tupla1, tupla2)
        self.assertEqual(resultado, ('a', 'b', 'c', 'd'))


# Prueba del Ejercicio 5
class TestRepetirTupla(unittest.TestCase):
    def test_repetir_tupla(self):
        tupla = ('a', 'b')
        resultado = repetir_tupla(tupla, 3)
        self.assertEqual(resultado, ('a', 'b', 'a', 'b', 'a', 'b'))

# Ejecutar las pruebas
if __name__ == '__main__':
    unittest.main()
