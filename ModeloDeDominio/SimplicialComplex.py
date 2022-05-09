# Clase SimplicialComplex.py desarrollada por Pablo Ascorbe Fernández 20/04/2022
import numpy as np


class SimplicialComplex:

    # Contructor de la clase SimplicialComplex, recibe el conjunto de simplices y calcula el resto de atributos de la
    # clase, como los facests del mismo y la matriz de cocaras.
    def __init__(self, omega=0, simplex=None, facets=None):
        self.omega = omega
        self.dimension = 0
        if facets:
            self.facets = facets
            simplex = facets_to_simplex(facets, set())
        self.simplex = simplex
        self.order_and_index()
        if not is_simplicial_complex(simplex):
            raise Exception("La lista de simplices no puede generar un complejo simplicial.")
        self.get_dimension()
        if self.omega < self.dimension:
            raise Exception("Los simplices no están definidos dentro de omega.")
        resultado = simplicial_matrix(self.simplex)
        self.matrix = resultado[0]
        self.c_vector = resultado[1]
        self.euler_char = euler_characteristic(self.c_vector)
        facets_aux = set(simplex_to_facets(self.simplex, self.matrix))
        if facets is None:
            self.facets = facets_aux
        else:
            if not facets_aux == self.facets:
                raise Exception("La lista de facets proporcionada es erronea.")

    # Método para devolver una string que representa nuestro complejo simplicial al llamar a print()
    def __str__(self):
        return "Dimension: "+str(self.dimension)+", Caracteristica de Euler: "+str(self.euler_char)+", facets: "\
               + str(self.facets)

    # Método que devuelve una string que representa a nuestro complejo simplicial
    def __repr__(self):
        return "Dimension: " + str(self.dimension) + ", Caracteristica de Euler: " + str(self.euler_char) \
               + ", facets: " + str(self.facets)

    # Método que comprueba si nuestro complejo simplicial puede colapsar con el par de simplices
    # sigma y tau proporcionado
    def can_collapse(self, sigma, tau):
        if tau and sigma not in self.simplex or tau not in self.facets or sigma not in tau.faces:
            return False
        sigma_index = list(self.simplex).index(sigma)
        tau_index = list(self.simplex).index(tau)
        sigma_row = self.matrix[sigma_index]
        for elm, i in zip(sigma_row[sigma_index+1::], range(sigma_index + 1, len(self.simplex))):
            if i != tau_index and elm == 1:
                return False
        return True

    # Método que comprueba si el complejo simplicial puede colapsar y de ser así lo colapsa con el par de sigma y tau
    # dados.
    def collapse(self, sigma, tau):
        if not self.can_collapse(sigma, tau):
            raise Exception("El complejo simplicial no puede colapsar con el par de simplices dado.")
        self.simplex.remove(sigma)
        self.simplex.remove(tau)
        self.recalculate()
        return self

    # Método que comprueba si nuestro complejo simplicial puede expandires con el par libre de simplices dado
    def can_expand(self, sigma, tau):
        aux = tau.faces.copy()
        aux.remove(sigma)
        if tau and sigma in self.simplex or sigma not in tau.faces or not set(sigma.faces).issubset(set(self.simplex)) \
                or not aux.issubset(set(self.simplex)):
            return False
        else:
            return True

    # Método que comprueba si el complejo simplicial puede expandirse y de ser así lo expande con el par de sigma y tau
    # dados.
    def expand(self, sigma, tau):
        if not self.can_expand(sigma, tau):
            raise Exception("El complejo simplicial no puede expandirse con el par de simplices dado.")
        self.simplex.append(sigma)
        self.simplex.append(tau)
        self.recalculate()
        return self

    # Método que ordena e indexa los simplices del complejos simplicial
    def order_and_index(self):
        self.simplex = sorted(self.simplex, key=lambda x: (x.dimension, x.name))
        for elm, i in zip(self.simplex, range(0, len(self.simplex))):
            elm.set_index(i)

    # Método que calcula la dimension del complejo simplicial y se la asigna a su atributo.
    def get_dimension(self):
        self.dimension = self.simplex[len(self.simplex) - 1].dimension

    # Método auxiliar que recalcula los parámetros del complejo simplicial, reordenando e indexando sus simplices,
    # volviendo a calcular su matriz de caras y su c-vector además de sus facests y dimensión
    def recalculate(self):
        self.order_and_index()
        resultado = simplicial_matrix(self.simplex)
        self.matrix = resultado[0]
        self.c_vector = resultado[1]
        self.facets = simplex_to_facets(self.simplex, self.matrix)
        self.get_dimension()


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


# Método para calcular el conjunto de simplices de un complejo simplicial dado su conjunto de facets.
def facets_to_simplex(facets, simplex):
    simplex = set.union(simplex, facets)
    for elm in facets:
        simplex = facets_to_simplex(elm.faces, simplex)
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
        for caras in elm.faces:
            row[caras.index] = 1
        matrix.append(row)
    matrix_traspuesta = np.transpose(matrix)
    matrix = matrix + matrix_traspuesta - np.identity(len(simplex))
    return matrix, c_vector


# Método que calcula la característica de Euler a partir del c-vector proporcionado
def euler_characteristic(c_vector):
    dimension_par = c_vector[0::2]
    dimension_impar = c_vector[1::2]
    return np.sum(dimension_par) - np.sum(dimension_impar)


# Método para calcular si un conjunto de simplices pueden conformar o no un complejo simplicial
def is_simplicial_complex(simplex):
    for elm in simplex:
        if elm.faces is None:
            return False
        elif elm.dimension > 0:
            for cara in elm.faces:
                if cara not in simplex or (elm.dimension - cara.dimension) != 1:
                    return False
        else:
            if not len(elm.faces) == 0:
                return False
    return True
