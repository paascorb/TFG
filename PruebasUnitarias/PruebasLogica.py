# Fichero de pruebas unitarias para la lógica de negocio desarrollado por Pablo Ascorbe Fernández 17/06/2022
import unittest
import PruebasUnitarias.PruebasAuxiliar as Puaux
from LogicaDeNegocio import SimplicialComplexManager, BooleanFunctionManager


class TestLogica(unittest.TestCase):

    def test_logica_sc(self):
        sc = Puaux.crear_sc_prueba()
        SimplicialComplexManager.add_simplicial_complex(sc, "Prueba_Logica_sc")
        sc.collapse(sc.simplex[4], sc.simplex[8])
        SimplicialComplexManager.update_simplicial_complex(sc, "Prueba_Logica_sc")
        sc_deserializado = SimplicialComplexManager.get_simplicial_complex("Prueba_Logica_sc")
        self.assertTrue(sc == sc_deserializado)
        SimplicialComplexManager.remove_simplicial_complex("Prueba_Logica_sc")

    def test_logica_bl(self):
        bf = Puaux.crear_bf_prueba()
        BooleanFunctionManager.add_boolean_function(bf, "Prueba_Logica_bf")
        bf.outputs[0] = 1
        BooleanFunctionManager.update_boolean_function(bf, "Prueba_Logica_bf")
        bf_deserializado = BooleanFunctionManager.get_boolean_function("Prueba_Logica_bf")
        self.assertTrue(bf == bf_deserializado)
        BooleanFunctionManager.remove_boolean_function("Prueba_Logica_bf")
