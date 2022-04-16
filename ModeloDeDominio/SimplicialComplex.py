# Clase SimplicialComplex.py desarrollada por Pablo Ascorbe Fernández 16/04/2022
import numpy as np


class SimplicialComplex:

    # Contructor de la clase SimplicialComplex, recibe el conjunto de simplices y calcula el resto de atributos de la
    # clase, como los facests del mismo y la matriz de cocaras.
    def __init__(self, simplex=None, facets=None):
        if simplex:
            simplex = sorted(simplex, key=lambda x: x.dimension)
            for elm, i in zip(simplex, range(0, len(simplex))):
                elm.set_index(i)
            self.simplex = simplex
            self.matrix = simplicial_matrix(self.simplex)
            self.facets = simplex_to_facets(self.simplex, self.matrix)
        else:
            self.facets = facets


# Método para pasar del conjunto de simplices a los facets, necesitamos la matriz de cocaras para hacer más eficiente
# este cambio
def simplex_to_facets(simplex, matrix):
    facets = set()
    matrix_traspuesta = np.transpose(matrix)
    for elm in simplex:
        row = matrix_traspuesta[elm.index]
        es_facet = True
        for i in range(elm.index, len(simplex)):
            if elm.index != i and row[i] == 1:
                es_facet = False
        if es_facet:
            facets.add(elm)
    return sorted(facets, key=lambda x: x.dimension)


# Método que calcula la matriz de cocaras de un complejos simplicial dados sus simplices
def simplicial_matrix(simplex):
    matrix = []
    for elm in simplex:
        row = [0] * len(simplex)
        row[elm.index] = 1
        for cocaras in elm.cofaces:
            row[cocaras.index] = 1
        matrix.append(row)
    return matrix
