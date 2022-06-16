# Fichero con clases auxiliares desarrollado por Pablo Ascorbe Fernández 12/05/2022
import numpy as np

"""
Métodos auxiliares para la clase SimplicialComplex:
"""


def is_simplicial_complex(simplex):
    """
    Método para calcular si un conjunto de símplices pueden conformar o no un complejo simplicial.
    Para ello, se comprueba que todos los símplices del conjunto tengan sus caras dentro del mismo.

    Además, que si la dimensión del símplice es 0 entonces su conjunto de caras es el conjunto vacío.
    Pero si la dimensión es superior a 0 entonces el número de caras debe ser igual a su dimensión más uno.

    Parameters
    ----------
    simplex : set
        Conjunto de símplices del que deseamos verificar si es o no válido para formar un complejo simplicial.

    Returns
    -------
    boolean
        Booleano que será True si el conjunto de símplices puede forma el complejo simplicial o False en caso contrario.
    """
    for elm in simplex:
        if elm.faces is None:
            return False
        elif elm.dimension > 0:
            for cara in elm.faces:
                if cara not in simplex or (elm.dimension - cara.dimension) != 1:
                    return False
        else:
            if not len(elm.faces) == 0:
                return False
    return True


def euler_characteristic(c_vector):
    """
    Método que calcula la característica de Euler a partir del c-vector proporcionado. Este cálculo se realiza sumando
    todas las posiciones pares del vector y restándole a esto las impares.

    Parameters
    ---------
    c_vector : list
        Vector de enteros que define el número de símplices agrupados por dimensión y ordenados de menor a mayor.

    Returns
    -------
    int
        Entero que representa la característica de Euler para el c-vector proporcionado.
    """
    dimension_par = c_vector[0::2]
    dimension_impar = c_vector[1::2]
    return np.sum(dimension_par) - np.sum(dimension_impar)


def simplex_to_facets(simplex, matrix):
    """
    Método para pasar del conjunto de símplices proporcionado a los facets. Para ello, necesitamos la matriz que
    representa las relaciones entre símplices, poniendo un 1 en sus caras y cocaras para hacerlo más eficientemente.
    Para ello, se calcula qué símplices, es decir su fila asociada en la matriz, no tiene unos más alla de su diagonal.
    Esto representa que no tiene cocaras asociadas, por tanto, no está contenido en ningún otro símplice. Significando
    que es un facet.

    Parameters
    ----------

    simplex : set
        Conjunto de símplices del que deseamos calcular sus facets.
    matrix : list
        Es una lista de listas, lo que representa una matriz de relaciones entre los símplices proporcionados.

    Returns
    -------
    set
        Conjunto de facets asociado al conjunto de símplices proporcionado por parámetros. Ordenado de menor a mayor
        dimensión y como segundo criterio el identificador.
    """
    facets = set()
    for elm in simplex:
        row = matrix[elm.index]
        es_facet = True
        for i in range(elm.index, len(simplex)):
            if elm.index != i and row[i] == 1:
                es_facet = False
        if es_facet:
            facets.add(elm)
    return sorted(facets, key=lambda x: (x.dimension, x.name))


def facets_to_simplex(facets, simplex=None):
    """
    Método para calcular el conjunto de símplices de un complejo simplicial dado su conjunto de facets.
    Este es un método recursivo, la intención es ir, para cada facet, calculando sus caras y añadiéndolas a la lista de
    símplices, y asi recursivamente profundizando en cada cara hasta llegar a los 0-símplices.

    Parameters
    ----------

    facets : set
        Conjunto de facets necesario para calcular la lista entera de símplices asociados.
    simplex : set
        Conjunto de símplices "recolectados" por el momento.

    Returns
    -------
    set
        Conjunto de todos los símplices "recolectados" de los facets proporcionados por parámetros. No están ordenados
        por dimensión ni identificador, por lo tanto, será necesario ordenarlos posteriormente.
    """
    if simplex is None:
        simplex = set()
    simplex = set.union(simplex, facets)
    for elm in facets:
        simplex = facets_to_simplex(elm.faces, simplex)
    return simplex


def fmatrix_and_cvector(simplex, dimension):
    """
    Método que calcula la matriz de caras, cocaras (fmatrix) y el c-vector (cvector) de un conjunto de símplices.
    Cada símplice ocupa una posición en el conjunto proporcionado.
    Por ello, esa posición será la misma en la matriz creada.

    Siendo, por ejemplo, la fila 3 la que corresponda al símplice que ocupe la posición 3 en el conjunto.
    La matriz resultado tendrá unos o ceros a la izquierda de la diagonal representando sus caras y a la derecha
    sus cocaras. Además, en el proceso se irá calculando el c-vector asociado.

    Parameters
    ----------
    simplex : set
        Conjunto de símplices. Como precondición se espera que estén ordenados por dimensión e indexados para facilitar
        la tarea de generar la matriz.
    dimension: int
        Es la dimensión máxima del conjunto de símplices, esta nos delimitará el tamaño del c-vector.

    Returns
    -------
    tuple
        Tupla que tiene en la primera posición la lista de listas que representa la matriz de caras y cocaras y en la
        segunda posición la lista de enteros que representa el c-vector.
    """
    matrix = []
    c_vector = [0] * (dimension + 1)
    current_dimension = 0
    for elm in simplex:
        if current_dimension < elm.dimension:
            current_dimension += 1
        c_vector[current_dimension] += 1
        row = [0] * len(simplex)
        row[elm.index] = 1
        for caras in elm.faces:
            row[caras.index] = 1
        matrix.append(row)
    matrix_traspuesta = np.transpose(matrix)
    matrix = matrix + matrix_traspuesta - np.identity(len(simplex))
    return matrix, c_vector


