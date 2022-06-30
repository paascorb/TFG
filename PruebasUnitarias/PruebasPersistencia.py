# Fichero de pruebas unitarias para la persistencia desarrollado por Pablo Ascorbe Fernández 26/05/2022
import unittest
import PruebasUnitarias.PruebasAuxiliar as Puaux
import ModeloDeDominio.Auxiliary as Aux
from Persistencia.PersistenceSimplicialComplex import *
from Persistencia.PersistenceBooleanFunction import *


class TestPersistence(unittest.TestCase):

    def test_persistence(self):
        # Ha sido comentado para evitar problemas ya que el método de persistencia ha cambiado ligeramente
        # # Simplex:
        # simplex = Simplex('a', 0)
        # # Ahora persistiremos en un fichero llamado "prueba_persistencia_simplex" nuestro simplex
        # serialize(simplex, 'SimplicialComplexes')
        # # Y para comprobar que funciona lo vamos a deserializar y compara con el original
        # simplex_deserializado = simplex_decode(deserialize(simplex, 'SimplicialComplexes'))
        # self.assertTrue(simplex == simplex_deserializado)

        # BooleanFunctions:
        bf = BooleanFunction('bf', 3, ['a', 'b', 'c'], [1, 1, 1, 1, 1, 1, 1, 1])
        # Ahora persistiremos en un fichero llamado "prueba_persistencia_bf" nuestra función booleana
        serialize(bf, 'BooleanFunctions')
        # Y para comprobar que funciona lo vamos a deserializar y compara con el original
        bf_deserializado = bf_decode(deserialize(bf, 'BooleanFunctions'))
        self.assertTrue(bf == bf_deserializado)
        remove(bf, "BooleanFunctions")

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
        serialize(sc, 'SimplicialComplexes')
        # Y para comprobar que funciona lo vamos a deserializar y compara con el original
        sc_deserializado = sc_decode(deserialize(sc, 'SimplicialComplexes'))
        self.assertTrue(sc == sc_deserializado)

    def test_vector_fields(self):
        sc = Puaux.crear_sc_prueba()
        vf = VectorField("vf", Aux.slice_fmatrix(sc.matrix, sc.c_vector), sc.c_vector)
        vf.add_route((sc.simplex[0], sc.simplex[4]))
        vf.add_route((sc.simplex[1], sc.simplex[7]))
        sc.add_vector_field(vf)
        serialize(sc, 'SimplicialComplexes')
        sc_deserializado = sc_decode(deserialize(sc, 'SimplicialComplexes'))
        self.assertTrue(sc == sc_deserializado)
        delete_simplicial_complex(sc)

    def test_persistencia_sc(self):
        sc = Puaux.crear_sc_prueba()
        create_simplicial_complex(sc)
        sc_deserializado = read_simplicial_complex(sc)
        self.assertTrue(sc == sc_deserializado, "Error en el test persistencia_sc")
        sc.collapse(Aux.get_sim_by_name(sc.simplex, "d"), Aux.get_sim_by_name(sc.simplex, "ad"))
        update_simplicial_complex(sc)
        up_sc_deserializado = read_simplicial_complex(sc)
        self.assertTrue(sc == up_sc_deserializado, "Error en el test persistencia_sc")
        # all_sc = list_simplicial_complex()
        # self.assertTrue(2 == len(all_sc))
        delete_simplicial_complex(sc)
        sc_to_delete = SimplicialComplex("sc", 0, [])
        delete_simplicial_complex(sc_to_delete)

    def test_persistencia_bf(self):
        bf = Puaux.crear_bf_prueba()
        create_boolean_function(bf)
        bf_DTO = BooleanFunction("fb_prueba", 0, [], [])
        bf_deserializada = read_boolean_function(bf_DTO)
        self.assertTrue(bf_deserializada == bf, "Error en el test persistencia_bf")
        delete_boolean_function(bf_DTO)

    if __name__ == '__main__':
        unittest.main()
