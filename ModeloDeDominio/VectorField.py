# Clase VectorField.py desarrollada por Pablo Ascorbe Fernández 16/06/2022
from LogicaDeNegocio.Exceptions import *
import ModeloDeDominio.Auxiliary as Aux


class VectorField:
    """
    Clase VectorField que modela los campos de vectores gradiente asociados a un complejo simplicial.

    Attributes
    ----------
    name: str
        Nombre del campo, es una cadena que funciona como identificador.
    c_vector: list
        C-vector del complejo simplicial asociado.
    fblocks: list
        Lista de listas que contiene los bloques de la matriz de adyacencias del complejo asociado.
    routes: dict
        Diccionario en que contiene las distintas rutas o caminos del campo.
    pairs_added: list
        Lista con todas las tuplas de símplices representando los vectores ya añadidos al campo.
    sources: list
        Lista que contiene todos los símplices que ya han sido source.
    targets: list
        Lista que contiene todos los símplices que ya han sido target.

    Methods
    -------
    add_route(pair)
        Método que añade el vector recibido al campo.
    check_source(sim)
        Método que comprueba si el símplice ha sido previamente source.
    check_target(sim)
        Método que comprueba si el símplice ha sido previamente target.
    check_pair(pair)
        Método que valida si los símplices del vector son válidos para añadir al campo.
    cross_out_pair(pair)
        Método que, si el vector ya es válido para añadir al campo, introduce sus símplices en las listas
        correspondientes para evitar que dichos símplices puedan volver a ser añadidos.
    generate_route(pair)
        Método que calcula los símplices alcanzables por sigma y además verifica si hay ciclos, de haberlos devolverá
        None en lugar de las nuevas rutas.
    """

    def __init__(self, name, fblocks, c_vector):
        """
        Constructor de la clase VectorField

        Parameters
        ----------
        name : str
            Nombre a modo de identificador del campo.
        fblocks : list
            Lista que contiene los bloques de la matriz de adyacencias.
        c_vector : list
            C-vector del complejo asociado al campo de vectores.
        """
        self.name = name
        self.c_vector = c_vector
        self.fblocks = fblocks
        self.routes = dict()
        self.pairs_added = list()
        self.sources = list()
        self.targets = list()

    def __str__(self):
        """Método para devolver un string que representa a nuestro campo cuando se llama a través de print().

        Returns
        -------
        string
            Cadena que representa a nuestro campo en la llamada a print(),
            dando información sobre su nombre y rutas.
        """
        return "Campo de vectores: " + self.name + " Rutas: " + str(self.routes)

    def __repr__(self):
        """Método que devuelve la string que representa a nuestro campo.

        Returns
        -------
        basestring
            Cadena que representa a nuestro campo.
        """
        return "Campo de vectores: " + self.name + " Rutas: " + str(self.routes)

    def add_route(self, pair):
        """
        Método que añade un vector al campo, primero comprueba que sea una pareja válida y luego que no genere ciclos.
        Si cumple ambas condiciones la añade al campo.

        Parameters
        ----------
        pair : tuple
            Tupla que representa al vector a incorporar al campo. Contiene los símplices sigma y tau.
        """
        pos = self.check_pair(pair)
        if all(self.check_source(x) and self.check_target(x) for x in pair) and pos is not None:
            route = self.generate_route(pair)
            if route is not None:
                self.cross_out_pair(pair)
                self.routes[pair[0].name] = route
                for elem in [key for key, value in self.routes.items() if pair[0].name in value]:
                    value = self.routes[elem]
                    value.extend(route)
                    value.remove(pair[0].name)
            else:
                raise CycleException("Error: se ha formado un ciclo.")
        else:
            raise InvalidPairException("Error: esa pareja no es válida para generar una ruta")

    def check_source(self, sim):
        """
        Método que comprueba si el símplice proporcionado por parámetros ya ha sido previamente source.

        Parameters
        ----------
        sim : Simplex
            Simplice que deseamos validar si ya ha sido source.

        Returns
        -------
        bool
            Cierto si no ha sido source previamente y falso en caso contrario.
        """
        if sim.dimension == len(self.fblocks):
            return True
        return True if sim.name not in self.sources else False

    def check_target(self, sim):
        """
        Método que comprueba si el símplice proporcionado por parámetros ya ha sido previamente target.

        Parameters
        ----------
        sim : Simplex
            Simplice que deseamos validar si ya ha sido target.

        Returns
        -------
        bool
            Cierto si no ha sido target previamente y falso en caso contrario.
        """
        if sim.dimension == 0:
            return True
        return True if sim.name not in self.targets else False

    def check_pair(self, pair):
        """
        Método que valida si la pareja cumple las condiciones necesarias para pertenecer al campo, en este caso.
        Que sigma sea cara de tau.

        Parameters
        ----------
        pair : tuple
            Tupla que contiene el vector a validar.

        Returns
        -------
        tuple
            Tupla que contiene la fila y columna de los símplices en su bloque, None en caso de que no estén
            relacionados.
        """
        fila = Aux.get_sim_pos(self.c_vector, pair[0])
        columna = Aux.get_sim_pos(self.c_vector, pair[1])
        return (fila, columna) if self.fblocks[pair[0].dimension][fila][columna] == 1 else None

    def cross_out_pair(self, pair):
        """
        Método que añade la pareja en las listas correspondientes para evitar que esta se vuelva a incorporar.

        Parameters
        ----------
        pair : tuple
            Pareja que deseamos añadir en las listas de validación.
        """
        if pair[0].dimension > 0:
            self.targets.append(pair[0].name)
        if pair[1].dimension + 1 == len(self.fblocks):
            self.sources.append(pair[1].name)
        self.pairs_added.append(pair)
        self.sources.append(pair[0].name)
        self.targets.append(pair[1].name)

    def generate_route(self, pair):
        """
        Método que calcula las rutas alcanzadas por sigma, en caso de que sigma se alcance a sí misma entonces en lugar
        de devolver dichas rutas devolverá None.

        Parameters
        ----------
        pair : tuple
            Pareja de la cual deseamos calcular sus nuevos caminos alcanzables.

        Returns
        -------
        list
            Lista que contiene los nuevos símplices alcanzables o None en caso de ciclo.
        """
        accesible_routes = list()
        for sim in pair[1].faces:
            value = self.routes.get(sim.name, sim.name)
            if isinstance(value, str):
                accesible_routes.extend([value])
            else:
                accesible_routes.extend(value)
        accesible_routes.remove(pair[0].name)
        return accesible_routes if pair[0].name not in accesible_routes else None

    def json_encode(self):
        """
        Método que codifica el objeto a un diccionario para su correcta serialización a JSON.

        Returns
        -------
        dict
            Diccionario que representa al campo de vectores.
        """
        routes = None if self.routes is None else self.routes
        targets = None if self.routes is None else self.targets
        sources = None if self.routes is None else self.sources
        return {'id': self.name,
                'fblocks': self.fblocks,
                'c_vector': self.c_vector,
                'routes': routes,
                'targets': targets,
                'sources': sources}
