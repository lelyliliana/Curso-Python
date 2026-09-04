# Unidad 18 — Análisis de datos con NumPy y pandas

Los programas anteriores guardaron información en colecciones, archivos, APIs y bases de datos. En esta unidad aprenderás a convertir datos tabulares en respuestas reproducibles mediante NumPy y, principalmente, pandas.

---

## 🎯 Objetivos de aprendizaje

Al finalizar podrás:

- Explicar el flujo de un análisis de datos.
- Crear, inspeccionar, operar y filtrar arrays de NumPy.
- Construir `Series` y `DataFrame` de pandas.
- Cargar e inspeccionar archivos CSV locales.
- Seleccionar, filtrar, limpiar y transformar datos.
- Tratar faltantes y conversiones con una decisión explícita.
- Ordenar, agregar y agrupar observaciones.
- Combinar tablas y exportar resultados.
- Organizar un análisis repetible en funciones.
- Probar transformaciones con las utilidades de `pd.testing`.

---

## 📋 Antes de comenzar

Necesitas haber completado la Unidad 17. Usaremos listas, diccionarios, archivos CSV, funciones, type hints y pytest.

NumPy y pandas son paquetes externos. Instálalos dentro del entorno virtual de tu proyecto:

```bash
python -m pip install numpy pandas pytest
```

Puedes comprobarlos con `python -m pip show numpy pandas pytest`. No necesitamos red durante el análisis: el proyecto incluye un CSV local.

No estudiaremos machine learning, estadística inferencial ni visualización avanzada. Los notebooks son habituales para explorar, pero no son obligatorios: continuaremos con scripts reproducibles.

---

# 1. ¿Qué es analizar datos?

Analizar datos es aplicar pasos razonados para responder una pregunta. No consiste solamente en hacer gráficos.

```text
datos
  ↓
limpieza
  ↓
transformación
  ↓
resumen
  ↓
interpretación
```

Por ejemplo: recibimos notas, corregimos espacios y tipos, calculamos promedios y finalmente interpretamos qué programa requiere atención. Una tabla limpia no explica por sí sola el contexto ni convierte una relación en una causa.

# 2. El ecosistema de Python para datos

- **NumPy** aporta arrays y cálculo numérico eficiente.
- **pandas** trabaja con datos tabulares etiquetados.
- **Matplotlib** permite visualizaciones; Seaborn y Plotly también forman parte del ecosistema.

Aquí veremos NumPy básico y pandas como herramienta principal. Dejaremos la visualización para otro momento.

# Parte I — NumPy básico

# 3. Primer array

La convención `import numpy as np` crea el alias breve `np`:

```python
import numpy as np

numeros = np.array([1, 2, 3, 4])

print(numeros)
print(type(numeros))
```

Resultado aproximado:

```text
[1 2 3 4]
<class 'numpy.ndarray'>
```

Una lista es una colección general de Python. Un `ndarray` es una estructura optimizada para cálculo, normalmente homogénea, que permite operaciones vectorizadas. No esperes que todos sus métodos y comportamientos sean los de una lista.

# 4. `shape`, `ndim` y `dtype`

Tres atributos describen un array:

```python
import numpy as np

numeros = np.array([1, 2, 3, 4])

print(numeros.shape)
print(numeros.ndim)
print(numeros.dtype)
```

- `shape` informa el tamaño de cada dimensión: `(4,)` significa una dimensión con cuatro elementos.
- `ndim` informa la cantidad de dimensiones: `1`.
- `dtype` informa el tipo almacenado. Su nombre exacto, como `int64`, puede variar según la plataforma.

# 5. Arrays de dos dimensiones

Una matriz tiene filas y columnas:

```python
import numpy as np

matriz = np.array([
    [1, 2],
    [3, 4],
])

print(matriz)
print(matriz.shape)
print(matriz.ndim)
```

