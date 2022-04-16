# Clase Simplex.py desarrollada por Pablo Ascorbe Fernández 16/04/2022
class Simplex:

    # Constructor de la clase Simplex, tiene 3 atributos: la dimensión del simplice, si nombre a modo de identificador,
    # y el atributo cofaces que es una lista de las cocaras del simplice.
    def __init__(self, dimension, name, cofaces):
        self.dimension = dimension
        self.name = name
        self.cofaces = cofaces

    def __str__(self):
        return "Dimensión del simplice: "+str(self.dimension)+", nombre: "+str(self.name)+", cocaras: "\
               + str(set(str(elm) for elm in self.cofaces))
