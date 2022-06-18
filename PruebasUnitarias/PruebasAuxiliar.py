from ModeloDeDominio.BooleanFunction import BooleanFunction
from ModeloDeDominio.Simplex import Simplex
from ModeloDeDominio.SimplicialComplex import SimplicialComplex


def crear_sc_prueba():
    """
    Método para las pruebas unitarias que crea un complejo simplicial de prueba para poder trabajar con él.

    Returns
    -------
    SimplicialComplex
        Complejo simplicial de prueba que contiene 4 0-símplices, 4 1-símplices y 1 2-símplice.
    """
    s = Simplex('a', 0)
    v = Simplex('b', 0)
    w = Simplex('c', 0)
    r = Simplex('d', 0)
    sv = Simplex('ab', 1)
    sw = Simplex('ac', 1)
    vw = Simplex('bc', 1)
    sr = Simplex('ad', 1)
    svw = Simplex('abc', 2)

    s.set_faces()
    v.set_faces()
    w.set_faces()
    r.set_faces()
    sv.set_faces({s, v})
    sw.set_faces({s, w})
    vw.set_faces({v, w})
    sr.set_faces({s, r})
    svw.set_faces({sv, sw, vw})

    simplices = [s, v, w, r, sv, sw, vw, sr, svw]

    return SimplicialComplex('sc_prueba', 10, simplices)


def crear_bf_prueba():
    """
    Método para las pruebas unitarias que crea una función booleana de prueba para poder trabajar con ella.

    Returns
    -------
    BooleanFunction
        Función booleana de prueba para trabajar en las pruebas unitarias.
    """
    return BooleanFunction("fb_prueba", 4, [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0])


def comparar_matrices(m1, m2):
    """
    Método para comparar matrices, en este caso lista de listas. Compara primero sus tamaños y si son iguales entonces
    elemento a elemento. Si encuentra alguna diferencia devuelve False. True si son iguales.

    Parameters
    ----------
    m1 : list
        Lista de listas que representa la primera matriz.
    m2 : list
        Lista de litas que representa la segunda matriz.

    Returns
    -------
    boolean
        Booleano que será False si las matrices son distintas y True en caso contrario.
    """
    filas1 = len(m1)
    columnas1 = len(m1[0])
    if filas1 != len(m2) and columnas1 != len(m2[0]):
        return False
    else:
        for i in range(0, filas1):
            for j in range(0, columnas1):
                if m1[i][j] != m2[i][j]:
                    return False
    return True
