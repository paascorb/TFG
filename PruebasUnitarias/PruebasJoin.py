# Fichero de pruebas unitarias para la funcion join desarrollado por Pablo Ascorbe Fernández 19/06/2022
import unittest
import PruebasUnitarias.PruebasAuxiliar as Puaux

import ModeloDeDominio.Auxiliary as Aux
import LogicaDeNegocio.Join as Join
from ModeloDeDominio.Simplex import Simplex
from ModeloDeDominio.SimplicialComplex import SimplicialComplex


class TestJoin(unittest.TestCase):

    def test_generate_sim_name(self):
        sc = Puaux.crear_sc_prueba()
        expected_name = "ab"
        name = Join.generate_sim_name([Aux.get_sim_by_name(sc.simplex, "b"),
                                       Aux.get_sim_by_name(sc.simplex, "a")])
        self.assertTrue(name == expected_name)

    def test_join_1(self):
        K = Puaux.crear_sc_prueba()
        u = Puaux.crear_sim_prueba()
        u.set_faces()
        L = SimplicialComplex("L", 1, [u])
        self.assertTrue(Join.join(K, L).dimension == 3, "Error en el test join_1")

    def test_join_2(self):
        # Complejo simplicial K
        a = Simplex("a", 0)
        b = Simplex("b", 0)
        c = Simplex("c", 0)
        ab = Simplex("ab", 1)
        bc = Simplex("bc", 1)
        ac = Simplex("ac", 1)
        abc = Simplex("abc", 2)
        a.set_faces()
        b.set_faces()
        c.set_faces()
        ab.set_faces({a, b})
        bc.set_faces({b, c})
        ac.set_faces({a, c})
        abc.set_faces({ab, bc, ac})
        K = SimplicialComplex("K", 3, [a, b, c, ab, bc, ac, abc])
        # Complejos simplicial L
        u = Simplex("u", 0)
        v = Simplex("v", 0)
        uv = Simplex("uv", 1)
        u.set_faces()
        v.set_faces()
        uv.set_faces({u, v})
        L = SimplicialComplex("L", 2, [u, v, uv])
        expected_c_vector = [5, 10, 10, 5, 1]
        self.assertTrue(Join.join(K, L).c_vector == expected_c_vector, "Error en el test join_2")

    if __name__ == '__main__':
        unittest.main()