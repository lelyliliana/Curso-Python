# Unidad 19 — Automatización con Python

[Volver al índice del curso](../README.md) · [Ver el curso en Aprende con Leli](https://lelyliliana.github.io/aprende-con-leli/cursos/python/)

Muchas tareas con archivos siguen reglas sencillas pero consumen tiempo cuando se repiten. En esta unidad aprenderás a convertir esas reglas en scripts seguros, observables y comprobables.

---

## 🎯 Objetivos de aprendizaje

Al finalizar podrás:

- Identificar cuándo conviene automatizar una tarea.
- Explorar y construir rutas portables con `pathlib`.
- Crear, copiar, mover, renombrar y eliminar con controles previos.
- Procesar archivos por lotes y trabajar en directorios temporales.
- Crear respaldos, archivos ZIP y hashes de integridad.
- Configurar scripts con variables de entorno y argumentos CLI.
- Ejecutar procesos externos de forma controlada.
- Registrar eventos con `logging`.
- Diseñar automatizaciones repetibles e idempotentes a nivel básico.
- Probar operaciones de archivos sin tocar datos reales.

---

## 📋 Antes de comenzar

Necesitas haber completado la Unidad 18. Retomaremos funciones, archivos, excepciones, módulos, context managers, type hints, variables de entorno y pytest.

Todos los módulos de esta unidad pertenecen a la biblioteca estándar. Pytest solo es necesario para ejecutar el proyecto de pruebas. No usaremos red, scraping, automatización de navegador, CI/CD ni administración avanzada del sistema.

> **Regla central:** primero lista, después simula y únicamente entonces modifica. Practica siempre en una carpeta temporal o desechable.

---

# 1. ¿Qué significa automatizar?

```text
Tarea manual repetitiva
        ↓
reglas claras
        ↓
script Python
        ↓
ejecución automática y repetible
```

Podemos organizar archivos, renombrar documentos, procesar varios CSV, generar reportes, copiar respaldos, verificar carpetas o ejecutar herramientas externas.

Conviene automatizar cuando la tarea se repite, sus reglas son relativamente estables, existe riesgo de errores manuales, ahorra tiempo y podemos validar el resultado. No siempre compensa: una tarea única y breve, reglas ambiguas o una operación de alto riesgo sin controles pueden ser mejores candidatas para revisión humana.

# 2. Automatizar con seguridad y `dry run`

Un **dry run** muestra lo que ocurriría sin aplicar cambios:

```text
leer y listar
      ↓
validar reglas
      ↓
simular cambios
      ↓
revisar el plan
      ↓
aplicar cambios
```

```python
def mostrar_accion(origen: str, destino: str, dry_run: bool = True) -> None:
    if dry_run:
        print(f"Simular: {origen} -> {destino}")
        return
    print(f"Ejecutar: {origen} -> {destino}")

mostrar_accion("entrada/datos.csv", "salida/csv/datos.csv")
```

Una simulación no sustituye backups, permisos mínimos, pruebas ni revisión de colisiones, pero reduce sorpresas.

# Parte I — Rutas y operaciones con archivos

# 3. `pathlib` como herramienta principal

`Path` representa rutas sin concatenar separadores manualmente:

```python
from pathlib import Path

actual = Path.cwd()
personal = Path.home()
ruta = Path("datos") / "entrada"

print(actual)
print(personal.name)
print(ruta)
```

`cwd()` indica el directorio actual y `home()` la carpeta personal. No escribas rutas personales dentro del código; usa rutas relativas, argumentos o configuración.

# 4. Comprobar rutas

```python
from pathlib import Path

ruta = Path("datos")

print(ruta.exists())
print(ruta.is_file())
print(ruta.is_dir())
```

`exists()` comprueba existencia; `is_file()` y `is_dir()` distinguen archivo y directorio. El estado puede cambiar después de comprobarlo, por lo que también debemos manejar errores de la operación.

# 5. Crear carpetas

Este ejemplo debe ejecutarse solo en una carpeta de práctica:

```python
from pathlib import Path

ruta = Path("practica") / "salida" / "csv"
ruta.mkdir(parents=True, exist_ok=True)
```

`parents=True` crea padres ausentes y `exist_ok=True` permite repetir la operación si la carpeta ya existe. Este es un ejemplo básico de idempotencia.

# 6. Iterar un directorio

```python
from pathlib import Path

carpeta = Path("entrada")

if carpeta.is_dir():
    for elemento in sorted(carpeta.iterdir()):
        print(elemento.name)
```

`iterdir()` entrega elementos directos. `sorted()` proporciona un orden estable, útil para planes y pruebas reproducibles.

# 7. Patrones con `glob()` y `rglob()`

```python
from pathlib import Path

carpeta = Path("entrada")
csv_directos = sorted(carpeta.glob("*.csv"))
txt_recursivos = sorted(carpeta.rglob("*.txt"))

print(csv_directos)
print(txt_recursivos)
```

`glob()` busca según un patrón; `rglob()` desciende por subcarpetas. El patrón `*.csv` no garantiza que el contenido sea un CSV válido.

# 8. Nombre, raíz y sufijo

```python
from pathlib import Path

archivo = Path("reportes") / "reporte_2026.csv"

print(archivo.name)
print(archivo.stem)
print(archivo.suffix)
print(archivo.with_suffix(".json"))
```

`name` es `reporte_2026.csv`, `stem` es `reporte_2026` y `suffix` es `.csv`. `with_suffix()` construye otra ruta; no renombra el archivo por sí solo.

# 9. Renombrar sin sobrescribir

`Path.rename()` cambia la ruta de un archivo. Antes hay que comprobar el destino y definir una política: abortar, omitir o crear otro nombre.

```python
from pathlib import Path

origen = Path("practica") / "documento1.txt"
destino = origen.with_name("documento_001.txt")

if destino.exists():
    raise FileExistsError(f"El destino ya existe: {destino}")

# Ejecuta esta línea solo después de revisar ambas rutas:
# origen.rename(destino)
```

La comprobación debe ocurrir también en modo real, no solo en la simulación.

# 10. Copiar y mover

`shutil` reúne operaciones de nivel más alto:

```python
from pathlib import Path
import shutil

origen = Path("practica") / "entrada" / "datos.csv"
destino = Path("practica") / "salida" / "datos.csv"

if origen.is_file() and not destino.exists():
    destino.parent.mkdir(parents=True, exist_ok=True)
    # shutil.copy2(origen, destino)
    # shutil.move(origen, destino)
```

`copy2()` copia contenido e intenta conservar metadatos habituales; `copy()` conserva menos metadatos. `move()` mueve archivos o directorios. Para construir e inspeccionar rutas preferimos `Path`; para copias y movimientos, `shutil` resulta claro.

# 11. Copiar directorios

```python
from pathlib import Path
import shutil

origen = Path("practica") / "entrada"
destino = Path("practica") / "copia_entrada"

if origen.is_dir() and not destino.exists():
    # Quita el comentario únicamente dentro de una práctica controlada.
    # shutil.copytree(origen, destino)
    pass
```

`copytree()` copia un árbol completo. Verifica tamaño, destino y espacio disponible antes de usarlo.

# 12. Eliminar exige una advertencia especial

- `Path.unlink()` elimina un archivo o enlace.
- `Path.rmdir()` elimina un directorio vacío.
- `shutil.rmtree()` elimina recursivamente un árbol y es especialmente peligroso.

No ejecutaremos estas operaciones sobre el repositorio. Para experimentar, utiliza `TemporaryDirectory`, valida una ruta específica y lista primero su contenido. Una eliminación no debe construirse con una ruta amplia, un glob sin revisar ni una variable vacía.

# 13. Renombrado por lotes

Un plan estable puede transformar `documento1.txt` en `documento_001.txt`:

```python
from pathlib import Path

carpeta = Path("documentos")

for numero, archivo in enumerate(sorted(carpeta.glob("*.txt")), start=1):
    destino = archivo.with_name(f"documento_{numero:03d}.txt")
    print(f"Simular: {archivo.name} -> {destino.name}")
```

`enumerate()` numera, `:03d` rellena con ceros y `sorted()` evita un orden accidental. Antes del modo real, comprueba todas las colisiones; así una colisión tardía no deja un lote a medias.

# 14. Procesamiento por lotes

```python
from pathlib import Path

def procesar(archivo: Path) -> None:
    print(f"Procesando {archivo.name}")

carpeta = Path("entrada")
for archivo in sorted(carpeta.glob("*.csv")):
    procesar(archivo)
```

Esto conecta con la Unidad 18: cada CSV podría cargarse, limpiarse y guardarse en una carpeta de procesados. Separa funciones como `buscar_archivos()`, `validar_archivo()`, `procesar_archivo()` y `guardar_resultado()` en lugar de construir una función gigante.

Una estructura segura distingue responsabilidades:

```text
proyecto/
├── entrada/
├── salida/
└── respaldo/
```

# 15. Archivos y carpetas temporales

`tempfile` crea recursos temporales administrados:

```python
from pathlib import Path
from tempfile import TemporaryDirectory

with TemporaryDirectory() as carpeta_temporal:
    ruta = Path(carpeta_temporal) / "ejemplo.txt"
    ruta.write_text("dato temporal", encoding="utf-8")
    print(ruta.read_text(encoding="utf-8"))
```

Al salir del `with`, la carpeta se limpia. `NamedTemporaryFile` ofrece un archivo temporal con nombre; sus detalles de reapertura pueden variar entre sistemas, por lo que aquí preferimos una carpeta temporal. Pytest ofrece `tmp_path` con una finalidad semejante por prueba.

# Parte II — Respaldos e integridad

# 16. Copia antes de modificar

```text
archivo original
       ↓
crear backup
       ↓
verificar backup
       ↓
modificar copia o destino
```

El respaldo debe ubicarse en un destino conocido y no sobrescribirse silenciosamente.

# 17. Nombres con fecha y hora

```python
from datetime import datetime

marca = datetime.now().strftime("%Y%m%d_%H%M%S")
nombre = f"reporte_{marca}.csv"

print(nombre)
```

El formato representa año, mes, día, hora, minuto y segundo. No dependas de un instante exacto en pruebas: inyecta una marca fija cuando debas comprobar el nombre.

# 18. Crear un ZIP

```python
from pathlib import Path
import shutil

ruta_origen = Path("practica") / "respaldo"

if ruta_origen.is_dir():
    # Crea respaldo.zip; úsalo solo en la carpeta de práctica.
    shutil.make_archive("respaldo", "zip", ruta_origen)
```

`shutil.make_archive()` cubre respaldos sencillos. El módulo `zipfile` permite controlar entradas y compresión con más detalle, pero no profundizaremos todavía.

# 19. Hash SHA-256

Un hash es una huella del contenido, no cifrado. Leer por bloques evita cargar archivos enormes completos:

```python
import hashlib
from pathlib import Path

def calcular_hash(archivo: Path) -> str:
    huella = hashlib.sha256()
    with archivo.open("rb") as flujo:
        while bloque := flujo.read(65_536):
            huella.update(bloque)
    return huella.hexdigest()
```

Si original y copia producen la misma huella, sus contenidos coinciden con una confianza práctica muy alta. Esto ayuda a verificar copias y detectar cambios, pero no demuestra por sí solo procedencia, permisos ni seguridad completa.

# Parte III — Configuración y CLI

# 20. Variables de entorno

```python
import os
from pathlib import Path

carpeta_entrada = Path(os.getenv("CARPETA_ENTRADA", "entrada"))
print(carpeta_entrada)
```

Evita rutas hardcodeadas. Un orden sencillo es: argumento CLI explícito, después variable de entorno y finalmente valor predeterminado. No uses necesariamente secretos como ejemplo y nunca los muestres en logs.

# 21. De `sys.argv` a `argparse`

`sys.argv` contiene las cadenas recibidas por el proceso. Analizarlas a mano se vuelve frágil; `argparse` genera validación sintáctica y ayuda:

```python
from argparse import ArgumentParser

parser = ArgumentParser(description="Inspecciona una carpeta")
parser.add_argument("ruta")
parser.add_argument("--salida", default="salida")
parser.add_argument("--dry-run", action="store_true")
args = parser.parse_args()

print(args.ruta, args.salida, args.dry_run)
```

`-h` y `--help` se generan automáticamente. `action="store_true"` produce `True` cuando aparece la opción. argparse comprueba la forma de los argumentos; reglas como “la carpeta debe existir” pertenecen a la lógica del programa.

# 22. Un `main()` comprobable

```python
from argparse import ArgumentParser

def main(argv: list[str] | None = None) -> int:
    parser = ArgumentParser()
    parser.add_argument("ruta")
    args = parser.parse_args(argv)
    print(f"Ruta: {args.ruta}")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
```

`parse_args(argv)` permite pasar una lista desde pruebas. Por convención, `0` representa éxito y un código distinto indica error, aunque sus significados concretos dependen de cada herramienta. `main()` devuelve el código; `SystemExit` lo convierte en la salida del proceso. El main guard impide ejecutar acciones al importar.

# Parte IV — Procesos externos

# 23. `subprocess.run()`

```python
import subprocess
import sys

resultado = subprocess.run(
    [sys.executable, "--version"],
    capture_output=True,
    text=True,
    check=True,
    timeout=10,
)

print(resultado.stdout or resultado.stderr)
```

Usamos una lista de argumentos y `sys.executable` para invocar el mismo intérprete. `capture_output=True` captura `stdout` y `stderr`; `text=True` los entrega como texto; `timeout` evita una espera ilimitada; `check=True` lanza `subprocess.CalledProcessError` ante un código distinto de cero. Sin `check=True`, inspecciona `resultado.returncode`.

# 24. No usar `shell=True` por defecto

El shell interpreta caracteres y expansiones. Construir un comando como cadena con datos externos puede permitir inyección de comandos. Prefiere:

```python
import subprocess

nombre_archivo = "reporte mensual.txt"
resultado = subprocess.run(
    ["herramienta", "--archivo", nombre_archivo],
    capture_output=True,
    text=True,
    timeout=30,
)
print(resultado.returncode)
```

Este bloque es ilustrativo: requiere una herramienta ficticia y no debe ejecutarse. Usa una lista y el valor predeterminado `shell=False`. También es posible invocar `[sys.executable, "-m", "pytest"]`, pero las pruebas de este proyecto no ejecutan pytest recursivamente.

Git y otras herramientas pueden automatizarse con `subprocess`, pero aquí no crearemos scripts que hagan commit o push.

# Parte V — Registro y robustez

# 25. `print` y `logging`

`print()` ofrece salida directa al usuario. `logging` registra eventos del funcionamiento:

```python
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

logger.debug("Detalles para diagnóstico")
logger.info("Proceso iniciado")
logger.warning("Archivo omitido")
logger.error("No fue posible procesar el archivo")
```

Los niveles son `DEBUG`, `INFO`, `WARNING`, `ERROR` y `CRITICAL`. No estudiaremos handlers complejos. Nunca registres contraseñas, tokens ni claves API.

# 26. Errores por archivo

```python
from pathlib import Path
import logging

logger = logging.getLogger(__name__)

def procesar_archivos(archivos: list[Path]) -> tuple[int, int]:
    procesados = 0
    errores = 0
    for archivo in archivos:
        try:
            archivo.read_text(encoding="utf-8")
        except (OSError, UnicodeError) as error:
            errores += 1
            logger.error("Archivo %s: %s", archivo.name, error)
        else:
            procesados += 1
    return procesados, errores
```

No captures `Exception` para continuar silenciosamente. Un backup crítico quizá deba fallar rápido; cien archivos independientes quizá permitan continuar y resumir procesados, omitidos y errores.

# 27. Idempotencia y checkpoints

Una operación idempotente puede repetirse sin duplicar o volver inconsistente el resultado. `mkdir(exist_ok=True)` es un ejemplo sencillo. Una organización puede omitir archivos ya procesados o rechazar destinos existentes en vez de reemplazarlos.

Los procesos largos pueden guardar un **checkpoint** con los elementos completados para reanudar, pero requieren diseño cuidadoso. No estudiaremos reentrancia ni construiremos un sistema complejo en esta unidad.

# 28. Ejecución programada y portabilidad

Un script probado puede ejecutarse manualmente, mediante cron en sistemas compatibles, con el Programador de tareas de Windows o dentro de CI/CD. Aquí solo reconocemos esas opciones: no modificaremos la configuración del sistema.

Para scripts portables:

- Usa `Path` en vez de separadores manuales.
- Evita rutas absolutas personales.
- Usa `sys.executable` al invocar Python.
- No asumas que todos los comandos existen en cada sistema.
- Documenta argumentos, permisos y directorio de ejecución.

# 29. Proyecto real: organizador seguro

```text
proyecto_automatizacion/
├── automatizador.py
├── cli.py
└── tests/
    └── test_automatizador.py
```

`automatizador.py` incluye:

- `buscar_archivos()`: lista archivos directos en orden estable y filtra extensión.
- `crear_respaldo()`: copia con timestamp sin sobrescribir.
- `calcular_hash()`: calcula SHA-256 por bloques.
- `organizar_archivos()`: planifica y después organiza por extensión.

```text
entrada/              salida/
├── informe.pdf       ├── csv/datos.csv
├── datos.csv    →    ├── pdf/informe.pdf
└── notas.txt         └── txt/notas.txt
```

La función valida **todas** las colisiones antes de mover el primer archivo. Con `dry_run=True` devuelve el mismo plan, pero no crea carpetas ni mueve datos.

# 30. CLI real

Desde `proyecto_automatizacion/`:

```bash
python cli.py entrada --destino salida --extension .csv --dry-run
python cli.py entrada --destino salida --ejecutar
python cli.py --help
```

La simulación es el modo predeterminado. `--ejecutar` debe escribirse expresamente para mover. `main(argv=None) -> int` separa parseo, lógica y salida, y ningún módulo modifica archivos al importarse.

# 31. Pruebas aisladas

La suite utiliza `tmp_path`; nunca toca archivos del repositorio:

```python
from pathlib import Path

def test_escribir_en_temporal(tmp_path: Path) -> None:
    archivo = tmp_path / "dato.txt"
    archivo.write_text("seguro", encoding="utf-8")

    assert archivo.read_text(encoding="utf-8") == "seguro"
```

También inyecta una marca fija al probar respaldos. Una función relacionada con procesos externos debería sustituir `subprocess.run` mediante `monkeypatch` o `Mock`; no necesitamos ejecutar comandos reales en esta suite.

```bash
cd unidad19-automatizacion/ejemplos/proyecto_automatizacion
python -m pytest -v
```

# 32. Errores frecuentes

- Hardcodear rutas personales o concatenarlas como cadenas.
- Eliminar sin comprobar o usar `shutil.rmtree()` sin límites claros.
- Sobrescribir destinos o descubrir una colisión después de medio lote.
- Modificar originales sin respaldo cuando el riesgo lo requiere.
- Carecer de dry run o hacer que la simulación modifique carpetas.
- Capturar todos los errores y continuar silenciosamente.
- Usar `shell=True` con datos externos o construir comandos mediante cadenas.
- Ignorar `returncode`, `check=True` y timeouts.
- Hardcodear `python` cuando `sys.executable` es más robusto.
- Ejecutar acciones al importar un módulo.
- Crear una CLI imposible de probar o mezclar parseo con toda la lógica.
- Usar `print()` para todos los eventos internos.
- Registrar secretos.
- Suponer que una ejecución exitosa garantiza seguridad futura.

# 33. Ejercicios

## Ejercicio 1 — Construir una ruta

Crea con `Path` una ruta relativa para `entrada/reportes`, sin concatenar cadenas.

## Ejercicio 2 — Crear carpetas

Dentro de una práctica temporal, crea `salida/csv` con padres y repetición segura.

## Ejercicio 3 — `iterdir()`

Lista en orden estable archivos y carpetas directos, indicando su tipo.

## Ejercicio 4 — `glob()`

Encuentra únicamente CSV directos y explica qué no valida el patrón.

## Ejercicio 5 — `rglob()`

Busca TXT de forma recursiva y compara el resultado con `glob()`.

## Ejercicio 6 — Partes del nombre

Muestra `name`, `stem` y `suffix` de tres nombres diferentes.

## Ejercicio 7 — Renombrado

Diseña primero un plan para renombrar documentos con numeración de tres dígitos.

## Ejercicio 8 — Copia

Copia un archivo temporal con `copy2()` y verifica su contenido.

## Ejercicio 9 — Movimiento

Mueve un archivo entre dos carpetas temporales y comprueba ambas rutas.

## Ejercicio 10 — Dry run

Añade un parámetro `dry_run=True` y demuestra que no modifica nada.

## Ejercicio 11 — Colisiones

Haz que tu función aborte antes de modificar si cualquier destino existe.

## Ejercicio 12 — Lote

Procesa varios CSV con funciones separadas para buscar, validar y procesar.

## Ejercicio 13 — `TemporaryDirectory`

Crea un archivo dentro de un context manager y observa cuándo desaparece.

## Ejercicio 14 — Backup

Crea una copia antes de transformar un archivo y conserva el original.

## Ejercicio 15 — Timestamp

Genera un nombre con fecha y hora; prueba el formato con una marca inyectada.

## Ejercicio 16 — ZIP

Comprime una carpeta temporal y comprueba que el ZIP fue creado.

## Ejercicio 17 — Hash

Calcula SHA-256 por bloques y verifica que una modificación cambia la huella.

## Ejercicio 18 — Variable de entorno

Obtén `CARPETA_ENTRADA` con un valor predeterminado portable.

## Ejercicio 19 — Primer `argparse`

Crea una CLI con una ruta posicional y ayuda descriptiva.

## Ejercicio 20 — Opción `--dry-run`

Añade simulación y decide cómo exigir confirmación para el modo real.

## Ejercicio 21 — Código de salida

Devuelve `0` ante éxito y otro código documentado ante ruta inválida.

## Ejercicio 22 — `subprocess`

Diseña una llamada con lista de argumentos, `sys.executable` y captura de salida.

## Ejercicio 23 — `check=True`

Explica y prueba con un mock cómo manejarías `CalledProcessError`.

## Ejercicio 24 — Timeout

Añade un límite y explica cómo tratarías `TimeoutExpired` sin ejecutar esperas reales.

## Ejercicio 25 — Logging

Registra un archivo procesado, uno omitido y un error sin datos sensibles.

## Ejercicio 26 — Idempotencia

Revisa qué ocurriría al ejecutar dos veces tu script y corrige duplicaciones.

## Ejercicio 27 — Diseño seguro

Diseña una automatización completa con validación, dry run, backup, errores y resumen.

No consultes soluciones completas ni practiques sobre archivos importantes.

# 34. Reto — Organizador y respaldo de archivos

Construye una herramienta CLI que:

1. Reciba una carpeta de entrada.
2. Inspeccione archivos.
3. Clasifique por extensión.
4. Permita dry run.
5. Cree respaldo antes de mover.
6. Evite sobrescrituras.
7. Calcule un hash opcional.
8. Registre operaciones.
9. Produzca un resumen final.

Interfaz sugerida:

```bash
python cli.py entrada --destino salida --backup respaldo --dry-run
```

Usa `pathlib`, `shutil`, `argparse`, `logging`, excepciones, funciones pequeñas, main guard y códigos de salida. Prueba todo con `tmp_path`; no uses rutas hardcodeadas, red ni `shell=True`. No se entrega la solución completa.

# 35. Comprobación de aprendizaje

- [ ] Identifico tareas que conviene y que no conviene automatizar.
- [ ] Construyo rutas con `Path` y uso `exists()`, `is_file()` e `is_dir()`.
- [ ] Creo directorios y recorro con `iterdir()`, `glob()` y `rglob()`.
- [ ] Copio, muevo y renombro con comprobaciones previas.
- [ ] Distingo `unlink()`, `rmdir()` y el peligro de `rmtree()`.
- [ ] Diseño un dry run que no modifica el filesystem.
- [ ] Evito colisiones antes de iniciar un lote.
- [ ] Uso `TemporaryDirectory` y `tmp_path`.
- [ ] Creo backups con timestamps comprobables.
- [ ] Creo ZIP y calculo hashes por bloques.
- [ ] Leo configuración desde variables de entorno.
- [ ] Construyo una CLI testeable con `argparse` y `main(argv=None)`.
- [ ] Utilizo códigos de salida y main guard.
- [ ] Ejecuto subprocess con lista, `check`, captura y timeout.
- [ ] Evito `shell=True` como patrón predeterminado.
- [ ] Distingo salida al usuario y eventos de logging.
- [ ] Diseño operaciones idempotentes a nivel introductorio.
- [ ] Manejo errores por archivo según el riesgo y genero un resumen.
- [ ] Mantengo scripts portables y sin acciones al importar.
- [ ] Pruebo automatizaciones sin tocar archivos reales.

# 36. Lo que aprendimos

```text
Tarea manual
    ↓
reglas
    ↓
script
    ↓
validación
    ↓
dry run
    ↓
automatización
    ↓
registro y resultado
```

Ya sabemos construir programas, APIs, pruebas, procesamiento de datos y automatizaciones. La siguiente unidad reunirá las prácticas necesarias para desarrollar proyectos Python con enfoque profesional.

---

# 🧭 Navegación

⬅️ [Volver a la Unidad 18 — Análisis de datos](../unidad18-datos/)

🏠 [Volver al inicio del curso](../README.md)

➡️ [Continuar a la Unidad 20 — Python profesional](../unidad20-python-profesional/)


---

## Continuar el curso

- **Unidad anterior:** [Unidad 18 — Análisis de datos con NumPy y pandas](../unidad18-datos/README.md)
- **Volver al índice:** [Todas las unidades](../README.md)
- **Siguiente unidad:** [Unidad 20 — Python profesional](../unidad20-python-profesional/README.md)
