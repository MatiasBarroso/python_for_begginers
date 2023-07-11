import unittest
from ejercicios import *


# Prueba del Ejercicio 1
class TestCrearDiccionario(unittest.TestCase):
    def test_crear_diccionario(self):
        resultado = crear_diccionario()
        self.assertEqual(resultado, {})

# Prueba del Ejercicio 2
class TestObtenerValor(unittest.TestCase):
    def test_obtener_valor(self):
        diccionario = {'nombre': 'Juan', 'edad': 25, 'ciudad': 'México'}
        resultado1 = obtener_valor(diccionario, 'nombre')
        resultado2 = obtener_valor(diccionario, 'apellido')
        self.assertEqual(resultado1, 'Juan')
        self.assertEqual(resultado2, None)


# Prueba del Ejercicio 3
class TestModificarValor(unittest.TestCase):
    def test_modificar_valor(self):
        diccionario = {'nombre': 'Juan', 'edad': 25, 'ciudad': 'México'}
        modificar_valor(diccionario, 'edad', 30)
        self.assertEqual(diccionario['edad'], 30)


# Prueba del Ejercicio 4
class TestAgregarElemento(unittest.TestCase):
    def test_agregar_elemento(self):
        diccionario = {'nombre': 'Juan', 'edad': 25}
        agregar_elemento(diccionario, 'ciudad', 'México')
        self.assertEqual(diccionario['ciudad'], 'México')


# Prueba del Ejercicio 5
class TestEliminarElemento(unittest.TestCase):
    def test_eliminar_elemento(self):
        diccionario = {'nombre': 'Juan', 'edad': 25, 'ciudad': 'México'}
        eliminar_elemento(diccionario, 'edad')
        self.assertNotIn('edad', diccionario)

# Ejecutar las pruebas
if __name__ == '__main__':
    unittest.main()
