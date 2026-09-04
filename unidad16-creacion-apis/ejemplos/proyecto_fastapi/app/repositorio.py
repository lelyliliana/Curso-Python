"""Repositorio en memoria para estudiantes."""

from app.modelos import Estudiante


class RepositorioEstudiantes:
    def __init__(self) -> None:
        self._estudiantes: dict[int, Estudiante] = {}
        self._siguiente_id = 1

    def reset(self) -> None:
        self._estudiantes.clear()
        self._siguiente_id = 1

    def listar(self, programa: str | None = None, limite: int = 10) -> list[Estudiante]:
        estudiantes = list(self._estudiantes.values())
        if programa is not None:
            estudiantes = [e for e in estudiantes if e.programa == programa]
        return estudiantes[:limite]

    def obtener(self, estudiante_id: int) -> Estudiante | None:
        return self._estudiantes.get(estudiante_id)

    def crear(self, nombre: str, edad: int, programa: str) -> Estudiante:
        estudiante = Estudiante(self._siguiente_id, nombre, edad, programa)
        self._estudiantes[estudiante.id] = estudiante
        self._siguiente_id += 1
        return estudiante

    def actualizar(self, estudiante_id: int, cambios: dict[str, object]) -> Estudiante | None:
        estudiante = self.obtener(estudiante_id)
        if estudiante is None:
            return None
        for campo, valor in cambios.items():
            setattr(estudiante, campo, valor)
        return estudiante

    def eliminar(self, estudiante_id: int) -> bool:
        return self._estudiantes.pop(estudiante_id, None) is not None
