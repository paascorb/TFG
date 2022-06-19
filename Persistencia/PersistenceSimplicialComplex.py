# Fichero de persistencia de la clase SimplicialComplex por Pablo Ascorbe 19/06/2022
from Persistencia.JSONPersistence import *
from Persistencia.Conversor import *


def create_simplicial_complex(sc):
    """
    TODO
    :param sc:
    :return:
    """
    serialize(sc, "SimplicialComplexes")


def read_simplicial_complex(sc):
    """
    TODO
    :param sc:
    :return:
    """
    return sc_decode(deserialize(sc, "SimplicialComplexes"))


def update_simplicial_complex(sc):
    """
    TODO
    :param sc:
    :return:
    """
    remove(sc, "SimplicialComplexes")
    serialize(sc, "SimplicialComplexes")


def delete_simplicial_complex(sc):
    """
    TODO
    :param sc:
    :return:
    """
    remove(sc, "SimplicialComplexes")


def list_simplicial_complex():
    """
    TODO
    :return:
    """
    deserialize_objects = deserialize_all("SimplicialComplexes")
    objects = list()
    for elem in deserialize_objects:
        objects.append(sc_decode(elem))
    return objects