Su `shape` es `(2, 2)`: dos filas y dos columnas. `ndim` vale `2`.

# 6. Indexación y slicing

En un array 2D se separan fila y columna con una coma:

```python
import numpy as np

matriz = np.array([
    [10, 20, 30],
    [40, 50, 60],
])

print(matriz[0, 1])
print(matriz[1, :])
print(matriz[:, 0])
print(matriz[:, 1:])
```

`matriz[0, 1]` es `20`; `:` selecciona todas las posiciones de esa dimensión y `1:` selecciona desde la posición uno.

## 💡 Experimenta

Cambia `matriz[:, 1:]` por `matriz[0:2, 0:2]`. Predice primero su forma y luego consulta `shape`.

# 7. Operaciones vectorizadas y broadcasting

Una operación vectorizada se aplica elemento a elemento sin escribir el ciclo explícito:

```python
import numpy as np

notas = np.array([3.0, 3.5, 4.0])

print(notas * 2)
print(notas + 0.2)
```

Sumar `0.2` a todo el array es un caso sencillo de **broadcasting**: NumPy extiende conceptualmente el escalar a cada posición.

La alternativa tradicional sería `[nota * 2 for nota in notas]`. Las dos expresan una transformación, pero la versión vectorizada comunica directamente la operación numérica.

# 8. Operaciones entre arrays

```python
import numpy as np

primer_parcial = np.array([3.0, 4.0, 4.5])
segundo_parcial = np.array([4.0, 3.5, 4.5])
promedios = (primer_parcial + segundo_parcial) / 2

print(promedios)
```

Las dimensiones deben ser compatibles. Dos arrays de tres valores pueden sumarse posición por posición; formas incompatibles normalmente producen `ValueError`. No profundizaremos aún en todas las reglas de broadcasting.

# 9. Agregaciones

Las agregaciones reducen varios valores a un resumen:

```python
import numpy as np

notas = np.array([3.0, 3.5, 4.8, 4.0])

print(notas.sum())
print(notas.mean())
print(notas.min())
print(notas.max())
```

Obtendremos suma, media, mínimo y máximo. El método pertenece al array; NumPy también ofrece funciones como `np.mean(notas)`.

# 10. Filtrado booleano

Una comparación produce un array de booleanos. Podemos usarlo como máscara:

```python
import numpy as np

notas = np.array([2.5, 3.0, 4.2, 2.8])
mascara = notas >= 3.0

print(mascara)
print(notas[mascara])
```

Resultado:

```text
[False  True  True False]
[3.  4.2]
```

Esto se relaciona con `filter()` y las comprensiones, pero expresa la condición sobre el array completo.

# 11. Valores faltantes con `NaN`

`np.nan` representa habitualmente un valor numérico faltante. Puede propagarse:

```python
import numpy as np

notas = np.array([4.0, np.nan, 3.5])

print(np.isnan(notas))
print(notas.mean())
print(np.nanmean(notas))
```

`np.isnan()` identifica las posiciones ausentes. `mean()` produce `nan` en este caso; `np.nanmean()` omite los faltantes. Omitirlos es una decisión que debe documentarse, no un arreglo automático.

# Parte II — pandas

# 12. `Series`: valores con índice

La convención es `import pandas as pd`. Una `Series` es una secuencia unidimensional con índice:

```python
import pandas as pd

notas = pd.Series([4.0, 3.5, 4.8], index=["Ana", "Luis", "Marta"])

print(notas)
print(notas.loc["Luis"])
```

Los nombres de la izquierda son etiquetas del índice; los valores de la derecha son las notas.

# 13. `DataFrame`: una tabla etiquetada

Un `DataFrame` organiza filas, columnas e índice:

```python
import pandas as pd

estudiantes = pd.DataFrame(
    {
        "nombre": ["Ana", "Luis"],
        "nota": [4.5, 3.8],
    }
)

print(estudiantes)
```

