import unittest
from datetime import datetime, time
from ejercicios import dia_de_semana, hora_formato_12


class TestDiaDeSemana(unittest.TestCase):
    def test_dia_de_semana(self):
        fecha = datetime(2023, 7, 25)
        self.assertEqual(dia_de_semana(fecha), 'Lunes')


class TestHoraFormato12(unittest.TestCase):
    def test_hora_formato_12(self):
        hora_am = time(9, 30)
        self.assertEqual(hora_formato_12(hora_am), '09:30 AM')


if __name__ == '__main__':
    unittest.main()
