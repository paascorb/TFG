# Fichero de persistencia de la clase BooleanFunction por Pablo Ascorbe 19/06/2022
from Persistencia.JSONPersistence import *
from Persistencia.Conversor import *


def create_boolean_function(bf):
    """
    Método de la capa de persistencia que almacena el objeto en el almacén.

    Parameters
    ----------
    bf : BooleanFunction
        Función booleana que se almacenará en el sistema de persistencia.
    """
    serialize(bf, "BooleanFunctions")


def read_boolean_function(bf):
    """
    Método de la capa de persistencia que lee el objeto del almacén.

    Parameters
    ----------
    bf : BooleanFunction
        Función booleana que se recuperará del sistema de persistencia.
    """
    return bf_decode(deserialize(bf, "BooleanFunctions"))


def update_boolean_function(bf):
    """
    Método de la capa de persistencia que actualiza el objeto en el almacén.

    Parameters
    ----------
    bf : BooleanFunction
        Función booleana que se actualizará en el sistema de persistencia.
    """
    remove(bf, "BooleanFunctions")
    serialize(bf, "BooleanFunctions")


def delete_boolean_function(bf):
    """
    Método de la capa de persistencia que elimina el objeto en el almacén.

    Parameters
    ----------
    bf : BooleanFunction
        Función booleana que será eliminada del sistema de persistencia.
    """
    remove(bf, "BooleanFunctions")


def list_boolean_function():
    """
    Método de la capa de persistencia que recupera todas las funciones booleanas del almacén.

    Returns
    -------
    list
        Lista con todos los objetos ya decodificados a partir de su diccionario json recuperado.
    """
    deserialize_objects = deserialize_all("BooleanFunctions")
    objects = list()
    for elem in deserialize_objects:
        objects.append(bf_decode(elem))
    return objects