Cada columna es una `Series`. El índice inicial `0, 1` identifica filas, pero no es necesariamente un dato del negocio.

# 14. Desde una lista de diccionarios

La estructura ya conocida se convierte directamente:

```python
import pandas as pd

registros = [
    {"nombre": "Ana", "nota": 4.5},
    {"nombre": "Luis", "nota": 3.8},
]
estudiantes = pd.DataFrame(registros)

print(estudiantes)
```

Las claves se transforman en columnas y cada diccionario representa una fila.

# 15. Leer un CSV

Desde la carpeta `proyecto_analisis/`:

```python
import pandas as pd

datos = pd.read_csv("datos.csv")
print(datos.head())
```

`read_csv()` usa la primera fila como encabezados y la coma como separador predeterminado. pandas intenta inferir tipos, pero puede equivocarse ante datos mezclados. Para otros separadores se configura `sep`, por ejemplo `sep=";"`.

# 16. Inspección inicial

Antes de transformar, conoce el conjunto:

```python
import pandas as pd

datos = pd.DataFrame(
    {
        "nombre": ["Ana", "Luis", "Marta"],
        "edad": [19, 21, 20],
        "nota": [4.5, 3.2, 4.8],
    }
)

print(datos.head(2))
print(datos.tail(2))
print(datos.shape)
print(datos.columns)
print(datos.dtypes)
datos.info()
print(datos.describe())
```

- `head()` y `tail()` muestran los extremos.
- `shape` entrega `(filas, columnas)`.
- `columns` y `dtypes` describen nombres y tipos.
- `info()` **imprime** un resumen con tipos y valores no nulos.
- `describe()` devuelve estadísticas descriptivas básicas; no constituye por sí solo una interpretación ni análisis inferencial.

# 17. Seleccionar columnas, filas y posiciones

```python
import pandas as pd

datos = pd.DataFrame(
    {
        "nombre": ["Ana", "Luis", "Marta"],
        "programa": ["Datos", "Sistemas", "Datos"],
        "nota": [4.5, 3.2, 4.8],
    }
)

print(datos["nota"])
print(datos[["nombre", "nota"]])
print(datos.loc[0:1, ["nombre", "nota"]])
print(datos.iloc[0:2, 0:2])
```

Un par de corchetes con una columna suele devolver `Series`; una lista de columnas dentro de los corchetes devuelve `DataFrame`. `loc` selecciona por etiquetas y condiciones; `iloc`, por posiciones enteras. En `loc[0:1]` se incluye la etiqueta final, mientras que `iloc[0:2]` excluye la posición final.

# 18. Filtrar filas

```python
import pandas as pd

datos = pd.DataFrame(
    {
        "nombre": ["Ana", "Luis", "Marta"],
        "edad": [19, 17, 22],
        "programa": ["Sistemas", "Arte", "Datos"],
        "nota": [4.5, 3.5, 2.8],
    }
)

aprobados_adultos = datos.loc[
    (datos["nota"] >= 3.0) & (datos["edad"] >= 18)
]
programas_tecnicos = datos.loc[
    datos["programa"].isin(["Sistemas", "Datos"])
]
notas_validas = datos.loc[datos["nota"].between(3.0, 5.0)]

print(aprobados_adultos)
print(programas_tecnicos)
print(notas_validas)
```

Con `Series` se usan `&` para “y” y `|` para “o”, con cada condición entre paréntesis. `and` y `or` esperan un único booleano y producen un error de valor ambiguo. `isin()` comprueba pertenencia y `between()` incluye los límites por defecto.

# 19. Métodos de texto y columnas nuevas

Los métodos `.str` aplican operaciones de cadenas a una columna:

```python
import pandas as pd

datos = pd.DataFrame(
    {
        "nombre": ["  ana torres", "LUIS ROJAS  "],
        "nota": [4.5, 3.0],
    }
)

datos = datos.copy()
datos.loc[:, "nombre"] = datos["nombre"].str.strip().str.title()
datos.loc[:, "aprobado"] = datos["nota"] >= 3.0
datos.loc[:, "nota_porcentaje"] = datos["nota"] / 5 * 100

print(datos)
```

