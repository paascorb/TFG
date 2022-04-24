from ModeloDeDominio.Simplex import *
from ModeloDeDominio.SimplicialComplex import *

s = Simplex(0, 'a')
v = Simplex(0, 'b')
w = Simplex(0, 'c')
r = Simplex(0, 'e')
sv = Simplex(1, 'ab')
sw = Simplex(1, 'ac')
vw = Simplex(1, 'bc')
sr = Simplex(1, 'ae')
svw = Simplex(2, 'abc')

s.set_cofaces({})
v.set_cofaces({})
w.set_cofaces({})
r.set_cofaces({})
sv.set_cofaces({s, v})
sw.set_cofaces({s, w})
vw.set_cofaces({v, w})
sr.set_cofaces({s, r})
svw.set_cofaces({sv, sw, vw})

simplices = {s, v, w, r, sv, sw, vw, sr, svw}
facets = {sr, svw}
sc = SimplicialComplex(simplices)
sc_fac = SimplicialComplex(None, facets)

print(sc.facets)
print(sc.matrix)
print(sc.c_vector)
print(sc.euler_char)
print(sc)
print(sc_fac)
print(sc_fac.simplex)
