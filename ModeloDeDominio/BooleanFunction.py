# Clase SimplicialComplex.py desarrollada por Pablo Ascorbe Fernández 11/05/2022


class BooleanFunction:
    """
    Clase BooleanFunction que modela una función booleana. En nuestro caso, que trabajamos en un contexto de complejos
    simpliciales, nos interesarán aquellas que sean monótonas.

    Attributes
    ----------

    """
    # Contructor de la clase BooleanFunction.
    def __init__(self, num_variables, outputs):
        if 2**num_variables == outputs:
            self.num_variables = num_variables
            self.outputs = outputs
        else:
            raise Exception("El outputs debería corresponder con 2 elevado al número de variables.")
