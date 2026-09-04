"""Operaciones aritméticas sencillas para practicar pruebas."""


def sumar(numero_1: float, numero_2: float) -> float:
    """Devuelve la suma de dos números."""
    return numero_1 + numero_2


def dividir(dividendo: float, divisor: float) -> float:
    """Devuelve el cociente y rechaza un divisor igual a cero."""
    if divisor == 0:
        raise ValueError("El divisor no puede ser cero")
    return dividendo / divisor
