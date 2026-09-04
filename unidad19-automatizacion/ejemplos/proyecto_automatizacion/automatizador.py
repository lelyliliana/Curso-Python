"""Funciones seguras para buscar, respaldar y organizar archivos."""

from datetime import datetime
import hashlib
from pathlib import Path
import shutil


def _normalizar_extension(extension: str) -> str:
    """Devuelve una extensión en minúsculas, sin punto inicial."""
    normalizada = extension.strip().lower().lstrip(".")
    if not normalizada:
        raise ValueError("La extensión no puede estar vacía")
    return normalizada


def buscar_archivos(origen: Path, extension: str | None = None) -> list[Path]:
    """Busca archivos directos en orden estable y permite filtrar por extensión."""
    if not origen.exists():
        raise FileNotFoundError(f"No existe la carpeta de origen: {origen}")
    if not origen.is_dir():
        raise NotADirectoryError(f"La ruta de origen no es una carpeta: {origen}")

    archivos = sorted(elemento for elemento in origen.iterdir() if elemento.is_file())
    if extension is None:
        return archivos

    extension_normalizada = _normalizar_extension(extension)
    return [
        archivo
        for archivo in archivos
        if archivo.suffix.lower().lstrip(".") == extension_normalizada
    ]


def crear_respaldo(
    archivo: Path,
    destino: Path,
    marca_tiempo: str | None = None,
) -> Path:
    """Copia un archivo con timestamp sin reemplazar respaldos existentes."""
    if not archivo.is_file():
        raise FileNotFoundError(f"No existe el archivo para respaldar: {archivo}")

    marca = marca_tiempo or datetime.now().strftime("%Y%m%d_%H%M%S")
    ruta_respaldo = destino / f"{archivo.stem}_{marca}{archivo.suffix}"
    if ruta_respaldo.exists():
        raise FileExistsError(f"El respaldo ya existe: {ruta_respaldo}")

    destino.mkdir(parents=True, exist_ok=True)
    shutil.copy2(archivo, ruta_respaldo)
    return ruta_respaldo


def calcular_hash(archivo: Path, tamano_bloque: int = 65_536) -> str:
    """Calcula la huella SHA-256 leyendo el archivo por bloques."""
    if tamano_bloque <= 0:
        raise ValueError("El tamaño de bloque debe ser positivo")

    huella = hashlib.sha256()
    with archivo.open("rb") as flujo:
        while bloque := flujo.read(tamano_bloque):
            huella.update(bloque)
    return huella.hexdigest()


def organizar_archivos(
    origen: Path,
    destino: Path,
    dry_run: bool = True,
    extension: str | None = None,
) -> list[tuple[Path, Path]]:
    """Organiza archivos por extensión y devuelve el plan aplicado o simulado.

    Antes de modificar el filesystem se comprueban todas las colisiones. Los
    archivos sin extensión se ubican en ``sin_extension``.
    """
    archivos = buscar_archivos(origen, extension)
    movimientos: list[tuple[Path, Path]] = []

    for archivo in archivos:
        categoria = archivo.suffix.lower().lstrip(".") or "sin_extension"
        ruta_destino = destino / categoria / archivo.name
        if ruta_destino.exists():
            raise FileExistsError(f"El destino ya existe: {ruta_destino}")
        movimientos.append((archivo, ruta_destino))

    if dry_run:
        return movimientos

    for archivo, ruta_destino in movimientos:
        ruta_destino.parent.mkdir(parents=True, exist_ok=True)
        shutil.move(str(archivo), str(ruta_destino))

    return movimientos
