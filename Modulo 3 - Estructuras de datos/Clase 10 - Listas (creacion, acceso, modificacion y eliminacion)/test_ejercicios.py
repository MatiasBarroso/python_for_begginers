import unittest
from ejercicios import *

# Prueba del Ejercicio 1
class TestObtenerTercerElemento(unittest.TestCase):
    def test_obtener_tercer_elemento(self):
        lista = [10, 20, 30, 40, 50]
        resultado = obtener_tercer_elemento(lista)
        self.assertEqual(resultado, 30)


# Prueba del Ejercicio 2
class TestModificarSegundoElemento(unittest.TestCase):
    def test_modificar_segundo_elemento(self):
        lista = ['manzana', 'naranja', 'plátano']
        modificar_segundo_elemento(lista, 'uva')
        self.assertEqual(lista, ['manzana', 'uva', 'plátano'])


# Prueba del Ejercicio 3
class TestEliminarPrimerElemento(unittest.TestCase):
    def test_eliminar_primer_elemento(self):
        lista = ['rojo', 'verde', 'azul']
        eliminar_primer_elemento(lista)
        self.assertEqual(lista, ['verde', 'azul'])


# Prueba del Ejercicio 4
class TestOperacionesConLista(unittest.TestCase):
    def test_operaciones_con_lista(self):
        numeros = [10, 20, 30]
        self.assertEqual(operaciones_con_lista(numeros), [10, 20, 25, 30, 40])


# Prueba del Ejercicio 5
class TestBuscarIndice(unittest.TestCase):
    def test_buscar_indice(self):
        numeros = [5, 3, 8, 2, 10]
        resultado = buscar_indice(8, numeros)
        self.assertEqual(resultado, 2)


# Prueba del Ejercicio 6
class TestCalcularSuma(unittest.TestCase):
    def test_calcular_suma(self):
        numeros = [1, 2, 3, 4, 5]
        resultado = calcular_suma(numeros)
        self.assertEqual(resultado, 15)


# Prueba del Ejercicio 7
class TestConcatenarListas(unittest.TestCase):
    def test_concatenar_listas(self):
        frutas1 = ['manzana', 'naranja']
        frutas2 = ['plátano', 'uva']
        resultado = concatenar_listas(frutas1, frutas2)
        self.assertEqual(resultado, ['manzana', 'naranja', 'plátano', 'uva'])


# Prueba del Ejercicio 8
class TestInvertirLista(unittest.TestCase):
    def test_invertir_lista(self):
        letras = ['a', 'b', 'c', 'd', 'e']
        invertir_lista(letras)
        self.assertEqual(letras, ['e', 'd', 'c', 'b', 'a'])


# Prueba del Ejercicio 9
class TestContarElemento(unittest.TestCase):
    def test_contar_elemento(self):
        numeros = [1, 2, 3, 2, 4, 2]
        resultado = contar_elemento(2, numeros)
        self.assertEqual(resultado, 3)


# Prueba del Ejercicio 10
class TestEliminarDuplicados(unittest.TestCase):
    def test_eliminar_duplicados(self):
        colores = ['rojo', 'verde', 'azul', 'rojo', 'verde']
        
        resultado = eliminar_duplicados(colores)
        lista_sin_duplicados = sorted(resultado)
        self.assertEqual(lista_sin_duplicados, ['azul', 'rojo', 'verde'])

# Ejecutar las pruebas
if __name__ == '__main__':
    unittest.main()
