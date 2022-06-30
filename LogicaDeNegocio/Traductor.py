# Fichero de traducción entre sc y fb desarrollado por Pablo Ascorbe Fernández 15/06/2022
import ModeloDeDominio.Auxiliary as Aux
from LogicaDeNegocio.Join import *
from ModeloDeDominio.BooleanFunction import BooleanFunction
from ModeloDeDominio.Simplex import Simplex
from ModeloDeDominio.SimplicialComplex import SimplicialComplex


def boolean_function_to_simplicial_complex(bf):
    """
    Método que traduce la función booleana recibida por parámetros a un complejo simplicial. Como precondición se espera
    que la función booleana sea monótona.

    Parameters
    ----------
    bf : BooleanFunction
        Función booleana que querremos transformar a su complejo simplicial asociado.

    Returns
    -------
    SimplicialComplex
        Complejo simplicial traducido de la función booleana recibida.
    """
    aux_output = bf.outputs
    simplices = list()
    for i in reversed(range(1, len(aux_output))):
        if aux_output[i] == 1 and not any(x.name == str(i) for x in simplices):
            act_sim = Simplex(str(i), Aux.num_1(i) - 1)
            simplices.append(act_sim)
            construct_simplex(act_sim, simplices)
    simplices = Aux.order_simplicial_list(simplices)
    rename_simplices_for_boolean_function(simplices, bf.name_variables)
    sc = SimplicialComplex(bf.name, bf.num_variables, simplices)
    return sc

def rename_simplices_for_boolean_function(simplices, name_variables):
    """
    TODO
    :param simplices:
    :param name_variables:
    :return:
    """
    vertex_count = 0
    for sim in simplices:
        if sim.dimension == 0:
            sim.name = name_variables[vertex_count]
            vertex_count += 1
        else:
            sim.name = generate_sim_name(sim.faces)

def construct_simplex(act_simp, simplices):
    """
    TODO: documentarlo
    :param act_simp:
    :param simplices:
    :return:
    """
    bin_num = bin(int(act_simp.name))[2:]
    num_ones = bin_num.count('1')
    pos_num = 0
    faces = set()
    for i in range(1, num_ones + 1):
        aux_copy = bin_num
        for elem in aux_copy[pos_num:]:
            if elem == '1':
                aux_copy = aux_copy[:pos_num] + '0' + aux_copy[pos_num + 1:]
                pos_num += 1
                break
            pos_num += 1
        child = int(aux_copy, 2)
        child_sim = next((x for x in simplices if x.name == str(child)), None)
        if not child_sim:
            s = Simplex(str(child), Aux.num_1(child) - 1)
            if s.dimension != -1:
                simplices.append(s)
                faces.add(s)
                if s.dimension > 0:
                    construct_simplex(s, simplices)
                else:
                    s.set_faces()
        else:
            faces.add(child_sim)
    act_simp.set_faces(faces)


def simplicial_complex_to_boolean_function(sc):
    """
    TODO
    Parameters
    ----------
    sc : SimplicialComplex

    :return:
    """
    num_variables = sc.c_vector[0]
    outputs = [0] * (2**num_variables)
    outputs[0] = 1
    sim_pos = dict()
    for sim in sc.simplex:
        pos = 2**sim.index if sim.dimension == 0 else position_in_ouput(sim, sim_pos)
        outputs[pos] = 1
        sim_pos[sim.name] = pos
    return BooleanFunction(sc.name, num_variables, get_vertex_names(sc.simplex), outputs)

def get_vertex_names(simplices):
    """
    TODO
    :param simplices:
    :return:
    """
    vertex = [x for x in simplices if x.dimension == 0]
    return [x.name for x in vertex]

def position_in_ouput(simplex, sim_pos):
    """
    TODO
    :param simplex:
    :param sim_pos:
    :return:
    """
    faces_pos = list()
    for face in simplex.faces:
        faces_pos.append(sim_pos[face.name])
    return reduce(lambda x, y: x | y, faces_pos)
