"""API pública mínima del paquete gestor_tareas."""

from .modelos import Tarea
from .servicio import ServicioTareas

__all__ = ["ServicioTareas", "Tarea"]
