# Fichero de pruebas unitarias para VectorField por Pablo Ascorbe Fernández 16/06/2022
import unittest
import LogicaDeNegocio.Auxiliary as Aux
import PruebasUnitarias.Auxiliar as Puaux


class TestVectorField(unittest.TestCase):

    def test_trocear_fmatrix(self):
        sc = Puaux.crear_sc_prueba()
        fblock_esperado = [[[1, 1, 1, 0], [1, 0, 0, 1], [0, 1, 0, 1], [0, 0, 1, 0]], [[1], [1], [0], [1]]]
        fblock_real = Aux.trocear_fmatrix(sc.matrix, sc.c_vector)
        self.assertTrue(Puaux.comparar_matrices(fblock_esperado[0], fblock_real[0]) is True,
                        "Error en el test trocear_fmatrix")

    if __name__ == '__main__':
        unittest.main()
