# Fichero logica de negocio para BF desarrollado por Pablo Ascorbe Fernández 17/06/2022
from Persistencia.PersistenceBooleanFunction import *


def add_boolean_function(bf):
    """
    Método que almacena, llamando a la función correspondiente de la capa de persistencia, una función booleana.

    Parameters
    ----------
    bf : BooleanFunction
        Función booleana la cual se desea almacenar.
    """
    create_boolean_function(bf)


def get_boolean_function(bf_name):
    """
    Método que lee o rescata la función booleana del almacenamiento cuyo nombre coincide con el nombre pasado por
    parámetros.

    Parameters
    ----------
    bf_name : str
        Cadena que representa el nombre de la función que se desea persistir.
    """
    return read_boolean_function(BooleanFunction(bf_name, 0, [], []))


def remove_boolean_function(bf_name):
    """
    Método que elimina el objeto persistido cuyo nombre coincida con la cadena recibida por parámetros.

    Parameters
    ----------
    bf_name : str
        Cadena que representa el nombre de la función booleana que se desea eliminar.
    """
    delete_boolean_function(BooleanFunction(bf_name, 0, [], []))


def edit_boolean_function(bf):
    """
    Método actualiza la información de la función booleana recibida por parámetros. Como precondición se espera que
    exista una función con su mismo nombre.

    Parameters
    ----------
    bf : BooleanFunction
        Función booleana que se desea actualizar.
    """
    update_boolean_function(bf)


def list_boolean_functions():
    """
    Método que recupera todas las funciones booleanas almacenadas en la aplicación. Si no existe ninguna la lista
    estará vacía.

    Returns
    -------
    list
        Lista que contiene todos las funciones booleanas almacenadas en la aplicación.
    """
    return list_boolean_function()
