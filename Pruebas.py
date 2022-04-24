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

s.set_faces({})
v.set_faces({})
w.set_faces({})
r.set_faces({})
sv.set_faces({s, v})
sw.set_faces({s, w})
vw.set_faces({v, w})
sr.set_faces({s, r})
svw.set_faces({sv, sw, vw})

simplices = {s, v, w, r, sv, sw, vw, sr, svw}
facets = {sr, svw}
sc = SimplicialComplex(10, simplices)
sc_fac = SimplicialComplex(10, None, facets)

print(sc.facets)
print(sc.matrix)
print(sc.c_vector)
print(sc.euler_char)
print(sc)
print(sc_fac)
print(sc_fac.simplex)
print(sc.collapse(r, sr))
print(sc.collapse(sv, svw))
print(sc.collapse(s, sw))
print(sc.collapse(w, vw))
