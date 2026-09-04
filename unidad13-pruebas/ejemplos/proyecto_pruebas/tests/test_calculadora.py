"""Pruebas para las operaciones de calculadora."""

import pytest

from calculadora import dividir, sumar


def test_sumar_dos_numeros_positivos() -> None:
    assert sumar(2, 3) == 5


@pytest.mark.parametrize(
    ("numero_1", "numero_2", "esperado"),
    [
        (2, 3, 5),
        (-1, 1, 0),
        (0, 0, 0),
        (2.5, 1.5, 4.0),
    ],
)
def test_sumar_varios_casos(
    numero_1: float,
    numero_2: float,
    esperado: float,
) -> None:
    assert sumar(numero_1, numero_2) == esperado


def test_dividir_dos_numeros() -> None:
    assert dividir(10, 4) == 2.5


def test_dividir_por_cero_lanza_error() -> None:
    with pytest.raises(ValueError, match="divisor no puede ser cero"):
        dividir(10, 0)
