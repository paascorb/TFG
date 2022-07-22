# Persistencia para SimplicialComplex hecho por Pablo Ascorbe 25/05/2022
import json
import os


def serialize(obj, table):
    """
    Método que serializa el objeto recibido por parámetros en un fichero .JSON, se espera como precondición que el
    objeto tenga un método para traducirlo a un diccionario con el formato json.

    Parameters
    ----------
    obj : any
        Objeto que será almacenado en un fichero .json.
    table : str
        Cadena que representa el directorio donde se almacenará el objeto.
    """
    project_root = os.path.dirname(os.path.dirname(__file__))
    with open(project_root + '/Almacen/' + table + "/" + obj.name + '.json', 'w') as f:
        json.dump(obj, f, default=lambda o: o.json_encode(), indent=4)


def deserialize(obj, table):
    """
    Método que recupera el objeto recibido por parámetros del almacén correspondiente, se espera como precondición que
    dicho objeto se encuentre almacenado en el sistema de persistencia.

    Parameters
    ----------
    obj : any
        Diccionario json del objeto que se desea recuperar del almacén.
    table : str
        Cadena que representa el directorio que contiene el objeto.
    """
    project_root = os.path.dirname(os.path.dirname(__file__))
    with open(project_root + '/Almacen/' + table + "/" + obj.name + '.json') as f:
        return json.load(f)


def remove(obj, table):
    """
    Método que elimina el objeto recibido por parámetros del almacén correspondiente, se espera como precondición que
    dicho objeto se encuentre almacenado en el sistema de persistencia.

    Parameters
    ----------
    obj : any
        Objeto que será eliminado del almacén.
    table : str
        Cadena que representa el directorio que contiene dicho objeto.
    """
    project_root = os.path.dirname(os.path.dirname(__file__))
    os.remove(project_root + '/Almacen/' + table + "/" + obj.name + '.json')


def deserialize_all(table):
    """
    Método que recupera todos los objetos del directorio recibido por parámetros.

    Parameters
    ----------
    table : str
        Cadena que representa el directorio del que se recuperarán los objetos.

    Returns
    -------
    list
        Lista que contiene todos los diccionarios json que representan los objetos del directorio recibido.
    """
    project_root = os.path.dirname(os.path.dirname(__file__))
    path = project_root + '/Almacen/' + table
    all_files = [f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))]
    object_deserialize = list()
    for file in all_files:
        with open(path + "/" + file) as f:
            object_deserialize.append(json.load(f))
    return object_deserialize
