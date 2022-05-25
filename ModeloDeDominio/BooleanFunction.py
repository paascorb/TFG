# Clase SimplicialComplex.py desarrollada por Pablo Ascorbe Fernández 11/05/2022


class BooleanFunction:
    """
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
        else:
            raise Exception("Los outputs deberían corresponder con 2 elevado al número de variables.")

    def __str__(self):
        return "Función booleana con " + str(self.num_variables) + " variables y con " \
               + str(self.outputs) + " como salidas."

    def __repr__(self):
        return "Función booleana con " + str(self.num_variables) + " variables y con " \
               + str(self.outputs) + " como salidas."

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
                'outputs': self.outputs}
