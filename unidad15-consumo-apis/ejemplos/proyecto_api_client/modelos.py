"""Modelos de datos recibidos desde la API académica."""

from dataclasses import dataclass
from typing import Any


@dataclass
class Estudiante:
    """Representa un estudiante obtenido desde la API."""

    id: int
    nombre: str
    edad: int
    programa: str

    def __post_init__(self) -> None:
        if self.id < 1:
            raise ValueError("El id debe ser positivo")
        if not self.nombre.strip():
            raise ValueError("El nombre no puede estar vacío")
        if self.edad < 0:
            raise ValueError("La edad no puede ser negativa")
        if not self.programa.strip():
            raise ValueError("El programa no puede estar vacío")

    @classmethod
    def desde_dict(cls, datos: dict[str, Any]) -> "Estudiante":
        """Construye un estudiante tras validar la estructura básica."""
        campos = ("id", "nombre", "edad", "programa")
        faltantes = [campo for campo in campos if campo not in datos]
        if faltantes:
            raise ValueError(f"Faltan campos: {', '.join(faltantes)}")
        if type(datos["id"]) is not int or type(datos["edad"]) is not int:
            raise ValueError("El id y la edad deben ser enteros")
        if not isinstance(datos["nombre"], str) or not isinstance(
            datos["programa"], str
        ):
            raise ValueError("El nombre y el programa deben ser textos")
        return cls(
            id=datos["id"],
            nombre=datos["nombre"],
            edad=datos["edad"],
            programa=datos["programa"],
        )
