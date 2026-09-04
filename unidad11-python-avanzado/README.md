# Unidad 11 — Python avanzado

Esta unidad profundiza en iteración, evaluación perezosa, closures, decoradores y context managers: mecanismos distintos que permiten controlar cómo se producen valores y cómo se envuelven operaciones y recursos.

---

## 🎯 Objetivos de aprendizaje

Al finalizar podrás explicar y utilizar iterables, iteradores, generadores, closures, decoradores y administradores de contexto, seleccionándolos solo cuando mejoren el diseño.

---

## 📋 Antes de comenzar

Necesitas dominar funciones como valores, clases, excepciones, módulos y `with open()`. No usaremos metaclases, descriptores personalizados, `async` ni paquetes externos.

---

# 1. ¿Qué hace realmente un `for`?

```python
datos = [10, 20, 30]

for elemento in datos:
    print(elemento)
```

`for` trabaja con un **iterable**, objeto del cual puede obtenerse un iterador:

```text
iterable → iter() → iterador → next() → elementos
```

Listas, tuplas, cadenas, diccionarios, conjuntos y `range` son iterables. Iterable e iterador no significan exactamente lo mismo.

---

# 2. `iter()`, `next()` y `StopIteration`

```python
numeros = [10, 20, 30]
iterador = iter(numeros)

print(next(iterador))
print(next(iterador))
print(next(iterador))

try:
    print(next(iterador))
except StopIteration:
    print("El iterador se agotó")
```

El iterador conserva su posición. `for` obtiene el iterador, solicita valores y termina al encontrar `StopIteration`, sin que normalmente tengamos que manejarla.

---

# 3. Iteradores de una sola pasada

Una lista puede recorrerse nuevamente obteniendo otro iterador. Un iterador ya consumido no vuelve al inicio:

```python
resultado = map(lambda numero: numero * 2, [1, 2, 3])

print(list(resultado))
print(list(resultado))
```

Resultado:

```text
[2, 4, 6]
[]
```

Esto también se relaciona con `filter()` y `zip()`.

---

# 4. Iterador personalizado

```python
class Contador:
    def __init__(self, limite):
        self.actual = 1
        self.limite = limite

    def __iter__(self):
        return self

    def __next__(self):
        if self.actual > self.limite:
            raise StopIteration
        valor = self.actual
        self.actual += 1
        return valor

for numero in Contador(3):
    print(numero)
```

Un iterador implementa `__next__()` y `__iter__()` devuelve un iterador válido. Algunos objetos, como `Contador`, son iterable e iterador a la vez.

---

# 5. Generadores y `yield`

Un generador produce valores progresivamente:

```python
def contar_hasta(limite):
    numero = 1
    while numero <= limite:
        yield numero
        numero += 1

generador = contar_hasta(3)
print(type(generador))
print(next(generador))
print(next(generador))
print(next(generador))
```

Llamar la función no ejecuta todo: devuelve un generador. `yield` entrega un valor temporal y pausa el estado; `return` entrega un resultado y finaliza la función.

```python
def contar_hasta(limite):
    for numero in range(1, limite + 1):
        yield numero

for numero in contar_hasta(5):
    print(numero)
```

La evaluación perezosa produce bajo demanda y puede evitar materializar datos completos. No es automáticamente más rápida ni siempre preferible.

---

# 6. Expresiones generadoras

```python
lista = [numero ** 2 for numero in range(1, 6)]
generador = (numero ** 2 for numero in range(1, 6))

print(lista)
print(list(generador))
```

`[]` crea inmediatamente una lista reutilizable; `()` crea aquí una expresión generadora de una pasada. Los paréntesis no representan simplemente una tupla en este contexto.

---

# 7. Generadores para archivos y `yield from`

```python
from pathlib import Path

def leer_lineas(ruta):
    with ruta.open("r", encoding="utf-8") as archivo:
        for linea in archivo:
            yield linea.strip()

ruta = Path("datos.txt")
ruta.write_text("Ana\nLuis\n", encoding="utf-8")

for linea in leer_lineas(ruta):
    print(linea)
```

Las líneas se procesan progresivamente, útil para archivos grandes.

```python
def combinar():
    yield from [1, 2, 3]
    yield from [4, 5]

print(list(combinar()))
```

`yield from` delega la producción a otro iterable. Los métodos avanzados como `send()` quedan como anticipo para otro momento.

---

# 8. Closures

Un closure combina una función interna con variables del entorno donde fue creada:

```python
def crear_saludo(mensaje):
    def saludar(nombre):
        return f"{mensaje}, {nombre}"
    return saludar

saludo_formal = crear_saludo("Buenos días")
print(saludo_formal("Ana"))
```

