# Persistencia para SimplicialComplex hecho por Pablo Ascorbe 25/05/2022
import json
import os
# TODO: Documentarlo todo


def serialize(obj, table):
    project_root = os.path.dirname(os.path.dirname(__file__))
    with open(project_root + '/Almacen/' + table + "/" + obj.name + '.json', 'w') as f:
        json.dump(obj, f, default=lambda o: o.json_encode(), indent=4)


def deserialize(obj, table):
    project_root = os.path.dirname(os.path.dirname(__file__))
    with open(project_root + '/Almacen/' + table + "/" + obj.name + '.json') as f:
        return json.load(f)


def remove(obj, table):
    project_root = os.path.dirname(os.path.dirname(__file__))
    os.remove(project_root + '/Almacen/' + table + "/" + obj.name + '.json')


def deserialize_all(table):
    project_root = os.path.dirname(os.path.dirname(__file__))
    path = project_root + '/Almacen/' + table
    all_files = [f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))]
    object_deserialize = list()
    for file in all_files:
        with open(path + "/" + file) as f:
            object_deserialize.append(json.load(f))
    return object_deserialize
