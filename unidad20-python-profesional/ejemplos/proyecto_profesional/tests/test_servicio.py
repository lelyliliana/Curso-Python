from pathlib import Path

import pytest

from gestor_tareas.config import Config, cargar_config
from gestor_tareas.logging_config import configurar_logging
from gestor_tareas.modelos import Tarea
from gestor_tareas.servicio import ServicioTareas, TareaNoEncontradaError


def test_crear_tarea_normaliza_titulo_y_genera_id() -> None:
    servicio = ServicioTareas()

    tarea = servicio.crear("  Escribir documentación  ")

    assert tarea == Tarea(id=1, titulo="Escribir documentación")


def test_crear_varias_tareas_genera_ids_consecutivos() -> None:
    servicio = ServicioTareas()

    primera = servicio.crear("Primera")
    segunda = servicio.crear("Segunda")

    assert (primera.id, segunda.id) == (1, 2)


def test_listar_devuelve_tareas_en_orden() -> None:
    servicio = ServicioTareas()
    primera = servicio.crear("Primera")
    segunda = servicio.crear("Segunda")

    resultado = servicio.listar()

    assert resultado == (primera, segunda)


def test_buscar_devuelve_tarea_existente() -> None:
    servicio = ServicioTareas([Tarea(id=7, titulo="Revisar pruebas")])

    resultado = servicio.buscar(7)

    assert resultado.titulo == "Revisar pruebas"


def test_completar_actualiza_estado() -> None:
    servicio = ServicioTareas()
    tarea = servicio.crear("Ejecutar pruebas")

    resultado = servicio.completar(tarea.id)

    assert resultado.completada is True
    assert servicio.buscar(tarea.id).completada is True


def test_buscar_tarea_inexistente_lanza_error_de_dominio() -> None:
    servicio = ServicioTareas()

    with pytest.raises(TareaNoEncontradaError, match="id 99"):
        servicio.buscar(99)


@pytest.mark.parametrize("titulo", ["", "   ", "\t"])
def test_rechazar_titulo_vacio(titulo: str) -> None:
    servicio = ServicioTareas()

    with pytest.raises(ValueError, match="título"):
        servicio.crear(titulo)


def test_instancias_mantienen_estado_independiente() -> None:
    primer_servicio = ServicioTareas()
    segundo_servicio = ServicioTareas()

    primer_servicio.crear("Solo en el primero")

    assert len(primer_servicio.listar()) == 1
    assert segundo_servicio.listar() == ()


def test_cargar_config_usa_valores_predeterminados(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    monkeypatch.delenv("APP_LOG_LEVEL", raising=False)
    monkeypatch.delenv("APP_DATA_DIR", raising=False)

    resultado = cargar_config()

    assert resultado == Config(log_level="INFO", data_dir=Path("data"))


def test_cargar_config_lee_y_normaliza_entorno(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    monkeypatch.setenv("APP_LOG_LEVEL", " debug ")
    monkeypatch.setenv("APP_DATA_DIR", "datos/pruebas")

    resultado = cargar_config()

    assert resultado.log_level == "DEBUG"
    assert resultado.data_dir == Path("datos/pruebas")


def test_cargar_config_rechaza_nivel_invalido(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    monkeypatch.setenv("APP_LOG_LEVEL", "DETALLADO")

    with pytest.raises(ValueError, match="APP_LOG_LEVEL"):
        cargar_config()


def test_configurar_logging_rechaza_nivel_invalido() -> None:
    with pytest.raises(ValueError, match="inválido"):
        configurar_logging("VERBOSE")