Las dos columnas calculadas usan operaciones vectorizadas.

# 20. `apply()` y `Series.map()`

`apply()` ejecuta una función sobre los valores de una `Series`:

```python
import pandas as pd

def agregar_prefijo(codigo: str) -> str:
    return f"EST-{codigo.strip().upper()}"

datos = pd.DataFrame({"codigo": ["e01", " e02 "]})
datos["codigo_largo"] = datos["codigo"].apply(agregar_prefijo)

equivalencias = {"E01": "Activo", "E02": "Pendiente"}
datos["estado"] = datos["codigo"].str.strip().str.upper().map(equivalencias)

print(datos)
```

`Series.map()` transforma según una función, diccionario o Series y no es el `map()` integrado de Python. Cuando existe una operación vectorizada clara, suele ser más directa y eficiente que `apply()`; no uses `apply()` para todo.

# 21. Identificar valores faltantes

```python
import pandas as pd

datos = pd.DataFrame(
    {
        "nombre": ["Ana", "Luis", "Marta"],
        "nota": [4.5, None, 3.8],
    }
)

print(datos["nota"].isna())
print(datos["nota"].notna())
print(datos.isna().sum())
```

`isna()` marca ausencias; `notna()` marca valores presentes. La suma de booleanos cuenta faltantes por columna.

# 22. `dropna()` y `fillna()` exigen criterio

```python
import pandas as pd

datos = pd.DataFrame({"nota": [4.5, None, 3.5]})

solo_con_nota = datos.dropna(subset=["nota"])
con_mediana = datos.copy()
con_mediana["nota"] = con_mediana["nota"].fillna(datos["nota"].median())

print(solo_con_nota)
print(con_mediana)
```

`dropna()` puede eliminar filas o columnas y perder información. `fillna()` introduce un valor: la mediana podría tener sentido en un ejercicio, pero podría falsear una nota real. Otra regla válida es conservar `NaN` y excluirlo de ciertos cálculos. El proyecto adopta esta última: **no inventa calificaciones**.

# 23. Tipos y conversiones seguras

`astype()` convierte cuando los valores ya son compatibles:

```python
import pandas as pd

datos = pd.DataFrame({"edad": [18.0, 20.0]})
datos["edad"] = datos["edad"].astype(int)

print(datos.dtypes)
```

Para datos externos mezclados, `to_numeric()` permite detectar problemas:

```python
import pandas as pd

datos = pd.DataFrame({"nota": ["4.5", "sin nota", "3.8"]})
datos["nota"] = pd.to_numeric(datos["nota"], errors="coerce")

print(datos)
```

`errors="coerce"` reemplaza valores no convertibles por `NaN`. Esto evita detener la conversión, pero puede ocultar datos inválidos si no contamos y revisamos los nuevos faltantes.

# 24. Fechas

```python
import pandas as pd

datos = pd.DataFrame({"fecha": ["2026-09-01", "2026-09-02"]})
datos["fecha"] = pd.to_datetime(datos["fecha"])

print(datos.dtypes)
```

`pd.to_datetime()` interpreta fechas. En datos ambiguos conviene definir formato y estrategia de errores de manera explícita.

# 25. Ordenar y resumir

```python
import pandas as pd

datos = pd.DataFrame(
    {
        "programa": ["Datos", "Sistemas", "Datos", "Software"],
        "nota": [4.5, 3.2, 3.5, 4.5],
    }
)

print(datos.sort_values("nota", ascending=False))
print(datos.sort_index())
print(datos["nota"].mean())
print(datos["nota"].sum())
print(datos["nota"].min())
print(datos["nota"].max())
print(datos["nota"].count())
print(datos["nota"].median())
print(datos["programa"].value_counts())
print(datos["programa"].unique())
print(datos["programa"].nunique())
```

