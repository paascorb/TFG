import unittest
import PruebasUnitarias.PruebasAuxiliar as Puaux
from Presentacion.Hasse import mostrar_diagrama_hasse


class TestHasse(unittest.TestCase):

    def test_hasse(self):
        sc = Puaux.crear_sc_prueba()
        mostrar_diagrama_hasse(sc)
        