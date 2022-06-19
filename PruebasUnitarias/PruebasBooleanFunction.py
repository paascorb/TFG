# Fichero de pruebas unitarias para la lógica de las fb desarrollado por Pablo Ascorbe Fernández 23/05/2022
import unittest
import ModeloDeDominio.Auxiliary as Aux


class TestBooleanFunction(unittest.TestCase):

    def test_check_output(self):
        self.assertTrue([2, 4].sort() == Aux.check_output(6).sort(), "Error en test_check_output")
        self.assertTrue([6, 5, 4, 3, 2, 1].sort() == Aux.check_output(7).sort(), "Error en test_check_output")
        self.assertTrue(list(range(1, 31)).sort() == Aux.check_output(31).sort(), "Error en test_check_output")
        self.assertTrue(list(range(1, 1023)).sort() == Aux.check_output(1023).sort(), "Error en test_check_output")
        # Sin comprobar, en el método check_output(), si la lista tiene ya o no ese elemento para calcular sus hijos
        # este ha tardado 16.191s
        # Comprobando si está previamente para no hacer calculos redundantes pasamos de 16.191s a 0.039s
        # Con la última modificación ha pasado a 0.002s
        self.assertTrue(list(range(1, 2047)).sort() == Aux.check_output(2047, list()).sort()
                        , "Error en test_check_output")
        # Con el numero 2^11 que es exactamente 2048, si le quitamos uno son 2047 que serían unos en las 11 primeras
        # posiciones, nos ha tardado 164.24s. Cambiando el método ha pasado a 0.142s
        # 0.002s con la última modificación
        self.assertTrue(list(range(1, 4095)).sort() == Aux.check_output(4095, list()).sort()
                        , "Error en test_check_output")
        # Para 2^12 tenemos un resultado 1.106s con la primera modificación (no comprobar elementos ya verificados).
        # Para la segunda modificación conseguimos un tiempo de 0.561s
        self.assertTrue(list(range(1, 16383)).sort() == Aux.check_output(16383, list()).sort()
                        , "Error en test_check_output")
        # Para 2^14 no tenemos el tiempo que tardaba original mente la función pero con las dos últimas actualizaciones
        # tarda 9.447s
        self.assertTrue(list(range(1, 32767)).sort() == Aux.check_output(32767, list()).sort()
                        , "Error en test_check_output")
        # Con 2^15 son 41.674s
        # self.assertTrue(list(range(1, 1048575)).sort() == Aux.check_output(1048575, list()).sort())
        # Con el método inicial era totalmente inviable ejecutar 2^20.
        # Con la nueva modificación tampoco logramos ejecutarlo.
        # Con la última modificación, muy pensada en este caso concreto ha pasado a ser 0.076s
        # self.assertTrue(list(range(1, 3145727)).sort() == Aux.check_output(3145727, list()).sort()) aun así esta línea
        # ha estado más de 1 hora

    def test_is_monotone(self):
        self.assertTrue(True is Aux.is_monotone([1, 1, 1, 1]), "Error en test_is_monotone")
        self.assertTrue(True is Aux.is_monotone([0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0]),
                        "Error en test_is_monotone")

    if __name__ == '__main__':
        unittest.main()
