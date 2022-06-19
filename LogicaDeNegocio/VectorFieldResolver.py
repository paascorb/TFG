# Lógica de negocio para crear un campo de vectores completo desarrollada por Pablo Ascorbe Fernández 17/06/2022
import ModeloDeDominio.Auxiliary as Aux
from LogicaDeNegocio.Exceptions import *


def resolve_field(vf, sc):
    """
    TODO
    :param vf:
    :param sc:
    :return:
    """
    for i, fblock in enumerate(vf.fblocks):
        resolve_block(fblock, i, vf, sc)


def resolve_block(fblock, dimension, vf, sc, debug=None):
    """
    Método que resuelve todas las rutas posibles para la matriz proporcionada llamada fblock, que es el bloque en forma
    de matriz de dimensión igual al parámetro homónimo. Esta dimensión es la de los símplices que están representados en
    las filas del bloque que son los símplices source, y los target, que son las columnas, serán de dimensión uno
    superior.

    El método irá iterando sobre la matriz y buscando todas las parejas viables para realizar una ruta, cuando encuentre
    una ruta factible la generará añadiéndola al campo de vectores. Así hasta recorrer la matriz entera.

    En el caso activar el flag de debug el programa avisará cuando encuentre con una pareja que genere un ciclo.

    Parameters
    ----------
    fblock : list
        Lista de listas que representa el bloque de relaciones entre símplices,
        siendo las filas las caras y las columnas las cocaras.
    dimension : int
        Dimensión de las caras, representa la dimensión de los símplices que son source.
    vf : VectorField
        Campo de vectores sobre el que se irán añadiendo las rutas válidas encontradas.
    sc : SimplicialComplex
        Complejo simplicial sobre el que se está generando el campo de vectores, y necesario para conseguir la pareja
        de símplices que generarán las rutas.
    debug : bool
        Bit o flag que por defecto está desactivado, pero en el caso de estar activado permitirá al método informar de
        qué ciclos se han ido generando y que parejas han sido las culpables.
    """
    for source, i in zip(fblock, range(0, len(fblock))):
        for target, j in zip(source, range(0, len(source))):
            if target == 1:
                sigma = sc.simplex[Aux.get_sim_index(i, dimension, sc.c_vector)]
                tau = sc.simplex[Aux.get_sim_index(j, dimension + 1, sc.c_vector)]
                pair = (sigma, tau)
                if all(vf.check_source(x) and vf.check_target(x) for x in pair):
                    try:
                        vf.add_route(pair)
                        break
                    except CycleException:
                        if debug is not None:
                            print("Ciclo generado: \r\n" +
                                  "Parejas: " + "Source: " + str(pair[0]) + " | Target: " + str(pair[1]) + "\r\n" +
                                  "Rutas:" + str(vf.routes))
