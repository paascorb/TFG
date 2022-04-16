from ModeloDeDominio.Simplex import *

s = Simplex(0, 'a', {})
v = Simplex(0, 'b', {})
sv = Simplex(1, 'ab', {s, v})
print(str(sv))

