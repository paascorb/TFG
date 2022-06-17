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
        # for elem in sc.simplex:
        #     print(elem.name + " caras: " + str(elem.faces))
        vf = VectorField("vf", sc.matrix, sc.c_vector)
        vf.add_route((sc.simplex[0], sc.simplex[4]))
        vf.add_route((sc.simplex[1], sc.simplex[7]))
        #vf.add_route((sc.simplex[2], sc.simplex[5]))
        print(vf.routes)

    if __name__ == '__main__':
        unittest.main()