La función conserva `mensaje` después de terminar `crear_saludo`.

`nonlocal` permite modificar una variable del ámbito envolvente:

```python
def crear_contador():
    cuenta = 0

    def incrementar():
        nonlocal cuenta
        cuenta += 1
        return cuenta

    return incrementar

contador = crear_contador()
print(contador())
print(contador())
```

Local pertenece a la función actual, `nonlocal` a una función exterior y global al módulo. Un closure sirve para configuración o estado pequeño; si crece, una clase puede ser más clara.

---

# 9. Primer decorador

Un decorador recibe una función y devuelve otra que la envuelve:

```python
def decorador(funcion):
    def envoltura():
        print("Antes")
        resultado = funcion()
        print("Después")
        return resultado
    return envoltura

def saludar():
    print("Hola")
    return "saludo completado"

saludar = decorador(saludar)
print(saludar())
```

La sintaxis `@` expresa la misma transformación:

```python
def decorador(funcion):
    def envoltura():
        return funcion()
    return envoltura

@decorador
def saludar():
    return "Hola"

print(saludar())
```

---

# 10. Decoradores generales y `wraps`

```python
from functools import wraps

def registrar_llamada(funcion):
    @wraps(funcion)
    def envoltura(*args, **kwargs):
        print(f"Llamando a {funcion.__name__}")
        return funcion(*args, **kwargs)
    return envoltura

@registrar_llamada
def sumar(numero_1, numero_2):
    """Suma dos números."""
    return numero_1 + numero_2

print(sumar(3, 4))
print(sumar.__name__)
```

`*args` y `**kwargs` admiten firmas distintas; la envoltura preserva el retorno. `wraps` conserva metadatos como `__name__` y `__doc__`.

---

# 11. Medir y registrar llamadas

```python
from functools import wraps
from time import perf_counter

def medir_tiempo(funcion):
    @wraps(funcion)
    def envoltura(*args, **kwargs):
        inicio = perf_counter()
        resultado = funcion(*args, **kwargs)
        duracion = perf_counter() - inicio
        print(f"Duración aproximada: {duracion:.6f} s")
        return resultado
    return envoltura

@medir_tiempo
def sumar_numeros(limite):
    return sum(range(limite))

print(sumar_numeros(1000))
```

Es demostrativo, no un benchmark riguroso. El registro profesional se estudiará después.

---

# 12. Decoradores con parámetros y apilados

```python
from functools import wraps

def repetir(veces):
    def decorador(funcion):
        @wraps(funcion)
        def envoltura(*args, **kwargs):
            resultado = None
            for _ in range(veces):
                resultado = funcion(*args, **kwargs)
            return resultado
        return envoltura
    return decorador

@repetir(3)
def saludar(nombre):
    print(f"Hola, {nombre}")
    return nombre

print(saludar("Ana"))
```

Las capas reciben primero configuración, luego función y finalmente argumentos de llamada.

```text
@decorador_a
@decorador_b
def funcion(): ...

funcion = decorador_a(decorador_b(funcion))
```

El decorador más cercano se aplica primero. Un decorador propio también puede envolver métodos; `@property`, `@classmethod` y `@staticmethod` son decoradores integrados con propósitos específicos.

---

# 13. Context managers

`with` funciona con objetos que controlan entrada y salida:

```python
class Recurso:
    def __enter__(self):
        print("Entrando")
        return self

    def usar(self):
        print("Usando recurso")

    def __exit__(self, tipo_error, valor_error, traceback):
        print("Saliendo")
        return False

with Recurso() as recurso:
    recurso.usar()
```

Sin excepción, los tres parámetros de error son `None`. Devolver `True` puede suprimir una excepción; `False` o `None` permite propagarla. No suprimas fallos sin una razón explícita.

---

# 14. `contextmanager`

```python
from contextlib import contextmanager

@contextmanager
def recurso_temporal():
    print("Entrando")
    try:
        yield "recurso disponible"
    finally:
        print("Limpiando y saliendo")

with recurso_temporal() as recurso:
    print(recurso)
```

Antes de `yield` ocurre la entrada; el valor queda disponible con `as`; después ocurre la salida. `finally` garantiza limpieza incluso con una excepción. Aquí `yield` forma un context manager, no un flujo de datos normal. No necesitamos `ExitStack`.

Ejemplo controlado con error:

```python
from contextlib import contextmanager

@contextmanager
def sesion():
    print("Abrir")
    try:
        yield
    finally:
        print("Cerrar")

try:
    with sesion():
        raise ValueError("Problema controlado")
except ValueError:
    print("Error manejado")
```

