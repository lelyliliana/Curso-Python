"""Reglas de negocio del gestor de tareas en memoria."""

from collections.abc import Iterable

from .modelos import Tarea


class TareaNoEncontradaError(LookupError):
    """Indica que no existe una tarea con el identificador solicitado."""


class ServicioTareas:
    """Administra una colección propia de tareas sin entrada o salida directa."""

    def __init__(self, tareas: Iterable[Tarea] | None = None) -> None:
        self._tareas = list(tareas) if tareas is not None else []
        ids = [tarea.id for tarea in self._tareas]
        if len(ids) != len(set(ids)):
            raise ValueError("No puede haber identificadores repetidos")
        self._siguiente_id = max(ids, default=0) + 1

    def crear(self, titulo: str) -> Tarea:
        """Crea, almacena y devuelve una tarea con id consecutivo."""
        tarea = Tarea(id=self._siguiente_id, titulo=titulo)
        self._tareas.append(tarea)
        self._siguiente_id += 1
        return tarea

    def listar(self) -> tuple[Tarea, ...]:
        """Devuelve una vista inmutable de la colección de tareas."""
        return tuple(self._tareas)

    def buscar(self, tarea_id: int) -> Tarea:
        """Busca por id o lanza un error explícito del dominio."""
        for tarea in self._tareas:
            if tarea.id == tarea_id:
                return tarea
        raise TareaNoEncontradaError(f"No existe la tarea con id {tarea_id}")

    def completar(self, tarea_id: int) -> Tarea:
        """Marca una tarea como completada y devuelve el modelo actualizado."""
        tarea = self.buscar(tarea_id)
        tarea.completada = True
        return tarea
