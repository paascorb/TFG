# Fichero de pruebas unitarias para VectorField por Pablo Ascorbe Fernández 16/06/2022
import unittest
import LogicaDeNegocio.Auxiliary as Aux
import PruebasUnitarias.Auxiliar as Puaux
from ModeloDeDominio.VectorField import VectorField


class TestVectorField(unittest.TestCase):

    def test_trocear_fmatrix(self):
        sc = Puaux.crear_sc_prueba()
        fblock_esperado = [[[1, 1, 1, 0], [1, 0, 0, 1], [0, 1, 0, 1], [0, 0, 1, 0]], [[1], [1], [0], [1]]]
        fblock_real = Aux.slice_fmatrix(sc.matrix, sc.c_vector)
        self.assertTrue(Puaux.comparar_matrices(fblock_esperado[0], fblock_real[0]) is True,
                        "Error en el test trocear_fmatrix")

    def test_add_route(self):
        sc = Puaux.crear_sc_prueba()
        vf = VectorField("vf", Aux.slice_fmatrix(sc.matrix, sc.c_vector), sc.c_vector)
        vf.add_route((sc.simplex[0], sc.simplex[4]))
        vf.add_route((sc.simplex[1], sc.simplex[7]))
        # vf.add_route((sc.simplex[2], sc.simplex[5]))
        vf.add_route((sc.simplex[5], sc.simplex[8]))
        vf.add_route((sc.simplex[3], sc.simplex[6]))
        routes_esperadas = {'a': ['c'], 'b': ['c'], 'ac': ['bc', 'ab'], 'd': ['c']}
        self.assertTrue(vf.routes == routes_esperadas, "Error: en el test add_route")

    if __name__ == '__main__':
        unittest.main()
