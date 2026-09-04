"""Operaciones CRUD para una base SQLite de estudiantes."""

import sqlite3
from collections.abc import Iterator
from contextlib import contextmanager
from pathlib import Path

from estudiantes import Estudiante

RutaBase = str | Path


@contextmanager
def obtener_conexion(ruta_db: RutaBase) -> Iterator[sqlite3.Connection]:
    """Abre una conexión, controla la transacción y garantiza su cierre."""
    conexion = sqlite3.connect(ruta_db)
    conexion.row_factory = sqlite3.Row
    conexion.execute("PRAGMA foreign_keys = ON")
    try:
        yield conexion
        conexion.commit()
    except Exception:
        conexion.rollback()
        raise
    finally:
        conexion.close()


def inicializar_db(ruta_db: RutaBase) -> None:
    """Crea la tabla de estudiantes cuando todavía no existe."""
    with obtener_conexion(ruta_db) as conexion:
        conexion.execute(
            """
            CREATE TABLE IF NOT EXISTS estudiantes (
                id INTEGER PRIMARY KEY,
                nombre TEXT NOT NULL,
                edad INTEGER NOT NULL CHECK (edad >= 0),
                programa TEXT NOT NULL
            )
            """
        )


def _fila_a_estudiante(fila: sqlite3.Row) -> Estudiante:
    return Estudiante(
        id=fila["id"],
        nombre=fila["nombre"],
        edad=fila["edad"],
        programa=fila["programa"],
    )


def crear_estudiante(ruta_db: RutaBase, estudiante: Estudiante) -> Estudiante:
    """Inserta un estudiante y devuelve una copia con el id generado."""
    with obtener_conexion(ruta_db) as conexion:
        cursor = conexion.execute(
            """
            INSERT INTO estudiantes (nombre, edad, programa)
            VALUES (?, ?, ?)
            """,
            (estudiante.nombre, estudiante.edad, estudiante.programa),
        )
        estudiante_id = cursor.lastrowid

    if estudiante_id is None:
        raise RuntimeError("SQLite no devolvió el id del estudiante")

    return Estudiante(
        id=estudiante_id,
        nombre=estudiante.nombre,
        edad=estudiante.edad,
        programa=estudiante.programa,
    )


def listar_estudiantes(ruta_db: RutaBase) -> list[Estudiante]:
    """Devuelve todos los estudiantes ordenados por nombre e id."""
    with obtener_conexion(ruta_db) as conexion:
        filas = conexion.execute(
            """
            SELECT id, nombre, edad, programa
            FROM estudiantes
            ORDER BY nombre ASC, id ASC
            """
        ).fetchall()
    return [_fila_a_estudiante(fila) for fila in filas]


def buscar_estudiante_por_id(
    ruta_db: RutaBase,
    estudiante_id: int,
) -> Estudiante | None:
    """Busca un estudiante por id o devuelve None si no existe."""
    with obtener_conexion(ruta_db) as conexion:
        fila = conexion.execute(
            """
            SELECT id, nombre, edad, programa
            FROM estudiantes
            WHERE id = ?
            """,
            (estudiante_id,),
        ).fetchone()
    return None if fila is None else _fila_a_estudiante(fila)


def actualizar_estudiante(
    ruta_db: RutaBase,
    estudiante: Estudiante,
) -> bool:
    """Actualiza un estudiante existente e indica si encontró su id."""
    if estudiante.id is None:
        raise ValueError("Se necesita un id para actualizar")

    with obtener_conexion(ruta_db) as conexion:
        cursor = conexion.execute(
            """
            UPDATE estudiantes
            SET nombre = ?, edad = ?, programa = ?
            WHERE id = ?
            """,
            (
                estudiante.nombre,
                estudiante.edad,
                estudiante.programa,
                estudiante.id,
            ),
        )
        return cursor.rowcount == 1


def eliminar_estudiante(ruta_db: RutaBase, estudiante_id: int) -> bool:
    """Elimina un estudiante por id e indica si existía."""
    with obtener_conexion(ruta_db) as conexion:
        cursor = conexion.execute(
            "DELETE FROM estudiantes WHERE id = ?",
            (estudiante_id,),
        )
        return cursor.rowcount == 1
