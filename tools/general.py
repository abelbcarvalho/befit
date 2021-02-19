# Esse arquivo possui funções para testes gerais


def instance(objeto=object, classe=None) -> bool:
    """Testa a instancia.

    Args:
        objeto (optional): instancia. Defaults to object.
        classe (optional): classe. Defaults to None.

    Returns:
        bool: True se a instancia procede.
    """
    return isinstance(objeto, classe)


def is_none_empty(word='') -> bool:
    """Testa se uma string é None ou Vazia.

    Args:
        word (str, optional): palavra/frase. Defaults to ''.

    Returns:
        bool: True if it is None or Empty.
    """
    return not word or word.__len__() < 1


def is_small_equal(word='', size=25) -> bool:
    """Verifica se o tamanho de uma string é
    menor ou igual a algum inteiro enviado.

    Args:
        word (str, optional): a string. Defaults to ''.
        size (int, optional): o tamanho. Defaults to 25.

    Returns:
        bool: True se o tamanho de word é menor ou igual
        a size.
    """
    return word.__len__() <= size


def tira_espacos_inicio_final(word='') -> str:
    """Tira os espaços do final e do inicio de uma string.
    Exemplo:
    '    str    '
    Se torna:
    'str'

    Args:
        word (str, optional): palavra a ser mudada. Defaults to ''.

    Returns:
        str: sem espaços no final e no inicio
    """
    return word.strip() if is_none_empty(word=word) else None


def is_float_positive(point=0.0) -> bool:
    """Testa se um numero float é maior que 0.

    Args:
        point (float, optional): valor float. Defaults to 0.0.

    Returns:
        bool: True se point > 0.0.
    """
    return point > 0.00


def is_int_positive(inter=0) -> bool:
    """Verifica se um inteiro é positivo.

    Args:
        inter (int, optional): número inteiro. Defaults to 0.

    Returns:
        bool: True se inter > 0.
    """
    return inter > 0
