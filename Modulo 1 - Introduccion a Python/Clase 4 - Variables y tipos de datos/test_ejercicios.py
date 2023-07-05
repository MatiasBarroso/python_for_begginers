import unittest
from ejercicios import *

class TestEjercicios(unittest.TestCase):

    def test_ejercicio1(self):
        self.assertIsNotNone(name, "La variable 'nombre' no ha sido asignada.")
        self.assertIsInstance(name, str, "La variable 'nombre' debe ser una cadena de texto.")

        self.assertIsNotNone(age, "La variable 'edad' no ha sido asignada.")
        self.assertIsInstance(age, int, "La variable 'edad' debe ser un número entero.")

        self.assertIsNotNone(student, "La variable 'estudiante' no ha sido asignada.")
        self.assertIsInstance(student, bool, "La variable 'estudiante' debe ser un valor booleano.")

    def test_ejercicio2(self):
        self.assertIsNotNone(number1, "La variable 'numero1' no ha sido asignada.")
        self.assertIsInstance(number1, int, "La variable 'numero1' debe ser un número entero.")

        self.assertIsNotNone(number2, "La variable 'numero2' no ha sido asignada.")
        self.assertIsInstance(number2, int, "La variable 'numero2' debe ser un número entero.")

        self.assertIsNotNone(sum, "La variable 'suma' no ha sido asignada.")
        self.assertIsInstance(sum, int, "La variable 'suma' debe ser un número entero.")

        self.assertIsNotNone(rest, "La variable 'resta' no ha sido asignada.")
        self.assertIsInstance(rest, int, "La variable 'resta' debe ser un número entero.")

        self.assertIsNotNone(multiplication, "La variable 'multiplicacion' no ha sido asignada.")
        self.assertIsInstance(multiplication, int, "La variable 'multiplicacion' debe ser un número entero.")

        self.assertIsNotNone(division, "La variable 'division' no ha sido asignada.")
        self.assertIsInstance(division, float, "La variable 'division' debe ser un número de punto flotante.")

if __name__ == '__main__':
    unittest.main()