---

# 15. Protocolos y modelo de datos

Python integra objetos mediante protocolos informales:

```text
iteración      → __iter__ y __next__
context manager → __enter__ y __exit__
representación → __str__ y __repr__
```

`len(objeto)`, `for` y `with` activan métodos especiales correspondientes. No llamamos dunder methods directamente como práctica habitual ni introducimos `typing.Protocol` todavía.

---

# 16. Pipeline perezoso

```python
def producir_notas(limite):
    for numero in range(1, limite + 1):
        print(f"Produciendo {numero}")
        yield numero * 0.5

def filtrar_validas(notas):
    for nota in notas:
        if 0.0 <= nota <= 5.0:
            yield nota

for nota in filtrar_validas(producir_notas(12)):
    print(f"Procesada: {nota}")
```

Cada dato avanza progresivamente sin crear listas intermedias.

---

# 17. Decorador de validación

```python
from functools import wraps

def validar_nota(funcion):
    @wraps(funcion)
    def envoltura(nota, *args, **kwargs):
        if not 0.0 <= nota <= 5.0:
            raise ValueError("Nota fuera del rango")
        return funcion(nota, *args, **kwargs)
    return envoltura

@validar_nota
def describir_nota(nota, prefijo="Nota"):
    return f"{prefijo}: {nota:.1f}"

print(describir_nota(4.5, prefijo="Final"))
```

---

# 18. Combinar sin crear una monstruosidad

```text
generador → procesamiento perezoso → función decorada → contexto → ejecución controlada
```

Esta combinación puede ser útil, pero cada pieza debe conservar una responsabilidad comprensible. Varios pasos nombrados suelen ser mejores que una expresión sofisticada.

---

# 19. Cuándo no usar estas herramientas

- Usa una lista pequeña si es más clara que un generador.
- Usa una función normal si no necesitas un closure.
- No ocultes lógica crítica dentro de un decorador.
- No crees un context manager sin recurso o contexto real.
- No implementes un iterador si un iterable integrado resuelve el problema.

---

# 20. Errores frecuentes

- Confundir iterable e iterador, llamar `next()` al primero o reutilizar uno consumido.
- Omitir `StopIteration` o implementar incorrectamente `__iter__()`.
- Confundir `yield` con `return` o esperar una lista de un generador.
- Consumir un generador dos veces o convertirlo inmediatamente sin necesidad.
- Confundir local, `nonlocal` y global; olvidar `nonlocal` al modificar el exterior.
- Usar un closure cuando una clase sería más clara.
- Ejecutar una función al decorarla en vez de pasarla.
- Perder el retorno, argumentos o metadatos en una envoltura.
- Crear decoradores complejos u olvidar su orden de aplicación.
- Omitir limpieza, suprimir excepciones accidentalmente o devolver `True` sin comprenderlo.
- Confundir el `yield` de `contextmanager` con un generador de datos y omitir `finally`.

---

# 21. Ejercicios

