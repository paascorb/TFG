# Clase Simplex.py desarrollada por Pablo Ascorbe Fernández 16/04/2022

class Simplex:
    """
    Clase Simplex que modela el concepto de símplice, que se corresponde con la cláusula convexa de n+1 puntos
    donde n es la dimensión del mismo. Necesario para componer nuestra clase SimplicialComplex.

    Attributes
    ----------
    dimension: int
        Dimensión del símplice, es un número natural con el 0 incluido.
    name : string
        Nombre del símplice, es una cadena de caracteres que funciona como un identificador.
    index : int
        Índice del símplice dentro de un complejo simplicial, por ello este parámetro es opcional y será asignado dentro
        de un complejo simplicial.
    faces : set
        Conjunto de símplices que definen sus caras, este atributo también es opcional y solo tiene sentido en el
        contexto de un complejo simplicial para definir sus relaciones en el mismo.

    Methods
    -------
    set_index(index)
        Método setter para modificar el atributo index que hace referencia al índice del símplice cuando esté contenido
        en un complejo simplicial.
    set_faces(faces)
        Método para modificar el atributo faces del símplice añadiendo las relaciones que tiene
        dentro del complejo simplicial.

    Examples
    --------
    >>> simplice_a  = Simplex(0, 'a')

    Crearía un símplice de dimensión 0 y nombre o identificador 'a'.

    >>> simplice_b = Simplex(0, 'b')
    >>> simplice_ab = Simplex(1, 'ab')

    Ahora tendríamos 3 símplices: 2 de dimensión 0, es decir dos puntos; 1 de dimensión 1. Pero ahora queremos definir
    que el 1-símplice está compuesto por nuestros dos puntos 'a' y 'b', para ello:

    >>> simplice_ab.set_faces({simplice_a, simplice_b})

    De esta manera le hemos asignado a nuestro simplice de dimensión 1 sus dos caras: los dos simplices 'a' y 'b'.
    """
    def __init__(self, dimension, name):
        """
        Constructor de la clase Simplex.

        Parameters
        ----
        dimension : int
            Dimensión del símplice, es un número natural con el 0 incluido.
        name : string
            Nombre del símplice, es una cadena de caracteres que funciona como un identificador.
        """

        self.dimension = dimension
        self.name = name
        self.index = None
        self.faces = None

    def __str__(self):
        """Método para devolver un string que representa a nuestro símplice cuando se llama a través de print().

        Returns
        -------
        string
            Cadena que representa a nuestro símplice en la llamada a print(),
            dando información sobre su dimensión y nombre.
        """
        return "Dimensión del simplice: "+str(self.dimension)+", nombre: "+str(self.name)

    def __repr__(self):
        """Método que devuelve la string que representa a nuestro símplice.

        Returns
        -------
        basestring
            Cadena que representa a nuestro símplice.
        """
        return "Simplice: "+str(self.name)

    def set_index(self, index):
        """Método setter para modificar el atributo index que hace referencia al índice del símplice cuando
        esté contenido en un complejo simplicial.

        Parameters
        ---------
        index : int
            Atributo opcional que representa el índice del simplice en el complejo simplicial.
        """
        self.index = index

    def set_faces(self, faces):
        """Método para modificar el atributo faces del símplice añadiendo las relaciones que tiene
        dentro del complejo simplicial.

        Parameters
        --------
        faces : set
            Conjunto de caras del símplice, definiendo sus relaciones de composición dentro del complejo simplicial.

        Raises
        -----
        Exception
            Si el conjunto de caras proporcionado no es correcto para el número de caras que debería tener por su
            dimensión

        Examples
        -------

        Si la dimensión del símplice es 0 no debería tener caras, por ello simplemente crearíamos un set vacío

        >>> 0_simplice.set_faces(set())

        Si la dimensión es 1 debería tener 1 + 1 caras

        >>> 1_simplice.set_faces({0_simplice_a, 0_simplice_b})

        Y si es 2 debería tener 3 (2 + 1)

        >>> 2_simplice.set_faces({1_simplice_a, 1_simplice_b, 1_simplice_c})

        y así sucesivamente hasta dimensiones superiores.

        """
        if self.dimension == 0 and len(faces) != self.dimension:
            raise Exception("El número de caras es incorrecto para la dimensión del símplice")
        elif self.dimension != 0 and (self.dimension + 1) != len(faces):
            raise Exception("El número de caras es incorrecto para la dimensión del símplice")
        else:
            self.faces = faces
