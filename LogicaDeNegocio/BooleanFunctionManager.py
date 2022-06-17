# Fichero logica de negocio para BF desarrollado por Pablo Ascorbe Fernández 17/06/2022
from Persistencia import Persistence, AuxiliaryParsing


def add_boolean_function(bf, fichero):
    """
    TODO
    :param bf:
    :param fichero:
    :return:
    """
    Persistence.serialize(bf, fichero)


def get_boolean_function(fichero):
    """
    TODO
    :param fichero:
    :return:
    """
    return AuxiliaryParsing.bf_decode(Persistence.deserialize(fichero))


def remove_boolean_function(fichero):
    """
    TODO
    :param fichero:
    :return:
    """
    Persistence.remove(fichero)


def update_boolean_function(bf, fichero):
    """
    TODO
    :param bf:
    :param fichero:
    :return:
    """
    Persistence.remove(fichero)
    Persistence.serialize(bf, fichero)
