"""Pruebas para el modelo de estudiantes."""

import pytest

from estudiantes import Estudiante


@pytest.fixture
def estudiante_con_notas() -> Estudiante:
    return Estudiante("Ana", [4.0, 3.5, 4.5])


def test_crear_estudiante_sin_notas() -> None:
    estudiante = Estudiante("Luis")

    assert estudiante.nombre == "Luis"
    assert estudiante.notas == []


def test_cada_estudiante_recibe_una_lista_independiente() -> None:
    estudiante_1 = Estudiante("Ana")
    estudiante_2 = Estudiante("Luis")

    estudiante_1.agregar_nota(4.5)

    assert estudiante_2.notas == []


def test_agregar_nota_valida() -> None:
    estudiante = Estudiante("Ana")

    estudiante.agregar_nota(4.5)

    assert estudiante.notas == [4.5]


@pytest.mark.parametrize("nota", [-0.1, 5.1])
def test_agregar_nota_invalida_lanza_error(nota: float) -> None:
    estudiante = Estudiante("Ana")

    with pytest.raises(ValueError, match="entre 0.0 y 5.0"):
        estudiante.agregar_nota(nota)


@pytest.mark.parametrize("nota", [0.0, 5.0])
def test_agregar_notas_limite(nota: float) -> None:
    estudiante = Estudiante("Ana")

    estudiante.agregar_nota(nota)

    assert estudiante.notas == [nota]


def test_calcular_promedio(estudiante_con_notas: Estudiante) -> None:
    assert estudiante_con_notas.calcular_promedio() == 4.0


def test_calcular_promedio_sin_notas_lanza_error() -> None:
    estudiante = Estudiante("Ana")

    with pytest.raises(ValueError, match="No hay notas"):
        estudiante.calcular_promedio()


def test_nombre_vacio_lanza_error() -> None:
    with pytest.raises(ValueError, match="nombre no puede estar vacío"):
        Estudiante("   ")
