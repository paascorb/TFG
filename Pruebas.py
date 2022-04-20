from ModeloDeDominio.Simplex import *
from ModeloDeDominio.SimplicialComplex import *

s = Simplex(0, 'a', {})
v = Simplex(0, 'b', {})
w = Simplex(0, 'c', {})
r = Simplex(0, 'e', {})
sv = Simplex(1, 'ab', {s, v})
sw = Simplex(1, 'ac', {s, w})
vw = Simplex(1, 'bc', {v, w})
sr = Simplex(1, 'ae', {s, r})
svw = Simplex(2, 'abc', {sv, sw, vw})

simplices = {s, v, w, r, sv, sw, vw, sr, svw}
facets = {sr, svw}
sc = SimplicialComplex(simplices)
sc_fac = SimplicialComplex(None, facets)

print(sc_fac.simplex)
print(sc.facets)
print(sc.matrix)
print(sc.c_vector)
print(sc.euler_char)
print(sc)
print(sc_fac)
