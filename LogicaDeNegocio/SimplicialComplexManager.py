# Fichero logica de negocio para CS desarrollado por Pablo Ascorbe Fernández 25/05/2022
from Persistencia import AuxiliaryParsing, Persistence


def add_simplicial_complex(sc, fichero):
    """

    :param sc:
    :param fichero:
    :return:
    """
    Persistence.serialize(sc, fichero)


def get_simplicial_complex(fichero):
    """
    TODO
    :param fichero:
    :return:
    """
    return AuxiliaryParsing.sc_decode(Persistence.deserialize(fichero))


def remove_simplicial_complex(fichero):
    """
    TODO
    :param fichero:
    :return:
    """
    Persistence.remove(fichero)


def update_simplicial_complex(sc, fichero):
    """
    TODO
    :param sc:
    :param fichero:
    :return:
    """
    Persistence.remove(fichero)
    Persistence.serialize(sc, fichero)
