# Fichero de pruebas unitarias para la lógica de negocio desarrollado por Pablo Ascorbe Fernández 17/06/2022
import unittest
import PruebasUnitarias.PruebasAuxiliar as Puaux
from LogicaDeNegocio import SimplicialComplexManager, BooleanFunctionManager


class TestLogica(unittest.TestCase):

    def test_logica_sc(self):
        sc = Puaux.crear_sc_prueba()
        SimplicialComplexManager.add_simplicial_complex(sc)
        sc.collapse(sc.simplex[4], sc.simplex[8])
        SimplicialComplexManager.edit_simplicial_complex(sc)
        sc_deserializado = SimplicialComplexManager.get_simplicial_complex(sc.name)
        self.assertTrue(sc == sc_deserializado)
        SimplicialComplexManager.remove_simplicial_complex(sc.name)

    def test_logica_bl(self):
        bf = Puaux.crear_bf_prueba()
        BooleanFunctionManager.add_boolean_function(bf)
        bf.outputs[0] = 1
        BooleanFunctionManager.edit_boolean_function(bf)
        bf_deserializado = BooleanFunctionManager.get_boolean_function(bf.name)
        self.assertTrue(bf == bf_deserializado)
        BooleanFunctionManager.remove_boolean_function(bf.name)
