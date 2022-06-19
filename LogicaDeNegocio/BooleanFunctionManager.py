# Fichero logica de negocio para BF desarrollado por Pablo Ascorbe Fernández 17/06/2022
from Persistencia.PersistenceBooleanFunction import *


def add_boolean_function(bf):
    """
    TODO
    :param bf:
    :return:
    """
    create_boolean_function(bf)


def get_boolean_function(bf_name):
    """
    TODO
    :param bf_name:
    :return:
    """
    return read_boolean_function(BooleanFunction(bf_name, 0, []))


def remove_boolean_function(bf_name):
    """
    TODO
    :param bf_name:
    :return:
    """
    delete_boolean_function(BooleanFunction(bf_name, 0, []))


def edit_boolean_function(bf):
    """
    TODO
    :param bf:
    :return:
    """
    update_boolean_function(bf)


def list_boolean_functions():
    """
    TODO
    :return:
    """
    return list_boolean_function()
