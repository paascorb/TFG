# Fichero de pruebas unitarias para la clase SimplicialComplex desarrollado por Pablo Ascorbe Fernández 18/06/2022
import unittest
import PruebasUnitarias.PruebasAuxiliar as Puaux
import ModeloDeDominio.Auxiliary as Aux


class TestSimplicialComplex(unittest.TestCase):

    def test_get_sim_by_name(self):
        sc = Puaux.crear_sc_prueba()
        simplex_esperado = sc.simplex[8]
        simplex_recibido = Aux.get_sim_by_name(sc.simplex, "abc")
        self.assertTrue(simplex_recibido == simplex_esperado, "Error en el test get_sim_by_name")

    def test_closure(self):
        sc = Puaux.crear_sc_prueba()
        closure_esperada = [Aux.get_sim_by_name(sc.simplex, "abc"), Aux.get_sim_by_name(sc.simplex, "ab"),
                            Aux.get_sim_by_name(sc.simplex, "bc"), Aux.get_sim_by_name(sc.simplex, "ac"),
                            Aux.get_sim_by_name(sc.simplex, "a"), Aux.get_sim_by_name(sc.simplex, "b"),
                            Aux.get_sim_by_name(sc.simplex, "c")]
        closure_recibida = sc.closure(Aux.get_sim_by_name(sc.simplex, "abc"))
        self.assertTrue(Aux.order_simplicial_list(closure_recibida) ==
                        Aux.order_simplicial_list(closure_esperada), "Error en test closure")

    def test_star(self):
        sc = Puaux.crear_sc_prueba()
        star = sc.star(Aux.get_sim_by_name(sc.simplex, "b"))
        expected_star = [Aux.get_sim_by_name(sc.simplex, 'bc'), Aux.get_sim_by_name(sc.simplex, 'b'),
                         Aux.get_sim_by_name(sc.simplex, 'abc'), Aux.get_sim_by_name(sc.simplex, 'ab'),
                         Aux.get_sim_by_name(sc.simplex, 'a'), Aux.get_sim_by_name(sc.simplex, 'ac'),
                         Aux.get_sim_by_name(sc.simplex, 'c')]
        self.assertTrue(Aux.order_simplicial_list(star) == Aux.order_simplicial_list(expected_star),
                        "Error en el test star")

    def test_link(self):
        sc = Puaux.crear_sc_prueba()
        link = sc.link(Aux.get_sim_by_name(sc.simplex, "a"))
        expected_link = [Aux.get_sim_by_name(sc.simplex, 'b'), Aux.get_sim_by_name(sc.simplex, 'd'),
                         Aux.get_sim_by_name(sc.simplex, 'bc'), Aux.get_sim_by_name(sc.simplex, 'c')]
        self.assertTrue(Aux.order_simplicial_list(link) == Aux.order_simplicial_list(expected_link),
                        "Error en el test link")

    if __name__ == '__main__':
        unittest.main()
