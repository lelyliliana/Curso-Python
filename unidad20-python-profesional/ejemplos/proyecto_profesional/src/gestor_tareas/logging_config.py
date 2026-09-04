"""Configuración centralizada y explícita del logging."""

import logging


NIVELES_LOG = {
    "DEBUG": logging.DEBUG,
    "INFO": logging.INFO,
    "WARNING": logging.WARNING,
    "ERROR": logging.ERROR,
    "CRITICAL": logging.CRITICAL,
}


def configurar_logging(nivel: str) -> None:
    """Configura el logging raíz con un nivel conocido."""
    nombre_nivel = nivel.strip().upper()
    if nombre_nivel not in NIVELES_LOG:
        raise ValueError(f"Nivel de logging inválido: {nivel}")

    logging.basicConfig(
        level=NIVELES_LOG[nombre_nivel],
        format="%(asctime)s %(levelname)s %(name)s: %(message)s",
    )
