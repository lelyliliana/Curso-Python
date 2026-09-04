"""Transformaciones reproducibles para el conjunto académico de ejemplo."""

from pathlib import Path

import pandas as pd


COLUMNAS_ESPERADAS = ["codigo", "nombre", "edad", "programa", "nota"]


def cargar_datos(ruta: str | Path) -> pd.DataFrame:
    """Carga un CSV y comprueba que contiene las columnas necesarias."""
    datos = pd.read_csv(ruta)
    columnas_faltantes = [
        columna for columna in COLUMNAS_ESPERADAS if columna not in datos.columns
    ]
    if columnas_faltantes:
        raise ValueError(f"Faltan columnas requeridas: {columnas_faltantes}")
    return datos


def limpiar_datos(datos: pd.DataFrame) -> pd.DataFrame:
    """Normaliza textos y tipos sin modificar el DataFrame recibido.

    Las notas ausentes o no convertibles se conservan como NaN: no se inventa una
    calificación. Los registros sin código, nombre, edad o programa se descartan
    porque carecen de los datos mínimos para este análisis académico.
    """
    limpio = datos.copy()

    limpio["codigo"] = limpio["codigo"].astype("string").str.strip().str.upper()
    limpio["nombre"] = limpio["nombre"].astype("string").str.strip().str.title()
    limpio["programa"] = (
        limpio["programa"].astype("string").str.strip().str.title()
    )
    limpio["edad"] = pd.to_numeric(limpio["edad"], errors="coerce").astype("Int64")
    limpio["nota"] = pd.to_numeric(limpio["nota"], errors="coerce")

    columnas_indispensables = ["codigo", "nombre", "edad", "programa"]
    limpio = limpio.dropna(subset=columnas_indispensables)
    limpio = limpio.drop_duplicates(subset="codigo", keep="first")
    return limpio.reset_index(drop=True)


def filtrar_aprobados(datos: pd.DataFrame) -> pd.DataFrame:
    """Devuelve una copia con estudiantes cuya nota es al menos 3.0."""
    return datos.loc[datos["nota"] >= 3.0].copy().reset_index(drop=True)


def resumen_por_programa(datos: pd.DataFrame) -> pd.DataFrame:
    """Resume cantidad de notas, promedio y nota máxima de cada programa."""
    resumen = datos.groupby("programa", as_index=False).agg(
        cantidad_notas=("nota", "count"),
        promedio=("nota", "mean"),
        nota_maxima=("nota", "max"),
    )
    return resumen.sort_values("programa").reset_index(drop=True)


def estudiante_mejor_nota(datos: pd.DataFrame) -> pd.Series | None:
    """Devuelve datos del primer máximo o None si no existen notas válidas."""
    con_nota = datos.dropna(subset=["nota"])
    if con_nota.empty:
        return None

    indice = con_nota["nota"].idxmax()
    columnas = ["codigo", "nombre", "programa", "nota"]
    return con_nota.loc[indice, columnas].copy()


def main() -> None:
    """Carga el CSV local y muestra resultados sin crear archivos de salida."""
    ruta_datos = Path(__file__).with_name("datos.csv")
    datos = limpiar_datos(cargar_datos(ruta_datos))

    print("Primeras filas limpias:")
    print(datos.head())
    print("\nResumen por programa:")
    print(resumen_por_programa(datos))


if __name__ == "__main__":
    main()