`sort_values()` ordena por valores y `sort_index()` por índice. `count()` cuenta valores no faltantes. `value_counts()` produce frecuencias, `unique()` los valores distintos y `nunique()` su cantidad.

# 26. `groupby()`: dividir, agregar y combinar

Agrupar es una operación central:

```python
import pandas as pd

datos = pd.DataFrame(
    {
        "programa": ["Datos", "Datos", "Sistemas"],
        "jornada": ["Día", "Noche", "Día"],
        "nota": [4.5, 3.5, 4.0],
    }
)

promedios = datos.groupby("programa")["nota"].mean()
resumen = datos.groupby("programa", as_index=False)["nota"].agg(
    ["count", "mean", "max"]
)
por_programa_jornada = datos.groupby(
    ["programa", "jornada"], as_index=False
)["nota"].mean()

print(promedios)
print(resumen)
print(por_programa_jornada)
```

`groupby()` divide filas según las claves, aplica la agregación y combina resultados. Con `as_index=False`, las claves permanecen como columnas, lo que facilita seguir transformando un DataFrame.

También podemos nombrar resultados de forma explícita:

```python
import pandas as pd

datos = pd.DataFrame(
    {"programa": ["Datos", "Datos", "Sistemas"], "nota": [4.5, 3.5, 4.0]}
)
resumen = datos.groupby("programa", as_index=False).agg(
    cantidad=("nota", "count"),
    promedio=("nota", "mean"),
    maxima=("nota", "max"),
)

print(resumen)
```

# 27. Tabla dinámica: introducción

Una tabla dinámica resume valores cruzando categorías:

```python
import pandas as pd

datos = pd.DataFrame(
    {
        "programa": ["Datos", "Datos", "Sistemas"],
        "jornada": ["Día", "Noche", "Día"],
        "nota": [4.5, 3.5, 4.0],
    }
)
tabla = pd.pivot_table(
    datos,
    values="nota",
    index="programa",
    columns="jornada",
    aggfunc="mean",
)

print(tabla)
```

Aquí basta reconocer que `pivot_table()` organiza una agregación en filas y columnas.

# 28. Combinar DataFrames con `merge()`

```python
import pandas as pd

estudiantes = pd.DataFrame(
    {"nombre": ["Ana", "Luis", "Marta"], "programa_id": [1, 2, 3]}
)
programas = pd.DataFrame(
    {"programa_id": [1, 2], "programa": ["Datos", "Sistemas"]}
)

coincidencias = pd.merge(estudiantes, programas, on="programa_id", how="inner")
todos_estudiantes = pd.merge(estudiantes, programas, on="programa_id", how="left")

print(coincidencias)
print(todos_estudiantes)
```

`inner` conserva coincidencias en ambas tablas; `left` conserva todas las filas de la izquierda. `right` conserva las de la derecha y `outer`, las de ambos lados. Verifica claves, cantidad de filas y valores faltantes: un `inner` puede descartar silenciosamente estudiantes sin programa coincidente.

# 29. Concatenar tablas similares

```python
import pandas as pd

grupo_a = pd.DataFrame({"nombre": ["Ana"], "nota": [4.5]})
grupo_b = pd.DataFrame({"nombre": ["Luis"], "nota": [3.8]})
todos = pd.concat([grupo_a, grupo_b], ignore_index=True)

print(todos)
```

`concat()` apila aquí filas con columnas semejantes. No reemplaza `merge()`: concatenar reúne bloques; combinar relaciona mediante claves.

# 30. Duplicados y nombres de columnas

```python
import pandas as pd

datos = pd.DataFrame(
    {"codigo": ["E01", "E01", "E02"], "nombre_estudiante": ["Ana", "Ana", "Luis"]}
)

print(datos.duplicated(subset="codigo"))
sin_repetidos = datos.drop_duplicates(subset="codigo", keep="first")
renombrado = sin_repetidos.rename(columns={"nombre_estudiante": "nombre"})

print(renombrado)
```

