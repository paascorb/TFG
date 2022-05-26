# Persistencia para SimplicialComplex hecho por Pablo Ascorbe 25/05/2022
import json
import os
# TODO: Documentarlo todo


def serialize(obj, filename=None):
    if filename is None:
        filename = obj.name
    project_root = os.path.dirname(os.path.dirname(__file__))
    with open(project_root + '/Almacen/' + filename + '.json', 'w') as f:
        json.dump(obj, f, default=lambda o: o.json_encode(), indent=4)


def deserialize(filename):
    project_root = os.path.dirname(os.path.dirname(__file__))
    with open(project_root + '/Almacen/' + filename + '.json') as f:
        return json.load(f)


def remove(filename):
    project_root = os.path.dirname(os.path.dirname(__file__))
    os.remove(project_root + '/Almacen/' + filename + '.json')
