# Unidad 13 — Pruebas automatizadas con Python

[Volver al índice del curso](../README.md) · [Ver el curso en Aprende con Leli](https://lelyliliana.github.io/aprende-con-leli/cursos/python/)

Cuando modificamos un programa, necesitamos comprobar que lo anterior continúa funcionando. En esta unidad comenzaremos con `assert` y una breve introducción a `unittest`, pero utilizaremos **pytest** como herramienta principal para construir y ejecutar pruebas reales.

---

## 🎯 Objetivos de aprendizaje

Al finalizar podrás:

- Explicar qué es una prueba automatizada y qué riesgos ayuda a reducir.
- Diferenciar casos felices, casos límite y errores esperados.
- Organizar y ejecutar pruebas con pytest.
- Utilizar parametrización, fixtures, `pytest.raises`, `tmp_path` y `capsys`.
- Sustituir dependencias sencillas mediante `monkeypatch` y mocks.
- Distinguir pruebas unitarias y de integración.
- Relacionar pruebas, cobertura, TDD y refactorización segura.
- Diseñar pruebas rápidas, deterministas, aisladas y centradas en comportamiento.

---

## 📋 Antes de comenzar

Necesitas haber completado la Unidad 12. Utilizaremos funciones, clases, excepciones, módulos, entornos virtuales, type hints, dataclasses y refactorización.

No utilizaremos bases de datos, APIs, red ni servicios externos. Pytest es la única dependencia necesaria para ejecutar el proyecto de ejemplo; no se instala automáticamente.

---

# 1. ¿Por qué hacer pruebas?

Al cambiar código podemos romper algo que funcionaba. La comprobación manual se vuelve lenta cuando existen muchas funciones, reglas y casos límite.

```text
Código
  ↓
Pruebas
  ↓
Confianza
  ↓
Cambios más seguros
```

Una prueba automatizada prepara un escenario, ejecuta código y compara el resultado real con el esperado. Reduce riesgos y detecta regresiones, pero no demuestra que un sistema sea perfecto: solo comprueba los casos diseñados.

---

# 2. Prueba manual y prueba automatizada

Una comprobación manual muestra un valor para que una persona lo interprete:

```python
def sumar(numero_1: float, numero_2: float) -> float:
    return numero_1 + numero_2

print(sumar(2, 3))
```

Una prueba automatizada expresa directamente la expectativa:

```python
def sumar(numero_1: float, numero_2: float) -> float:
    return numero_1 + numero_2

assert sumar(2, 3) == 5
```

Si la condición es verdadera, el programa continúa. Si es falsa, Python lanza `AssertionError`.

---

# 3. `assert` y sus límites

Podemos añadir un mensaje para explicar el fallo:

```python
def sumar(numero_1: float, numero_2: float) -> float:
    return numero_1 + numero_2

resultado = sumar(2, 3)
esperado = 5

assert resultado == esperado, "El resultado de la suma es incorrecto"
```

`assert` es apropiado en pruebas y para ciertas invariantes internas. No debe validar datos esenciales de usuario en código de producción, porque Python puede ejecutarse con optimizaciones que eliminan los asserts. Para reglas indispensables utiliza una condición y `raise`:

```python
def dividir(dividendo: float, divisor: float) -> float:
    if divisor == 0:
        raise ValueError("El divisor no puede ser cero")
    return dividendo / divisor
```

---

# 4. Caso feliz, casos límite y errores esperados

El **caso feliz** representa el uso normal:

```python
def sumar(numero_1: float, numero_2: float) -> float:
    return numero_1 + numero_2

assert sumar(2, 3) == 5
```

Los **casos límite** exploran fronteras: cero, colección vacía, un único elemento o valores mínimo y máximo permitidos.

```python
def sumar(numero_1: float, numero_2: float) -> float:
    return numero_1 + numero_2

assert sumar(0, 0) == 0
assert sumar(-1, 1) == 0
assert sumar(2.5, 1.5) == 4.0
```

También debemos comprobar **errores esperados**. Si `calcular_promedio([])` promete lanzar `ValueError`, esa excepción forma parte de su comportamiento observable.

---

# 5. Introducción breve a `unittest`

Python incluye `unittest` en su biblioteca estándar:

```python
import unittest

def sumar(numero_1: float, numero_2: float) -> float:
    return numero_1 + numero_2

class TestCalculadora(unittest.TestCase):
    def test_sumar(self) -> None:
        self.assertEqual(sumar(2, 3), 5)

if __name__ == "__main__":
    unittest.main()
```

`TestCase` reúne pruebas y ofrece métodos como `assertEqual`. Es una solución completa y estándar. En esta unidad solo necesitamos reconocerla porque pytest permitirá comenzar con una sintaxis más directa.

---

# 6. ¿Por qué utilizaremos pytest?

Pytest es una herramienta externa popular que ofrece:

- Pruebas sencillas con `assert` normal.
- Descubrimiento automático.
- Fixtures para preparar datos y recursos.
- Parametrización de varios casos.
- Un ecosistema amplio de extensiones.

Ser externo significa que debes instalarlo en un entorno virtual; no viene incluido con Python.

---

# 7. Preparar el proyecto real

Entra a la raíz del ejemplo:

```bash
cd unidad13-pruebas/ejemplos/proyecto_pruebas
```

Crea un entorno virtual sin repetir todo el procedimiento de la Unidad 9.

### Windows

```powershell
py -m venv .venv
.venv\Scripts\Activate.ps1
```

### Linux y macOS

```bash
python3 -m venv .venv
source .venv/bin/activate
```

Instala y comprueba pytest dentro del entorno:

```bash
python -m pip install pytest
python -m pytest --version
```

No fijamos una versión concreta porque no es necesaria para estos ejemplos.

---

# 8. Estructura del ejemplo

```text
proyecto_pruebas/
├── calculadora.py
├── estudiantes.py
└── tests/
    ├── test_calculadora.py
    └── test_estudiantes.py
```

Los módulos contienen código de aplicación y `tests/` contiene sus pruebas. No necesitamos `__init__.py` porque ejecutaremos pytest desde `proyecto_pruebas/`, una raíz desde la cual los módulos se pueden importar directamente.

---

# 9. Descubrimiento de pruebas

Pytest descubre normalmente archivos llamados `test_*.py` o `*_test.py`, y funciones cuyos nombres comienzan con `test_`:

```python
def test_sumar_dos_numeros() -> None:
    assert 2 + 3 == 5
```

Un nombre como `test_calcular_promedio_con_tres_notas()` documenta mejor el comportamiento que `test_1()`.

---

# 10. Primera prueba real con pytest

El archivo `calculadora.py` contiene:

```python
def sumar(numero_1: float, numero_2: float) -> float:
    """Devuelve la suma de dos números."""
    return numero_1 + numero_2
```

Y `tests/test_calculadora.py` importa la función:

```python
from calculadora import sumar

def test_sumar_dos_numeros_positivos() -> None:
    assert sumar(2, 3) == 5
```

La prueba comprueba nuestro contrato, no que Python sepa sumar: verifica que `sumar()` utiliza correctamente sus entradas y entrega el resultado esperado.

---

# 11. Ejecutar pruebas

Ejecuta desde `unidad13-pruebas/ejemplos/proyecto_pruebas/`:

```bash
python -m pytest
```

Pytest informa pruebas que pasaron (`passed`) y fallos (`failed`). Para ver cada caso:

```bash
python -m pytest -v
```

También puedes ejecutar un archivo:

```bash
python -m pytest tests/test_calculadora.py
```

O una prueba concreta:

```bash
python -m pytest tests/test_calculadora.py::test_sumar_dos_numeros_positivos
```

`python -m pytest` ayuda a utilizar pytest con el intérprete del entorno activo.

---

# 12. Patrón AAA

AAA organiza una prueba en tres momentos:

1. **Arrange:** preparar datos y objetos.
2. **Act:** ejecutar el comportamiento.
3. **Assert:** comprobar el resultado.

```python
def calcular_total(precio: float, cantidad: int) -> float:
    return precio * cantidad

def test_calcular_total() -> None:
    precio = 2500.0
    cantidad = 4

    total = calcular_total(precio, cantidad)

    assert total == 10000.0
```

Las líneas en blanco hacen visibles las fases. No es obligatorio escribir comentarios `Arrange`, `Act` y `Assert` en cada prueba.

---

# 13. Varios casos y parametrización

Podríamos crear `test_sumar_positivos`, `test_sumar_negativos` y `test_sumar_con_cero`. Cuando la operación es la misma y solo cambian datos y resultado, la parametrización evita duplicación:

```python
import pytest

def sumar(numero_1: float, numero_2: float) -> float:
    return numero_1 + numero_2

@pytest.mark.parametrize(
    ("numero_1", "numero_2", "esperado"),
    [
        (2, 3, 5),
        (-1, 1, 0),
        (0, 0, 0),
        (2.5, 1.5, 4.0),
    ],
)
def test_sumar_varios_casos(
    numero_1: float,
    numero_2: float,
    esperado: float,
) -> None:
    assert sumar(numero_1, numero_2) == esperado
```

Pytest crea un caso independiente por cada tupla. Parametriza casos relacionados y mantén datos comprensibles; una tabla gigantesca puede dificultar el diagnóstico.

Para límites académicos:

```python
import pytest

def validar_nota(nota: float) -> None:
    if not 0.0 <= nota <= 5.0:
        raise ValueError("Nota inválida")

@pytest.mark.parametrize("nota", [0.0, 3.0, 5.0])
def test_aceptar_notas_validas(nota: float) -> None:
    validar_nota(nota)
```

Que la función termine sin excepción es la expectativa de esta prueba.

---

# 14. Excepciones con `pytest.raises`

El context manager `pytest.raises` comprueba que el bloque lance la excepción indicada:

```python
import pytest

def calcular_promedio(notas: list[float]) -> float:
    if not notas:
        raise ValueError("La lista de notas está vacía")
    return sum(notas) / len(notas)

def test_promedio_sin_notas_lanza_error() -> None:
    with pytest.raises(ValueError):
        calcular_promedio([])
```

También podemos comprobar parte del mensaje:

```python
import pytest

def calcular_promedio(notas: list[float]) -> float:
    if not notas:
        raise ValueError("La lista de notas está vacía")
    return sum(notas) / len(notas)

def test_promedio_sin_notas_describe_el_error() -> None:
    with pytest.raises(ValueError, match="vacía"):
        calcular_promedio([])
```

No acoples una prueba al texto exacto si el mensaje no forma parte importante del contrato. Comprobar un fragmento estable suele ser suficiente.

---

# 15. Fixtures: preparación reutilizable

Varias pruebas pueden necesitar el mismo estudiante. Una fixture es una función marcada con `@pytest.fixture`:

```python
import pytest
from estudiantes import Estudiante

@pytest.fixture
def estudiante_con_notas() -> Estudiante:
    return Estudiante("Ana", [4.0, 3.5, 4.5])

def test_calcular_promedio(estudiante_con_notas: Estudiante) -> None:
    assert estudiante_con_notas.calcular_promedio() == 4.0
```

Pytest reconoce el nombre del parámetro, ejecuta la fixture y entrega su resultado a la prueba. No es una variable global: normalmente cada prueba obtiene su propia ejecución de la fixture.

Una fixture también puede devolver datos simples:

```python
import pytest

@pytest.fixture
def notas_validas() -> list[float]:
    return [4.0, 3.5, 4.5]

def test_hay_tres_notas(notas_validas: list[float]) -> None:
    assert len(notas_validas) == 3
```

Mantén las fixtures pequeñas. Si ocultan demasiadas decisiones, será difícil saber cómo se preparó el escenario.

---

# 16. Fixtures con `yield`

Una fixture puede preparar un recurso antes de `yield` y limpiarlo después:

```python
from collections.abc import Iterator
from pathlib import Path

import pytest

@pytest.fixture
def archivo_temporal(tmp_path: Path) -> Iterator[Path]:
    ruta = tmp_path / "datos.txt"
    ruta.write_text("Ana\n", encoding="utf-8")
    yield ruta
    # tmp_path será eliminado por pytest; aquí podrían cerrarse otros recursos.

def test_archivo_contiene_nombre(archivo_temporal: Path) -> None:
    assert archivo_temporal.read_text(encoding="utf-8") == "Ana\n"
```

El código posterior a `yield` corresponde al teardown. En este ejemplo pytest ya administra la carpeta, pero la forma permite comprender el ciclo de preparación y limpieza.

---

# 17. Archivos seguros con `tmp_path`

`tmp_path` es una fixture integrada que entrega una carpeta temporal exclusiva para la prueba. Así evitamos tocar archivos reales del proyecto:

```python
from pathlib import Path

def guardar_texto(ruta: Path, contenido: str) -> None:
    ruta.write_text(contenido, encoding="utf-8")

def test_guardar_texto(tmp_path: Path) -> None:
    ruta = tmp_path / "reporte.txt"

    guardar_texto(ruta, "Promedio: 4.0")

    assert ruta.read_text(encoding="utf-8") == "Promedio: 4.0"
```

Cada prueba debe crear sus datos y no depender de archivos producidos por otra.

---

# 18. Probar JSON temporal

```python
import json
from pathlib import Path

def guardar_estudiantes(ruta: Path, datos: list[dict[str, object]]) -> None:
    ruta.write_text(
        json.dumps(datos, ensure_ascii=False),
        encoding="utf-8",
    )

def cargar_estudiantes(ruta: Path) -> list[dict[str, object]]:
    contenido = ruta.read_text(encoding="utf-8")
    return json.loads(contenido)

def test_guardar_y_cargar_estudiantes(tmp_path: Path) -> None:
    ruta = tmp_path / "estudiantes.json"
    datos = [{"nombre": "Ana", "nota": 4.5}]

    guardar_estudiantes(ruta, datos)
    recuperados = cargar_estudiantes(ruta)

    assert recuperados == datos
```

Esta prueba integra dos funciones reales con el sistema de archivos temporal, sin acceder a una base de datos ni a la red.

---

# 19. Capturar salida con `capsys`

`capsys` captura lo escrito en la salida estándar:

```python
import pytest

def mostrar_saludo(nombre: str) -> None:
    print(f"Hola, {nombre}")

def test_mostrar_saludo(capsys: pytest.CaptureFixture[str]) -> None:
    mostrar_saludo("Ana")

    captura = capsys.readouterr()

    assert captura.out == "Hola, Ana\n"
```

Cuando sea posible, una función que devuelve datos suele ser más fácil de probar que otra muy acoplada a `print()`. Usa `capsys` cuando la salida sea realmente parte del comportamiento.

---

# 20. Sustituciones temporales con `monkeypatch`

`monkeypatch` reemplaza temporalmente un valor o comportamiento durante una prueba. Al terminar, pytest restaura el original.

```python
import pytest

def leer_nombre() -> str:
    return input("Nombre: ").strip()

def test_leer_nombre(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setattr("builtins.input", lambda _: "Ana")

    resultado = leer_nombre()

    assert resultado == "Ana"
```

No abusamos de pruebas para `input()`. Es preferible separar la interfaz de la lógica y probar directamente las funciones que reciben valores.

---

# 21. Mocks: aislar una dependencia

Un mock es un objeto simulado. Puede representar una API, correo, base de datos o reloj sin utilizar el recurso real. `Mock` pertenece a la biblioteca estándar:

```python
from unittest.mock import Mock

def duplicar_dato(servicio: object) -> int:
    dato = servicio.obtener_dato()
    return dato * 2

servicio = Mock()
servicio.obtener_dato.return_value = 10

resultado = duplicar_dato(servicio)

assert resultado == 20
servicio.obtener_dato.assert_called_once()
```

Además del resultado, comprobamos que la dependencia recibió una llamada. Hazlo solo si esa interacción forma parte del contrato relevante.

`patch` sustituye temporalmente un nombre en el lugar donde se utiliza:

```python
from unittest.mock import patch

def obtener_hora() -> str:
    return "hora real"

with patch(__name__ + ".obtener_hora", return_value="10:00"):
    assert obtener_hora() == "10:00"
```

Demasiados mocks pueden crear pruebas que replican la implementación interna y sobreviven aunque el sistema real falle. Prioriza comportamiento observable y utiliza objetos reales cuando sean rápidos y seguros.

---

# 22. Pruebas unitarias y de integración

Una prueba unitaria comprueba una unidad pequeña de comportamiento con un aislamiento razonable. Una prueba de integración comprueba que varias partes reales colaboran, por ejemplo persistencia y archivo temporal.

| Aspecto | Unitaria | Integración |
|---|---|---|
| Alcance | Pequeño | Varias piezas conectadas |
| Dependencias | Aisladas cuando aporta valor | Reales dentro del límite elegido |
| Velocidad habitual | Muy rápida | Puede ser más lenta |
| Ejemplo | Calcular un promedio | Guardar y cargar JSON temporal |

La pirámide de pruebas propone muchas pruebas pequeñas, algunas integraciones y pocas pruebas de extremo a extremo. Es una guía, no un dogma universal; la combinación depende del sistema y sus riesgos.

---

# 23. TDD: rojo, verde y refactorización

Test-Driven Development propone un ciclo:

```text
Red: escribir una prueba que falla
             ↓
Green: implementar lo mínimo para que pase
             ↓
Refactor: mejorar conservando las pruebas verdes
```

Para crear `es_par()`:

1. Escribir `assert es_par(4) is True`.
2. Observar el fallo porque todavía no existe el comportamiento.
3. Implementar la función.
4. Ejecutar hasta que pase.
5. Refactorizar si existe algo que mejorar.

TDD es una opción de trabajo, no un requisito para aprovechar pruebas. No dejaremos pruebas deliberadamente fallidas en el repositorio.

---

# 24. Pruebas y refactorización

```text
Pruebas pasan
      ↓
Cambiar estructura interna
      ↓
Pruebas siguen pasando
      ↓
Mayor confianza
```

Si reemplazamos una comprensión por un ciclo y el resultado observable es idéntico, las pruebas deberían continuar pasando. Una prueba frágil que inspecciona variables internas obligaría a cambiarla sin que el comportamiento real haya cambiado.

Prioriza probar:

- Reglas de negocio.
- Transformaciones y resultados.
- Casos límite.
- Errores esperados.
- Interacciones externas relevantes.

No es necesario comprobar directamente que Python suma correctamente, getters sin lógica o detalles internos sin efecto observable, salvo que exista una razón concreta.

---

# 25. Cobertura con criterio

La cobertura indica qué partes del código fueron ejecutadas durante las pruebas. Una línea ejecutada puede no haber sido comprobada correctamente, por lo que **100 % de cobertura no significa 100 % de calidad**.

Como ampliación opcional existe `pytest-cov`:

```bash
python -m pip install pytest-cov
python -m pytest --cov=.
```

No necesitas instalarlo para esta unidad. Utiliza la cobertura para descubrir zonas sin explorar, no como una puntuación que sustituye el diseño de buenos casos.

---

# 26. Pruebas rápidas, deterministas y aisladas

Una suite confiable procura:

- Mismos datos de entrada, mismo resultado.
- Evitar red real, esperas con `sleep()` y hora real innecesaria.
- Utilizar carpetas temporales en vez de archivos compartidos.
- Permitir que cada prueba se ejecute sola y en cualquier orden razonable.
- Evitar estado global mutable entre pruebas.

Si una prueba necesita el resultado de otra, ambas dejan de estar aisladas. Prepara el estado mediante una fixture o dentro de la propia prueba.

---

# 27. Recorrido por los archivos reales

`calculadora.py` contiene `sumar()` y `dividir()`. La división aplica una regla explícita: divisor cero produce `ValueError`. `test_calculadora.py` comprueba suma, decimales, negativos, cero, división y su error.

`estudiantes.py` define una dataclass con `field(default_factory=list)`. Una nota válida está entre `0.0` y `5.0`, incluidos los extremos. Calcular el promedio sin notas produce `ValueError`. `test_estudiantes.py` cubre creación, listas independientes, notas válidas, inválidas y límite, promedio y fixture.

Ejecuta la suite completa antes de experimentar:

```bash
python -m pytest -v
```

Después cambia temporalmente un resultado esperado para observar un reporte de fallo. Revierte ese cambio y confirma que todo vuelve a pasar.

---

# 28. Errores frecuentes

- Nombrar archivos o funciones sin el prefijo `test_` y esperar descubrimiento automático.
- Ejecutar pytest desde una ubicación equivocada o con un intérprete donde no está instalado.
- Confundir un fallo de expectativa con un error de importación o colección.
- Escribir un `assert` incorrecto o una prueba que no comprueba nada relevante.
- Usar `assert` para validación esencial de producción en lugar de `raise`.
- Hacer que las pruebas dependan de orden, estado global o una ejecución anterior.
- Modificar archivos reales cuando `tmp_path` ofrece aislamiento.
- Depender de red, hora real o esperas innecesarias.
- Olvidar `pytest.raises` al comprobar un error esperado.
- Crear fixtures con demasiado comportamiento o compartir objetos mutables accidentalmente.
- Parametrizar casos diferentes de manera tan compacta que resulte difícil comprenderlos.
- Mockear todo o verificar detalles internos irrelevantes.
- Perseguir 100 % de cobertura sin analizar la calidad de las expectativas.

---

# 29. Ejercicios

## Ejercicio 1 — Primer `assert`

Escribe una función que calcule el área de un rectángulo y comprueba un resultado mediante `assert`.

## Ejercicio 2 — Casos felices

Diseña tres casos normales para `sumar()` y explica qué comportamiento documenta cada uno.

## Ejercicio 3 — Casos límite

Prueba una función de notas con `0.0`, `5.0`, una sola nota y una lista vacía según su contrato.

## Ejercicio 4 — Error esperado

Define qué debe ocurrir al dividir por cero y escribe una prueba que compruebe la excepción elegida.

## Ejercicio 5 — Primera prueba pytest

Crea una función cuyo nombre comience con `test_` para comprobar una función académica pequeña.

## Ejercicio 6 — Ejecución detallada

Ejecuta la suite con `-v`, identifica los identificadores de las pruebas y ejecuta después un único archivo.

## Ejercicio 7 — Parametrización

Reúne al menos cuatro casos homogéneos de una función de cálculo mediante `pytest.mark.parametrize`.

## Ejercicio 8 — `pytest.raises`

Comprueba que una nota fuera del rango produzca `ValueError`.

## Ejercicio 9 — Mensaje del error

Agrega `match` al ejercicio anterior usando solo una parte estable y significativa del mensaje.

## Ejercicio 10 — Primera fixture

Crea una fixture que entregue un estudiante con tres notas y úsala para calcular su promedio.

## Ejercicio 11 — Fixture reutilizable

Usa la misma fixture en dos pruebas independientes sin permitir que una modificación contamine la otra.

## Ejercicio 12 — `tmp_path`

Escribe una prueba que cree, lea y compruebe un TXT dentro de `tmp_path`.

## Ejercicio 13 — JSON temporal

Guarda una colección académica como JSON temporal, cárgala y compara el resultado con los datos originales.

## Ejercicio 14 — `capsys`

Captura la salida de una función que muestra un reporte. Después considera si devolver una cadena simplificaría el diseño.

## Ejercicio 15 — Simular `input()`

Utiliza `monkeypatch` para proporcionar un nombre sin interacción humana y comprueba el valor normalizado.

## Ejercicio 16 — Primer `Mock`

Crea un servicio simulado que devuelva una nota y úsalo en una función que genere una descripción.

## Ejercicio 17 — Comprobar una llamada

Verifica con `assert_called_once_with()` que una dependencia recibió el código de estudiante correcto.

## Ejercicio 18 — Prueba unitaria

Diseña una prueba unitaria para una regla de aprobación y explica cuál es su unidad de comportamiento.

## Ejercicio 19 — Prueba de integración

Integra funciones reales de guardar y cargar con un archivo temporal, sin mocks ni archivos del proyecto.

## Ejercicio 20 — Refactorizar con pruebas

Ejecuta pruebas, refactoriza una función sin cambiar su contrato y vuelve a ejecutarlas.

## Ejercicio 21 — Detectar fragilidad

Revisa una prueba que depende de una variable interna o del orden de una lista irrelevante y reescríbela alrededor del comportamiento observable.

## Ejercicio 22 — Cobertura con criterio

Sin perseguir un porcentaje, identifica una rama importante no ejecutada y diseña un caso que compruebe su resultado.

## Ejercicio 23 — Diseñar una matriz de casos

Para `calcular_promedio()`, enumera casos felices, límites y errores antes de escribir las pruebas.

## Ejercicio 24 — Reparar una suite dependiente

Refactoriza tres pruebas que comparten estado global para que cada una prepare sus datos o use una fixture segura.

No consultes soluciones completas. Ejecuta primero una prueba específica y después la suite entera.

---

# 30. Reto — Suite de pruebas del sistema académico

Toma una versión simplificada del sistema académico y construye una suite con pytest.

## Comportamientos mínimos

### `Estudiante`

- Aceptar una nota válida.
- Rechazar una nota inválida.
- Calcular el promedio.
- Manejar explícitamente una lista vacía.

### `Curso`

- Agregar un estudiante.
- Evitar duplicados si esa regla forma parte de tu modelo.
- Buscar un estudiante.
- Calcular el promedio general.

### Persistencia

- Guardar y cargar JSON.
- Manejar archivo inexistente.
- Manejar JSON inválido.

## Requisitos técnicos

- Usa fixtures para datos compartidos de preparación.
- Parametriza casos homogéneos.
- Comprueba errores con `pytest.raises`.
- Utiliza `tmp_path` para todos los archivos.
- Incluye al menos un uso apropiado de `monkeypatch` o `Mock`.
- Mantén pruebas independientes del orden y sin estado global mutable.
- No uses bases de datos, APIs, red ni servicios externos.

No se entrega la solución completa. Diseña primero una tabla de comportamientos y resultados esperados.

---

# 31. Comprobación de aprendizaje

- [ ] Distingo una prueba manual de una automatizada.
- [ ] Uso `assert` y comprendo por qué no sustituye validaciones esenciales.
- [ ] Diseño casos felices, casos límite y errores esperados.
- [ ] Reconozco `unittest` como herramienta estándar introductoria.
- [ ] Instalo pytest en un entorno virtual y ejecuto la suite desde la raíz correcta.
- [ ] Comprendo descubrimiento, nombres y selección de pruebas.
- [ ] Organizo pruebas con Arrange, Act y Assert.
- [ ] Utilizo parametrización y `pytest.raises`.
- [ ] Creo fixtures pequeñas y comprendo su inyección por nombre.
- [ ] Uso `yield` para teardown cuando es necesario.
- [ ] Pruebo archivos con `tmp_path` y salida con `capsys`.
- [ ] Sustituyo `input()` mediante `monkeypatch`.
- [ ] Creo mocks sencillos y compruebo llamadas relevantes.
- [ ] Distingo pruebas unitarias y de integración.
- [ ] Comprendo el ciclo Red, Green, Refactor de TDD.
- [ ] Interpreto cobertura sin equipararla con calidad.
- [ ] Diseño pruebas aisladas, rápidas y deterministas.
- [ ] Refactorizo con mayor confianza sin probar detalles internos innecesarios.

---

# 32. Lo que aprendimos

```text
Código
  ↓
Caso
  ↓
Prueba
  ↓
Resultado esperado
  ↓
Comparación
 ↙       ↘
pasa     falla
```

```text
Pruebas
   ↓
Refactorización
   ↓
Pruebas
   ↓
Confianza
```

Hasta ahora hemos almacenado datos principalmente en memoria, TXT, CSV y JSON. La Unidad 14 introducirá persistencia estructurada mediante bases de datos y SQL.

---

# 🧭 Navegación

⬅️ [Volver a la Unidad 12 — Tipado y buenas prácticas](../unidad12-tipado-buenas-practicas/)

🏠 [Volver al inicio del curso](../README.md)

➡️ [Continuar a la Unidad 14 — Bases de datos](../unidad14-bases-datos/)


---

## Continuar el curso

- **Unidad anterior:** [Unidad 12 — Tipado y buenas prácticas](../unidad12-tipado-buenas-practicas/README.md)
- **Volver al índice:** [Todas las unidades](../README.md)
- **Siguiente unidad:** [Unidad 14 — Bases de datos con Python y SQLite](../unidad14-bases-datos/README.md)