`duplicated()` detecta y `drop_duplicates()` elimina según un criterio. Dos nombres iguales pueden pertenecer a personas diferentes: define qué columnas forman realmente un duplicado antes de borrar.

# 31. Exportar CSV y JSON

Después de revisar la ruta, puedes exportar sin convertir el índice en una columna artificial:

```python
datos.to_csv("salida.csv", index=False)
datos.to_json("salida.json", orient="records", force_ascii=False)
```

Las orientaciones de JSON cambian su estructura; `records` produce una colección de registros. Estos ejemplos muestran la API, pero no se ejecutan durante la validación del curso para no dejar archivos generados.

No sobrescribas el origen. Una organización posible es:

```text
data/
├── original/
└── procesados/
```

# 32. Un pipeline reproducible

```text
leer
  ↓
inspeccionar
  ↓
limpiar nombres
  ↓
convertir tipos
  ↓
tratar faltantes
  ↓
validar
  ↓
analizar
  ↓
exportar
```

Un análisis reproducible permite repetir los mismos pasos sobre los mismos datos. Las funciones y scripts dejan decisiones visibles; una serie de ediciones manuales difíciles de recordar no.

```python
import pandas as pd

def limpiar_nombres(datos: pd.DataFrame) -> pd.DataFrame:
    limpio = datos.copy()
    limpio.loc[:, "nombre"] = limpio["nombre"].str.strip().str.title()
    return limpio
```

La función recibe sus datos, produce otro DataFrame y no depende de una variable global. `copy()` expresa que no deseamos mutar la entrada y `.loc` hace explícita la asignación. pandas ha evolucionado respecto a vistas, copias y advertencias como `SettingWithCopyWarning`; para esta unidad basta trabajar sobre copias explícitas y seleccionar con `.loc`.

## 💡 Experimenta

Ejecuta `limpiar_nombres()` y compara antes y después. Añade espacios a un nombre, llama de nuevo a la función y comprueba que el DataFrame original conserva esos espacios.

# 33. El proyecto de análisis académico

```text
proyecto_analisis/
├── analisis.py
├── datos.csv
└── tests/
    └── test_analisis.py
```

El CSV contiene doce registros ficticios, varios programas, espacios exteriores, una nota ausente y una nota repetida razonable. No contiene información personal real.

`analisis.py` ofrece:

- `cargar_datos(ruta)`: lee y valida columnas.
- `limpiar_datos(datos)`: normaliza textos y tipos sobre una copia, descarta registros sin identificadores esenciales y conserva notas faltantes como `NaN`.
- `filtrar_aprobados(datos)`: selecciona notas mayores o iguales a `3.0`.
- `resumen_por_programa(datos)`: calcula cantidad, promedio y máximo.
- `estudiante_mejor_nota(datos)`: devuelve la primera fila con la nota máxima o `None`.
- `main()`: carga el archivo local y muestra resultados; no escribe salidas.

Desde la carpeta del proyecto:

```bash
python analisis.py
python -m pytest -v
```

# 34. Probar transformaciones de datos

Los tests crean DataFrames pequeños cuando eso hace más claro el escenario y usan `tmp_path` para CSV temporales. Para igualdad estructural:

```python
import pandas as pd

esperado = pd.DataFrame({"nota": [3.0, 4.0]})
resultado = pd.DataFrame({"nota": [3.0, 4.0]})

pd.testing.assert_frame_equal(resultado, esperado)
pd.testing.assert_series_equal(resultado["nota"], esperado["nota"])
```

`resultado == esperado` devuelve comparaciones elemento a elemento, no un único booleano. En pruebas detalladas usa `pd.testing`; `.equals()` también sirve cuando basta una respuesta booleana sobre igualdad estructural.

