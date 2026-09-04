"""Demostración manual de las operaciones CRUD del proyecto."""

from pathlib import Path

from database import (
    actualizar_estudiante,
    buscar_estudiante_por_id,
    crear_estudiante,
    eliminar_estudiante,
    inicializar_db,
    listar_estudiantes,
)
from estudiantes import Estudiante


def main() -> None:
    """Ejecuta una demostración pequeña sobre estudiantes.db."""
    ruta_db = Path("estudiantes.db")
    inicializar_db(ruta_db)

    ana = crear_estudiante(
        ruta_db,
        Estudiante(None, "Ana", 20, "Ingeniería"),
    )
    luis = crear_estudiante(
        ruta_db,
        Estudiante(None, "Luis", 22, "Sistemas"),
    )

    print("Estudiantes creados:")
    for estudiante in listar_estudiantes(ruta_db):
        print(estudiante)

    print("Búsqueda:", buscar_estudiante_por_id(ruta_db, ana.id))

    luis.edad = 23
    actualizar_estudiante(ruta_db, luis)
    print("Actualizado:", buscar_estudiante_por_id(ruta_db, luis.id))

    if ana.id is not None:
        eliminar_estudiante(ruta_db, ana.id)
    print("Registros restantes:", listar_estudiantes(ruta_db))


if __name__ == "__main__":
    main()
