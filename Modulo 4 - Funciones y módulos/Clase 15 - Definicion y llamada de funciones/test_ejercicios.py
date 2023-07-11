import unittest
from ejercicios import *

# Pruebas utilizando unittest
class TestFunciones(unittest.TestCase):
    def test_calcular_promedio(self):
        calificaciones1 = [8, 9, 7, 6, 8]
        self.assertEqual(calcular_promedio(calificaciones1), 7.6)
        calificaciones2 = [10, 9, 8, 10, 9, 10]
        self.assertEqual(calcular_promedio(calificaciones2), 9.33)

    def test_generar_usuario(self):
        self.assertEqual(generar_usuario("Juan", "Perez"), "juan.perez")
        self.assertEqual(generar_usuario("María", "Gómez"), "maría.gómez")

    def test_analizar_tweets(self):
        tweets = [
            "Me encantó la película",
            "No me gustó nada el final",
            "Excelente servicio en el restaurante",
            "Hoy hace un día hermoso"
        ]
        self.assertEqual(analizar_tweets(tweets, "encantó"), 25.0)
        self.assertEqual(analizar_tweets(tweets, "día"), 25.0)
        self.assertEqual(analizar_tweets(tweets, "malo"), 0.0)

    def test_convertir_temperatura(self):
        self.assertEqual(convertir_temperatura(25), 77.0)
        self.assertEqual(convertir_temperatura(0), 32.0)
        self.assertEqual(convertir_temperatura(-10), 14.0)

if __name__ == "__main__":
    unittest.main()