# 35. Errores frecuentes

- Confundir una lista con un `ndarray` y esperar la misma API en todo.
- Olvidar dimensiones o combinar arrays con `shape` incompatible.
- Escribir ciclos cuando existe una operación vectorizada clara.
- Confundir una `Series` con un `DataFrame`.
- Usar `and` u `or` con Series, u olvidar paréntesis con `&` y `|`.
- Suponer que `read_csv()` siempre infiere el tipo correcto.
- Eliminar `NaN` sin medir la pérdida de información.
- Rellenar faltantes con cero, media o mediana sin justificación.
- Forzar tipos y ocultar valores que no pudieron convertirse.
- Modificar los datos originales accidentalmente.
- Usar `apply()` para toda transformación.
- Eliminar duplicados sin definir qué significa “duplicado”.
- Hacer `merge()` con claves incorrectas o ignorar filas perdidas en un `inner`.
- Confiar únicamente en `describe()` para interpretar un problema.
- Confundir correlación con causalidad.
- Realizar pasos manuales imposibles de reproducir.
- Comparar DataFrames con `==` esperando un solo booleano.

# 36. Ejercicios

## Ejercicio 1 — Primer array

Crea un array con cinco edades y muestra su tipo.

## Ejercicio 2 — Forma y dimensiones

Crea una matriz de tres filas y dos columnas; consulta `shape` y `ndim`.

## Ejercicio 3 — Tipo del array

Crea arrays de enteros y decimales, compara sus `dtype` y explica el resultado observado.

## Ejercicio 4 — Vectorización

Convierte un array de precios en precios con un incremento del 10 %, sin ciclo explícito.

## Ejercicio 5 — Filtro NumPy

Selecciona de un array las notas entre `3.0` y `5.0` usando una máscara booleana.

## Ejercicio 6 — Primera Series

Crea una `Series` de notas cuyo índice contenga nombres ficticios.

## Ejercicio 7 — Primer DataFrame

Crea una tabla con código, nombre, programa y nota desde un diccionario.

## Ejercicio 8 — Leer CSV

Carga `datos.csv` y comprueba la cantidad de filas y columnas sin modificarlo.

## Ejercicio 9 — Inspección

Usa `head()`, `info()` y `dtypes`; registra dos observaciones sobre calidad de datos.

## Ejercicio 10 — Selección

Obtén primero la Series `nota` y luego un DataFrame con `nombre` y `nota`.

## Ejercicio 11 — `loc`

Selecciona nombres y notas de estudiantes del programa Datos mediante una condición.

## Ejercicio 12 — `iloc`

Selecciona las tres primeras filas y las dos primeras columnas por posición.

## Ejercicio 13 — Filtrado

Obtén estudiantes de Sistemas con nota mayor o igual a `3.0`; usa paréntesis y `&`.

## Ejercicio 14 — Columna calculada

Crea `nota_porcentaje` a partir de la escala de cero a cinco.

## Ejercicio 15 — Faltantes

Cuenta los faltantes por columna y propone, sin aplicar todavía, una estrategia razonada.

## Ejercicio 16 — Conversión numérica

Convierte una columna textual con `pd.to_numeric(errors="coerce")` y cuenta los nuevos `NaN`.

## Ejercicio 17 — Ordenamiento

Ordena estudiantes por nota descendente y después restaura el orden del índice.

## Ejercicio 18 — Frecuencias

Cuenta estudiantes por programa con `value_counts()`.

## Ejercicio 19 — Agrupación

Calcula la nota media por programa con `groupby()`.

## Ejercicio 20 — Varias agregaciones

Obtén cantidad, media y máximo de nota por programa mediante `agg()`.

## Ejercicio 21 — Combinación

Crea una segunda tabla de programas y compárala al combinar con `inner` y `left`.

## Ejercicio 22 — Duplicados

