# Unidad 12 — Tipado y buenas prácticas

[Volver al índice del curso](../README.md) · [Ver el curso en Aprende con Leli](https://lelyliliana.github.io/aprende-con-leli/cursos/python/)

Un programa puede producir el resultado esperado y, aun así, ser difícil de comprender o modificar. En esta unidad aprenderás a comunicar mejor la intención del código mediante convenciones, type hints, `dataclasses`, documentación y refactorizaciones pequeñas.

---

## 🎯 Objetivos de aprendizaje

Al finalizar podrás:

- Escribir código legible y consistente sin tratar las convenciones como leyes absolutas.
- Utilizar type hints modernos en variables, funciones, colecciones y clases.
- Elegir abstracciones como `Iterable`, `Sequence`, `Mapping` y `Callable`.
- Describir diccionarios estructurados mediante `TypedDict`.
- Modelar objetos que contienen principalmente datos mediante `dataclass`.
- Escribir docstrings y comentarios que aporten información útil.
- Reconocer problemas de diseño y refactorizar en pasos pequeños.
- Distinguir formatter, linter, type checker y pruebas.

---

## 📋 Antes de comenzar

Necesitas haber completado la Unidad 11. Utilizaremos funciones, clases, excepciones, módulos, decoradores, context managers, iterables y generadores.

No estudiaremos todavía pruebas formales, bases de datos, APIs, concurrencia, frameworks, CI/CD ni empaquetado profesional. Todos los ejemplos utilizan únicamente la biblioteca estándar.

> **Recomendación:** primero ejecuta cada ejemplo. Después cambia nombres, datos o tipos y observa qué información comunica mejor cada versión.

---

# 1. Del código funcional al código sostenible

Un programa puede funcionar y resultar difícil de leer, modificar, probar, reutilizar o mantener:

```text
Código que funciona
        ↓
Código comprensible
        ↓
Código mantenible
        ↓
Código sostenible
```

Las buenas prácticas son principios y convenciones útiles, no reglas absolutas. El contexto importa: una solución clara para un ejercicio pequeño puede no ser suficiente para un proyecto con varios módulos.

El código se lee muchas más veces de las que se escribe. Compara:

```text
x = 18
a = 32
tmp = x * a
```

con:

```python
precio_unitario = 18
cantidad_productos = 32
precio_total = precio_unitario * cantidad_productos

print(precio_total)
```

Los nombres descriptivos reducen el trabajo de adivinar qué representa cada valor.

---

# 2. Convenciones de nombres

Python utiliza habitualmente:

- `snake_case` para variables, funciones y métodos.
- `PascalCase` para clases.
- `UPPER_CASE` para constantes por convención.

```python
MAX_INTENTOS = 3

class RegistroEstudiante:
    def calcular_promedio(self, notas):
        promedio_general = sum(notas) / len(notas)
        return promedio_general

registro = RegistroEstudiante()
print(registro.calcular_promedio([4.0, 3.5, 4.5]))
```

Python no impide modificar `MAX_INTENTOS`; las mayúsculas comunican que el programa debería tratarlo como constante.

## 💡 Experimenta

Renombra `registro` como `r` y `promedio_general` como `x`. Ejecuta nuevamente: el resultado no cambia, pero compara cuánto tarda otra persona en comprender la intención.

---

# 3. PEP 8, indentación y espacios

PEP 8 es una guía de estilo para código Python. No forma parte de la sintaxis ni garantiza que la lógica sea correcta, pero favorece la consistencia entre proyectos.

La indentación sí forma parte de la sintaxis. Utiliza cuatro espacios por nivel y evita mezclar tabulaciones y espacios.

Deja espacios alrededor de operadores:

```python
precio = 2500
cantidad = 4
total = precio * cantidad

if total >= 10000:
    print("Compra mayor o igual a 10000")
```

En argumentos por nombre no se agregan espacios alrededor de `=`:

```python
def mostrar_precio(valor=10):
    print(valor)

mostrar_precio(valor=25)
```

---

# 4. Líneas legibles y organización visual

Los paréntesis permiten dividir expresiones largas de forma natural:

```python
precio = 12000
cantidad = 3
factor_impuesto = 1.19

resultado = (
    precio
    * cantidad
    * factor_impuesto
)

print(resultado)
```

No necesitas memorizar un límite rígido para comenzar. Divide una línea cuando dificulte la lectura. Las líneas en blanco también separan funciones, clases y bloques conceptuales; no deben fragmentar instrucciones que pertenecen a una misma idea.

---

# 5. Imports organizados

Una organización habitual separa:

1. Biblioteca estándar.
2. Paquetes externos.
3. Módulos propios.

```text
import json
from pathlib import Path

import requests

from mi_paquete import servicio
```

`requests` aparece solo como ejemplo de ubicación: **no lo instalaremos ni utilizaremos en esta unidad**. Dentro de cada grupo, mantén un orden consistente.

Elimina imports que no se utilizan. Ocultan las dependencias reales, distraen al leer y pueden confundir a quien mantenga el módulo.

---

# 6. Type hints: comunicar intención

En la Unidad 4 conocimos anotaciones sencillas:

```python
def sumar(numero_1: int, numero_2: int) -> int:
    return numero_1 + numero_2

resultado: int = sumar(4, 5)
print(resultado)
```

Los type hints ayudan a documentar la intención, mejorar el autocompletado y permitir que herramientas de análisis estático señalen posibles inconsistencias.

## Los hints no fuerzan tipos durante la ejecución

Observa este ejemplo deliberadamente inadecuado:

```python
def duplicar(numero: int) -> int:
    return numero * 2

resultado = duplicar("Hola")  # Llamada contraria al tipo declarado.
print(resultado)
```

Python imprime `HolaHola`: la anotación no bloquea automáticamente la llamada. Los hints tampoco convierten valores ni validan datos externos. Este ejemplo demuestra su naturaleza; no recomienda ignorarlos.

---

# 7. Tipos básicos y colecciones tipadas

```python
nombre: str = "Ana"
edad: int = 20
promedio: float = 4.3
activo: bool = True

materias: list[str] = ["Python", "Bases de datos"]
notas: dict[str, float] = {"Python": 4.5}
posicion: tuple[int, int] = (4, 8)
etiquetas: set[str] = {"programación", "datos"}

print(nombre, edad, promedio, activo)
print(materias, notas, posicion, etiquetas)
```

Este curso prioriza la sintaxis moderna `list[str]`, `dict[str, float]`, `tuple[int, int]` y `set[str]`. En proyectos antiguos puedes encontrar `List`, `Dict` y `Tuple` importados desde `typing`.

---

# 8. Uniones, ausencia y `Optional`

El operador `|` expresa alternativas:

```python
def convertir_nota(nota: int | float) -> float:
    return float(nota)

def normalizar_codigo(codigo: int | str) -> str:
    return str(codigo).strip()

def buscar_estudiante(nombre: str) -> str | None:
    estudiantes = {"Ana": "E001", "Luis": "E002"}
    return estudiantes.get(nombre)

print(convertir_nota(4))
print(normalizar_codigo(25))
print(buscar_estudiante("Marta"))
```

`int | float` acepta dos tipos numéricos; `int | str` significa “entero o cadena”. `str | None` indica que puede existir una cadena o ausencia de resultado.

Una anotación no asigna un valor predeterminado:

```python
def mostrar_alias(alias: str | None = None) -> str:
    if alias is None:
        return "Sin alias"
    return alias

print(mostrar_alias())
```

`Optional[str]` es conceptualmente equivalente a `str | None` en este caso. `Union[int, str]` es una sintaxis anterior o alternativa. Para el código moderno del curso priorizaremos `|`.

---

# 9. `Any` y aliases de tipos

`Any` indica a las herramientas que un valor puede utilizarse como cualquier tipo:

```python
from typing import Any

def mostrar_valor(valor: Any) -> None:
    print(valor)

mostrar_valor({"curso": "Python"})
```

Es útil en fronteras muy dinámicas, pero reduce las garantías del análisis. No lo uses por comodidad si puedes expresar un tipo preciso.

Un alias comunica intención:

```python
CodigoEstudiante = str
Notas = list[float]

def registrar_notas(codigo: CodigoEstudiante, notas: Notas) -> None:
    print(codigo, notas)

registrar_notas("E001", [4.0, 4.5])
```

Estos aliases no crean necesariamente tipos nuevos durante la ejecución; asignan nombres más significativos a expresiones de tipo.

---

# 10. Funciones como datos: `Callable`

`Callable[[int], int]` describe una función que recibe un `int` y devuelve un `int`:

```python
from collections.abc import Callable

def aplicar(
    numero: int,
    operacion: Callable[[int], int],
) -> int:
    return operacion(numero)

def calcular_doble(numero: int) -> int:
    return numero * 2

print(aplicar(5, calcular_doble))
```

La lista interior contiene los tipos de los parámetros; el último tipo representa el retorno. Esto conecta con las funciones de orden superior de la Unidad 10.

---

# 11. `Iterable`, `Iterator`, `Sequence` y `Mapping`

Aceptar una abstracción adecuada puede hacer una función más flexible:

```python
from collections.abc import Iterable, Iterator, Mapping, Sequence

def duplicar_valores(datos: Iterable[int]) -> list[int]:
    return [valor * 2 for valor in datos]

def generar_codigos(cantidad: int) -> Iterator[str]:
    for numero in range(1, cantidad + 1):
        yield f"E{numero:03d}"

def calcular_promedio(notas: Sequence[float]) -> float:
    if not notas:
        raise ValueError("Se necesita al menos una nota")
    return sum(notas) / len(notas)

def mostrar_notas(notas: Mapping[str, float]) -> None:
    for materia, nota in notas.items():
        print(f"{materia}: {nota}")

print(duplicar_valores({1, 2, 3}))
print(list(generar_codigos(3)))
print(calcular_promedio((4.0, 3.5, 4.5)))
mostrar_notas({"Python": 4.5})
```

- `Iterable` acepta algo que puede recorrerse; no exige una lista.
- `Iterator` describe un iterador, como el que devuelve un generador.
- `Sequence` representa una secuencia ordenada y legible, como lista o tupla.
- `Mapping` representa una estructura clave-valor, como un diccionario.

No necesitamos estudiar toda la jerarquía de `collections.abc`.

---

# 12. Type hints en clases

```python
class Estudiante:
    institucion: str = "Universidad Central"

    def __init__(
        self,
        nombre: str,
        edad: int,
        notas: list[float],
    ) -> None:
        self.nombre: str = nombre
        self.edad: int = edad
        self.notas: list[float] = notas

    def calcular_promedio(self) -> float:
        if not self.notas:
            return 0.0
        return sum(self.notas) / len(self.notas)

estudiante = Estudiante("Ana", 20, [4.0, 4.5])
print(estudiante.calcular_promedio())
```

En los métodos no se anota `self` normalmente. Python moderno ofrece `Self` para algunos casos avanzados, pero no lo necesitamos aquí.

---

# 13. Atributos de clase con `ClassVar`

`ClassVar` comunica al analizador que el atributo pertenece a la clase, no a cada instancia:

```python
from typing import ClassVar

class Estudiante:
    institucion: ClassVar[str] = "Universidad Central"

    def __init__(self, nombre: str) -> None:
        self.nombre = nombre

print(Estudiante.institucion)
print(Estudiante("Ana").nombre)
```

La anotación mejora la comunicación con herramientas; no cambia por sí sola el mecanismo de atributos estudiado en la Unidad 7.

---

# 14. Valores limitados con `Literal`

```python
from typing import Literal

Estado = Literal["activo", "inactivo"]

def describir_estado(estado: Estado) -> str:
    return f"Estado: {estado}"

print(describir_estado("activo"))
```

`Literal` resulta útil cuando solo unos valores concretos son válidos para el análisis estático. No valida durante la ejecución y no conviene usarlo para cada cadena posible.

---

# 15. Diccionarios estructurados con `TypedDict`

```python
from typing import TypedDict

class EstudianteDict(TypedDict):
    nombre: str
    edad: int
    nota: float

def mostrar_estudiante(estudiante: EstudianteDict) -> None:
    print(f"{estudiante['nombre']}: {estudiante['nota']}")

datos: EstudianteDict = {
    "nombre": "Ana",
    "edad": 20,
    "nota": 4.5,
}

mostrar_estudiante(datos)
```

`TypedDict` describe las claves y tipos esperados principalmente para herramientas de tipado. El valor sigue siendo un diccionario; no se convierte en un objeto de dominio ni se valida automáticamente.

---

# 16. Type hints y datos JSON

```python
import json
from typing import TypedDict

class CursoDict(TypedDict):
    nombre: str
    cupos: int

texto_json = '{"nombre": "Python", "cupos": 25}'
datos_cargados = json.loads(texto_json)

if not isinstance(datos_cargados, dict):
    raise ValueError("Se esperaba un objeto JSON")

curso: CursoDict = {
    "nombre": str(datos_cargados["nombre"]),
    "cupos": int(datos_cargados["cupos"]),
}

print(curso)
```

La anotación documenta la estructura que queremos después de procesar los datos. Un archivo externo puede contener claves ausentes o valores incorrectos: requiere validación real, independientemente de los hints.

---

# 17. ¿Por qué `dataclass`?

Una clase dedicada principalmente a guardar datos suele repetir inicialización, representación e igualdad. El decorador `@dataclass` puede generar esos métodos:

```python
from dataclasses import dataclass

@dataclass
class Producto:
    nombre: str
    precio: float
    cantidad: int

producto = Producto("Teclado", 120000.0, 2)
otro_producto = Producto("Teclado", 120000.0, 2)

print(producto)
print(producto == otro_producto)
```

Por defecto genera un `__init__()`, un `__repr__()` útil y una comparación `__eq__()` basada en los campos participantes. Su comportamiento depende de la configuración de la dataclass.

---

# 18. Valores predeterminados y `default_factory`

Los campos obligatorios deben aparecer antes de los que tienen valor predeterminado, igual que los parámetros de una función:

```python
from dataclasses import dataclass, field

@dataclass
class Estudiante:
    nombre: str
    activo: bool = True
    notas: list[float] = field(default_factory=list)

estudiante_1 = Estudiante("Ana")
estudiante_2 = Estudiante("Luis")
estudiante_1.notas.append(4.5)

print(estudiante_1)
print(estudiante_2)
```

No escribas `notas: list[float] = []`: una colección mutable no debe funcionar como valor predeterminado compartido. `field(default_factory=list)` llama `list` para crear una lista nueva por instancia.

`field()` también permite opciones básicas como excluir un campo de la representación:

```python
from dataclasses import dataclass, field

@dataclass
class Cuenta:
    titular: str
    clave_temporal: str = field(repr=False)

print(Cuenta("Ana", "cambiar123"))
```

Ocultar el valor de `repr` no sustituye medidas reales de seguridad.

---

# 19. Validación con `__post_init__()`

El `__init__()` generado llama a `__post_init__()` después de asignar los campos:

```python
from dataclasses import dataclass

@dataclass
class Producto:
    nombre: str
    precio: float

    def __post_init__(self) -> None:
        self.nombre = self.nombre.strip()
        if not self.nombre:
            raise ValueError("El nombre no puede estar vacío")
        if self.precio < 0:
            raise ValueError("El precio no puede ser negativo")

producto = Producto(" Teclado ", 120000.0)
print(producto)
```

Es útil para validar o calcular datos derivados después de la inicialización. Los type hints por sí solos no realizan esta validación.

---

# 20. Una dataclass también puede tener comportamiento

```python
from dataclasses import dataclass, field

@dataclass
class Estudiante:
    nombre: str
    notas: list[float] = field(default_factory=list)

    def agregar_nota(self, nota: float) -> None:
        if not 0.0 <= nota <= 5.0:
            raise ValueError("La nota debe estar entre 0.0 y 5.0")
        self.notas.append(nota)

    def calcular_promedio(self) -> float:
        if not self.notas:
            return 0.0
        return sum(self.notas) / len(self.notas)

estudiante = Estudiante("Ana")
estudiante.agregar_nota(4.0)
estudiante.agregar_nota(4.5)
print(estudiante.calcular_promedio())
```

`dataclass` no significa “clase sin métodos”. Reduce código repetitivo cuando los datos tienen un papel central.

---

# 21. `frozen=True` y `slots=True`

```python
from dataclasses import dataclass

@dataclass(frozen=True)
class Coordenada:
    fila: int
    columna: int

posicion = Coordenada(2, 5)
print(posicion)
```

`frozen=True` impide la asignación normal a campos, pero ofrece **inmutabilidad superficial**: no vuelve mágicamente inmutables todos los objetos contenidos.

```python
from dataclasses import dataclass

@dataclass(slots=True)
class Etiqueta:
    nombre: str

etiqueta = Etiqueta("urgente")
print(etiqueta)
```

`slots=True` restringe atributos dinámicos y puede reducir memoria cuando existen muchas instancias. Es una opción moderna, no una garantía universal de rendimiento.

---

# 22. Dataclass o clase tradicional

| Situación | Opción que puede encajar |
|---|---|
| Predominan campos de datos | `dataclass` |
| Queremos reducir inicialización y representación repetitivas | `dataclass` |
| Inicialización muy personalizada | Clase tradicional |
| Encapsulamiento o comportamiento especial predominante | Clase tradicional |

Ninguna es superior universalmente. Elige la forma que comunique mejor el modelo.

---

# 23. Docstrings en funciones, clases y módulos

Una docstring documenta una interfaz. En un módulo aparece como primera instrucción:

```python
"""Herramientas para procesar estudiantes."""

class Estudiante:
    """Representa un estudiante y sus notas académicas."""

    def __init__(self, nombre: str, notas: list[float]) -> None:
        self.nombre = nombre
        self.notas = notas

    def calcular_promedio(self) -> float:
        """Calcula el promedio de las notas registradas."""
        if not self.notas:
            raise ValueError("No hay notas registradas")
        return sum(self.notas) / len(self.notas)

print(Estudiante("Ana", [4.0, 5.0]).calcular_promedio())
```

Documenta propósito, condiciones relevantes y resultados que no sean evidentes. Evita repetir literalmente el nombre. Existen estilos Google, NumPy y reStructuredText; un proyecto debe escoger uno de forma consistente, pero aquí no impondremos uno ni estudiaremos Sphinx.

---

# 24. Comentarios: explicar el porqué

Una docstring documenta un módulo, clase o función como interfaz. Un comentario explica una decisión o detalle interno.

Este comentario aporta contexto:

```python
estudiantes = ["Luis", "Ana", "Marta"]

# Se conserva el orden original porque el reporte debe
# coincidir con la importación del sistema externo.
for estudiante in estudiantes:
    print(estudiante)
```

En cambio, `indice += 1  # aumenta el índice en uno` solo traduce una instrucción evidente. Los comentarios desactualizados pueden ser peores que su ausencia.

---

# 25. Funciones pequeñas y cohesivas

Una función cohesiva tiene una responsabilidad comprensible, un nombre claro y entradas y salidas visibles. No existe un número mágico de líneas.

Una firma como esta puede revelar responsabilidades mezcladas:

```text
procesar(datos, guardar=True, enviar=False, imprimir=True)
```

No todo parámetro booleano es malo, pero varios flags que transforman radicalmente la operación sugieren separar acciones:

```python
def calcular_reporte(notas: list[float]) -> str:
    promedio = sum(notas) / len(notas)
    return f"Promedio: {promedio:.2f}"

def mostrar_reporte(reporte: str) -> None:
    print(reporte)

reporte = calcular_reporte([4.0, 3.5, 4.5])
mostrar_reporte(reporte)
```

---

# 26. Guard clauses y menos anidamiento

Una guard clause maneja temprano un caso inválido o especial:

```python
def calcular_promedio(notas: list[float]) -> float:
    if not notas:
        raise ValueError("Se necesita al menos una nota")

    return sum(notas) / len(notas)

print(calcular_promedio([4.0, 3.5, 4.5]))
```

Compara la forma anidada:

```text
def describir_estudiante(estudiante):
    if estudiante is not None:
        if estudiante["activo"]:
            return "Estudiante activo"
        else:
            return "Estudiante inactivo"
    else:
        return "No encontrado"
```

con una salida temprana más lineal:

```python
def describir_estudiante(estudiante: dict[str, object] | None) -> str:
    if estudiante is None:
        return "No encontrado"
    if not estudiante["activo"]:
        return "Estudiante inactivo"
    return "Estudiante activo"

print(describir_estudiante({"activo": True}))
```

---

# 27. DRY sin abstracción prematura

DRY significa *Don't Repeat Yourself*: evita mantener la misma regla de conocimiento en varios lugares. Sin embargo, eliminar cualquier parecido entre dos líneas puede crear abstracciones confusas.

Primero comprende el patrón; después extráelo:

```python
def validar_nota(nota: float) -> None:
    if not 0.0 <= nota <= 5.0:
        raise ValueError("La nota debe estar entre 0.0 y 5.0")

def registrar_nota(notas: list[float], nota: float) -> None:
    validar_nota(nota)
    notas.append(nota)

notas_estudiante: list[float] = []
registrar_nota(notas_estudiante, 4.5)
print(notas_estudiante)
```

Una pequeña repetición temporal puede ser preferible a una abstracción prematura cuyo propósito nadie comprende.

---

# 28. Constantes y números mágicos

Un número literal puede ser claro localmente. Si representa una regla reutilizada, una constante expresa mejor su intención:

```python
NOTA_APROBACION = 3.0

def esta_aprobado(promedio: float) -> bool:
    return promedio >= NOTA_APROBACION

print(esta_aprobado(3.8))
```

No conviertas cada número en constante. Hazlo cuando el nombre aporte significado o la regla aparezca en varios lugares.

---

# 29. Booleanos claros y `None`

Prefiere condiciones directas:

```python
activo = True
resultado: str | None = None

if activo:
    print("Activo")

if not activo:
    print("Inactivo")

if resultado is None:
    print("Sin resultado")

if resultado is not None:
    print(resultado)
```

Evita `activo == True`, `activo == False` y `resultado == None` como estilo habitual. `is None` comprueba específicamente el objeto único `None`.

---

# 30. EAFP y LBYL

LBYL (*Look Before You Leap*) comprueba antes de actuar:

```python
from pathlib import Path

ruta = Path("datos_inexistentes.txt")

if ruta.exists():
    print(ruta.read_text(encoding="utf-8"))
else:
    print("El archivo no existe")
```

EAFP (*Easier to Ask Forgiveness than Permission*) intenta la operación y maneja un fallo específico:

```python
from pathlib import Path

ruta = Path("datos_inexistentes.txt")

try:
    print(ruta.read_text(encoding="utf-8"))
except FileNotFoundError:
    print("El archivo no existe")
```

Python utiliza EAFP con frecuencia, pero ninguno de los estilos es universalmente correcto. La elección depende del costo, la claridad y la posibilidad de que el estado cambie entre comprobación y uso.

---

# 31. Código *pythonic* y el Zen de Python

Código *pythonic* aprovecha convenciones naturales del lenguaje: `enumerate()` en vez de un contador manual, `zip()` para recorridos paralelos, `with` para recursos y comprensiones cuando siguen siendo claras.

No significa “más corto a toda costa”. Puedes ejecutar:

```python
import this
```

El Zen de Python reúne aforismos sobre diseño. Algunas ideas breves son “Explicit is better than implicit”, “Simple is better than complex” y “Readability counts”: priorizan intención visible, sencillez y legibilidad, no trucos compactos.

---

# 32. ¿Qué es refactorizar?

Refactorizar es cambiar la estructura interna sin modificar intencionalmente el comportamiento observable. No significa agregar funcionalidades.

Señales que pueden justificarlo:

- Duplicación.
- Funciones gigantes o con demasiados parámetros.
- Nombres confusos.
- Anidamiento profundo.
- Responsabilidades mezcladas.
- Dependencias globales innecesarias.

Son indicios, no métricas rígidas.

---

# 33. Refactorizar paso a paso

Este bloque inicial mezcla datos, cálculo y salida:

```python
nombre = "Ana"
notas = [4.0, 3.5, 4.5]
promedio = sum(notas) / len(notas)
print(f"{nombre}: {promedio:.2f}")
```

Podemos extraer responsabilidades, mejorar nombres, agregar tipos y documentar:

```python
from collections.abc import Sequence

def calcular_promedio(notas: Sequence[float]) -> float:
    """Calcula el promedio de una secuencia no vacía de notas."""
    if not notas:
        raise ValueError("Se necesita al menos una nota")
    return sum(notas) / len(notas)

def crear_resumen(nombre: str, promedio: float) -> str:
    """Construye el resumen académico de un estudiante."""
    return f"{nombre}: {promedio:.2f}"

nombre_estudiante = "Ana"
notas_estudiante = [4.0, 3.5, 4.5]
promedio_estudiante = calcular_promedio(notas_estudiante)
print(crear_resumen(nombre_estudiante, promedio_estudiante))
```

Haz cambios pequeños y verificables. No refactorices todo de golpe: las pruebas automatizadas de la Unidad 13 aumentarán la confianza al cambiar código.

---

# 34. Formatter, linter y type checker

Son herramientas con responsabilidades distintas:

| Herramienta | Propósito | No garantiza |
|---|---|---|
| Formatter | Ajusta automáticamente el formato | Lógica correcta |
| Linter | Señala convenciones, imports sin usar y código sospechoso | Ausencia de errores |
| Type checker | Analiza type hints sin ejecutar el programa | Datos válidos en runtime |
| Pruebas | Comprueban comportamientos seleccionados | Cobertura de todos los casos |

Black es un formatter popular; Ruff puede aplicar linting y formato; mypy y Pyright realizan análisis estático de tipos. Son herramientas externas, sus opciones evolucionan y **no se instalarán en esta unidad**.

VS Code puede mostrar análisis mediante extensiones como Pylance, relacionado con Pyright. No dependemos de una interfaz concreta ni modificaremos su configuración. Revisa siempre los cambios automáticos: ninguna herramienta sustituye el criterio ni las pruebas.

---

# 35. Ejemplo integrador — Sistema académico refactorizado

El siguiente ejemplo reúne nombres, constantes, abstracciones de colecciones, una dataclass, docstrings, validación y responsabilidades separadas:

```python
from collections.abc import Iterable, Sequence
from dataclasses import dataclass, field

NOTA_MINIMA = 0.0
NOTA_MAXIMA = 5.0
NOTA_APROBACION = 3.0

def validar_nota(nota: float) -> None:
    """Valida que una nota pertenezca al rango académico."""
    if not NOTA_MINIMA <= nota <= NOTA_MAXIMA:
        raise ValueError(
            f"La nota debe estar entre {NOTA_MINIMA} y {NOTA_MAXIMA}"
        )

def calcular_promedio(notas: Sequence[float]) -> float:
    """Calcula el promedio de una secuencia no vacía."""
    if not notas:
        raise ValueError("No hay notas registradas")
    return sum(notas) / len(notas)

@dataclass
class Estudiante:
    """Representa un estudiante y sus resultados académicos."""

    codigo: str
    nombre: str
    notas: list[float] = field(default_factory=list)

    def __post_init__(self) -> None:
        self.codigo = self.codigo.strip().upper()
        self.nombre = self.nombre.strip().title()
        if not self.codigo:
            raise ValueError("El código no puede estar vacío")
        if not self.nombre:
            raise ValueError("El nombre no puede estar vacío")
        for nota in self.notas:
            validar_nota(nota)

    def agregar_nota(self, nota: float) -> None:
        """Agrega una nota válida al estudiante."""
        validar_nota(nota)
        self.notas.append(nota)

    def calcular_promedio(self) -> float:
        """Calcula el promedio de las notas registradas."""
        return calcular_promedio(self.notas)

    def esta_aprobado(self) -> bool:
        """Indica si el promedio alcanza la nota de aprobación."""
        return self.calcular_promedio() >= NOTA_APROBACION

def crear_reporte(estudiantes: Iterable[Estudiante]) -> list[str]:
    """Crea una línea de reporte por cada estudiante."""
    reporte: list[str] = []
    for estudiante in estudiantes:
        try:
            promedio = estudiante.calcular_promedio()
            estado = "aprobado" if estudiante.esta_aprobado() else "no aprobado"
            reporte.append(
                f"{estudiante.codigo} - {estudiante.nombre}: "
                f"{promedio:.2f} ({estado})"
            )
        except ValueError:
            reporte.append(
                f"{estudiante.codigo} - {estudiante.nombre}: sin notas"
            )
    return reporte

estudiantes = [
    Estudiante(" e001 ", " ana pérez ", [4.0, 3.5, 4.5]),
    Estudiante("E002", "Luis Gómez"),
]

for linea in crear_reporte(estudiantes):
    print(linea)
```

La propiedad `@property` no aparece porque acceder a estos campos directamente es suficiente. Agregar mecanismos sin necesidad no mejora el diseño.

## 💡 Experimenta

Agrega un tercer estudiante, intenta registrar una nota fuera del rango y captura `ValueError`. Después cambia `crear_reporte()` para recibir una tupla: `Iterable` permite hacerlo sin modificar la función.

---

# 36. Errores frecuentes

## Tipado

- Pensar que los type hints validan o convierten automáticamente en runtime.
- Usar `Any` para todo y perder información útil.
- Exigir `list` cuando `Iterable` o `Sequence` expresa mejor la necesidad.
- Confundir `str | None` con asignar un valor predeterminado.
- Creer que `TypedDict`, `Literal` o `ClassVar` cambian automáticamente el comportamiento en ejecución.
- Anotar una función con un retorno que no coincide con lo que realmente devuelve.

## Dataclasses

- Intentar usar una lista mutable como default en vez de `default_factory`.
- Olvidar validar datos externos en `__post_init__()` cuando el dominio lo requiere.
- Usar dataclass para lógica cuya inicialización o encapsulamiento sería más clara con una clase tradicional.
- Suponer que `frozen=True` hace profundamente inmutables todas las estructuras internas.

## Estilo y diseño

- Utilizar nombres crípticos, imports sin usar o funciones enormes.
- Escribir comentarios que solo repiten el código.
- Mantener duplicación de una misma regla o, en el extremo contrario, abstraer demasiado pronto.
- Ocultar reglas detrás de números mágicos sin contexto.
- Crear anidamiento excesivo y responsabilidades mezcladas.
- Usar `== None`, `== True` o `== False` como estilo habitual.
- Obsesionarse con reducir líneas o creer que PEP 8 garantiza calidad lógica.

## Herramientas

- Creer que formatter, linter o type checker sustituyen la ejecución y las pruebas.
- Aplicar cambios automáticos sin revisar el resultado.

---

# 37. Ejercicios

1. Refactoriza variables llamadas `x`, `a` y `tmp` en un cálculo de matrícula utilizando nombres que comuniquen propósito. No cambies el resultado.
2. Corrige un fragmento con indentación inconsistente, operadores sin espacios y líneas demasiado largas siguiendo PEP 8 con criterio.
3. Agrega type hints básicos a una función que reciba nombre, edad y promedio, y devuelva un mensaje.
4. Anota correctamente una lista de materias, un diccionario de notas, una coordenada y un conjunto de códigos.
5. Diseña una función que acepte un código `int | str` y otra que pueda devolver `str | None`. Explica por qué la unión no valida datos.
6. Escribe una función de orden superior cuyo parámetro sea `Callable[[float], float]`. Pruébala con dos operaciones compatibles.
7. Cambia una función que exige `list[int]` para aceptar `Iterable[int]` cuando solo necesita recorrer los valores. Compruébala con lista, tupla y generador.
8. Usa `Sequence[float]` en una función que necesita `len()` y recorrido ordenado para calcular un promedio.
9. Usa `Mapping[str, float]` en una función que lea notas por materia sin modificar la estructura recibida.
10. Agrega a una clase un atributo institucional tipado con `ClassVar[str]` y explica la diferencia frente a un atributo de instancia.
11. Crea un alias con `Literal` para tres estados de matrícula y úsalo en una función. No agregues validación runtime implícita que `Literal` no ofrece.
12. Define un `TypedDict` para un producto cargado desde JSON. Identifica qué validaciones reales seguirían siendo necesarias.
13. Convierte una clase sencilla de producto en `@dataclass` y comprueba su representación e igualdad por campos.
14. Modela un curso con una lista de estudiantes usando `field(default_factory=list)`. Demuestra que dos cursos no comparten la lista.
15. Incorpora `__post_init__()` a una dataclass para normalizar un código y rechazar una cantidad negativa mediante `ValueError`.
16. Crea una dataclass pequeña con `frozen=True`; intenta reasignar un campo dentro de un ejemplo controlado y explica el límite de la inmutabilidad superficial.
17. Escribe docstrings útiles para un módulo, una clase y dos funciones. Evita limitarte a repetir sus nombres.
18. Refactoriza una función con varios niveles de condiciones mediante guard clauses que atiendan primero los casos inválidos.
19. Simplifica una búsqueda muy anidada mediante retornos tempranos, conservando exactamente sus resultados posibles.
20. Localiza una regla de validación duplicada en dos funciones y extráela solo si representa el mismo conocimiento del dominio.
21. Revisa una abstracción creada para dos líneas apenas parecidas. Decide si mantenerla o aceptar repetición temporal y justifica tu elección.
22. Organiza imports conceptuales en estándar, externos y propios; elimina los no utilizados. No instales el paquete externo mostrado.
23. Compara una solución LBYL y otra EAFP para leer un archivo ausente. Explica qué excepción específica debe manejarse.
24. Refactoriza completamente una función o clase académica: mejora nombres, separa responsabilidades, agrega tipos, constantes, docstrings, guard clauses y excepciones específicas sin añadir funciones nuevas al sistema.

---

# 38. Reto — Refactorización del sistema académico

Retoma el sistema académico de unidades anteriores y mejora su estructura interna sin agregar funcionalidades.

Puedes trabajar con `Estudiante`, `Curso` y `Docente`. Requisitos mínimos:

- Modela `Estudiante` mediante dataclass si resulta apropiado.
- Incluye `codigo: str`, `nombre: str` y `notas: list[float]`.
- Crea cada lista de notas con `field(default_factory=list)`.
- Agrega type hints al resto de funciones y métodos.
- Utiliza nombres descriptivos, constantes y docstrings útiles.
- Separa responsabilidades mediante funciones o métodos cohesionados.
- Maneja casos inválidos con guard clauses y excepciones específicas.
- Organiza imports y evita imports sin usar.
- Evita estado global y duplicación innecesaria.
- Justifica al menos una ocasión en la que decidiste no crear una abstracción.

Trabaja en pasos pequeños y ejecuta el programa después de cada cambio. No incorpores pytest, unittest como tema central, bases de datos, APIs ni dependencias externas. No se entrega una solución completa.

---

# 39. Comprobación de aprendizaje

- [ ] Aplico PEP 8 y convenciones de nomenclatura con criterio.
- [ ] Organizo imports y elimino los que no se utilizan.
- [ ] Escribo type hints básicos y para colecciones modernas.
- [ ] Comprendo uniones con `|` y la relación entre `str | None` y `Optional[str]`.
- [ ] Uso `Callable`, `Iterable`, `Iterator`, `Sequence` y `Mapping` apropiadamente.
- [ ] Comprendo los límites de `Any`.
- [ ] Uso `ClassVar`, `Literal` y `TypedDict` sin confundirlos con validación runtime.
- [ ] Creo dataclasses y comprendo sus métodos generados.
- [ ] Utilizo `field(default_factory=list)` para campos mutables.
- [ ] Valido o normalizo datos mediante `__post_init__()` cuando corresponde.
- [ ] Comprendo la inmutabilidad superficial de `frozen=True`.
- [ ] Distingo dataclass de clase tradicional según el problema.
- [ ] Escribo docstrings y comentarios que aportan contexto.
- [ ] Diseño funciones pequeñas y utilizo guard clauses para reducir anidamiento.
- [ ] Aplico DRY sin caer en abstracción prematura.
- [ ] Uso condiciones booleanas claras e `is None`.
- [ ] Distingo EAFP de LBYL y elijo según el contexto.
- [ ] Refactorizo en cambios pequeños sin alterar intencionalmente el comportamiento.
- [ ] Distingo formatter, linter, type checker y pruebas, incluidos sus límites.

---

# 40. Lo que aprendimos

```text
Código funcional
       ↓
Nombres claros
       ↓
Tipado explícito
       ↓
Documentación
       ↓
Estructuras adecuadas
       ↓
Refactorización
       ↓
Código mantenible
```

Ya podemos escribir código más explícito y estructurado. Sin embargo, cuando modificamos un programa necesitamos comprobar que sigue funcionando.

La Unidad 13 introducirá pruebas automatizadas, pytest, asserts, fixtures, parametrización, mocks y cobertura.

---

# 🧭 Navegación

⬅️ [Volver a la Unidad 11 — Python avanzado](../unidad11-python-avanzado/)

🏠 [Volver al inicio del curso](../README.md)

➡️ [Continuar a la Unidad 13 — Pruebas](../unidad13-pruebas/)


---

## Continuar el curso

- **Unidad anterior:** [Unidad 11 — Python avanzado](../unidad11-python-avanzado/README.md)
- **Volver al índice:** [Todas las unidades](../README.md)
- **Siguiente unidad:** [Unidad 13 — Pruebas automatizadas con Python](../unidad13-pruebas/README.md)
