# Fichero de pruebas unitarias para la persistencia desarrollado por Pablo Ascorbe Fernández 26/05/2022
import unittest
import PruebasUnitarias.PruebasAuxiliar as Puaux
import LogicaDeNegocio.Auxiliary as Aux
from ModeloDeDominio.BooleanFunction import BooleanFunction
from ModeloDeDominio.Simplex import Simplex
from ModeloDeDominio.SimplicialComplex import SimplicialComplex
from ModeloDeDominio.VectorField import VectorField
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

        # SimplicialComplex:
        s = Simplex('a', 0)
        v = Simplex('b', 0)
        w = Simplex('c', 0)
        r = Simplex('e', 0)
        t = Simplex('f', 0)
        sv = Simplex('ab', 1)
        sw = Simplex('ac', 1)
        vw = Simplex('bc', 1)
        sr = Simplex('ae', 1)
        rt = Simplex('ef', 1)
        svw = Simplex('abc', 2)

        s.set_faces()
        v.set_faces()
        w.set_faces()
        r.set_faces()
        t.set_faces()
        sv.set_faces({s, v})
        sw.set_faces({s, w})
        vw.set_faces({v, w})
        sr.set_faces({s, r})
        rt.set_faces({r, t})
        svw.set_faces({sv, sw, vw})

        simplices = {s, v, w, r, t, sv, sw, vw, sr, rt, svw}
        sc = SimplicialComplex('sc', 10, simplices)
        # Ahora persistiremos en un fichero llamado "prueba_persistencia_sc" nuestro complejo simplicial
        Persistence.serialize(sc, 'prueba_persistencia_sc')
        # Y para comprobar que funciona lo vamos a deserializar y compara con el original
        sc_deserializado = AuxiliaryParsing.sc_decode(Persistence.deserialize('prueba_persistencia_sc'))
        self.assertTrue(sc == sc_deserializado)

    def test_vector_fields(self):
        sc = Puaux.crear_sc_prueba()
        vf = VectorField("vf", Aux.slice_fmatrix(sc.matrix, sc.c_vector), sc.c_vector)
        vf.add_route((sc.simplex[0], sc.simplex[4]))
        vf.add_route((sc.simplex[1], sc.simplex[7]))
        sc.add_vector_field(vf)
        Persistence.serialize(sc, 'pruebas_persistencia_vf')
        sc_deserializado = AuxiliaryParsing.sc_decode(Persistence.deserialize('pruebas_persistencia_vf'))
        self.assertTrue(sc == sc_deserializado)

    if __name__ == '__main__':
        unittest.main()
