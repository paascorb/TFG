from simplicial import SimplicialComplex
from Presentacion.Hasse import *


prueba = SimplicialComplex()

prueba.addSimplex(id='a')
prueba.addSimplex(id='b')
prueba.addSimplex(id='c')
prueba.addSimplex(id='d')
prueba.addSimplex(id='e')
prueba.addSimplex(id='f')

prueba.addSimplex(fs=['a', 'b'], id='ab')
prueba.addSimplex(fs=['a', 'c'], id='ac')
prueba.addSimplex(fs=['b', 'c'], id='bc')
prueba.addSimplex(fs=['d', 'c'], id='dc')
prueba.addSimplex(fs=['e', 'd'], id='de')
prueba.addSimplex(fs=['f', 'e'], id='ef')

prueba.addSimplex(fs=['ab', 'ac', 'bc'], id='abc')

# prueba.addSimplex(id='a', attr={'num': 0})
# prueba.addSimplex(id='b', attr={'num': 1})
# prueba.addSimplex(id='c', attr={'num': 2})
# prueba.addSimplex(id='d', attr={'num': 3})
# prueba.addSimplex(id='e', attr={'num': 4})
# prueba.addSimplex(id='f', attr={'num': 5})
#
# prueba.addSimplex(fs=['a', 'b'], id='ab', attr={'num': 6})
# prueba.addSimplex(fs=['a', 'c'], id='ac', attr={'num': 7})
# prueba.addSimplex(fs=['b', 'c'], id='bc', attr={'num': 8})
# prueba.addSimplex(fs=['d', 'c'], id='dc', attr={'num': 9})
# prueba.addSimplex(fs=['e', 'd'], id='de', attr={'num': 10})
# prueba.addSimplex(fs=['f', 'e'], id='ef', attr={'num': 11})
#
# prueba.addSimplex(fs=['ab', 'ac', 'bc'], id='abc', attr={'num': 12})

mostrar_diagrama_hasse(prueba)