def order_and_index(simplex):
    """
    Método que ordena por dimensión y por segundo criterio nombre e indexa poniendo como índice la posición que ocupa,
    dado ese orden, dentro del set.

    Parameters
    ----------

    simplex : set
        Conjunto de símplices que necesitamos ordenar por dimensión y nombre e indexar.

    Returns
    -------
    set
        Conjunto que contiene los mismos símplices que el conjunto proporcionado pero ordenados e indexados.
    """
    simplex = sorted(simplex, key=lambda x: (x.dimension, x.name))
    for elm, i in zip(simplex, range(0, len(simplex))):
        elm.set_index(i)
    return simplex


def dimension_from_simplex(simplex):
    """
    Método que saca la dimensión del último símplice de la lista. Es por ello, que para sacar la dimensión de la lista
    de símplices es necesario que esté ordenada por dimensión.

    Parameters
    ----------
    simplex : set
        Lista de símplices que como precondición se espera que esté ordenada por dimensión.

    Returns
    -------
    int
        Entero que representa la dimensión del último símplice de la lista proporcionada.
    """
    return list(simplex)[len(simplex) - 1].dimension


"""
Métodos auxiliares para la clase BooleanFunction
"""


def is_monotone(outputs):
    """
    TODO: Documentarlo
    :param outputs:
    :return:
    """

    aux_outputs = outputs.copy()
    outputs_checked = list()
    for i in reversed(range(0, len(outputs))):
        if aux_outputs[i] == 1:
            outputs_checked = check_output(i, outputs_checked)
            for elem in outputs_checked:
                if outputs[elem] == 0:
                    return False
                else:
                    aux_outputs[elem] = -1
            aux_outputs[i] = -1
    return True


def check_output(num, result=None):
    """
    Este método calcula los hijos del número pasado por parámetros. Esto en el contexto de las funciones booleanas
    monótonas tiene que ver con el número de 1s y 0s que encontramos.

    Un ejemplo que se ve muy fácil es el siguiente:

    El 7 en binario es el 111, si por cada uno, sustituimos de derecha a izquierda un uno por un cero tenemos 3 hijos:
    El 6 110, el 5 101 y el 3 011. Si seguimos con esta idea los hijos de 3 serían el 2 y el 1.
    Por tanto, todos los hijos de 7 son el conjunto: 6, 5, 4, 3, 2, 1.

    Parameters
    ----------
    num : int
        Número en decimal positivo sobre el que calcularemos sus "hijos"
    result : list
         Parámetro opcional, es una lista que sirve como referencia para el cálculo de los hijos del número pasado por
         parámetros de forma recursiva. De esa manera se puede llevar la cuenta de los hijos ya calculados.

    Returns
    -------
    list
        Lista que contiene todos los hijos de cualquier dimensión del número pasado por parámetros.

    """
    if result is None:
        result = list()
    bin_num = bin(num)[2:]
    num_ones = bin_num.count('1')
    if len(bin_num) == num_ones:
        return list(range(1, (2 ** num_ones) - 1))
    pos_num = 0
    for i in range(1, num_ones + 1):
        aux_copy = bin_num
        for elem in aux_copy[pos_num:]:
            if elem == '1':
                aux_copy = aux_copy[:pos_num] + '0' + aux_copy[pos_num + 1:]
                pos_num += 1
                break
            pos_num += 1
        child = int(aux_copy, 2)
        if child not in result:
            if num_ones > 2:
                result = check_output(child, result)
            result.append(child)
    return result


def num_1(num):
    """
    TODO: documentarlo
    :param num:
    :return:
    """
    return bin(num)[2:].count('1')


"""
Métodos auxiliares para la clase VectorField
"""


def trocear_fmatrix(fmatrix, c_vector):
    """
    TODO
    :param fmatrix:
    :param c_vector:
    :return:
    """
    fblocks = list()
    aux_matrix = np.array(fmatrix)
    for i in range(0, len(c_vector)-1):
        aux_matrix = aux_matrix[:, c_vector[i]:]
        fblock = aux_matrix[:c_vector[i], :c_vector[i+1]]
        aux_matrix = aux_matrix[c_vector[i]:, :]
        fblocks.append(fblock)
    return  fblocks


