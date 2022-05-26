# Métodos auxiliares para la persistencia hecho por Pablo Ascorbe 25/05/2022
from ModeloDeDominio.BooleanFunction import BooleanFunction
from ModeloDeDominio.Simplex import Simplex

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
    simplex.set_faces(json_dict.get('faces'))
    simplex.set_faces(json_dict.get('faces'))
    return simplex


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
