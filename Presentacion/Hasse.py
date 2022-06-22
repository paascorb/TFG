from igraph import *
import ModeloDeDominio.Auxiliary as Aux
from LogicaDeNegocio.Exceptions import CycleException
from ModeloDeDominio.VectorField import VectorField


class Hasse:
    """
    TODO
    """

    def __init__(self, sc):
        """
        TODO
        :param sc:
        """
        self.pair = list()
        g = Graph(directed=True)
        self.sc = sc
        sc.create_vector_field("hasse_vf")
        self.vf = sc.vector_fields[0]
        self.all_routes = dict()
        self.g = g
        self.g.add_vertices(len(self.sc.simplex))
        self.label = []
        self.pos = []

        for i in range(sc.dimension + 1):
            for simplice in Aux.list_simplex_by_dim(sc.simplex, i):
                self.label.append(simplice.name)
                self.pos.append((Aux.get_sim_pos(sc.c_vector, simplice), -i))
                if i > 0:
                    for face in simplice.faces:
                        self.g.add_edge(simplice.index, face.index)

    def paint_edges_for_sim(self, sim, color, is_source):
        for edge in self.g.es:
            if is_source:
                if edge.source == sim.index:
                    edge["color"] = color
            else:
                if edge.target == sim.index:
                    edge["color"] = color

    def point_up_edge(self, source, target):
        self.pair.append((source, target))
        ciclo = False
        route = [x.name for x in source.faces]
        route.remove(target.name)
        self.all_routes[target.name] = route
        try:
            self.vf.add_route((target, source))
        except CycleException:
            ciclo = True
        self.vf.sources.append(source)
        self.vf.sources.append(target)
        self.vf.targets.append(source)
        self.vf.targets.append(target)
        aux = Graph(directed=True)
        aux.add_vertices(len(self.sc.simplex))

        for i in range(self.sc.dimension + 1):
            for simplice in Aux.list_simplex_by_dim(self.sc.simplex, i):
                if i > 0:
                    for face in simplice.faces:
                        if any(x for x in self.pair if x[0] == simplice and x[1] == face):
                            aux.add_edge(face.index, simplice.index)["color"] = "black"
                        elif (simplice in self.vf.targets or simplice in self.vf.sources) \
                                or (face in self.vf.targets or face in self.vf.sources):
                            aux.add_edge(simplice.index, face.index)["color"] = "gray"
                        else:
                            aux.add_edge(simplice.index, face.index)["color"]
        self.g = aux
        if ciclo:
            self.paint_cycle((target, source))
        self.plot_hasse()

    def paint_cycle(self, pair):
        routes = self.get_routes_of(pair[0].name, pair[0].name)
        routes_flat = [x for xs in routes for x in xs]
        sim_in_cycle = self.get_elems_of_cycle(routes_flat)
        pair_in_cycle = self.get_pairs_of_cylce(sim_in_cycle)
        pair_in_cycle_flat = [x for xs in pair_in_cycle for x in xs]
        for elem in pair_in_cycle_flat:
            for edge in self.g.es:
                if edge.target == elem[0].index and edge.source == elem[1].index:
                    edge["color"] = "red"

    def get_routes_of(self, sim_name, stop_crit, routes = None):
        if routes is None:
            routes = list()
        if stop_crit in self.all_routes[sim_name]:
            routes.append(self.all_routes[sim_name])
            return routes
        routes.append(self.all_routes[sim_name])
        for elem in self.all_routes[sim_name]:
            self.get_routes_of(elem, stop_crit, routes)
        return routes

    def get_elems_of_cycle(self, cylce_route):
        sim_in_cylce = list()
        for key, value in self.all_routes.items():
            if key in cylce_route:
                sim_in_cylce.append(key)
        return sim_in_cylce

    def get_pairs_of_cylce(self, sim_in_cycle):
        pair_in_cylce = list()
        for elem in sim_in_cycle:
            pair_in_cylce.append([x for x in self.pair if x[1].name == elem])
        return pair_in_cylce

    def plot_hasse(self):
        plot(self.g, vertex_label=self.label, target="../Recursos/Hasse.png", vertex_color='white', edge_width=3,
             vertex_size=30, vertex_frame_color='white', layout=self.pos)


