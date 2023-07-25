import unittest
from ejercicio import *


class TestEjercicios(unittest.TestCase):
    def test_formatear_cadena(self):
        resultado1 = formatear_cadena("Ana", 25, "Madrid")
        self.assertEqual(resultado1, "¡Hola, mi nombre es Ana, tengo 25 años y soy de Madrid!")

        resultado2 = formatear_cadena("Carlos", 30, "Barcelona")
        self.assertEqual(resultado2, "¡Hola, mi nombre es Carlos, tengo 30 años y soy de Barcelona!")

    def test_formatear_url(self):
        resultado1 = formatear_url("www.ejemplo.com", "inicio")
        self.assertEqual(resultado1, "https://www.ejemplo.com/inicio")

        resultado2 = formatear_url("www.python.org", "documentacion")
        self.assertEqual(resultado2, "https://www.python.org/documentacion")
        
    def test_formatear_cadena(self):
        resultado1 = formatear_cadena("Ana", 25, "Madrid")
        self.assertEqual(resultado1, "¡Hola, mi nombre es Ana, tengo 25 años y soy de Madrid!")

        resultado2 = formatear_cadena("Carlos", 30, "Barcelona")
        self.assertEqual(resultado2, "¡Hola, mi nombre es Carlos, tengo 30 años y soy de Barcelona!")

    def test_formatear_url(self):
        resultado1 = formatear_url("www.ejemplo.com", "inicio")
        self.assertEqual(resultado1, "https://www.ejemplo.com/inicio")

        resultado2 = formatear_url("www.python.org", "documentacion")
        self.assertEqual(resultado2, "https://www.python.org/documentacion")
    


unittest.main()