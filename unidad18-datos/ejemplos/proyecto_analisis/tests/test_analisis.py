from pathlib import Path

import pandas as pd

from analisis import (
    cargar_datos,
    estudiante_mejor_nota,
    filtrar_aprobados,
    limpiar_datos,
    resumen_por_programa,
)


COLUMNAS = ["codigo", "nombre", "edad", "programa", "nota"]


def crear_datos() -> pd.DataFrame:
    """Crea datos pequeños e independientes para las pruebas."""
    return pd.DataFrame(
        {
            "codigo": [" e01 ", "E02", "e03"],
            "nombre": ["  ana torres ", "LUIS ROJAS", "Marta Díaz"],
            "edad": ["19", "21", "20"],
            "programa": [" sistemas ", "Sistemas", "Datos"],
            "nota": ["4.5", "sin nota", "2.8"],
        }
    )


def test_cargar_csv_y_conservar_columnas(tmp_path: Path) -> None:
    ruta = tmp_path / "estudiantes.csv"
    crear_datos().to_csv(ruta, index=False)

    resultado = cargar_datos(ruta)

    assert list(resultado.columns) == COLUMNAS
    assert len(resultado) == 3


def test_cargar_csv_sin_columna_requerida_lanza_error(tmp_path: Path) -> None:
    ruta = tmp_path / "incompleto.csv"
    pd.DataFrame({"codigo": ["E01"]}).to_csv(ruta, index=False)

    try:
        cargar_datos(ruta)
    except ValueError as error:
        assert "Faltan columnas" in str(error)
    else:
        raise AssertionError("Se esperaba ValueError")


def test_limpiar_normaliza_nombres_codigos_y_programas() -> None:
    resultado = limpiar_datos(crear_datos())

    assert resultado.loc[0, "nombre"] == "Ana Torres"
    assert resultado.loc[0, "codigo"] == "E01"
    assert resultado.loc[0, "programa"] == "Sistemas"


def test_limpiar_convierte_nota_y_conserva_faltante_como_nan() -> None:
    resultado = limpiar_datos(crear_datos())

    assert resultado.loc[0, "nota"] == 4.5
    assert pd.isna(resultado.loc[1, "nota"])


def test_limpiar_no_muta_dataframe_original() -> None:
    original = crear_datos()
    esperado = original.copy(deep=True)

    limpiar_datos(original)

    pd.testing.assert_frame_equal(original, esperado)


def test_filtrar_aprobados_excluye_reprobados_y_faltantes() -> None:
    limpio = limpiar_datos(crear_datos())

    resultado = filtrar_aprobados(limpio)

    esperado = limpio.loc[[0]].reset_index(drop=True)
    pd.testing.assert_frame_equal(resultado, esperado)


def test_filtrar_aprobados_no_muta_dataframe_original() -> None:
    original = limpiar_datos(crear_datos())
    esperado = original.copy(deep=True)

    filtrar_aprobados(original)

    pd.testing.assert_frame_equal(original, esperado)


def test_resumen_por_programa_calcula_agregaciones() -> None:
    datos = pd.DataFrame(
        {
            "programa": ["Datos", "Sistemas", "Sistemas"],
            "nota": [3.0, 4.0, 5.0],
        }
    )
    esperado = pd.DataFrame(
        {
            "programa": ["Datos", "Sistemas"],
            "cantidad_notas": [1, 2],
            "promedio": [3.0, 4.5],
            "nota_maxima": [3.0, 5.0],
        }
    )

    resultado = resumen_por_programa(datos)

    pd.testing.assert_frame_equal(resultado, esperado)


def test_estudiante_mejor_nota_devuelve_primera_coincidencia() -> None:
    datos = pd.DataFrame(
        {
            "codigo": ["E01", "E02"],
            "nombre": ["Ana", "Luis"],
            "programa": ["Datos", "Sistemas"],
            "nota": [4.8, 4.2],
        }
    )
    esperado = pd.Series(
        {"codigo": "E01", "nombre": "Ana", "programa": "Datos", "nota": 4.8}
    )
    esperado.name = 0

    resultado = estudiante_mejor_nota(datos)

    assert resultado is not None
    pd.testing.assert_series_equal(resultado, esperado)


def test_estudiante_mejor_nota_sin_notas_devuelve_none() -> None:
    datos = pd.DataFrame(
        {
            "codigo": ["E01"],
            "nombre": ["Ana"],
            "programa": ["Datos"],
            "nota": [float("nan")],
        }
    )

    assert estudiante_mejor_nota(datos) is None
