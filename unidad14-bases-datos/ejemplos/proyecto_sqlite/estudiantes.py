"""Modelo de estudiante utilizado por la capa de persistencia."""

from dataclasses import dataclass


@dataclass
class Estudiante:
    """Representa un estudiante almacenado en SQLite."""

    id: int | None
    nombre: str
    edad: int
    programa: str

    def __post_init__(self) -> None:
        self.nombre = self.nombre.strip()
        self.programa = self.programa.strip()
        if not self.nombre:
            raise ValueError("El nombre no puede estar vacío")
        if self.edad < 0:
            raise ValueError("La edad no puede ser negativa")
        if not self.programa:
            raise ValueError("El programa no puede estar vacío")
