# Clase SimplicialComplex.py desarrollada por Pablo Ascorbe Fernández 20/04/2022
import numpy as np


class SimplicialComplex:

    # Contructor de la clase SimplicialComplex, recibe el conjunto de simplices y calcula el resto de atributos de la
    # clase, como los facests del mismo y la matriz de cocaras.
    def __init__(self, simplex=None, facets=None):
        if facets:
            self.facets = facets
            simplex = facets_to_simplex(facets, set())
        simplex = sorted(simplex, key=lambda x: (x.dimension, x.name))
        for elm, i in zip(simplex, range(0, len(simplex))):
            elm.set_index(i)
        self.simplex = simplex
        resultado = simplicial_matrix(simplex)
        self.dimension = simplex[len(simplex) - 1].dimension
        self.matrix = resultado[0]
        self.c_vector = resultado[1]
        if facets is None:
            self.facets = set(simplex_to_facets(self.simplex, self.matrix))
        self.euler_char = euler_characteristic(self.c_vector)

    # Método para devolver una string que representa nuestro complejo simplicial al llamar a print()
    def __str__(self):
        return "Dimension: "+str(self.dimension)+", Caracteristica de Euler: "+str(self.euler_char)+", facets: "\
               + str(self.facets)

    # Método que devuelve una string que representa a nuestro complejo simplicial
    def __repr__(self):
        return "Dimension: " + str(self.dimension) + ", Caracteristica de Euler: " + str(self.euler_char) \
               + ", facets: " + str(self.facets)


# Método para pasar del conjunto de simplices a los facets, necesitamos la matriz de cocaras para hacer más eficiente
# este cambio
def simplex_to_facets(simplex, matrix):
    facets = set()
    for elm in simplex:
        row = matrix[elm.index]
        es_facet = True
        for i in range(elm.index, len(simplex)):
            if elm.index != i and row[i] == 1:
                es_facet = False
        if es_facet:
            facets.add(elm)
    return sorted(facets, key=lambda x: x.dimension)


def facets_to_simplex(facets, simplex):
    simplex = set.union(simplex, facets)
    for elm in facets:
        simplex = facets_to_simplex(elm.cofaces, simplex)
    return simplex


# Método que calcula la matriz de cocaras, caras y el c-vector de un conjunto de simplices
def simplicial_matrix(simplex):
    matrix = []
    c_vector = [0] * (simplex[len(simplex)-1].dimension + 1)
    dimension = 0
    for elm in simplex:
        if dimension < elm.dimension:
            dimension += 1
        c_vector[dimension] += 1
        row = [0] * len(simplex)
        row[elm.index] = 1
        for cocaras in elm.cofaces:
            row[cocaras.index] = 1
        matrix.append(row)
    matrix_traspuesta = np.transpose(matrix)
    matrix = matrix + matrix_traspuesta - np.identity(len(simplex))
    return matrix, c_vector


# Método que calcula la característica de Euler a partir del c-vector proporcionado
def euler_characteristic(c_vector):
    dimension_par = c_vector[0::2]
    dimension_impar = c_vector[1::2]
    return np.sum(dimension_par) - np.sum(dimension_impar)
