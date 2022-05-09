# Clase Simplex.py desarrollada por Pablo Ascorbe Fernández 16/04/2022
class Simplex:

    # Constructor de la clase Simplex, tiene 2 atributos: la dimensión del simplice y su nombre a modo de identificador.
    # Los otros 2: el índice y sus caras no son intrínsecamente del símplice pero sí que corresponden a este en el
    # contexto de complejo simplicial. Es por ello que me ha parecido interesante añadirlos para poder trabajar con
    # ellos en el contexto en el que lo haremos que serán los complejos simpliciales. Aunque sea de forma opcional.
    def __init__(self, dimension, name):
        self.dimension = dimension
        self.name = name
        self.index = None
        self.faces = None

    # Método para devolver un string que representa a nuestro símplice cuando se llama atraves de print().
    def __str__(self):
        return "Dimensión del simplice: "+str(self.dimension)+", nombre: "+str(self.name)

    # Método que devuelve la string que representa a nuestro símplice.
    def __repr__(self):
        return "Simplice: "+str(self.name)

    # Método set para modificar el atributo index que hace referencia al índice del simplice cuando esté contenido en un
    # complejo simplicial
    def set_index(self, index):
        self.index = index

    # Método para modificar el atributo faces del simplica añadiendo las relaciones que tiene dentro del complejo
    # Simplicial
    def set_faces(self, faces):
        self.faces = faces
