from igraph import *


def mostrar_diagrama_hasse(sim_complex):
    g = Graph(sim_complex.numberOfSimplices())
    label = []
    pos = []

    for i in range(0, sim_complex.maxOrder() + 1):
        for simplice in sorted(sim_complex.simplicesOfOrder(i)):
            label.append(simplice)
            pos.append((sim_complex.indexOf(simplice), -i))
            if i < sim_complex.maxOrder():
                for face in sim_complex.faceOf(simplice):
                    try:
                        g.add_edge(sim_complex[simplice]['num'], sim_complex[face]['num'])
                    except KeyError:
                        g.add_edge(calcular_posicion(sim_complex, simplice, sim_complex.orderOf(simplice)),
                                   calcular_posicion(sim_complex, face, sim_complex.orderOf(face)))

    plot(g, vertex_label=label, vertex_color='white', edge_width=3, vertex_size=20,
         vertex_frame_color='white', layout=pos)


def calcular_posicion(sim_complex, sim, order):
    if order != 0:
        return calcular_posicion(sim_complex, sim, order - 1) + len(sim_complex.simplicesOfOrder(order - 1))
    else:
        return sim_complex.indexOf(sim)
