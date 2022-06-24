# Métodos de lógica de negocio que calculan el join y cono por Pablo Ascorbe 18/06/2022
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
    all_simplex = k_sc.simplex + l_sc.simplex
    for K_simplex in k_sc.simplex:
        k_sim_faces = list(K_simplex.faces) if K_simplex.dimension > 0 else [K_simplex]
        for L_simplex in l_sc.simplex:
            faces_aux = k_sim_faces.copy()
            faces_aux.extend(L_simplex.faces if L_simplex.dimension > 0 else [L_simplex])
            simplex = Simplex(generate_sim_name(faces_aux), len(faces_aux) - 1)
            faces = set()
            for sim in all_simplex:
                for face in faces_aux:
                    if sim.name == face.name:
                        faces.add(sim)
            simplex.set_faces(faces)
            # simplex.set_faces(set(all_simplex_by_names(all_simplex, generate_faces_names(simplex.name))))
            all_simplex.append(simplex)
    for elem in all_simplex:
        print("-------")
        print(elem)
        print(elem.faces)
    return SimplicialComplex("L*K", k_sc.omega + l_sc.omega, all_simplex)


def cono(k):
    """
    TODO
    :param k:
    :return:
    """
    point = Simplex("Point", 0)
    point.set_faces()
    sc_point = SimplicialComplex("sc_point", 1, [point])
    return join(k, sc_point)


def generate_sim_name(faces):
    """
    TODO
    :param faces:
    :return:
    """
    faces_ids = list(map(lambda x: x.name, faces))
    faces_aux = list()
    if any(x for x in faces_ids if len(x) > 1):
        faces_aux = faces_ids
        faces_aux.sort()
    else:
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
    print(simplex, names)
    result = list()
    for elem in names:
        result.append(next((sim for sim in simplex if sim.name == elem), None))
    return result
