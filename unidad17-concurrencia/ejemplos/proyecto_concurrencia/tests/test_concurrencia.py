"""Pruebas rápidas y deterministas de las demostraciones."""

import asyncio

import pytest

from asyncio_demo import ejecutar_varias, procesar_tarea, tarea_con_error
from multiprocessing_demo import ejecutar_secuencial, sumar_cuadrados
from threading_demo import ejecutar_con_threads
from threading_demo import procesar_tarea as procesar_tarea_thread


def test_funcion_usada_por_threading() -> None:
    assert procesar_tarea_thread("informe", espera=0) == "informe completada"


def test_thread_pool_conserva_resultados() -> None:
    resultados = ejecutar_con_threads(["uno", "dos", "tres"])
    assert resultados == ["uno completada", "dos completada", "tres completada"]


def test_funcion_cpu_pura() -> None:
    assert sumar_cuadrados(4) == 14


def test_version_cpu_secuencial() -> None:
    assert ejecutar_secuencial([3, 4]) == [5, 14]


def test_coroutine_devuelve_resultado() -> None:
    resultado = asyncio.run(procesar_tarea("informe", espera=0))
    assert resultado == "informe completada"


def test_gather_conserva_orden_de_resultados() -> None:
    resultados = asyncio.run(ejecutar_varias(["uno", "dos", "tres"]))
    assert resultados == ["uno completada", "dos completada", "tres completada"]


def test_error_async_se_propaga() -> None:
    with pytest.raises(ValueError, match="simulado"):
        asyncio.run(tarea_con_error())
