"""Modelo académico sencillo para practicar pruebas automatizadas."""

from dataclasses import dataclass, field


@dataclass
class Estudiante:
    """Representa un estudiante y sus notas académicas."""

    nombre: str
    notas: list[float] = field(default_factory=list)

    def __post_init__(self) -> None:
        self.nombre = self.nombre.strip()
        if not self.nombre:
            raise ValueError("El nombre no puede estar vacío")
        for nota in self.notas:
            self._validar_nota(nota)

    @staticmethod
    def _validar_nota(nota: float) -> None:
        if not 0.0 <= nota <= 5.0:
            raise ValueError("La nota debe estar entre 0.0 y 5.0")

    def agregar_nota(self, nota: float) -> None:
        """Agrega una nota perteneciente al rango académico."""
        self._validar_nota(nota)
        self.notas.append(nota)

    def calcular_promedio(self) -> float:
        """Calcula el promedio o falla cuando no existen notas."""
        if not self.notas:
            raise ValueError("No hay notas registradas")
        return sum(self.notas) / len(self.notas)
