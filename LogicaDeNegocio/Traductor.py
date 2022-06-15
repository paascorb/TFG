# Fichero con clases auxiliares desarrollado por Pablo Ascorbe Fernández 15/06/2022
import LogicaDeNegocio.Auxiliary as Aux
from ModeloDeDominio.Simplex import Simplex
from ModeloDeDominio.SimplicialComplex import SimplicialComplex
from ModeloDeDominio.BooleanFunction import BooleanFunction


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
    for i in reversed(range(1, len(bf.outputs))):
        if aux_output[i] == 1 and not any(x.name == str(i) for x in simplices):
            simplices.append(Simplex(str(i), Aux.num_1(i)-1))
            construct_simplex(i, simplices)
    sc = SimplicialComplex(bf.name, bf.num_variables, simplices)
    return sc


def construct_simplex(num, simplices):
    """
    TODO: documentarlo
    :param num:
    :param simplices:
    :return:
    """
    bin_num = bin(num)[2:]
    num_ones = bin_num.count('1')
    pos_num = 0
    faces = set()
    coface = next(x for x in simplices if x.name == str(num))
    for i in range(1, num_ones + 1):
        aux_copy = bin_num
        for elem in aux_copy[pos_num:]:
            if elem == '1':
                aux_copy = aux_copy[:pos_num] + '0' + aux_copy[pos_num + 1:]
                pos_num += 1
                break
            pos_num += 1
        child = int(aux_copy, 2)
        if not any(x.name == str(child) for x in simplices):
            s = Simplex(str(child), Aux.num_1(child) - 1)
            simplices.append(s)
            faces.add(s)
            if s.dimension > 0:
                construct_simplex(child, simplices)
            else:
                s.set_faces()
        else:
            s = next(x for x in simplices if x.name == str(child))
            faces.add(s)
    coface.set_faces(faces)

