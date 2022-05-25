from ModeloDeDominio.Simplex import *
from ModeloDeDominio.SimplicialComplex import *
from ModeloDeDominio.BooleanFunction import *
from LogicaDeNegocio.Auxiliary import *
import json
from Persistencia import Persistence
from Persistencia import AuxiliaryParsing

s = Simplex('a', 0)
v = Simplex('b', 0)
w = Simplex('c', 0)
r = Simplex('e', 0)
t = Simplex('f', 0)
n = Simplex('g', 0)
sv = Simplex('ab', 1)
sw = Simplex('ac', 1)
vw = Simplex('bc', 1)
sr = Simplex('ae', 1)
rt = Simplex('ef', 1)
rn = Simplex('eg', 1)
svw = Simplex('abc', 2)

s.set_faces()
v.set_faces()
w.set_faces()
r.set_faces()
t.set_faces()
n.set_faces()
sv.set_faces({s, v})
sw.set_faces({s, w})
vw.set_faces({v, w})
sr.set_faces({s, r})
rt.set_faces({r, t})
rn.set_faces({r, n})
svw.set_faces({sv, sw, vw})

simplices = {s, v, w, r, t, sv, sw, vw, sr, rt, svw}
facets = {sr, svw}
sc = SimplicialComplex('sc_prueba', 10, simplices)
# sc_fac = SimplicialComplex(10, None, facets)
#
# print(sc.facets)
# print(sc.matrix)
# print(sc.c_vector)
# print(sc.euler_char)
# print(sc)
# print(sc_fac)
# print(sc_fac.simplex)
# try:
#     print(sc.collapse(r, sr))
# except Exception as ex:
#     print(ex.args)
# print(sc.collapse(t, rt))
# print(sc.can_expand(n, rn))
# print(sc.expand(n, rn))

# prueba_fb = BooleanFunction(3, [1, 1, 1, 1, 1, 1, 1, 1])
# print(prueba_fb)

# print(check_output(7))
# print(check_output(15))
# print(check_output(441135))
# print(list(range(1, 31)))

# print(is_monotone([1, 1, 1, 1, 1, 1, 1, 1]))
# print(is_monotone([0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0]))

# print(json.dumps(sc.__dict__))

# with open('Almacen/prueba1.json', 'w') as f:
#     print(json.dump(vw, f, default=lambda o: o.json_encode(), indent=4))

# with open('Almacen/prueba2.json', 'w') as f:
#     print(json.dump(sc, f, default=lambda o: o.json_encode(), indent=4))

# prueba_fb = BooleanFunction('fb_prueba', 3, [1, 1, 1, 1, 1, 1, 1, 1])
# print(json.dumps(prueba_fb, default=lambda o: o.json_encode(), indent=4))

# Persistencia.Persistence.serialize_sc(sc, 'pepito')
# Persistencia.Persistence.remove_sc('pepito')

data = open('Almacen/prueba1.json')
print(AuxiliaryParsing.simplex_decode(json.load(data)))

