# Unidad 9 — Módulos, paquetes y organización de proyectos

[Volver al índice del curso](../README.md) · [Ver el curso en Aprende con Leli](https://lelyliliana.github.io/aprende-con-leli/cursos/python/)

Hasta ahora los ejemplos podían vivir en un solo archivo. En esta unidad aprenderás a distribuir una aplicación entre archivos relacionados y a preparar un entorno reproducible.

---

## 🎯 Objetivos de aprendizaje

Al finalizar podrás crear módulos y paquetes, importar código, usar el *main guard*, comprender imports absolutos y relativos, organizar proyectos, trabajar con `.venv`, `pip`, `requirements.txt` y `.gitignore`.

---

## 📋 Antes de comenzar

Utilizaremos funciones, clases y excepciones. No estudiaremos aún testing formal, publicación en PyPI, `pyproject.toml` en profundidad ni frameworks.

---

# 1. El problema del archivo único

Un `sistema_estudiantes.py` puede terminar reuniendo clases, validaciones, persistencia y menú. Esto dificulta encontrar, reutilizar y mantener código.

```text
un archivo → módulos → paquetes → proyecto organizado
```

Dividir no significa crear tantos archivos como líneas: buscamos agrupaciones comprensibles.

---

# 2. ¿Qué es un módulo?

Un archivo `.py` puede funcionar como módulo:

```text
proyecto/
├── principal.py
└── calculos.py
```

`calculos.py`:

```python
def sumar(numero_1, numero_2):
    return numero_1 + numero_2
```

`principal.py`:

```python
import calculos

resultado = calculos.sumar(5, 3)
print(resultado)
```

Ejecuta `principal.py` desde `proyecto/`. `calculos.sumar` deja claro de qué espacio de nombres procede la función.

---

# 3. Formas de importar

```python
import statistics

print(statistics.mean([4.0, 3.5, 4.5]))
```

`from` importa nombres concretos:

```python
from statistics import mean, median

print(mean([4.0, 3.5, 4.5]))
print(median([4.0, 3.5, 4.5]))
```

`import modulo` conserva el origen visible; `from modulo import nombre` es más breve, pero exige evitar colisiones. Para varios nombres, mantén líneas legibles.

Los alias deben aclarar:

```python
import statistics as stats
from statistics import mean as calcular_media

print(stats.median([3, 4, 5]))
print(calcular_media([3, 4, 5]))
```

Evita `from modulo import *`: contamina el espacio de nombres, oculta el origen y puede provocar colisiones.

---

# 4. ¿Qué ocurre al importar?

Python ejecuta el código de nivel superior la primera vez que importa un módulo en un proceso.

```text
# saludos.py
print("Módulo cargado")

def saludar():
    return "Hola"
```

Importarlo mostraría el mensaje. Los módulos reutilizables deben evitar efectos secundarios innecesarios al nivel superior.

---

# 5. `__name__`, `__main__` y el *main guard*

Python asigna `__name__` a cada módulo. Al ejecutar un archivo directamente vale `"__main__"`; al importarlo, normalmente contiene su nombre de módulo.

```python
def main():
    print("Programa principal")

if __name__ == "__main__":
    main()
```

El *guard* separa código reutilizable del punto de entrada. Al importar, se definen los elementos sin ejecutar `main()`.

Sin el guard, un menú o escritura de archivo al nivel superior podría ejecutarse accidentalmente durante un import.

---

# 6. ¿Qué es un paquete?

Un paquete agrupa módulos relacionados:

```text
proyecto/
├── main.py
└── estudiantes/
    ├── __init__.py
    ├── modelos.py
    └── servicios.py
```

Para este curso usaremos `__init__.py` explícitamente: identifica con claridad un paquete tradicional y puede controlar lo que este expone. Evitaremos inicialización con efectos secundarios y no estudiaremos *namespace packages*.

```python
from estudiantes.modelos import Estudiante
```

La ruta significa `paquete.módulo.elemento`.

---

# 7. Imports absolutos y relativos

Un import absoluto parte de la raíz reconocida del proyecto:

```python
from estudiantes.modelos import Estudiante
```

Dentro del paquete, un import relativo puede ser:

```python
from .modelos import Estudiante
```

El punto significa “desde este paquete”. `..` puede referirse al nivel superior relacionado, pero evitaremos rutas relativas profundas.

Los imports relativos dependen del contexto de paquete. Ejecutar directamente un archivo interno puede producir:

```text
ImportError: attempted relative import with no known parent package
```

Desde la raíz podemos ejecutarlo como módulo:

```bash
python -m estudiantes.servicios
```

En Linux o macOS también puede ser:

```bash
python3 -m estudiantes.servicios
```

`python archivo.py` ejecuta una ruta de archivo; `python -m paquete.modulo` conserva el contexto de importación del paquete.

---

# 8. Dónde busca Python

`sys.path` contiene ubicaciones de búsqueda:

```python
import sys

for ubicacion in sys.path:
    print(ubicacion)
```

No uses `sys.path.append(...)` como parche habitual. Ejecuta desde la raíz correcta y organiza imports coherentes.

---

# 9. Colisiones y `__pycache__`

No llames `json.py`, `csv.py` o `random.py` a un archivo propio si quieres importar esos módulos estándar: Python podría importar tu archivo.

Al renombrarlo, revisa también residuos de `__pycache__`. Python crea esa carpeta con bytecode cacheado; no debemos editarla y normalmente no se versiona.

---

# 10. Separar responsabilidades

```text
sistema_academico/
├── main.py                 # punto de entrada
├── modelos/                # entidades
│   ├── __init__.py
│   ├── persona.py
│   ├── estudiante.py
│   ├── docente.py
│   └── curso.py
├── servicios/              # operaciones como persistencia
│   ├── __init__.py
│   └── persistencia.py
└── datos/                  # datos de la aplicación
    └── estudiantes.json
```

Esta es una propuesta, no la única arquitectura válida. Un módulo debe agrupar elementos relacionados: evita un `utilidades.py` enorme, pero tampoco crees un archivo por cada función pequeña.

---

# 11. Dependencias circulares

```text
a.py importa b.py
b.py importa a.py
```

Esto puede dejar módulos parcialmente inicializados. Revisa responsabilidades, mueve elementos compartidos a un módulo apropiado y elimina dependencias bidireccionales innecesarias. Un import local no debe convertirse en parche universal.

---

# 12. Tres orígenes del código

| Origen | Ejemplos | Disponibilidad |
|---|---|---|
| Biblioteca estándar | `json`, `csv`, `pathlib` | Incluida con Python |
| Paquete externo | `requests`, `pandas`, `pytest` | Suele instalarse con `pip` |
| Código propio | Nuestros módulos | Vive en el proyecto |

---

# 13. Entornos virtuales

Un proyecto puede necesitar dependencias diferentes de otro. `venv` crea un entorno aislado asociado al proyecto.

Desde la raíz:

### Windows

```bash
py -m venv .venv
```

También puede funcionar `python -m venv .venv`.

### Linux y macOS

```bash
python3 -m venv .venv
```

`.venv` contiene el intérprete y paquetes del entorno; normalmente no se versiona.

---

# 14. Activar, comprobar y desactivar

### PowerShell

```powershell
.venv\Scripts\Activate.ps1
```

Si una política bloquea el script, consulta la documentación o administración del equipo; no reduzcas la seguridad sin comprender el cambio.

### Símbolo del sistema

```bat
.venv\Scripts\activate.bat
```

### Linux y macOS

```bash
source .venv/bin/activate
```

Comprueba el intérprete:

```bash
python --version
python -c "import sys; print(sys.executable)"
```

En VS Code abre `Python: Select Interpreter` y elige `.venv`. Para salir:

```bash
deactivate
```

Esto no elimina el entorno.

---

# 15. `pip` dentro del entorno

Con el entorno activo, preferimos:

```bash
python -m pip install nombre-paquete
python -m pip list
python -m pip show nombre-paquete
python -m pip uninstall nombre-paquete
```

No necesitas instalar nada para completar esta explicación. Si más adelante instalas `requests`, quedará en el entorno activo; todavía no lo utilizaremos en profundidad. Verifica siempre qué intérprete y entorno están activos.

---

# 16. `requirements.txt`

Este archivo registra dependencias reproducibles. Una línea conceptual es:

```text
nombre-paquete==version
```

No fijamos aquí una versión real que envejezca. Para capturar lo instalado:

```bash
python -m pip freeze > requirements.txt
```

Para instalar desde él:

```bash
python -m pip install -r requirements.txt
```

```text
clonar → crear .venv → activar → instalar requirements → ejecutar
```

`pip freeze` incluye todo el entorno. Usa uno dedicado por proyecto para evitar dependencias ajenas.

---

# 17. `.gitignore`

Ejemplo básico:

```gitignore
.venv/
__pycache__/
*.pyc
.env
```

`.env` suele contener configuración sensible; estudiaremos variables de entorno más adelante. `.gitignore` no elimina archivos que Git ya rastrea.

Normalmente versionamos código, `README.md`, `requirements.txt`, configuración apropiada y pruebas cuando existan. No versionamos entornos, cachés, credenciales ni temporales. Los datos dependen del propósito del proyecto.

---

# 18. README y estructura pequeña

Un README debe explicar nombre, propósito, requisitos, instalación, ejecución, estructura y dependencias, como hace este curso.

```text
mi_proyecto/
├── README.md
├── requirements.txt
├── .gitignore
├── main.py
└── mi_paquete/
    ├── __init__.py
    ├── modelos.py
    └── servicios.py
```

Proyectos profesionales pueden utilizar `src/`, `tests/` y `pyproject.toml`. Este último centraliza configuración y empaquetado moderno, pero no estudiaremos *build backends*, wheels, publicación, Poetry, Hatch ni setuptools avanzado todavía.

---

# 19. Dividir el sistema académico

`modelos/persona.py`, `estudiante.py`, `docente.py` y `curso.py` contienen clases cohesionadas. `servicios/persistencia.py` guarda y carga; `main.py` coordina el menú.

Ejemplos de imports coherentes desde la raíz:

```python
from modelos.estudiante import Estudiante
from modelos.docente import Docente
from modelos.curso import Curso
from servicios.persistencia import guardar_datos, cargar_datos
```

Dentro de `modelos/estudiante.py`, si Persona está en el mismo paquete:

```python
from .persona import Persona
```

Ejecuta el punto de entrada desde `sistema_academico/`, no archivos internos aislados.

---

# 20. Ejemplo multiarchivo completo

```text
proyecto/
├── main.py
└── operaciones/
    ├── __init__.py
    └── calculos.py
```

`operaciones/calculos.py`:

```python
def sumar(numero_1, numero_2):
    return numero_1 + numero_2

def calcular_promedio(valores):
    if not valores:
        raise ValueError("Se necesita al menos un valor")
    return sum(valores) / len(valores)
```

`operaciones/__init__.py`:

```python
from .calculos import sumar, calcular_promedio
```

`main.py`:

```python
from operaciones import calcular_promedio, sumar

def main():
    print(sumar(5, 3))
    print(calcular_promedio([4.0, 3.5, 4.5]))

if __name__ == "__main__":
    main()
```

Desde `proyecto/`:

```bash
python main.py
```

Resultado:

```text
8
4.0
```

## 💡 Experimenta

Agrega `restar()` a `calculos.py`, expórtala desde `__init__.py` y úsala en `main.py`.

---

# 21. Errores frecuentes

- Ejecutar desde una ubicación incorrecta y obtener `ModuleNotFoundError`.
- Ejecutar directamente un módulo interno con import relativo.
- Nombrar un archivo como un módulo estándar o conservar residuos en `__pycache__`.
- Usar `import *` o efectos secundarios al importar.
- Olvidar el *main guard*.
- Crear dependencias circulares o modificar `sys.path` como parche.
- Olvidar `__init__.py` en la estructura tradicional del curso.
- Versionar `.venv`, cachés, credenciales o temporales.
- Instalar globalmente o activar el entorno equivocado.
- Confundir el `pip` de un intérprete con otro.
- Olvidar `requirements.txt` o ejecutar `pip freeze` en un entorno contaminado.
- Pensar que `.gitignore` elimina archivos ya rastreados.

---

# 22. Ejercicios

1. Crea e importa un módulo propio.
2. Usa `import modulo` y su espacio de nombres.
3. Repite con `from ... import ...`.
4. Crea un alias descriptivo.
5. Imprime `__name__` al ejecutar e importar.
6. Agrega una función `main()` y su guard.
7. Crea un paquete con `__init__.py`.
8. Importa una clase desde un submódulo.
9. Practica un import absoluto.
10. Practica uno relativo dentro del paquete.
11. Ejecuta un módulo con `python -m`.
12. Diagnostica una colisión con `json.py`.
13. Propón cómo romper una dependencia circular.
14. Divide un módulo grande por responsabilidades.
15. Evita fragmentar tres funciones muy relacionadas.
16. Crea y activa `.venv`.
17. Comprueba `sys.executable` y desactiva.
18. Consulta `pip list` y `pip show` sin instalar nada.
19. Genera `requirements.txt` en un entorno dedicado.
20. Crea `.gitignore` para Python.
21. Escribe el README de un proyecto pequeño.
22. Construye y ejecuta el ejemplo multiarchivo.
23. Organiza las clases del sistema académico.
24. Explica cuándo `src/` podría aparecer sin adoptarlo aún.

---

# 23. Reto — Proyecto académico organizado

Transforma el sistema de la Unidad 8 en la estructura de `modelos/`, `servicios/`, `datos/` y `main.py` mostrada anteriormente.

Requisitos:

- Usa imports claros y `__init__.py` explícitos.
- Separa entidades, persistencia y punto de entrada.
- Incluye `main()` y el *main guard*.
- Ejecuta siempre desde la raíz del proyecto.
- Crea `.venv`, `.gitignore`, `requirements.txt` y un README con instrucciones.
- Conserva validaciones, excepción personalizada y persistencia JSON.
- Evita dependencias circulares y efectos secundarios al importar.
- No publiques paquetes ni agregues frameworks.

No se entrega la solución completa: prueba cada módulo antes de conectar el menú.

---

# 24. Comprobación de aprendizaje

- [ ] Distingo módulo, paquete y proyecto.
- [ ] Uso `import`, `from`, varios nombres y alias.
- [ ] Evito `import *` y colisiones.
- [ ] Comprendo el código de nivel superior y `__name__`.
- [ ] Creo `main()` y su guard.
- [ ] Uso imports absolutos y relativos apropiadamente.
- [ ] Ejecuto módulos con `python -m`.
- [ ] Comprendo `sys.path` sin modificarlo como parche.
- [ ] Organizo responsabilidades sin extremos.
- [ ] Reconozco y reduzco dependencias circulares.
- [ ] Creo, activo, verifico y desactivo `.venv`.
- [ ] Uso `python -m pip` dentro del entorno.
- [ ] Comprendo `requirements.txt`, `pip freeze` y `.gitignore`.
- [ ] Distingo qué versionar y documento un proyecto.
- [ ] Reconozco `src/` y `pyproject.toml` sin entrar en empaquetado avanzado.

---

# 25. Lo que aprendimos

```text
Archivo único → módulos → paquetes → entorno aislado → proyecto reproducible
```

Ahora podemos organizar aplicaciones mantenibles y preparar dependencias sin convertir todavía el código en un paquete publicable.

La Unidad 10 estudiará herramientas de Python funcional para transformar y combinar datos.

---

# 🧭 Navegación

⬅️ [Volver a la Unidad 8 — POO avanzada](../unidad08-poo-avanzada/)

🏠 [Volver al inicio del curso](../README.md)

➡️ [Continuar a la Unidad 10 — Python funcional](../unidad10-python-funcional/)


---

## Continuar el curso

- **Unidad anterior:** [Unidad 8 — Programación orientada a objetos avanzada](../unidad08-poo-avanzada/README.md)
- **Volver al índice:** [Todas las unidades](../README.md)
- **Siguiente unidad:** [Unidad 10 — Python funcional](../unidad10-python-funcional/README.md)
