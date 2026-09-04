"""Modelos del dominio de tareas."""

from dataclasses import dataclass


@dataclass(slots=True)
class Tarea:
    """Representa una tarea identificada dentro del servicio."""

    id: int
    titulo: str
    completada: bool = False

    def __post_init__(self) -> None:
        self.titulo = self.titulo.strip()
        if self.id < 1:
            raise ValueError("El id debe ser positivo")
        if not self.titulo:
            raise ValueError("El título no puede estar vacío")
