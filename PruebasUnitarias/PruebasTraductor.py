# Fichero de pruebas unitarias para la lógica del traductor por Pablo Ascorbe Fernández 15/06/2022
import unittest
import LogicaDeNegocio.Traductor as Tra
import LogicaDeNegocio.Auxiliary as Aux
from ModeloDeDominio.BooleanFunction import BooleanFunction


class TestTraductor(unittest.TestCase):

    def test_traductor_bl_to_sc(self):
        bf = BooleanFunction('bf', 3, [1, 1, 1, 1, 1, 1, 1, 1])
        sc = Tra.boolean_function_to_simplicial_complex(bf)
        self.assertTrue(True is Aux.is_simplicial_complex(sc.simplex), "Error en el test_constructor_bl_to_sc")
        bf2 = BooleanFunction('bf2', 4, [1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 0, 0, 0])
        sc2 = Tra.boolean_function_to_simplicial_complex(bf2)
        self.assertTrue(True is Aux.is_simplicial_complex(sc2.simplex), "Error en el test_constructor_bl_to_sc")
        print(sc2)