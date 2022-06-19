# Fichero de persistencia de la clase BooleanFunction por Pablo Ascorbe 19/06/2022
from Persistencia.JSONPersistence import *
from Persistencia.Conversor import *


def create_boolean_function(bf):
    """
    TODO
    :param bf:
    :return:
    """
    serialize(bf, "BooleanFunctions")


def read_boolean_function(bf):
    """
    TODO
    :param bf:
    :return:
    """
    return bf_decode(deserialize(bf, "BooleanFunctions"))


def update_boolean_function(bf):
    """
    TODO
    :param bf:
    :return:
    """
    remove(bf, "BooleanFunctions")
    serialize(bf, "BooleanFunctions")


def delete_boolean_function(bf):
    """
    TODO
    :param bf:
    :return:
    """
    remove(bf, "BooleanFunctions")


def list_boolean_function():
    """
    TODO
    :return:
    """
    deserialize_objects = deserialize_all("BooleanFunctions")
    objects = list()
    for elem in deserialize_objects:
        objects.append(bf_decode(elem))
    return objects
