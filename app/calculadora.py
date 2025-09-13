"""
Modulo de operaciones aritméticas básicas. Una Calculadora.

Contiene funciones para sumar, restar, multiplicar y dividir numeros.
"""

def sumar(a, b):
    """
    Calcula la suma de dos numeros.

    Args:
        a (int): Primer numero.
        b (int): Segundo numero.

    Returns:
        int: La suma entre a y b.
    """
    return a + b


def restar(a, b):
    """
    Calcula la resta de dos numeros.

    Args:
        a (int): Primer numero.
        b (int): Segundo numero.

    Returns:
        int: La resta entre a y b.
    """
    return a - b


def multiplicar(a, b):
    """
    Calcula la multiplicacion de dos numeros.

    Args:
        a (int): Primer numero.
        b (int): Segundo numero.

    Returns:
        int: La multiplacion entre a y b.
    """
    return a * b


def dividir(a, b):
    """
    Calcula la division de dos numeros.

    Args:
        a (int): Primer numero.
        b (int): Segundo numero.

    Returns:
        int: La division entre a y b.
    """
    if b == 0:
        raise ZeroDivisionError("No se puede dividir por cero")
    return a / b
