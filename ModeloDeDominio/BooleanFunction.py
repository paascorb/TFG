# Clase SimplicialComplex.py desarrollada por Pablo Ascorbe Fernández 11/05/2022


class BooleanFunction:
    """
    TODO
    Clase BooleanFunction que modela una función booleana. En nuestro caso, que trabajamos en un contexto de complejos
    simpliciales, nos interesarán aquellas que sean monótonas.

    Attributes
    ----------
    """
    # Contructor de la clase BooleanFunction.
    def __init__(self, name, num_variables, outputs):
        self.name = name
        if 2**num_variables == len(outputs):
            self.num_variables = num_variables
            self.outputs = outputs
            self.monotone_flag = None
        else:
            raise Exception("Los outputs deberían corresponder con 2 elevado al número de variables.")

    def __str__(self):
        return "Función booleana con " + str(self.num_variables) + " variables y con " \
               + str(self.outputs) + " como salidas."

    def __repr__(self):
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
        computacional.

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
                'outputs': self.outputs,
                'm_flag': self.monotone_flag}
