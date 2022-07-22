# Clase SimplicialComplex.py desarrollada por Pablo Ascorbe Fernández 11/05/2022


class BooleanFunction:
    """
    Clase BooleanFunctions que modela una función booleana. En nuestro caso, que trabajamos en un contexto de complejos
    simpliciales, nos interesarán aquellas que sean monótonas.

    Attributes
    ----------
    name : str
        Nombre de la función booleana, es una cadena de caracteres que funciona como un identificador.
    num_variables : int
        Número de variables de la función booleana.
    name_variables : list
        Lista con los nombres de las variables de la función.
    outputs : list
        Lista que contiene 0s y 1s representando las salidas de la función booleana.
    monotone_flag : bool
        Cierto si la función es monótona creciente y falso en caso contrario.

    Methods
    -------
    set_monotone_flag(flag)
        Método setter para el atributo monotone_flag.
    """

    def __init__(self, name, num_variables, name_variables, outputs):
        """
        Constructor de la clase BooleanFunction

        Parameters
        ----------
        name : string
            Nombre de la función booleana, es una cadena de caracteres que funciona como un identificador.
        num_variables : int
            Número de variables de la función booleana.
        name_variables : list
            Lista con los nombres de las variables de la función.
        outputs : list
            Lista que contiene 0s y 1s representando las salidas de la función booleana.
        """
        self.name = name
        if 2**num_variables == len(outputs) or (num_variables == 0 and not outputs) \
                or num_variables == len(name_variables):
            self.name_variables = name_variables
            self.num_variables = num_variables
            self.outputs = outputs
            self.monotone_flag = None
        else:
            raise Exception("Los outputs deberían corresponder con 2 elevado al número de variables.")

    def __str__(self):
        """Método para devolver un string que representa a nuestra función booleana cuando se llama a través de print().

        Returns
        -------
        string
            Cadena que representa a nuestra función en la llamada a print(),
            dando información sobre sus variables y salidas.
        """
        return "Función booleana con " + str(self.num_variables) + " variables y con " \
               + str(self.outputs) + " como salidas."

    def __repr__(self):
        """Método que devuelve la string que representa a nuestra función.

        Returns
        -------
        str
            Cadena que representa a nuestra función booleana.
        """
        return "Función booleana con " + str(self.num_variables) + " variables y con " \
               + str(self.outputs) + " como salidas."

    def __eq__(self, other):
        """
        Método para la comparación entre objetos de la misma clase.

        Returns
        ------
        boolean
            Booleano que representa si dos objetos de la misma clase son iguales.
        """
        if not isinstance(other, BooleanFunction):
            return NotImplemented
        return self.name == other.name

    def set_monotone_flag(self, flag):
        """Método setter para modificar el flag de monotonía que indica si la función booleana es o no monótona. Este
        flag es opcional y por defecto estará puesto en None, pero se le puede dar valor para ahorrar tiempo
        computacional. Como precondición se sobrentiende que el valor del flag será True si la función es monótona y
        False en caso contrario.

        Parameters
        ---------
        flag : bool
            Flag que indica si la función es o no monótona.
        """
        self.monotone_flag = flag

    def json_encode(self):
        """
        Método que codifica el objeto a un diccionario para su correcta serialización a JSON.

        Returns
        -------
        dict
            Diccionario que representa a la función booleana.
        """
        return {'id': self.name,
                'num_variables': self.num_variables,
                'name_variables': self.name_variables,
                'outputs': self.outputs,
                'm_flag': self.monotone_flag}
