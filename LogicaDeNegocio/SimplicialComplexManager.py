# Fichero logica de negocio para CS desarrollado por Pablo Ascorbe Fernández 25/05/2022
from Persistencia.PersistenceSimplicialComplex import *


def add_simplicial_complex(sc):
    """
    Método que almacena, llamando a la función correspondiente de la capa de persistencia, un complejo simplicial.

    Parameters
    ----------
    sc : SimplicialComplex
        Complejo simplicial el cual se desea almacenar.
    """
    create_simplicial_complex(sc)


def get_simplicial_complex(sc_name):
    """
    Método que lee o rescata el complejo simplicial del almacenamiento cuyo nombre coincide con el nombre pasado por
    parámetros.

    Parameters
    ----------
    sc_name : str
        Cadena que representa el nombre del complejo que se desea persistir.
    """
    return read_simplicial_complex(SimplicialComplex(sc_name, 0, []))


def remove_simplicial_complex(sc_name):
    """
    Método que elimina el objeto persistido cuyo nombre coincida con la cadena recibida por parámetros.

    Parameters
    ----------
    sc_name : str
        Cadena que representa el nombre del complejo simplicial que se desea eliminar.
    """
    delete_simplicial_complex(SimplicialComplex(sc_name, 0, []))


def edit_simplicial_complex(sc):
    """
    Método actualiza la información del complejo simplicial recibido por parámetros. Como precondición se espera que
    exista un complejo con su mismo nombre.

    Parameters
    ----------
    sc : SimplicialComplex
        Complejo simplicial que se desea actualizar.
    """
    update_simplicial_complex(sc)


def list_simplicial_complexes():
    """
    Método que recupera todos los complejos simpliciales almacenados en la aplicación. Si no existe ninguno la lista
    estará vacía.

    Returns
    -------
    list
        Lista que contiene todos los complejos simpliciales almacenados en la aplicación.
    """
    return list_simplicial_complex()
