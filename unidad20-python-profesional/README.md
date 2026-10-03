# Unidad 20 — Python profesional

[Volver al índice del curso](../README.md) · [Ver el curso en Aprende con Leli](https://lelyliliana.github.io/aprende-con-leli/cursos/python/)

Un programa no se vuelve profesional por ser grande. Se vuelve más sostenible cuando su estructura comunica responsabilidades, su configuración es explícita y otras personas pueden instalarlo, probarlo y modificarlo con confianza.

---

## 🎯 Objetivos de aprendizaje

Al finalizar podrás:

- Organizar un proyecto moderno con `pyproject.toml`, `src/` y tests.
- Separar modelos, servicios, configuración y logging.
- Leer y validar configuración desde variables de entorno.
- Evitar secretos, efectos secundarios y estado global.
- Comprender versionado, documentación, Git y revisión de código.
- Diferenciar formatter, linter, type checker y pruebas.
- Explicar pre-commit, CI/CD y empaquetado a nivel introductorio.
- Aplicar principios básicos de mantenibilidad y seguridad.

---

## 📋 Antes de comenzar

Necesitas haber completado la Unidad 19. Usaremos módulos, paquetes, entornos virtuales, pip, type hints, dataclasses, excepciones, pytest, variables de entorno y logging.

No estudiaremos Docker, Kubernetes, cloud, DevOps avanzado ni publicación real en PyPI. El proyecto central usa únicamente la biblioteca estándar; pytest aparece como dependencia opcional de desarrollo.

---

# 1. De script a proyecto

```text
script
  ↓
módulos
  ↓
paquete
  ↓
tests
  ↓
configuración
  ↓
documentación
  ↓
proyecto mantenible
```

Un solo `script.py` puede resolver una tarea pequeña. Al crecer las reglas y el equipo, separar piezas reduce el acoplamiento y facilita las pruebas. “Profesional” describe disciplina y adecuación al contexto, no cantidad de archivos.

# 2. Una estructura moderna

```text
proyecto/
├── pyproject.toml       metadatos, dependencias y herramientas
├── README.md            propósito, instalación, uso y pruebas
├── .gitignore           archivos locales que Git debe omitir
├── src/
│   └── paquete/         código importable
└── tests/               comportamiento comprobado
```

La estructura debe responder a necesidades reales. Un ejercicio de veinte líneas no necesita imitar un sistema empresarial.

# 3. `src` layout

```text
src/
└── gestor_tareas/
    ├── __init__.py
    ├── config.py
    ├── logging_config.py
    ├── modelos.py
    └── servicio.py
```

El **src layout** separa el código instalable de archivos del proyecto. Ayuda a comprobar que los imports usan el paquete instalado y no una carpeta encontrada por accidente. Es una estrategia útil, no una obligación universal.

# 4. `__init__.py` y API pública

`__init__.py` identifica el paquete tradicional y puede exponer una API mínima:

```python
from .modelos import Tarea
from .servicio import ServicioTareas

__all__ = ["ServicioTareas", "Tarea"]
```

Evita importar indiscriminadamente, ejecutar lógica, leer archivos o configurar logging al importar. Una API pública pequeña reduce dependencias accidentales y facilita cambios internos.

# Parte I — `pyproject.toml` y dependencias

# 5. El archivo moderno del proyecto

`pyproject.toml` es el archivo estándar moderno para metadatos, construcción, dependencias y configuración de herramientas. No aprenderemos aquí todos los estándares relacionados.

```toml
[project]
name = "gestor-tareas"
version = "0.1.0"
description = "Ejemplo de proyecto Python"
requires-python = ">=3.11"
dependencies = []
```

El nombre de distribución puede contener guiones (`gestor-tareas`); el paquete importable usa guion bajo (`gestor_tareas`). Como el ejemplo no necesita paquetes externos en ejecución, `dependencies` está vacío.

# 6. Dependencias de desarrollo

```toml
[project.optional-dependencies]
dev = ["pytest"]
```

Pytest ayuda a desarrollar, pero no es necesario para usar la lógica. Ruff y mypy también podrían formar parte de un grupo de desarrollo; no imponemos un gestor ni instalamos herramientas globalmente.

`requirements.txt` suele enumerar elementos instalables para un entorno concreto. `pyproject.toml` además contiene metadatos del proyecto, dependencias declaradas, packaging y configuración de herramientas. Pueden coexistir si el flujo lo justifica.

# 7. Sistema de construcción

```toml
[build-system]
requires = ["setuptools>=68"]
build-backend = "setuptools.build_meta"
```

El backend convierte el proyecto en artefactos instalables. Existen alternativas; no profundizaremos en ellas. Declararlo no instala ni construye nada por sí solo.

# 8. Instalación editable

Desde la raíz del mini proyecto y dentro de un entorno virtual:

```bash
python -m pip install -e ".[dev]"
```

El modo editable instala referencias al código de desarrollo: los cambios en `src/` se reflejan sin reinstalar en cada edición. Así los imports funcionan sin modificar `sys.path` manualmente.

Durante la validación de esta unidad no instalaremos el proyecto. Usaremos `PYTHONPATH=src` solo en el proceso temporal de pytest.

# Parte II — Configuración segura

# 9. Evitar valores hardcodeados

Carpetas de datos, nivel de logging, URL de un servicio y timeout pueden cambiar entre desarrollo, pruebas y producción. Mezclarlos dentro de la lógica obliga a editar código por entorno.

```python
import os

nivel = os.getenv("APP_LOG_LEVEL", "INFO")
carpeta = os.getenv("APP_DATA_DIR", "data")
```

Las variables de entorno son cadenas. Si necesitamos un entero o booleano debemos convertir y validar explícitamente:

```python
import os

timeout_texto = os.getenv("APP_TIMEOUT", "30")
timeout = int(timeout_texto)

debug_texto = os.getenv("APP_DEBUG", "false").strip().lower()
if debug_texto not in {"true", "false"}:
    raise ValueError("APP_DEBUG debe ser true o false")
debug = debug_texto == "true"
```

# 10. Una dataclass de configuración

```python
from dataclasses import dataclass
from pathlib import Path

@dataclass(frozen=True, slots=True)
class Config:
    log_level: str
    data_dir: Path
```

`frozen=True` evita reasignaciones accidentales y comunica estabilidad. `cargar_config()` lee el entorno, aplica valores predeterminados, normaliza, valida y devuelve `Config`; no crea una global al importar.

# 11. Secretos y `.env`

Claves API, contraseñas y tokens no deben quedar en código, commits ni logs. Un archivo `.env` local puede contener variables para desarrollo, pero Python no lo carga automáticamente y este proyecto no requiere `python-dotenv`.

`.env` debe estar ignorado. Un `.env.example` puede documentar únicamente nombres y valores ficticios:

```text
APP_LOG_LEVEL=INFO
APP_DATA_DIR=data
API_TOKEN=valor_local_no_real
```

No crearemos ese archivo porque no está entre los autorizados.

# Parte III — Logging y responsabilidades

# 12. Logger por módulo

```python
import logging

logger = logging.getLogger(__name__)

def procesar() -> None:
    logger.info("Proceso iniciado")
```

Cada módulo obtiene un logger con su nombre. No llama `basicConfig()` al importar: una biblioteca no debería alterar la configuración global de quien la usa.

# 13. Configuración centralizada

```python
import logging

def configurar_logging(nivel: str) -> None:
    logging.basicConfig(
        level=nivel,
        format="%(asctime)s %(levelname)s %(name)s: %(message)s",
    )
```

`basicConfig()` basta para aplicaciones pequeñas; sistemas mayores pueden necesitar handlers y configuración estructurada. Los niveles `DEBUG`, `INFO`, `WARNING`, `ERROR` y `CRITICAL` expresan severidad y propósito.

Dentro de un `except`, `logger.exception()` registra el mensaje y traceback activo:

```python
try:
    resultado = int("dato inválido")
except ValueError:
    logger.exception("No fue posible convertir el dato")
```

No incluyas secretos ni datos personales innecesarios en mensajes o tracebacks compartidos.

# 14. Arquitectura básica

```text
CLI o API
    ↓
 servicio
    ↓
modelo / repositorio
```

- **Modelo:** representa conceptos y reglas locales.
- **Servicio:** coordina casos de uso.
- **Persistencia:** almacena y recupera.
- **Interfaz:** recibe entrada y presenta salida.

No es una implementación completa de Clean Architecture. Es una separación comprensible para evitar que una única función lea `input()`, imprima, valide, guarde y decida reglas.

# 15. El modelo `Tarea`

```python
from dataclasses import dataclass

@dataclass(slots=True)
class Tarea:
    id: int
    titulo: str
    completada: bool = False

    def __post_init__(self) -> None:
        self.titulo = self.titulo.strip()
        if not self.titulo:
            raise ValueError("El título no puede estar vacío")
```

La validación pertenece al modelo porque una tarea sin título no es válida sin importar la interfaz utilizada.

# 16. Servicio sin estado global

```python
class ServicioTareas:
    def __init__(self) -> None:
        self._tareas: list[Tarea] = []

    def listar(self) -> tuple[Tarea, ...]:
        return tuple(self._tareas)
```

Cada instancia controla su colección. No existe una lista global compartida entre pruebas o usuarios. El servicio real crea, lista, busca y completa tareas, pero no usa `input()` ni `print()`.

# 17. Inyección de dependencias sencilla

En vez de crear siempre la colección internamente, el constructor puede recibir tareas iniciales:

```python
tareas_iniciales = [Tarea(id=10, titulo="Documentar")]
servicio = ServicioTareas(tareas_iniciales)
```

Recibir una dependencia desde fuera facilita escenarios de prueba y permite sustituir una implementación sin frameworks de inyección.

# 18. Error del dominio

```python
class TareaNoEncontradaError(LookupError):
    """No existe la tarea solicitada."""
```

Una excepción propia aporta vocabulario cuando el llamador necesita distinguir la ausencia de una tarea. No construiremos una jerarquía excesiva para cada posible fallo.

# Parte IV — Versión y documentación

# 19. Versionado semántico

La forma `MAJOR.MINOR.PATCH`, por ejemplo `1.4.2`, comunica una estrategia:

- `MAJOR`: cambios incompatibles.
- `MINOR`: funcionalidad compatible.
- `PATCH`: correcciones compatibles.

Antes de `1.0.0` suelen existir convenciones particulares. SemVer es una estrategia útil, no una ley para todo proyecto. Cambiar nombres públicos o firmas puede romper usuarios; una deprecación ofrece una transición gradual antes de retirar una API.

Duplicar la versión en `pyproject.toml`, `__init__.py` y otros archivos puede desincronizarla. El mini proyecto mantiene una única versión en `pyproject.toml`.

# 20. Changelog y README

Un changelog registra cambios relevantes por versión para usuarios y mantenedores. No lo crearemos porque no está autorizado.

Un README profesional suele incluir:

- Propósito y alcance.
- Requisitos e instalación.
- Uso y configuración.
- Ejecución de pruebas.
- Estructura del proyecto.
- Licencia y contribución, cuando apliquen.

Docstrings y type hints documentan la API interna. Explica contratos y decisiones; no repitas cada línea en palabras.

# Parte V — Calidad automática

# 21. Cuatro herramientas diferentes

| Herramienta | Pregunta principal | Ejemplo |
|---|---|---|
| Formatter | ¿El formato es consistente? | Ruff formatter, Black |
| Linter | ¿Hay patrones problemáticos? | Ruff |
| Type checker | ¿Los tipos declarados son coherentes? | mypy, Pyright |
| Tests | ¿El comportamiento cumple expectativas? | pytest |

Una herramienta no sustituye a las demás. Un formatter no garantiza calidad ni lógica correcta. Decide una estrategia: no necesitas aplicar Black y Ruff formatter simultáneamente.

# 22. Configuración en `pyproject.toml`

Muchas herramientas leen secciones `[tool...]`. Un ejemplo conceptual sencillo sería:

```toml
[tool.ruff]
line-length = 88
```

Las opciones evolucionan entre versiones. El mini proyecto mantiene configuración mínima para no enseñar valores dudosos ni exigir herramientas ausentes.

# 23. Pre-commit

El framework externo `pre-commit` puede ejecutar formato, lint u otras comprobaciones antes de crear un commit. Es una defensa temprana, no reemplaza CI ni revisión. No lo instalaremos ni crearemos su archivo de configuración.

# Parte VI — Git, revisión e integración continua

# 24. Flujo básico de colaboración

```text
branch
  ↓
cambios enfocados
  ↓
tests
  ↓
commit claro
  ↓
code review
  ↓
merge
```

Los commits pequeños y enfocados facilitan comprender y revertir. Sus mensajes deben describir la intención. Conventional Commits es una convención opcional, no un requisito universal.

`main` suele representar una línea estable y las feature branches aíslan trabajo. Code review ayuda a detectar defectos, compartir conocimiento y mejorar el diseño; no busca culpables.

# 25. Integración y entrega continuas

```text
push o pull request
        ↓
entorno limpio
        ↓
instalar
        ↓
lint
        ↓
tipos
        ↓
tests
```

La integración continua (CI) ejecuta comprobaciones frecuentes. GitHub Actions puede ejecutar workflows, pero no crearemos uno en esta unidad. Continuous Delivery mantiene cambios listos para liberar; Continuous Deployment puede desplegarlos automáticamente. No profundizaremos en CD.

# 26. Entornos y reproducibilidad

Desarrollo, pruebas y producción pueden tener configuración distinta con el mismo código. “Funciona en mi máquina” suele revelar diferencias de versión, dependencias, variables o archivos locales.

Ayudan:

- `pyproject.toml` y rangos de versiones.
- Entornos aislados y, según el flujo, lock files.
- Tests en un entorno limpio.
- CI y documentación suficiente.

El rango de una dependencia de proyecto expresa compatibilidad admitida. Un lock file o entorno congelado registra resoluciones concretas para reproducibilidad. No estudiaremos herramientas de lock aquí.

# Parte VII — Seguridad y distribución

# 27. Dependencias y licencias

Minimiza dependencias, revisa mantenimiento y procedencia, y actualiza conscientemente. No instales paquetes al azar. El código de terceros tiene licencias y obligaciones: revisarlas forma parte del uso responsable, aunque esta unidad no ofrece asesoría legal.

Nunca subas claves, contraseñas, tokens o datos personales reales. `.gitignore` reduce accidentes, pero no elimina un secreto que ya entró en el historial.

# 28. `.gitignore`

El proyecto ignora:

```gitignore
.venv/
__pycache__/
*.pyc
.pytest_cache/
.coverage
htmlcov/
.env
dist/
build/
*.egg-info/
```

`pyproject.toml` sí debe versionarse: describe el proyecto.

# 29. Empaquetado y PyPI

Una **source distribution** contiene fuentes para construir; un **wheel** es un formato construido que suele instalarse sin ejecutar la construcción completa.

La herramienta externa `build` puede generar ambos:

```bash
python -m build
```

No la instalaremos ni ejecutaremos. PyPI es el repositorio público habitual de paquetes Python; esta unidad no publica nada. Antes de distribuir hay que revisar archivos incluidos, licencia, metadatos y secretos.

# 30. Comandos instalables

Un proyecto con una función CLI podría declarar:

```toml
[project.scripts]
gestor-tareas = "gestor_tareas.cli:main"
```

Nuestro mini proyecto no tiene `cli.py` autorizado, así que no incluye ese entry point. El ejemplo solo presenta el mecanismo.

# 31. Rendimiento y observabilidad

Mide antes de optimizar. Cambiar código claro por una variante compleja sin evidencia suele perjudicar mantenibilidad. `timeit` y `cProfile` ayudan a medir, pero solo los anticipamos.

La observabilidad reúne señales como logs, métricas y trazas. Aquí implementamos únicamente logging básico; no entraremos en plataformas ni instrumentación avanzada.

# 32. El mini proyecto profesional

```text
proyecto_profesional/
├── pyproject.toml
├── .gitignore
├── src/
│   └── gestor_tareas/
│       ├── __init__.py
│       ├── config.py
│       ├── logging_config.py
│       ├── modelos.py
│       └── servicio.py
└── tests/
    └── test_servicio.py
```

Decisiones principales:

- Distribución `gestor-tareas` y paquete `gestor_tareas`.
- Código central sin dependencias externas.
- `Config` frozen cargada bajo demanda desde el entorno.
- Logging centralizado que no se configura al importar.
- `Tarea` valida identificador y título.
- `ServicioTareas` posee estado por instancia, acepta datos iniciales y no realiza I/O.
- `TareaNoEncontradaError` expresa un fallo del dominio.
- Tests independientes para servicio y configuración.

# 33. Instalar y probar

Flujo normal, dentro de un entorno virtual:

```bash
cd unidad20-python-profesional/ejemplos/proyecto_profesional
python -m pip install -e ".[dev]"
python -m pytest -v
```

Para validar sin instalar, desde la misma carpeta:

### Linux y macOS

```bash
PYTHONPATH=src python -m pytest -v
```

### PowerShell

```powershell
$env:PYTHONPATH = "src"
python -m pytest -v
Remove-Item Env:PYTHONPATH
```

`PYTHONPATH` se limita a ese proceso o sesión; no se añade ningún hack a los tests ni al paquete.

# 34. Errores frecuentes

- Crear estructura sin criterio o demasiadas capas para un problema mínimo.
- Introducir imports circulares o lógica en `__init__.py`.
- Producir efectos secundarios al importar.
- Guardar secretos, versionar `.env` o escribir credenciales en logs.
- Hardcodear configuración o crearla como global difícil de sustituir.
- Configurar el root logger desde cada módulo.
- Mezclar lógica con CLI/API, usar estado global o crear dependencias internas rígidas.
- Mantener un `pyproject.toml` inválido o versiones duplicadas.
- Añadir dependencias innecesarias o instalar herramientas globalmente.
- Confundir formato automático con calidad e ignorar tests.
- Crear commits gigantes o mezclar objetivos independientes.
- Diseñar CI dependiente de archivos locales no versionados.
- Publicar sin revisar contenido, metadatos, licencias y secretos.
- Optimizar sin medir.

# 35. Ejercicios

## Ejercicio 1 — Diseñar estructura

Transforma mentalmente un script conocido en módulos, paquete y tests; justifica cada archivo.

## Ejercicio 2 — `src` layout

Dibuja un paquete bajo `src/` y explica qué separa.

## Ejercicio 3 — Primer `pyproject.toml`

Escribe metadatos mínimos válidos para un proyecto ficticio.

## Ejercicio 4 — Dependencias

Clasifica tres paquetes como ejecución o desarrollo y elimina uno innecesario.

## Ejercicio 5 — Extra de desarrollo

Declara pytest en `[project.optional-dependencies]`.

## Ejercicio 6 — Instalación editable

Explica qué resuelve `pip install -e .` y por qué evita hacks de imports.

## Ejercicio 7 — Configuración por entorno

Lee una carpeta y un nivel con valores predeterminados.

## Ejercicio 8 — `Config`

Modela los valores anteriores con una dataclass frozen.

## Ejercicio 9 — Logging centralizado

Escribe una función explícita que configure nivel y formato.

## Ejercicio 10 — Logger por módulo

Obtén `logging.getLogger(__name__)` sin llamar `basicConfig()` al importar.

## Ejercicio 11 — Modelo y servicio

Separa una entidad académica de sus casos de uso.

## Ejercicio 12 — Eliminar una global

Convierte una lista global en estado perteneciente a una instancia.

## Ejercicio 13 — Inyección

Permite recibir una colección o repositorio desde el constructor.

## Ejercicio 14 — Error de dominio

Diseña una excepción útil para una búsqueda fallida sin crear una jerarquía extensa.

## Ejercicio 15 — SemVer

Clasifica tres cambios hipotéticos como major, minor o patch y justifica.

## Ejercicio 16 — README

Redacta propósito, instalación, configuración, uso y pruebas de un proyecto anterior.

## Ejercicio 17 — `.gitignore`

Ignora caches, entorno, cobertura, builds y `.env`, pero conserva `pyproject.toml`.

## Ejercicio 18 — Herramientas de calidad

Relaciona formatter, linter, type checker y tests con preguntas distintas.

## Ejercicio 19 — Pre-commit conceptual

Propón qué verificaciones rápidas ejecutar antes de un commit.

## Ejercicio 20 — Flujo Git

Diseña un flujo pequeño de branch, tests, commit, revisión y merge.

## Ejercicio 21 — Code review

Revisa un cambio atendiendo corrección, claridad, pruebas y seguridad.

## Ejercicio 22 — CI conceptual

Dibuja pasos reproducibles que no dependan de archivos personales.

## Ejercicio 23 — Packaging

Explica la diferencia introductoria entre sdist y wheel.

## Ejercicio 24 — Detectar secretos

Revisa un árbol ficticio e identifica datos que nunca deberían versionarse.

## Ejercicio 25 — Estructura deficiente

Detecta acoplamiento, efectos al importar, estado global e imports circulares.

## Ejercicio 26 — Refactorización

Profesionaliza un proyecto pequeño en pasos, ejecutando pruebas después de cada cambio.

No consultes soluciones completas ni publiques paquetes o datos.

# 36. Reto — Profesionalizar un proyecto

Elige el sistema académico, una API, el automatizador o el analizador de datos y conviértelo en un proyecto mantenible.

Debe incluir:

- `src` layout, `pyproject.toml`, README y `.gitignore`.
- Configuración por entorno sin secretos.
- Logging explícito.
- Type hints y responsabilidades separadas.
- Manejo de errores y pruebas.
- Versión e instrucciones de instalación, ejecución y pruebas.

Diseña además, solo conceptualmente, un flujo de branches, code review y CI. No publiques ni despliegues y no se entrega una solución completa.

# 37. Comprobación de aprendizaje

- [ ] Distingo script, módulos, paquete y proyecto mantenible.
- [ ] Explico ventajas y límites del `src` layout.
- [ ] Creo un `pyproject.toml` válido con dependencias mínimas.
- [ ] Comprendo instalación editable y dependencias de desarrollo.
- [ ] Cargo y valido variables de entorno en una configuración frozen.
- [ ] Mantengo secretos fuera de código, commits y logs.
- [ ] Configuro logging explícitamente y uso logger por módulo.
- [ ] Separo modelo, servicio, persistencia e interfaz.
- [ ] Evito estado global y comprendo inyección básica.
- [ ] Uso errores de dominio cuando aportan vocabulario.
- [ ] Comprendo SemVer, changelog y compatibilidad hacia atrás.
- [ ] Escribo README, docstrings y type hints útiles.
- [ ] Distingo formatter, linter, type checker y tests.
- [ ] Comprendo pre-commit sin confundirlo con CI.
- [ ] Explico branches, commits enfocados y code review.
- [ ] Comprendo CI/CD a nivel introductorio.
- [ ] Distingo configuración de desarrollo, pruebas y producción.
- [ ] Comprendo rangos de dependencias y lock files.
- [ ] Reconozco sdist, wheel, entry points y PyPI.
- [ ] Aplico seguridad básica y reproducibilidad.

# 38. Lo que aprendimos

```text
Código
 ↓
estructura
 ↓
configuración
 ↓
logs
 ↓
tests
 ↓
calidad
 ↓
versionado
 ↓
documentación
 ↓
automatización
 ↓
proyecto profesional
```

Ya tenemos las herramientas necesarias. La última unidad será un proyecto integrador en el que diseñarás, construirás, probarás y documentarás una solución completa en Python.

---

# 🧭 Navegación

⬅️ [Volver a la Unidad 19 — Automatización](../unidad19-automatizacion/)

🏠 [Volver al inicio del curso](../README.md)

➡️ [Continuar a la Unidad 21 — Proyecto final](../unidad21-proyecto-final/)


---

## Continuar el curso

- **Unidad anterior:** [Unidad 19 — Automatización con Python](../unidad19-automatizacion/README.md)
- **Volver al índice:** [Todas las unidades](../README.md)
- **Siguiente unidad:** [Unidad 21 — Proyecto final](../unidad21-proyecto-final/README.md)
