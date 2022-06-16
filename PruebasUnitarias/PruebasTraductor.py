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

    def test_traductor_sc_to_bl(self):
        sc = Aux.crear_sc_prueba()
        fb = Tra.simplicial_complex_to_boolean_function(sc)
        output = [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0]
        self.assertTrue(fb.outputs == output, "Error en el test sc_to_bl")

    def test_position_in_ouput(self):
        sc = Aux.crear_sc_prueba()
        sim_pos = dict()
        for sim in sc.simplex[:sc.c_vector[0]]:
            pos = 2 ** sim.index
            sim_pos[sim] = pos
        self.assertTrue(5 == Tra.position_in_ouput(sc.simplex[5], sim_pos), "Error en el test de position_in_output")
