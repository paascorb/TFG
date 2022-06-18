# Fichero de pruebas unitarias para la clase SimplicialComplex desarrollado por Pablo Ascorbe Fernández 18/06/2022
import unittest
import PruebasUnitarias.PruebasAuxiliar as Puaux
import LogicaDeNegocio.Auxiliary as Aux


class TestSimplicialComplex(unittest.TestCase):

    def test_get_sim_by_name(self):
        sc = Puaux.crear_sc_prueba()
        simplex_esperado = sc.simplex[8]
        simplex_recibido = sc.get_sim_by_name("abc")
        self.assertTrue(simplex_recibido == simplex_esperado, "Error en el test get_sim_by_name")

    def test_closure(self):
        sc = Puaux.crear_sc_prueba()
        closure_esperada = [sc.get_sim_by_name("abc"), sc.get_sim_by_name("ab"), sc.get_sim_by_name("bc"),
                            sc.get_sim_by_name("ac"), sc.get_sim_by_name("a"), sc.get_sim_by_name("b"),
                            sc.get_sim_by_name("c")]
        closure_recibida = sc.closure(sc.get_sim_by_name("abc"))
        self.assertTrue(Aux.order_simplicial_list(closure_recibida) ==
                        Aux.order_simplicial_list(closure_esperada), "Error en test closure")

    def test_star(self):
        sc = Puaux.crear_sc_prueba()
        star = sc.star(sc.get_sim_by_name("a"))
        expected_star = [sc.get_sim_by_name('ab'), sc.get_sim_by_name('abc'), sc.get_sim_by_name('ad'),
                         sc.get_sim_by_name('ac'), sc.get_sim_by_name('a')]
        self.assertTrue(Aux.order_simplicial_list(star) == Aux.order_simplicial_list(expected_star),
                        "Error en el test star")

    def test_link(self):
        sc = Puaux.crear_sc_prueba()
        link = sc.link(sc.get_sim_by_name("a"))
        expected_link = [sc.get_sim_by_name('b'), sc.get_sim_by_name('d'), sc.get_sim_by_name('bc'),
                         sc.get_sim_by_name('c')]
        self.assertTrue(Aux.order_simplicial_list(link) == Aux.order_simplicial_list(expected_link),
                        "Error en el test link")

    if __name__ == '__main__':
        unittest.main()