Detecta códigos repetidos, decide qué fila conservar y justifica el criterio antes de eliminar.

## Ejercicio 23 — Exportación

Exporta una copia limpia a una carpeta de práctica con `index=False`; comprueba sus encabezados y elimina manualmente tu archivo al terminar.

## Ejercicio 24 — Función de limpieza

Escribe una función que reciba un DataFrame, copie, normalice nombres y devuelva el resultado.

## Ejercicio 25 — Prueba de DataFrame

Prueba la función anterior con `pd.testing.assert_frame_equal` y verifica que la entrada no cambió.

## Ejercicio 26 — Análisis completo

Formula una pregunta sobre `datos.csv` y construye un flujo de carga, inspección, limpieza, resumen e interpretación.

No consultes soluciones completas. Trabaja sobre copias y conserva siempre el CSV original.

# 37. Reto — Análisis académico reproducible

Construye tu propio análisis sobre el dataset local. Debe:

1. Cargar el CSV.
2. Inspeccionar estructura y tipos.
3. Limpiar nombres.
4. Convertir edades y notas.
5. Identificar faltantes.
6. Definir y documentar su tratamiento.
7. Identificar duplicados con un criterio explícito.
8. Calcular estudiantes aprobados.
9. Calcular el promedio general.
10. Obtener el promedio por programa.
11. Obtener la mejor nota por programa.
12. Contar estudiantes por programa.
13. Crear una columna `estado`.
14. Ordenar los resultados.
15. Exportar el dataset limpio sin sobrescribir el original.

Organiza la solución en funciones y crea pruebas para limpieza, filtrado y agregación. No uses red, bases externas, machine learning ni notebooks obligatorios. No se entrega la solución completa.

# 38. Comprobación de aprendizaje

- [ ] Explico el papel básico de NumPy y pandas.
- [ ] Creo un `ndarray` y consulto `shape`, `ndim` y `dtype`.
- [ ] Uso vectorización, agregaciones y filtrado booleano.
- [ ] Reconozco y detecto `NaN`.
- [ ] Distingo `Series` y `DataFrame`.
- [ ] Cargo un CSV local e inspecciono estructura, tipos y resumen.
- [ ] Selecciono con corchetes, `loc` e `iloc`.
- [ ] Combino filtros mediante `&`, `|` y paréntesis.
- [ ] Creo columnas mediante operaciones vectorizadas.
- [ ] Uso `apply()` y `map()` solo cuando aportan claridad.
- [ ] Detecto faltantes y justifico `dropna()` o `fillna()`.
- [ ] Convierto datos con `astype()`, `to_numeric()` y `to_datetime()`.
- [ ] Ordeno y uso `value_counts()`, `unique()` y `nunique()`.
- [ ] Agrupo con `groupby()`, `agg()` y `as_index=False`.
- [ ] Reconozco una tabla dinámica básica.
- [ ] Combino mediante `merge()` y `concat()`.
- [ ] Detecto duplicados y renombro columnas.
- [ ] Exporto CSV con `index=False` y JSON con una orientación elegida.
- [ ] Conservo originales y organizo transformaciones reproducibles.
- [ ] Pruebo DataFrames y Series con `pd.testing`.

# 39. Lo que aprendimos

```text
CSV
 ↓
DataFrame
 ↓
inspección
 ↓
limpieza
 ↓
transformación
 ↓
agrupación
 ↓
análisis
 ↓
resultado
```

Ahora podemos procesar y analizar datos estructurados mediante pasos repetibles. La siguiente unidad utilizará Python para automatizar tareas repetitivas del sistema y el procesamiento de archivos.

---

# 🧭 Navegación

⬅️ [Volver a la Unidad 17 — Concurrencia](../unidad17-concurrencia/)

🏠 [Volver al inicio del curso](../README.md)

➡️ [Continuar a la Unidad 19 — Automatización](../unidad19-automatizacion/)
