"""Interfaz de línea de comandos para el organizador de archivos."""

from argparse import ArgumentParser
import logging
from pathlib import Path

from automatizador import organizar_archivos


logger = logging.getLogger(__name__)


def crear_parser() -> ArgumentParser:
    """Construye el parser sin leer directamente los argumentos del proceso."""
    parser = ArgumentParser(description="Organiza archivos según su extensión")
    parser.add_argument("origen", type=Path, help="Carpeta que se inspeccionará")
    parser.add_argument("--destino", type=Path, help="Carpeta de salida")
    parser.add_argument("--extension", help="Procesa solo esta extensión")

    modo = parser.add_mutually_exclusive_group()
    modo.add_argument(
        "--dry-run",
        action="store_true",
        dest="dry_run",
        help="Muestra el plan sin mover archivos (modo predeterminado)",
    )
    modo.add_argument(
        "--ejecutar",
        action="store_false",
        dest="dry_run",
        help="Aplica realmente los movimientos",
    )
    parser.set_defaults(dry_run=True)
    return parser


def main(argv: list[str] | None = None) -> int:
    """Procesa argumentos, ejecuta el organizador y devuelve un código de salida."""
    args = crear_parser().parse_args(argv)
    destino = args.destino or args.origen.parent / "salida"

    try:
        movimientos = organizar_archivos(
            args.origen,
            destino,
            dry_run=args.dry_run,
            extension=args.extension,
        )
    except (FileNotFoundError, NotADirectoryError, FileExistsError, ValueError) as error:
        logger.error("No fue posible organizar los archivos: %s", error)
        return 1
    except OSError as error:
        logger.error("Falló una operación del filesystem: %s", error)
        return 1

    accion = "Simular" if args.dry_run else "Mover"
    for origen, ruta_destino in movimientos:
        print(f"{accion}: {origen} -> {ruta_destino}")
    print(f"Resumen: {len(movimientos)} archivo(s), dry_run={args.dry_run}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
