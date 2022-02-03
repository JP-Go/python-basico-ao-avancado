"""
Um módulo exemplo de documentação

Descrição longa do módulo
"""


def soma(x: int | float, y: int | float) -> int | float:
    """Descrição curta da função soma

    :param x,y: dois números quaisquer
    :type x,y: int or float

    :return: x+y
    :rtype: int or float

    :raises ValueError: Se x ou y não são inteiros ou floats

    Uma descrição longa da função soma que soma dois números. Podemos definir
    os tipos dos parâmetros
    """
    if not isinstance(x, int or float):
        raise ValueError("First param must be int or float")
    if not isinstance(y, int or float):
        raise ValueError("Second param must be int or float")

    return x + y
