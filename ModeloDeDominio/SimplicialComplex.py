# Clase SimplicialComplex.py desarrollada por Pablo Ascorbe Fernández 20/04/2022
import ModeloDeDominio.Auxiliary as Aux
from ModeloDeDominio.Simplex import Simplex
from ModeloDeDominio.VectorField import VectorField


class SimplicialComplex:
    """
        Clase SimplicialComplex que modela el concepto de complejos simplicial.

        Attributes
        ----------
        name : str
            Nombre del complejo, es una cadena de caracteres que funciona como un identificador.
        omega : int
            Entero que representa el conjunto de vértices sobre el que se está construyendo el complejo.
        simplex : list
            Conjunto de símplices del complejo.
        facets: list
            Conjunto de facets del complejo.
        dimension : int
            Dimensión máxima del conjunto de sus símplices.
        matrix : list
            Lista de listas que representa la matriz de adyacencias del complejo simplicial.
        c_vector: list
            C-vector del complejo simplicial.
        euler_char : int
            Característica de Euler del complejo simplicial.
        vector_fields : list
            Lista que contiene todos los campos que han sido incorporados al campo de vectores.

        Methods
        -------
        get_sim_cofaces(sim)
            Método que devuelve la lista de cocaras del símplice recibido por parámetros.
        can_collapse(sigma, tau)
            Método que comprueba que la pareja, sigma tau, recibida es válida para colapsar. Esto es que sigma sea cara
            de tau, que tau sea un facet, que las caras de tua estén en el complejo y que ambos símplices estén en el
            complejo. Además, sigma no puede tener otras cocaras en el complejo que no sean tau.
        collapse(sigma, tau)
            Método que colapsa el complejo simplicial a partir de la pareja sigma, tau proporcionada. Primero comprueba
            que dicha pareja es válida para colapsar el complejo y si no es válida devuelve una excepción.
        can_expand(self, sigma, tau)
            Método que comprueba que la pareja, sigma tau, recibida es válida para expandirse. Esto es que sigma sea
            cara de tau, y que las caras tanto de sigma como de tau estén en el complejo. Además, ni sigma ni tau deben
            estar previamente en el complejo simplicial.
        expand(self, sigma, tau)
            Método que expande el complejo simplicial a partir de la pareja sigma, tau proporcionada. Primero comprueba
            que dicha pareja es válida para expandir el complejo y si no es válida devuelve una excepción.
        add_vector_field(vf)
            Método que añade el campo de vectores recibido a la lista de campos.
        create_vector_field(name)
            Método que crea un campo de vectores con el nombre recibido por parámetros y lo añade a la lista de campos.
        closure(sim)
            Método que calcula la clausura del símplice proporcionado por parámetros.
        borde(sim)
            Método que calcula el borde del símplice proporcionado por parámetros.
        star(sim)
            Método que calcula el star cerrado del 0-símplice proporcionado por parámetros.
        open_star(sim)
            Método que calcula el star abierto del 0-símplice proporcionado por parámetros.
        link(sim)
            Método que calcula el link del vértice proporcionado por parámetros.
        recalculate()
            Método auxiliar que recalcula los parámetros del complejo simplicial, reordenando e indexando sus símplices,
            volviendo a calcular su matriz de caras y su c-vector además de sus facets y dimensión.
    """

    def __init__(self, name, omega=0, simplex=None, facets=None):
        """
        Constructor de la clase complejo simplicial.

        Parameters
        ----------
        name : str
            Nombre del complejo, es una cadena de caracteres que funciona como un identificador.
        omega : int
            Entero que representa el conjunto de vértices sobre el que se está construyendo el complejo.
        simplex : list
            Conjunto de símplices del complejo. Es opcional.
        facets: list
            Conjunto de facets del complejo. Es opcional.
        """
        self.name = name
        self.omega = omega
        if facets:
            self.facets = facets
            simplex = Aux.facets_to_simplex(facets)
        self.simplex = simplex
        self.simplex = Aux.order_and_index(self.simplex)
        if not Aux.is_simplicial_complex(simplex):
            raise Exception("La lista de simplices no puede generar un complejo simplicial.")
        self.dimension = Aux.dimension_from_simplex(self.simplex)
        resultado = Aux.fmatrix_and_cvector(self.simplex, self.dimension)
        self.matrix = resultado[0]
        self.c_vector = resultado[1]
        # Omega es el alfabeto, es decir, el número de vertices (0-símplices) que hay disponibles para hacer
        # combinaciones. Por tanto, define un conjunto finito de 0-símplices.
        if self.omega < self.c_vector[0]:
            raise Exception("Los simplices no están definidos dentro de omega.")
        self.euler_char = Aux.euler_characteristic(self.c_vector)
        self.vector_fields = list()
        facets_aux = set(Aux.simplex_to_facets(self.simplex, self.matrix))
        if facets is None:
            self.facets = facets_aux
        else:
            if not facets_aux == self.facets:
                raise Exception("La lista de facets proporcionada es errónea.")

    def __str__(self):
        """Método para devolver un string que representa a nuestro complejo cuando se llama a través de print().

        Returns
        -------
        str
            Cadena que representa a nuestro complejo en la llamada a print(),
            dando información sobre su dimensión, característica de Euler y facets.
        """
        return "Dimension: " + str(self.dimension) + ", Característica de Euler: " + str(self.euler_char) \
               + ", facets: " + str(self.facets)

    def __repr__(self):
        """Método que devuelve la string que representa a nuestro complejo.

        Returns
        -------
        basestring
            Cadena que representa a nuestro complejo.
        """
        return "Dimension: " + str(self.dimension) + ", Característica de Euler: " + str(self.euler_char) \
               + ", facets: " + str(self.facets)

    def __eq__(self, other):
        """
        Método para la comparación entre objetos de la misma clase.

        Returns
        ------
        boolean
            Booleano que representa si dos objetos de la misma clase son iguales.
        """
        if not isinstance(other, SimplicialComplex):
            return NotImplemented
        return self.name == other.name

    def get_sim_cofaces(self, sim):
        """
        Método que devuelve la lista de cocaras del símplice recibido por parámetros.

        Parameters
        ----------
        sim : Simplex
            Símplice del que deseamos calcular sus cocaras.

        Returns
        -------
        list
            Lista que contiene las cocaras del complejo recibido por parámetros.
        """
        init = sum(self.c_vector[:sim.dimension + 1])
        end = init + self.c_vector[(sim.dimension + 1)]
        row = self.matrix[sim.index]
        cofaces = list()
        for pos in range(init, end):
            if row[pos] == 1:
                cofaces.append(self.simplex[pos])
        return cofaces

    def can_collapse(self, sigma, tau):
        """
        Método que comprueba que la pareja, sigma tau, recibida es válida para colapsar. Esto es que sigma sea cara de
        tau, que tau sea un facet, que las caras de tua estén en el complejo y que ambos símplices estén en el complejo.
        Además, sigma no puede tener otras cocaras en el complejo que no sean tau.

        Parameters
        ----------
        sigma : Simplex
            Símplice sigma de la pareja libre a eliminar.
        tau : Simplex
            Símplice tau de la pareja libre a eliminar.

        Returns
        -------
        bool
            Cierto si puede colapsar y falso en caso contrario.
        """
        if tau and sigma not in self.simplex or tau not in self.facets or sigma not in tau.faces:
            return False
        sigma_index = list(self.simplex).index(sigma)
        tau_index = list(self.simplex).index(tau)
        sigma_row = self.matrix[sigma_index]
        for elm, i in zip(sigma_row[sigma_index+1::], range(sigma_index + 1, len(self.simplex))):
            if i != tau_index and elm == 1:
                return False
        return True

    def collapse(self, sigma, tau):
        """
        Método que colapsa el complejo simplicial a partir de la pareja sigma, tau proporcionada. Primero comprueba que
        dicha pareja es válida para colapsar el complejo y si no es válida devuelve una excepción.

        Parameters
        ----------
        sigma : Simplex
            Símplice sigma de la pareja libre a eliminar.
        tau : Simplex
            Símplice tau de la pareja libre a eliminar.

        Returns
        -------
        SimplicialComplex
            Es el complejo simplicial después de haber recibido el colapso, por si se desea trabajar con él.
        """
        if not self.can_collapse(sigma, tau):
            raise Exception("El complejo simplicial no puede colapsar con el par de simplices dado.")
        self.simplex.remove(sigma)
        self.simplex.remove(tau)
        self.recalculate()
        return self

    def can_expand(self, sigma, tau):
        """
        Método que comprueba que la pareja, sigma tau, recibida es válida para expandirse. Esto es que sigma sea cara de
        tau, y que las caras tanto de sigma como de tau estén en el complejo. Además, ni sigma ni tau deben estar
        previamente en el complejo simplicial.

        Parameters
        ----------
        sigma : Simplex
            Símplice sigma de la pareja libre a añadir.
        tau : Simplex
            Símplice tau de la pareja libre a añadir.

        Returns
        -------
        bool
            Cierto si puede expandirse y falso en caso contrario.
        """
        if sigma.dimension != tau.dimension - 1:
            return False
        aux = tau.faces.copy()
        aux.remove(sigma)
        if tau and sigma in self.simplex or sigma not in tau.faces or not set(sigma.faces).issubset(set(self.simplex)) \
                or not aux.issubset(set(self.simplex)):
            return False
        else:
            return True

    def expand(self, sigma, tau):
        """
        Método que expande el complejo simplicial a partir de la pareja sigma, tau proporcionada. Primero comprueba que
        dicha pareja es válida para expandir el complejo y si no es válida devuelve una excepción.

        Parameters
        ----------
        sigma : Simplex
            Símplice sigma de la pareja libre a añadir.
        tau : Simplex
            Símplice tau de la pareja libre a añadir.

        Returns
        -------
        SimplicialComplex
            Es el complejo simplicial después de haber recibido la expansión, por si se desea trabajar con él.
        """
        if not self.can_expand(sigma, tau):
            raise Exception("El complejo simplicial no puede expandirse con el par de simplices dado.")
        if sigma.dimension == 0:
            self.omega += 1
        self.simplex.append(sigma)
        self.simplex.append(tau)
        self.recalculate()
        return self

    def add_vector_field(self, vf):
        """
        Método que añade el campo de vectores recibido a la lista de campos.

        Parameters
        ----------
        vf : VectorField
            Campo de vectores que se desea añadir a la lista de campos de vectores.
        """
        self.vector_fields.append(vf)

    def create_vector_field(self, name):
        """
        Método que crea un campo de vectores con el nombre recibido por parámetros y lo añade a la lista de campos.

        Parameters
        ----------
        name : str
            Nombre del campo de vectores que se asociará al complejo.

        Returns
        -------
        VectorField
            Campo de vectores que se ha creado, por si se desea trabajar con él.
        """
        vf = VectorField(name, Aux.slice_fmatrix(self.matrix, self.c_vector), self.c_vector)
        self.vector_fields.append(vf)
        return vf

    def closure(self, sim):
        """
        Método que calcula la clausura del símplice proporcionado por parámetros.

        Parameters
        ----------
        sim : Simplex
            Símplice del que se desea calcular la clausura.

        Returns
        -------
        List
            Lista que contiene los símplices que conforman la clausura del símplice, esta lista puede conformar un
            complejo simplicial.
        """
        if sim.dimension == 0:
            return [sim]
        closure_list = list()
        closure_list.append(sim)
        for face in sim.faces:
            closure_list.extend(self.closure(face))
        return list(set(closure_list))

    def borde(self, sim):
        """
        Método que calcula el borde del símplice proporcionado por parámetros.

        Parameters
        ----------
        sim : Simplex
            Símplice del que se desea calcular el borde.

        Returns
        -------
        List
            Lista que contiene los símplices que conforman el borde del símplice, esta lista puede conformar un complejo
            simplicial.
        """
        borde = self.closure(sim)
        borde.remove(sim)
        return borde

    def star(self, sim):
        """
        Método que calcula el star cerrado del 0-símplice proporcionado por parámetros.

        Parameters
        ----------
        sim : Simplex
            Vértice del que se desea calcular el star.

        Returns
        -------
        List
            Lista que contiene los símplices que conforman el star del vértice, esta lista puede conformar un complejo
            simplicial.
        """
        if sim in self.facets:
            return [sim]
        star_list = list()
        star_list.append(sim)
        for coface in self.get_sim_cofaces(sim):
            star_list.extend(self.star(coface))
        aux = star_list.copy()
        for elem in aux:
            star_list.extend(self.closure(elem))
        return list(set(star_list))

    def open_star(self, sim):
        """
        Método que calcula el star abierto del 0-símplice proporcionado por parámetros.

        Parameters
        ----------
        sim : Simplex
            Vértice del que se desea calcular el star.

        Returns
        -------
        List
            Lista que contiene los símplices que conforman el star abierto del vértice.
        """
        if sim in self.facets:
            return [sim]
        open_star = list()
        open_star.append(sim)
        for coface in self.get_sim_cofaces(sim):
            open_star.extend(self.open_star(coface))
        return list(set(open_star))

    def link(self, sim):
        """
        Método que calcula el link del vértice proporcionado por parámetros.

        Parameters
        ----------
        sim : Simplex
            Vértice del que se desea calcular el star.

        Returns
        -------
        List
            Lista que contiene los símplices que conforman el link del vértice, esta lista puede conformar un complejo
            simplicial.
        """
        star = self.star(sim)
        open_star = self.open_star(sim)
        return [x for x in star if x not in open_star]

    def recalculate(self):
        """
        Método auxiliar que recalcula los parámetros del complejo simplicial, reordenando e indexando sus símplices,
        volviendo a calcular su matriz de caras y su c-vector además de sus facets y dimensión.
        """
        self.simplex = Aux.order_and_index(self.simplex)
        resultado = Aux.fmatrix_and_cvector(self.simplex, self.dimension)
        self.matrix = resultado[0]
        self.c_vector = resultado[1]
        self.facets = Aux.simplex_to_facets(self.simplex, self.matrix)
        self.dimension = Aux.dimension_from_simplex(self.simplex)

    def json_encode(self):
        """
        Método que codifica el objeto a un diccionario para su correcta serialización a JSON.

        Returns
        -------
        dict
            Diccionario que representa al complejo simplicial.
        """
        simplex = list()
        for elem in self.simplex:
            aux = Simplex(elem.name, elem.dimension)
            aux.faces = [o.name for o in elem.faces]
            aux.index = elem.index
            simplex.append(aux)
        return {'id': self.name,
                'omega': str(self.omega),
                'simplex': simplex,
                'vector_fields': self.vector_fields}