1. Crea una lista con tres temperaturas, obtén su iterador mediante `iter()` y guarda el resultado en una variable descriptiva. Imprime el tipo de la lista y el tipo del iterador.
2. Solicita con `next()` las tres temperaturas del ejercicio anterior. Antes de ejecutar, predice qué valor entregará cada llamada y después comprueba tu respuesta.
3. Realiza una cuarta llamada a `next()` dentro de `try` y captura específicamente `StopIteration`. Muestra un mensaje que explique que ya no quedan temperaturas.
4. Crea un objeto `map()` que duplique tres precios. Conviértelo dos veces a lista, imprime ambos resultados y explica por qué el segundo está vacío.
5. Implementa una clase iteradora `CuentaRegresiva` que reciba un número inicial, produzca valores hasta `1` y luego lance `StopIteration`. Recorre una instancia con `for`.
6. Escribe el generador `generar_pares(limite)` para producir, uno a uno, los números pares desde `2` hasta el límite incluido. Compruébalo con un ciclo.
7. Crea dos funciones pequeñas: una devuelve un número con `return` y otra lo produce con `yield`. Imprime los tipos que retorna cada llamada y explica la diferencia observada.
8. Construye una expresión generadora con los cuadrados del `1` al `10`. Consume solamente los tres primeros valores mediante `next()` y luego recorre los restantes.
9. Crea un archivo de práctica con varias líneas y un generador que las entregue sin el salto final. Usa `with` para leerlo y procesa las líneas sin cargar el archivo completo.
10. Define dos generadores de nombres y un tercero que delegue en ambos mediante `yield from`. Convierte el generador combinado a lista únicamente para verificar su resultado.
11. Crea un closure `crear_calculador_descuento(porcentaje)` que recuerde el porcentaje y devuelva una función capaz de calcular el precio final de distintos productos.
12. Construye un contador mediante closure. Usa `nonlocal` para aumentar el valor conservado y demuestra con tres llamadas que el estado persiste.
13. Escribe un decorador que muestre un mensaje antes y después de una función sin argumentos. Aplícalo mediante la asignación explícita `funcion = decorador(funcion)`.
14. Repite el ejercicio anterior utilizando la sintaxis `@decorador`. Ejecuta la función decorada al menos dos veces y compara el comportamiento con la versión explícita.
15. Mejora el decorador para aceptar `*args` y `**kwargs`, llamar una función que calcule el total de un producto y devolver correctamente el resultado. Verifica el retorno con `print()`.
16. Agrega `@wraps` al decorador anterior. Comprueba `__name__` y `__doc__` antes y después de incorporarlo, y anota qué metadatos se preservan.
17. Crea `@repetir(veces)`, un decorador parametrizado que ejecute una función la cantidad indicada. Conserva argumentos, retorno y metadatos.
18. Diseña dos decoradores sencillos que impriman mensajes de entrada y salida. Apílalos, predice el orden completo de los mensajes y contrástalo con la ejecución.
19. Implementa una clase `SesionEstudio` con `__enter__()` y `__exit__()`. Debe anunciar el inicio y el cierre de una sesión, y devolver desde `__enter__()` un objeto utilizable con `as`.
20. Crea el mismo concepto con `@contextmanager`. Coloca la limpieza en `finally` y demuestra tanto una ejecución normal como otra que produzca una excepción controlada.
21. Modifica temporalmente `__exit__()` para que devuelva `True` y después `False`. Provoca un `ValueError` controlado y explica cómo cambia la propagación de la excepción.
22. Para una lista pequeña, un mensaje configurado y la apertura de un archivo, decide razonadamente si usarías una lista o generador, una función normal o closure, y `with` o manejo manual.
23. Construye un pipeline perezoso que genere notas, descarte las que estén fuera de `0.0` a `5.0` y transforme las válidas a mensajes. Evita listas intermedias.
24. Recibe un decorador defectuoso que no retorna el resultado ni usa `wraps`. Refactorízalo, pruébalo con argumentos posicionales y nombrados, y verifica nombre, documentación y retorno.

---

# 22. Reto — Procesador perezoso de registros

Genera un TXT o JSON de práctica y construye:

```text
archivo → generador de registros → filtrado → transformación → reporte
```

Requisitos:

- Produce registros progresivamente sin cargar todo innecesariamente.
- Usa otra función generadora o expresión generadora para filtrar.
- Aplica un decorador de medición o registro con `wraps` y retorno preservado.
- Administra una sesión simulada mediante context manager.
- Garantiza limpieza con `finally` y maneja excepciones específicas.
- Convierte a lista solo donde sea necesario.
- Mantén funciones pequeñas y evita complejidad artificial.

No se entrega la solución completa.

---

# 23. Comprobación de aprendizaje

- [ ] Distingo iterable, iterador, `iter()`, `next()` y `StopIteration`.
- [ ] Implemento `__iter__()` y `__next__()`.
- [ ] Comprendo generadores, `yield`, expresiones generadoras y evaluación perezosa.
- [ ] Uso `yield from` y comprendo el consumo.
- [ ] Creo closures y utilizo `nonlocal` correctamente.
- [ ] Creo decoradores que preservan argumentos, retorno y metadatos.
- [ ] Comprendo decoradores parametrizados y apilados.
- [ ] Implemento `__enter__()` y `__exit__()`.
- [ ] Creo context managers con `contextmanager`, `yield` y `finally`.
- [ ] Selecciono herramientas avanzadas solo cuando aportan claridad.

---

# 24. Lo que aprendimos

```text
Iterable → Iterador → Generador → Evaluación perezosa
Función → Closure → Decorador
Recurso → Context manager → Entrada y salida controladas
```

La Unidad 12 se centrará en código explícito y mantenible mediante type hints, `typing`, `dataclasses`, documentación, PEP 8 y herramientas de calidad.

---

# 🧭 Navegación

⬅️ [Volver a la Unidad 10 — Python funcional](../unidad10-python-funcional/)

🏠 [Volver al inicio del curso](../README.md)

➡️ [Continuar a la Unidad 12 — Tipado y buenas prácticas](../unidad12-tipado-buenas-practicas/)
