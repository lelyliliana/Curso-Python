"""Configuración de la aplicación obtenida desde el entorno."""

from dataclasses import dataclass
import os
from pathlib import Path


NIVELES_LOG_VALIDOS = {"DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"}


@dataclass(frozen=True, slots=True)
class Config:
    """Valores de configuración validados e inmutables."""

    log_level: str
    data_dir: Path


def cargar_config() -> Config:
    """Lee variables de entorno, aplica valores predeterminados y valida."""
    log_level = os.getenv("APP_LOG_LEVEL", "INFO").strip().upper()
    data_dir_texto = os.getenv("APP_DATA_DIR", "data").strip()

    if log_level not in NIVELES_LOG_VALIDOS:
        opciones = ", ".join(sorted(NIVELES_LOG_VALIDOS))
        raise ValueError(f"APP_LOG_LEVEL debe ser uno de: {opciones}")
    if not data_dir_texto:
        raise ValueError("APP_DATA_DIR no puede estar vacío")

    return Config(log_level=log_level, data_dir=Path(data_dir_texto))
