# Métodos auxiliares para la persistencia hecho por Pablo Ascorbe 25/05/2022
from ModeloDeDominio.BooleanFunction import BooleanFunction
from ModeloDeDominio.Simplex import Simplex
from ModeloDeDominio.SimplicialComplex import SimplicialComplex

"""
Métodos para el parseo entre diccionarios y objetos de nuestro modelo de dominio
"""


def simplex_decode(json_dict):
    """
    Método que decodifica de un diccionario recibido por JSON al objeto deseado.

    Parameters
    ----------
    json_dict : dict
        Diccionario que representa a nuestro simplice

    Returns
    -------
    Simplex
        Simplice traducido del diccionario proporcionado.
    """

    simplex = Simplex(json_dict.get('id'), json_dict.get('dimension'))
    faces = set()
    if simplex.dimension != 0:
        for elem in json_dict.get('faces'):
            faces.add(simplex_decode(elem))
    simplex.set_faces(faces)
    return simplex


def simplex_decode_opt(json_dict):
    """
    Método que decodifica de un diccionario recibido por JSON al objeto deseado. Es una modificación del homónimo pero
    optimizado para la recuperación de complejos simpliciales. Para no recuperar cada uno recursivamente se hace solo
    por sus identificadores.

    Parameters
    ----------
    json_dict : dict
        Diccionario que representa a nuestro simplice

    Returns
    -------
    tuple
        Tupla con el simplice traducido del diccionario proporcionado y una lista con los identificadores de sus caras.
    """

    simplex = Simplex(json_dict.get('id'), json_dict.get('dimension'))
    return simplex, json_dict.get('faces')


def bf_decode(json_dict):
    """
    Método que decodifica de un diccionario recibido por JSON al objeto deseado.

    Parameters
    ----------
    json_dict : dict
        Diccionario que representa a nuestra función booleana

    Returns
    -------
    BooleanFunction
        Función booleana traducida del diccionario proporcionado.
    """

    bf = BooleanFunction(json_dict.get('id'), json_dict.get('num_variables'), json_dict.get('outputs'))
    bf.set_monotone_flag(json_dict.get('m_flag'))
    return bf


def sc_decode(json_dict):
    """
    Método que decodifica de un diccionario recibido por JSON al objeto deseado.

    Parameters
    ----------
    json_dict : dict
        Diccionario que representa a nuestro complejo simplicial

    Returns
    -------
    SimplicialComplex
        Complejo simplicial traducido del diccionario proporcionado.
    """
    simplex = list()
    faces = list()
    for elem in json_dict.get('simplex'):
        aux = simplex_decode_opt(elem)
        simplex.append(aux[0])
        faces.append(aux[1])
    for s, f in zip(simplex, faces):
        faces = set()
        for cara in f:
            faces.add(next((x for x in simplex if x.name == cara), None))
        s.faces = faces
    return SimplicialComplex(json_dict.get('id'), int(json_dict.get('omega')), simplex)
