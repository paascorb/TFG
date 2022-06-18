# Fichero de pruebas unitarias para VectorFieldResolver por Pablo Ascorbe Fernández 18/06/2022
import unittest
import PruebasUnitarias.PruebasAuxiliar as Puaux
from LogicaDeNegocio.VectorFieldResolver import *


class TestVectorField(unittest.TestCase):

    def test_resolve_block(self):
        sc = Puaux.crear_sc_prueba()
        sc.create_vector_field("vf")
        resolve_block(sc.vector_fields[0].fblocks[0], 0, sc.vector_fields[0], sc, True)
        self.assertTrue(bool(sc.vector_fields[0].routes))

    def test_resolve_field(self):
        sc = Puaux.crear_sc_prueba()
        sc.create_vector_field("vf")
        resolve_field(sc.vector_fields[0], sc)
        self.assertTrue(bool(sc.vector_fields[0]))

    if __name__ == '__main__':
        unittest.main()
