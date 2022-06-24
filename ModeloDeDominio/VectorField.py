# Clase VectorField.py desarrollada por Pablo Ascorbe Fernández 16/06/2022
from LogicaDeNegocio.Exceptions import *
import ModeloDeDominio.Auxiliary as Aux


class VectorField:
    """
    TODO
    """

    def __init__(self, name, fblocks, c_vector):
        """
        TODO
        :param name:
        :param fblocks:
        :param c_vector:
        """
        self.name = name
        self.c_vector = c_vector
        self.fblocks = fblocks
        self.routes = dict()
        self.pairs_added = list()
        self.sources = list()
        self.targets = list()

    def __str__(self):
        """
        TODO
        :return:
        """
        return "Campo de vectores: " + self.name + " Rutas: "+str(self.routes)

    def __repr__(self):
        """
        TODO
        :return:
        """
        return "Campo de vectores: " + self.name + " Rutas: "+str(self.routes)

    def add_route(self, pair):
        """
        TODO
        :param pair:
        :return:
        """
        pos = self.check_pair(pair)
        if all(self.check_source(x) and self.check_target(x) for x in pair) and pos is not None:
            route = self.generate_route(pair)
            if route is not None:
                self.cross_out_pair(pair)
                self.routes[pair[0].name] = route
                for elem in [key for key, value in self.routes.items() if pair[0].name in value]:
                    value = self.routes[elem]
                    value.extend(route)
                    value.remove(pair[0].name)
            else:
                raise CycleException("Error: se ha formado un ciclo.")
        else:
            raise InvalidPairException("Error: esa pareja no es válida para generar una ruta")

    def check_source(self, sim):
        """
        TODO
        :param sim:
        :return:
        """
        if sim.dimension == len(self.fblocks):
            return True
        return True if sim.name not in self.sources else False

    def check_target(self, sim):
        """
        TODO
        :param sim:
        :return:
        """
        if sim.dimension == 0:
            return True
        return True if sim.name not in self.targets else False

    def check_pair(self, pair):
        """
        TODO
        :param pair:
        :return:
        """
        fila = Aux.get_sim_pos(self.c_vector, pair[0])
        columna = Aux.get_sim_pos(self.c_vector, pair[1])
        return (fila, columna) if self.fblocks[pair[0].dimension][fila][columna] == 1 else None

    def cross_out_pair(self, pair):
        """
        TODO
        :param pair:
        :return:
        """
        if pair[0].dimension > 0:
            self.targets.append(pair[0].name)
        if pair[1].dimension + 1 == len(self.fblocks):
            self.sources.append(pair[1].name)
        self.pairs_added.append(pair)
        self.sources.append(pair[0].name)
        self.targets.append(pair[1].name)

    def generate_route(self, pair):
        """
        TODO
        :param pair:
        :return:
        """
        accesible_routes = list()
        for sim in pair[1].faces:
            value = self.routes.get(sim.name, sim.name)
            if isinstance(value, str):
                accesible_routes.extend([value])
            else:
                accesible_routes.extend(value)
        accesible_routes.remove(pair[0].name)
        return accesible_routes if pair[0].name not in accesible_routes else None

    def json_encode(self):
        """
        Método que codifica el objeto a un diccionario para su correcta serialización a JSON.

        Returns
        -------
        dict
            Diccionario que representa al campo de vectores.
        """
        routes = None if self.routes is None else self.routes
        targets = None if self.routes is None else self.targets
        sources = None if self.routes is None else self.sources
        return {'id': self.name,
                'fblocks': self.fblocks,
                'c_vector': self.c_vector,
                'routes': routes,
                'targets': targets,
                'sources': sources}
