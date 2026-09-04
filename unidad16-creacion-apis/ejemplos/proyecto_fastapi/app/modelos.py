"""Modelos internos del dominio académico."""

from dataclasses import dataclass


@dataclass
class Estudiante:
    """Representa un estudiante dentro de la aplicación."""

    id: int
    nombre: str
    edad: int
    programa: str
