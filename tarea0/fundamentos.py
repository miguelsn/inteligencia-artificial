import collections
import math
from typing import Any, DefaultDict, List, Set, Tuple

############################################################
# Tipos personalizados
# NOTA: No necesitas modificar estos.

"""
Puedes pensar en las llaves del defaultdict como posiciones en el
vector disperso, mientras que los valores representan los elementos en
esas posiciones.

Cualquier llave omitida del diccionario significa que ese elemento es
cero.

Ten en cuenta que el tipo de la llave utilizado no debe afectar el
algoritmo.
"""
SparseVector = DefaultDict[Any, float]
Position = Tuple[int, int]


############################################################
# Problema 3a


def find_alphabetically_first_word(text: str) -> str:
    """
    Dada una cadena |text|, regresa la palabra en |text| que aparece
    primero en orden lexicográfico creciente.

    Una palabra se define por una secuencia maximal de caracteres sin
    espacios en blanco.

    La función max() puede ser de utilidad. Si el texto de entrada es
    una cadena vacía, es aceptable regresar la cadena vacía o señalar
    un error.
    """
    # Inicio de tu código
    if text == "":
        return 0
    text = text.split()
        
    return min(text)
    # Fin de tu código


############################################################
# Problema 3b


def euclidean_distance(loc1: Position, loc2: Position) -> float:
    """
    Regresa la distancia Euclidiana entre dos posiciones, donde las
    posiciones son pares de números (p.ej. (3,5)).
    """
    # Inicio de tu código
    sq1 = pow((loc2[0]-loc1[0]), 2)
    sq2 = pow((loc2[1]-loc1[1]), 2)
    return pow(sq1+sq2, 0.5)
    # Fin de tu código


############################################################
# Problema 3c


def mutate_sentences(sentence: str) -> List[str]:
    """
    Dada una oración (secuencia de palabras), regresa una lista de
    todas las oraciones "similares".

    Definimos que una oración es "similar" a la oración original si:
    - tiene la misma cantidad de palabras, y
    - cada pareja de palabras adyacentes en la nueva oración también
    aparece en la oración original (las palabras dentro de cada pareja
    deben aparecer en el mismo orden en la oración de salida que en la
    oración original).

    Notas:
    - El orden de las oraciones en el resultado no importa.
    - No debes regresar oraciones duplicadas.
    - La oración que generes puede usar una palabra en la oración
      original más de una vez.

    Ejemplo:
    - Entrada: 'el gato y el ratón'
    - Salida: ['y el gato y el', 'el gato y el ratón',
               'el gato y el gato', gato y el gato y',]
    """
    # Inicio de tu código
    raise Exception("Aún no implementada")
    # Fin de tu código


############################################################
# Problema 3d


def sparse_vector_dot_product(v1: SparseVector, v2: SparseVector) -> float:
    """
    Dados dos vectores dispersos (vectores donde la mayoría de los
    elementos son cero) |v1| y |v2|, cada uno representado como
    collections.defaultdict(float), regresa su producto punto.

    Puede que te resulte útil utilizar sum() y una comprensión de
    lista.

    Esta función será utilizada posteriormente para clasificadores
    lineales.
    """
    # Inicio de tu código
    raise Exception("Aún no implementada")
    # Fin de tu código


############################################################
# Problema 3e


def increment_sparse_vector(
    v1: SparseVector,
    scale: float,
    v2: SparseVector,
) -> None:
    """
    Dados dos vectores dispersos |v1| y |v2|, realiza el cálculo:
    v1 += scale * v2.

    Si el valor de scale es cero, puedes modificar v1 para incluir
    cualesquiera llaves adicionales en v2, o simplemente no agregar
    nuevas llaves.

    Nota: Esta función debe MODIFICAR los elementos de v1, pero no
    regresarlo. No modifiques v2 en tu implementación.

    Esta función será de utilidad más adelante.
    """
    # Inicio de tu código
    raise Exception("Aún no implementada")
    # Fin de tu código


############################################################
# Problema 3f


def find_nonsingleton_words(text: str) -> Set[str]:
    """
    Divide la cadena |text| por espacios en blanco y regresa el
    conjunto de palabras que aparecen más de una vez.

    Puede que collections.defaultdict(int) te sea de utilidad.
    """
    # Inicio de tu código
    raise Exception("Aún no implementada")
    # Fin de tu código
