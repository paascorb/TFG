# Métodos de lógica de negocio que calculan el join y cono por Pablo Ascorbe 18/06/2022
import copy
from functools import reduce
from ModeloDeDominio.Simplex import Simplex
from ModeloDeDominio.SimplicialComplex import SimplicialComplex


def join(k_sc, l_sc):
    """
    TODO
    :param k_sc:
    :param l_sc:
    :return:
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
    TODO
    :param k:
    :return:
    """
    point = Simplex(name, 0)
    point.set_faces()
    sc_point = SimplicialComplex("sc_point", 1, [point])
    return join(k, sc_point)


def generate_sim_name(faces):
    """
    TODO
    :param faces:
    :return:
    """
    faces_aux = list()
    for elem in faces:
        faces_aux.extend(get_vertex_sim(elem))
    faces_aux = list(set(faces_aux))
    faces_aux.sort()
    return concatenate_list(faces_aux)


def get_vertex_sim(sim):
    if sim.dimension == 0:
        return [sim.name]
    else:
        result = list()
        for face in sim.faces:
            result.extend(get_vertex_sim(face))
        return result


def generate_faces_names(generative_sim):
    """
    TODO
    :param generative_sim:
    :return:
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
    TODO
    :param c_list:
    :return:
    """
    return reduce(lambda a, b: a + b, c_list)


def all_simplex_by_names(simplex, names, dim):
    """
    TODO
    :param simplex:
    :param names:
    :return:
    """
    result = list()
    for elem in names:
        result.append(next((sim for sim in simplex if sim.name == elem and sim.dimension == dim), None))
    return result
