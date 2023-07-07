import unittest
from ejercicios import *

class TestEjercicios(unittest.TestCase):

    def test_ejercicio1(self):
        # Prueba del cálculo del área de un triángulo
        base = 8
        altura = 5
        resultado_esperado = 20.0
        self.assertAlmostEqual(area_triangulo(base, altura), resultado_esperado)

    def test_ejercicio2(self):
        # Prueba de concatenación de cadenas
        cadena1 = "Hola"
        cadena2 = "Mundo"
        resultado_esperado = "Hola Mundo"
        self.assertEqual(mensaje(cadena1, cadena2), resultado_esperado)

    def test_ejercicio3(self):
        # Prueba de comparación de números
        es_mayor = 20 > (8 + 10)
        resultado_esperado = True
        self.assertEqual(es_mayor(), resultado_esperado)

    def test_ejercicio4(self):
        # Prueba de la función saludo_personalizado
        nombre = "Juan"
        edad = 25
        resultado_esperado = "¡Hola Juan! Tienes 25 años."
        self.assertEqual(saludo_personalizado(nombre, edad), resultado_esperado)

if __name__ == '__main__':
    unittest.main()
