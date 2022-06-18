#Fichero de python que contiene la función Join para dos complejos simpliciales por Pablo Ascorbe 19/06/2022
from functools import reduce
from ModeloDeDominio.Simplex import Simplex
from ModeloDeDominio.SimplicialComplex import SimplicialComplex


def join(K, L):
    """

    :param K:
    :param L:
    :return:
    """
    all_simplex = K.simplex + L.simplex
    for K_simplex in K.simplex:
        k_sim_faces = list(K_simplex.faces) if K_simplex.dimension > 0 else [K_simplex]
        for L_simplex in L.simplex:
            faces_aux = k_sim_faces.copy()
            faces_aux.extend(L_simplex.faces if L_simplex.dimension > 0 else [L_simplex])
            simplex = Simplex(generate_sim_name(faces_aux), len(faces_aux) - 1)
            simplex.set_faces(all_simplex_by_names(all_simplex, generate_faces_names(simplex.name)))
            all_simplex.append(simplex)
    return SimplicialComplex("L*K", K.omega + L.omega, all_simplex)


def generate_sim_name(faces):
    """
    TODO
    :param faces:
    :return:
    """
    faces_ids = list(map(lambda x: x.name, faces))
    faces_aux = list()
    for elem in faces_ids:
        faces_aux.extend(elem)
    faces_aux = list(set(faces_aux))
    faces_aux.sort()
    return concatenate_char_list(faces_aux)


def generate_faces_names(sim_name):
    """
    TODO
    :param sim_name:
    :return:
    """
    name_char = list(sim_name)
    result = list()
    for i in range(0, len(name_char)):
        aux = name_char.copy()
        aux.pop(i)
        result.append(concatenate_char_list(aux))
    return result


def concatenate_char_list(c_list):
    """
    TODO
    :param c_list:
    :return:
    """
    return reduce(lambda a, b: a + b, c_list)


def all_simplex_by_names(simplex, names):
    """
    TODO
    :param simplex:
    :param names:
    :return:
    """
    result = list()
    for elem in names:
        result.append(next((sim for sim in simplex if sim.name == elem), None))
    return result
