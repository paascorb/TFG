# Fichero de persistencia de la clase SimplicialComplex por Pablo Ascorbe 19/06/2022
from Persistencia.JSONPersistence import *
from Persistencia.Conversor import *


def create_simplicial_complex(sc):
    """
    Método de la capa de persistencia que almacena el objeto en el almacén.

    Parameters
    ----------
    sc : SimplicialComplex
        Complejo simplicial que se almacenará en el sistema de persistencia.
    """
    serialize(sc, "SimplicialComplexes")


def read_simplicial_complex(sc):
    """
    Método de la capa de persistencia que lee el objeto del almacén.

    Parameters
    ----------
    sc : SimplicialComplex
        Complejo simplicial que se recuperará del sistema de persistencia.
    """
    return sc_decode(deserialize(sc, "SimplicialComplexes"))


def update_simplicial_complex(sc):
    """
    Método de la capa de persistencia que actualiza el objeto en el almacén.

    Parameters
    ----------
    sc : SimplicialComplex
        Complejo simplicial que se actualizará en el sistema de persistencia.
    """
    remove(sc, "SimplicialComplexes")
    serialize(sc, "SimplicialComplexes")


def delete_simplicial_complex(sc):
    """
    Método de la capa de persistencia que elimina el objeto en el almacén.

    Parameters
    ----------
    sc : SimplicialComplex
        Complejo simplicial que será eliminado del sistema de persistencia.
    """
    remove(sc, "SimplicialComplexes")


def list_simplicial_complex():
    """
    Método de la capa de persistencia que recupera todos los complejos simpliciales del almacén.

    Returns
    -------
    list
        Lista con todos los objetos ya decodificados a partir de su diccionario json recuperado.
    """
    deserialize_objects = deserialize_all("SimplicialComplexes")
    objects = list()
    for elem in deserialize_objects:
        objects.append(sc_decode(elem))
    return objects
