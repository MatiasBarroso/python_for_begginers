import unittest
from ejercicios import *

class TestEjercicios(unittest.TestCase):
    def test_empleado_y_empleado_tiempo_completo(self):
        empleado1 = Empleado("Juan", 30, 2500, "Ventas")
        empleado2 = EmpleadoTiempoCompleto("María", 35, 3000, "Recursos Humanos")

        self.assertEqual(empleado1.get_salario(), 2500)
        empleado1.aumentar_salario(10)
        self.assertEqual(empleado1.get_salario(), 2750)

        self.assertEqual(empleado2.get_salario(), 3000)
        empleado2.aumentar_salario(5)
        self.assertEqual(empleado2.get_salario(), 3150)

        salario_anual_empleado2 = empleado2.calcular_salario_anual()
        self.assertEqual(salario_anual_empleado2, 37800)

    def test_crear_empleado(self):
        empleado3 = crear_empleado("Carlos", 28, 2000, "Contabilidad")
        self.assertEqual(empleado3.get_salario(), 2000)
        empleado3.aumentar_salario(8)
        self.assertEqual(empleado3.get_salario(), 2160)

unittest.main()