# Fichero de pruebas unitarias para la lógica del traductor por Pablo Ascorbe Fernández 15/06/2022
import unittest
from timeit import default_timer as timer
import LogicaDeNegocio.Traductor as Tra
import ModeloDeDominio.Auxiliary as Aux
from ModeloDeDominio.BooleanFunction import BooleanFunction
from ModeloDeDominio.Simplex import Simplex
import PruebasUnitarias.PruebasAuxiliar as Puaux


class TestTraductor(unittest.TestCase):

    def test_traductor_bl_to_sc(self):
        bf = BooleanFunction('bf', 3, ['a', 'b', 'c'], [1, 1, 1, 1, 1, 1, 1, 1])
        sc = Tra.boolean_function_to_simplicial_complex(bf)
        self.assertTrue(True is Aux.is_simplicial_complex(sc.simplex), "Error en el test_constructor_bl_to_sc")
        bf2 = BooleanFunction('bf2', 4, ['a', 'b', 'c', 'd'], [1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 0, 0, 0])
        sc2 = Tra.boolean_function_to_simplicial_complex(bf2)
        self.assertTrue(True is Aux.is_simplicial_complex(sc2.simplex), "Error en el test_constructor_bl_to_sc")

    def test_traductor_sc_to_bl(self):
        sc = Puaux.crear_sc_prueba()
        fb = Tra.simplicial_complex_to_boolean_function(sc)
        output = [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0]
        self.assertTrue(fb.outputs == output, "Error en el test sc_to_bl")

    def test_position_in_ouput(self):
        sc = Puaux.crear_sc_prueba()
        sim_pos = dict()
        for sim in sc.simplex[:sc.c_vector[0]]:
            pos = 2 ** sim.index
            sim_pos[sim.name] = pos
        self.assertTrue(5 == Tra.position_in_ouput(sc.simplex[5], sim_pos), "Error en el test de position_in_output")

    def test_tiempos_dicts_sim(self):
        start = timer()
        dict_sim = {}
        for i in range(1, 1000):
            dict_sim[Simplex(str(i), 0)] = i
        for key, value in dict_sim.items():
            key.name = str(value + 1)
        end = timer()
        print("Tiempo para dict mapeado con objetos: " + str(end - start) + "s")

    def test_tiempos_dicts_string(self):
        start = timer()
        dict_str = {}
        for i in range(1, 1000):
            dict_str[str(i)] = i
        for key, value in dict_str.items():
            dict_str[key] = str(value + 1)
        end = timer()
        print("Tiempo para dict mapeado con strings: " + str(end - start) + "s")

    def test_tiempos_dicts_sim_2(self):
        start = timer()
        dict_sim = {}
        for i in range(1, 1000000):
            dict_sim[Simplex(str(i), 0)] = i
        for key, value in dict_sim.items():
            key.name = str(value + 1)
        end = timer()
        print("Tiempo para dict mapeado con objetos y 1.000.000 componentes: " + str(end - start) + "s")

    def test_tiempos_dicts_string_2(self):
        start = timer()
        dict_str = {}
        for i in range(1, 1000000):
            dict_str[str(i)] = i
        for key, value in dict_str.items():
            dict_str[key] = str(value + 1)
        end = timer()
        print("Tiempo para dict mapeado con strings y 1.000.000 componentes: " + str(end - start) + "s")

    if __name__ == '__main__':
        unittest.main()
