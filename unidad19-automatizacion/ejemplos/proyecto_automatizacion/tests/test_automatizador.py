from pathlib import Path

import pytest

from automatizador import (
    buscar_archivos,
    calcular_hash,
    crear_respaldo,
    organizar_archivos,
)
from cli import crear_parser, main


def test_buscar_archivos_devuelve_solo_archivos_en_orden(tmp_path: Path) -> None:
    (tmp_path / "b.txt").write_text("b", encoding="utf-8")
    (tmp_path / "a.csv").write_text("a", encoding="utf-8")
    (tmp_path / "carpeta").mkdir()

    resultado = buscar_archivos(tmp_path)

    assert [archivo.name for archivo in resultado] == ["a.csv", "b.txt"]


def test_buscar_archivos_filtra_extension_sin_importar_punto_o_mayusculas(
    tmp_path: Path,
) -> None:
    (tmp_path / "datos.CSV").write_text("a", encoding="utf-8")
    (tmp_path / "notas.txt").write_text("b", encoding="utf-8")

    resultado = buscar_archivos(tmp_path, ".csv")

    assert [archivo.name for archivo in resultado] == ["datos.CSV"]


def test_buscar_archivos_rechaza_origen_inexistente(tmp_path: Path) -> None:
    with pytest.raises(FileNotFoundError, match="No existe"):
        buscar_archivos(tmp_path / "inexistente")


def test_crear_respaldo_crea_carpeta_y_conserva_contenido(tmp_path: Path) -> None:
    archivo = tmp_path / "informe.txt"
    archivo.write_text("contenido", encoding="utf-8")

    respaldo = crear_respaldo(archivo, tmp_path / "respaldos", "20260904_120000")

    assert respaldo.name == "informe_20260904_120000.txt"
    assert respaldo.read_text(encoding="utf-8") == "contenido"
    assert archivo.exists()


def test_crear_respaldo_no_sobrescribe(tmp_path: Path) -> None:
    archivo = tmp_path / "informe.txt"
    archivo.write_text("nuevo", encoding="utf-8")
    destino = tmp_path / "respaldos"
    destino.mkdir()
    existente = destino / "informe_20260904_120000.txt"
    existente.write_text("anterior", encoding="utf-8")

    with pytest.raises(FileExistsError):
        crear_respaldo(archivo, destino, "20260904_120000")

    assert existente.read_text(encoding="utf-8") == "anterior"


def test_calcular_hash_es_estable_y_cambia_con_el_contenido(tmp_path: Path) -> None:
    archivo = tmp_path / "datos.bin"
    archivo.write_bytes(b"abc")

    primera_huella = calcular_hash(archivo)
    segunda_huella = calcular_hash(archivo)
    archivo.write_bytes(b"abcd")

    assert primera_huella == segunda_huella
    assert primera_huella != calcular_hash(archivo)
    assert len(primera_huella) == 64


def test_dry_run_no_modifica_filesystem(tmp_path: Path) -> None:
    origen = tmp_path / "entrada"
    destino = tmp_path / "salida"
    origen.mkdir()
    archivo = origen / "notas.txt"
    archivo.write_text("texto", encoding="utf-8")

    movimientos = organizar_archivos(origen, destino, dry_run=True)

    assert movimientos == [(archivo, destino / "txt" / "notas.txt")]
    assert archivo.exists()
    assert not destino.exists()


def test_ejecucion_real_mueve_archivos_por_extension(tmp_path: Path) -> None:
    origen = tmp_path / "entrada"
    destino = tmp_path / "salida"
    origen.mkdir()
    (origen / "datos.csv").write_text("dato", encoding="utf-8")
    (origen / "informe.pdf").write_bytes(b"pdf")

    organizar_archivos(origen, destino, dry_run=False)

    assert (destino / "csv" / "datos.csv").read_text(encoding="utf-8") == "dato"
    assert (destino / "pdf" / "informe.pdf").read_bytes() == b"pdf"
    assert list(origen.iterdir()) == []


def test_colision_aborta_antes_de_mover_archivos(tmp_path: Path) -> None:
    origen = tmp_path / "entrada"
    destino = tmp_path / "salida"
    origen.mkdir()
    (origen / "a.csv").write_text("a", encoding="utf-8")
    (origen / "b.txt").write_text("b", encoding="utf-8")
    (destino / "txt").mkdir(parents=True)
    (destino / "txt" / "b.txt").write_text("anterior", encoding="utf-8")

    with pytest.raises(FileExistsError):
        organizar_archivos(origen, destino, dry_run=False)

    assert (origen / "a.csv").exists()
    assert (origen / "b.txt").exists()
    assert (destino / "txt" / "b.txt").read_text(encoding="utf-8") == "anterior"


def test_parser_acepta_argumentos_y_mantiene_dry_run_predeterminado() -> None:
    args = crear_parser().parse_args(["entrada", "--extension", ".txt"])

    assert args.origen == Path("entrada")
    assert args.extension == ".txt"
    assert args.dry_run is True


def test_main_dry_run_devuelve_cero_y_no_mueve(tmp_path: Path) -> None:
    origen = tmp_path / "entrada"
    destino = tmp_path / "salida"
    origen.mkdir()
    archivo = origen / "notas.txt"
    archivo.write_text("texto", encoding="utf-8")

    codigo = main([str(origen), "--destino", str(destino), "--dry-run"])

    assert codigo == 0
    assert archivo.exists()
    assert not destino.exists()


def test_main_ejecutar_mueve_y_devuelve_cero(tmp_path: Path) -> None:
    origen = tmp_path / "entrada"
    destino = tmp_path / "salida"
    origen.mkdir()
    (origen / "notas.txt").write_text("texto", encoding="utf-8")

    codigo = main([str(origen), "--destino", str(destino), "--ejecutar"])

    assert codigo == 0
    assert (destino / "txt" / "notas.txt").exists()


def test_main_maneja_error_explicito_y_devuelve_uno(tmp_path: Path) -> None:
    codigo = main([str(tmp_path / "inexistente")])

    assert codigo == 1
