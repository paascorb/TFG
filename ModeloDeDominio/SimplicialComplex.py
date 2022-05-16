# Clase SimplicialComplex.py desarrollada por Pablo Ascorbe Fernández 20/04/2022
import LogicaDeNegocio.AuxiliarySC as Aux


class SimplicialComplex:

    # Contructor de la clase SimplicialComplex, recibe el conjunto de simplices y calcula el resto de atributos de la
    # clase, como los facests del mismo y la matriz de cocaras.
    def __init__(self, omega=0, simplex=None, facets=None):
        self.omega = omega
        if facets:
            self.facets = facets
            simplex = Aux.facets_to_simplex(facets, set())
        self.simplex = simplex
        self.simplex = Aux.order_and_index(self.simplex)
        if not Aux.is_simplicial_complex(simplex):
            raise Exception("La lista de simplices no puede generar un complejo simplicial.")
        self.dimension = Aux.dimension_from_simplex(self.simplex)
        if self.omega < self.dimension:
            raise Exception("Los simplices no están definidos dentro de omega.")
        resultado = Aux.fmatrix_and_cvector(self.simplex, self.dimension)
        self.matrix = resultado[0]
        self.c_vector = resultado[1]
        self.euler_char = Aux.euler_characteristic(self.c_vector)
        facets_aux = set(Aux.simplex_to_facets(self.simplex, self.matrix))
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
        list(self.simplex).append(sigma)
        list(self.simplex).append(tau)
        self.recalculate()
        return self

    # TODO: Funciones Link, Star, Join y Cono

    # Método auxiliar que recalcula los parámetros del complejo simplicial, reordenando e indexando sus simplices,
    # volviendo a calcular su matriz de caras y su c-vector además de sus facests y dimensión
    def recalculate(self):
        self.simplex = Aux.order_and_index(self.simplex)
        resultado = Aux.fmatrix_and_cvector(self.simplex, self.dimension)
        self.matrix = resultado[0]
        self.c_vector = resultado[1]
        self.facets = Aux.simplex_to_facets(self.simplex, self.matrix)
        self.dimension = Aux.dimension_from_simplex(self.simplex)
