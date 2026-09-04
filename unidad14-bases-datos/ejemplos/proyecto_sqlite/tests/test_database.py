"""Pruebas del proyecto SQLite con una base temporal por prueba."""

import sqlite3
from contextlib import closing
from pathlib import Path

import pytest

from database import (
    actualizar_estudiante,
    buscar_estudiante_por_id,
    crear_estudiante,
    eliminar_estudiante,
    inicializar_db,
    listar_estudiantes,
    obtener_conexion,
)
from estudiantes import Estudiante


@pytest.fixture
def ruta_db(tmp_path: Path) -> Path:
    ruta = tmp_path / "test.db"
    inicializar_db(ruta)
    return ruta


def test_inicializar_db_crea_tabla(tmp_path: Path) -> None:
    ruta = tmp_path / "inicializacion.db"

    inicializar_db(ruta)

    with closing(sqlite3.connect(ruta)) as conexion:
        fila = conexion.execute(
            "SELECT name FROM sqlite_master WHERE type = ? AND name = ?",
            ("table", "estudiantes"),
        ).fetchone()
    assert fila == ("estudiantes",)


def test_crear_estudiante_asigna_id(ruta_db: Path) -> None:
    creado = crear_estudiante(
        ruta_db,
        Estudiante(None, "Ana", 20, "Ingeniería"),
    )

    assert creado.id == 1


def test_listar_estudiantes_ordenados(ruta_db: Path) -> None:
    crear_estudiante(ruta_db, Estudiante(None, "Luis", 22, "Sistemas"))
    crear_estudiante(ruta_db, Estudiante(None, "Ana", 20, "Ingeniería"))

    estudiantes = listar_estudiantes(ruta_db)

    assert [estudiante.nombre for estudiante in estudiantes] == ["Ana", "Luis"]


def test_buscar_estudiante_existente(ruta_db: Path) -> None:
    creado = crear_estudiante(
        ruta_db,
        Estudiante(None, "Ana", 20, "Ingeniería"),
    )

    encontrado = buscar_estudiante_por_id(ruta_db, creado.id)

    assert encontrado == creado


def test_buscar_estudiante_inexistente_devuelve_none(ruta_db: Path) -> None:
    assert buscar_estudiante_por_id(ruta_db, 999) is None


def test_actualizar_estudiante(ruta_db: Path) -> None:
    creado = crear_estudiante(
        ruta_db,
        Estudiante(None, "Ana", 20, "Ingeniería"),
    )
    creado.edad = 21
    creado.programa = "Sistemas"

    actualizado = actualizar_estudiante(ruta_db, creado)

    assert actualizado is True
    assert buscar_estudiante_por_id(ruta_db, creado.id) == creado


def test_actualizar_id_inexistente_devuelve_false(ruta_db: Path) -> None:
    estudiante = Estudiante(999, "Ana", 20, "Ingeniería")

    assert actualizar_estudiante(ruta_db, estudiante) is False


def test_eliminar_estudiante(ruta_db: Path) -> None:
    creado = crear_estudiante(
        ruta_db,
        Estudiante(None, "Ana", 20, "Ingeniería"),
    )

    eliminado = eliminar_estudiante(ruta_db, creado.id)

    assert eliminado is True
    assert buscar_estudiante_por_id(ruta_db, creado.id) is None


def test_restriccion_edad_hace_rollback(ruta_db: Path) -> None:
    with pytest.raises(sqlite3.IntegrityError):
        with obtener_conexion(ruta_db) as conexion:
            conexion.execute(
                """
                INSERT INTO estudiantes (nombre, edad, programa)
                VALUES (?, ?, ?)
                """,
                ("Ana", -1, "Ingeniería"),
            )

    assert listar_estudiantes(ruta_db) == []


def test_datos_persisten_entre_conexiones(ruta_db: Path) -> None:
    creado = crear_estudiante(
        ruta_db,
        Estudiante(None, "Ana", 20, "Ingeniería"),
    )

    recuperado = buscar_estudiante_por_id(ruta_db, creado.id)

    assert recuperado == creado
