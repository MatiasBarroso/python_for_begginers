import unittest

# Ejercicio 1
def convertir_a_entero(valor):
    try:
        # Completa aquí con la conversión a entero y devuelve el resultado
        pass
    except ValueError:
        # Completa aquí con el mensaje de error en caso de valor no numérico
        pass

# Ejercicio 2
def dividir(dividendo, divisor):
    try:
        # Completa aquí con la división y devuelve el resultado
        pass
    except ZeroDivisionError:
        # Completa aquí con el mensaje de error en caso de división por cero
        pass

# Ejercicio 3
def leer_archivo(nombre_archivo):
    try:
        # Completa aquí con la apertura y lectura del archivo, y devuelve el contenido
        pass
    except FileNotFoundError:
        # Completa aquí con el mensaje de error en caso de archivo no encontrado
        pass

# Ejercicio 4
def calcular_promedio(numeros):
    try:
        # Completa aquí con el cálculo del promedio y devuelve el resultado
        pass
    except ZeroDivisionError:
        # Completa aquí con el mensaje de error en caso de división por cero
        pass

# Ejercicio 5
def convertir_a_entero_str(cadena):
    try:
        # Completa aquí con la conversión de la cadena a entero y devuelve el resultado
        pass
    except ValueError:
        # Completa aquí con el mensaje de error en caso de cadena no numérica
        pass

# Tests utilizando unittest
class EjerciciosTest(unittest.TestCase):
    def test_convertir_a_entero(self):
        self.assertEqual(convertir_a_entero("123"), 123)
        self.assertEqual(convertir_a_entero("abc"), "Error: el valor ingresado no es numérico")

    def test_dividir(self):
        self.assertEqual(dividir(10, 2), 5)
        self.assertEqual(dividir(5, 0), "Error: división por cero")

    def test_leer_archivo(self):
        self.assertEqual(leer_archivo("archivo.txt"), "Contenido del archivo")
        self.assertEqual(leer_archivo("archivo_no_existente.txt"), "Error: archivo no encontrado")

    def test_calcular_promedio(self):
        self.assertEqual(calcular_promedio([1, 2, 3, 4, 5]), 3)
        self.assertEqual(calcular_promedio([]), "Error: la lista está vacía")

    def test_convertir_a_entero_str(self):
        self.assertEqual(convertir_a_entero_str("123"), 123)
        self.assertEqual(convertir_a_entero_str("abc"), "Error: la cadena no es numérica")

if __name__ == "__main__":
    unittest.main()
