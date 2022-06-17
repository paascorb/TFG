# Clase VectorField.py desarrollada por Pablo Ascorbe Fernández 16/06/2022
import LogicaDeNegocio.Auxiliary as Aux


class VectorField:
    """
    TODO
    """

    def __init__(self, name, fmatrix, c_vector):
        """
        TODO
        :param name:
        :param fmatrix:
        :param c_vector:
        """
        self.name = name
        self.c_vector = c_vector
        self.fblocks = Aux.slice_fmatrix(fmatrix, self.c_vector)
        self.routes = dict()

    def add_route(self, pair):
        """
        TODO
        :param pair:
        :return:
        """
        pos = self.check_pair(pair)
        if all(self.check_source(x) and self.check_target(x) for x in pair) and pos is not None:
            self.cross_out_pair(pair, pos)
            route = self.check_route(pair)
            if route is not None:
                self.routes[pair[0].name] = route
                for elem in [key for key, value in self.routes.items() if pair[0].name in value]:
                    value = self.routes[elem]
                    value.extend(route)
                    value.remove(pair[0].name)
            else:
                raise Exception("Error: se ha formado un ciclo.")
        else:
            raise Exception("Error: esa pareja no es válida para generar una ruta")

    def check_source(self, sim):
        """
        TODO
        :param sim:
        :return:
        """
        pos_source = Aux.get_sim_pos(self.c_vector, sim)
        return True if self.fblocks[sim.dimension][pos_source][0] != -1 else False

    def check_target(self, sim):
        """
        TODO
        :param sim:
        :return:
        """
        if sim.dimension == 0:
            return True
        pos_target = Aux.get_sim_pos(self.c_vector, sim)
        return True if self.fblocks[sim.dimension-1][0][pos_target] != -1 else False

    def check_pair(self, pair):
        """
        TODO
        :param pair:
        :return:
        """
        fila = Aux.get_sim_pos(self.c_vector, pair[0])
        columna = Aux.get_sim_pos(self.c_vector, pair[1])
        return (fila, columna) if self.fblocks[pair[0].dimension][fila][columna] == 1 else None

    def cross_out_pair(self, pair, pos):
        """
        TODO
        :param pair:
        :param pos:
        :return:
        """
        if pair[0].dimension > 0:
            fblock_ant = self.fblocks[pair[0].dimension - 1]
            Aux.cross_out_pos(pos[0], fblock_ant, False)
        if pair[1].dimension + 1 != len(self.fblocks):
            fblock_sig = self.fblocks[pair[1].dimension + 1]
            Aux.cross_out_pos(pos[1], fblock_sig, True)
        fblock = self.fblocks[pair[0].dimension]
        Aux.cross_out_pos(pos[0], fblock, True)
        Aux.cross_out_pos(pos[1], fblock, False)

    def check_route(self, pair):
        """
        TODO
        :param pair:
        :return:
        """
        accesible_routes = list()
        for sim in pair[1].faces:
            accesible_routes.extend(self.routes.get(sim.name, sim.name))
        accesible_routes.remove(pair[0].name)
        return accesible_routes if pair[0].name not in accesible_routes else None
