# Fichero de pruebas unitarias para la persistencia desarrollado por Pablo Ascorbe Fernández 26/05/2022
import unittest

from ModeloDeDominio.BooleanFunction import BooleanFunction
from ModeloDeDominio.Simplex import Simplex
from Persistencia import AuxiliaryParsing, Persistence


class TestPersistence(unittest.TestCase):

    def test_persistence(self):
        # Simplex:
        simplex = Simplex('a', 0)
        # Ahora persistiremos en un fichero llamado "prueba_persistencia_simplex" nuestro simplex
        Persistence.serialize(simplex, 'prueba_persistencia_simplex')
        # Y para comprobar que funciona lo vamos a deserializar y compara con el original
        simplex_deserializado = AuxiliaryParsing.simplex_decode(Persistence.deserialize('prueba_persistencia_simplex'))
        self.assertTrue(simplex == simplex_deserializado)

        # BooleanFunction:
        bf = BooleanFunction('bf', 3, [1, 1, 1, 1, 1, 1, 1, 1])
        # Ahora persistiremos en un fichero llamado "prueba_persistencia_bf" nuestra función booleana
        Persistence.serialize(bf, 'prueba_persistencia_bf')
        # Y para comprobar que funciona lo vamos a deserializar y compara con el original
        bf_deserializado = AuxiliaryParsing.bf_decode(Persistence.deserialize('prueba_persistencia_bf'))
        self.assertTrue(bf == bf_deserializado)
