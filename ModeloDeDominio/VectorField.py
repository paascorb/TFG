# Clase VectorField.py desarrollada por Pablo Ascorbe Fernández 16/06/2022
import LogicaDeNegocio.Auxiliary as Aux


class VectorField:

    def __init__(self, name, fmatrix, c_vector):
        self.name = name
        self.c_vector = c_vector
        self.fblocks = Aux.trocear_fmatrix(fmatrix, self.c_vector)
        self.routes = dict()

    def add_route(self, pair):
        pos = self.check_pair(pair)
        if all(self.check_source(x) and self.check_target(x) for x in pair) and pos is not None:
            fblock = self.fblocks[pair[0]]
            fblock[pos[0]][0] = -1
            fblock[0][pos[1]] = -1
        else:
            raise Exception("Error esa pareja no es válida para generar una ruta")

    def check_source(self, sim):
        pos_source = self.get_sim_pos(sim)
        return True if self.fblocks[sim.dimension][pos_source][0] != -1 else False

    def check_target(self, sim):
        if sim.dimension == 0:
            return True
        pos_target = self.get_sim_pos(sim)
        return True if self.fblocks[sim.dimension-1][0][pos_target] != -1 else False

    def check_pair(self, pair):
        fila = self.get_sim_pos(pair[0])
        columna = self.get_sim_pos(pair[1])
        return (fila, columna) if self.fblocks[pair[0].dimension][fila][columna] == 1 else None

    def get_sim_pos(self, sim):
        return sim.index - sum(self.c_vector[:sim.dimension])
