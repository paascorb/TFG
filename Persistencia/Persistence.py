# Persistencia para SimplicialComplex hecho por Pablo Ascorbe 25/05/2022
import json
import os


def serialize(sc, filename=None):
    if filename is None:
        filename = sc.name

    with open('Almacen/' + filename + '.json', 'w') as f:
        json.dump(sc, f, default=lambda o: o.json_encode(), indent=4)


def deserialize(filename):
    return json.load('Almacen/' + filename + '.json')


def remove(filename):
    os.remove('Almacen/' + filename + '.json')
