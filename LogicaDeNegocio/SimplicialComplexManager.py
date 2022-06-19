# Fichero logica de negocio para CS desarrollado por Pablo Ascorbe Fernández 25/05/2022
from Persistencia.PersistenceSimplicialComplex import *


def add_simplicial_complex(sc):
    """

    :param sc:
    :return:
    """
    create_simplicial_complex(sc)


def get_simplicial_complex(sc_name):
    """
    TODO
    :param sc_name:
    :return:
    """
    return read_simplicial_complex(SimplicialComplex(sc_name, 0, []))


def remove_simplicial_complex(sc_name):
    """
    TODO
    :param sc_name:
    :return:
    """
    delete_simplicial_complex(SimplicialComplex(sc_name, 0, []))


def edit_simplicial_complex(sc):
    """
    TODO
    :param sc:
    :return:
    """
    update_simplicial_complex(sc)


def list_simplicial_complexes():
    """
    TODO
    :return:
    """
    return list_simplicial_complex()
