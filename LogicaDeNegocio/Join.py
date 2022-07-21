# Métodos de lógica de negocio que calculan el join y cono por Pablo Ascorbe 18/06/2022
import copy
from functools import reduce
from ModeloDeDominio.Simplex import Simplex
from ModeloDeDominio.SimplicialComplex import SimplicialComplex


def join(k_sc, l_sc):
    """
    Método que calcula el join de los dos complejos simpliciales recibidos por parámetros. Primero se juntan todos los
    símplices en una misma lista y, luego, recorriendo todos los símplices del primer complejo se va calculando la unión
    de estos con cada símplice del segundo complejo. Terminando así por juntar todos los símplices de cada complejo con
    el resto del otro. La unión de los símplices se realiza calculando cuáles son sus caras por los vértices que lo
    componen y generándole un nombre correspondiente a dichos vértices.

    Parameters
    ----------
    k_sc : SimplicialComplex
        Primer complejo simplicial para calcular el join.
    l_sc : SimplicialComplex
        Segundo complejo simplicial para calcular el join.
    Returns
    -------
    SimplicialComplex
        Complejo simplicial correspondiente de realizar el join entre los dos complejos recibidos por parámetros.
    """
    k_simplex = copy.deepcopy(k_sc.simplex)
    l_simplex = copy.deepcopy(l_sc.simplex)
    all_simplex = k_simplex + l_simplex
    for K_simplex in k_sc.simplex:
        k_sim_faces = list(K_simplex.faces) if K_simplex.dimension > 0 else [K_simplex]
        for L_simplex in l_sc.simplex:
            faces_aux = k_sim_faces.copy()
            faces_aux.extend(L_simplex.faces if L_simplex.dimension > 0 else [L_simplex])
            simplex = Simplex(generate_sim_name(faces_aux), len(faces_aux) - 1)
            simplex.set_faces(set(all_simplex_by_names(all_simplex, generate_faces_names(faces_aux),
                                                       simplex.dimension - 1)))
            all_simplex.append(simplex)
    return SimplicialComplex("L*K", k_sc.omega + l_sc.omega, all_simplex)


def cono(k, name):
    """
    Método que calcula el cono del complejo símplicial recibido por parámetros. Dicho cono se calcula con un vértice
    cuyo nombre será el recibido por parámetros.

    Parameters
    ----------
    k : SimplicialComplex
        Complejo simplicial del que se calculará el cono.
    name : str
        Cadena que representa el nombre del vértice sobre el que se calculará el cono.

    Returns
    -------
    SimplicialComplex
        Complejo simplicial producto de hacer el cono del complejo recibido por parámetros y un vértice cuyo nombre
        coincida con la cadena recibida.
    """
    point = Simplex(name, 0)
    point.set_faces()
    sc_point = SimplicialComplex("sc_point", 1, [point])
    return join(k, sc_point)


def generate_sim_name(faces):
    """
    Método que genera el nombre de un símplice apartir de sus caras. Se calcula de cada cara sus vértices, eliminando
    repetidos, al tener todos los vértices se genera un nombre concatenando los nombres de dichos vértices.

    Parameters
    ----------
    faces : list
        Lista que contiene los símplices que representan las caras del simplice al cual deseamos generar su nombre.

    Returns
    -------
    str
        Cadena que representa el nombre del símplice deseado, resultado de concatenar los vértices obtenidos de sus
        caras.
    """
    faces_aux = list()
    for elem in faces:
        faces_aux.extend(get_vertex_sim(elem))
    faces_aux = list(set(faces_aux))
    faces_aux.sort()
    return concatenate_list(faces_aux)


def get_vertex_sim(sim):
    """
    Método que calcula los vértices del símplice recibido por parámetros. Se hace una busqueda recursiva en profundidad
    hasta encontrar los vertices.

    Parameters
    ----------
    sim : Simplex
        Símplice del cual deseamos calcular todos sus vértices.

    Returns
    -------
    list
        Lista que contiene todos los 0-símplices/vértices del símplice recibido por parámetros.
    """
    if sim.dimension == 0:
        return [sim.name]
    else:
        result = list()
        for face in sim.faces:
            result.extend(get_vertex_sim(face))
        return result


def generate_faces_names(generative_sim):
    """
    Método que calcula los nombres de las caras para un símplice a través de la lista de los símplices que lo han
    generado. También se podría hacer solo con el nombre del propio símplice, pero es algo más tedioso y restrictivo.

    Parameters
    ----------
    generative_sim : list
        Lista de los símplices que generan al símplice del cual deseamos construir los nombres de sus caras.

    Returns
    -------
    list
        Lista que contiene todos los nombres de las caras del simplice generado por los símplices pasados por
        parámetros.
    """
    sim_vertex_names = list()
    for elem in generative_sim:
        sim_vertex_names.extend(get_vertex_sim(elem))
    sim_vertex_names = list(set(sim_vertex_names))
    sim_vertex_names.sort()
    aux = sim_vertex_names.copy()
    result = list()
    for i, elem in enumerate(sim_vertex_names):
        aux.pop(i)
        result.append(concatenate_list(aux))
        aux = sim_vertex_names.copy()
    return result


def concatenate_list(c_list):
    """
    Método simple que concatena cada elemento de la lista recibida por parámetros.

    Parametros
    ----------
    c_list : list
        Lista de la cual se desea calcular la concatenación de sus elementos.

    Returns
    -------
    any
        Resultado de concatenar dicha lista.
    """
    return reduce(lambda a, b: a + b, c_list)


def all_simplex_by_names(simplex, names, dim):
    """
    Método que recupera todos los símplices de la lista de símplices recibida que coincidan con los nombres pasados por
    parámetros y que además tengan la misma dimensión que el parámetro dim.

    Parameters
    ----------
    simplex : list
        Lista de símplices de los cuales se desea recuperar únicamente aquellos que tengan el mismo nombre y dimensión
        recibido por parámetros.
    names : list
        Lista que contiene todos los nombres que se desean buscar en la lista de símplice recibida.
    dim : int
        Entero que representa la dimensión que deben tener los símplices buscados.

    Returns
    -------
    list
        Lista que contiene los símplices deseados, aquellos que cumplan con los criterios recibidos.
    """
    result = list()
    for elem in names:
        result.append(next((sim for sim in simplex if sim.name == elem and sim.dimension == dim), None))
    return result
