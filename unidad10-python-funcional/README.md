# Unidad 10 — Python funcional

[Volver al índice del curso](../README.md) · [Ver el curso en Aprende con Leli](https://lelyliliana.github.io/aprende-con-leli/cursos/python/)

Python permite combinar estilos imperativo, orientado a objetos y funcional. En esta unidad utilizaremos funciones para transformar, filtrar, combinar y reducir datos sin convertir la brevedad en un objetivo por sí misma.

---

## 🎯 Objetivos de aprendizaje

Al finalizar podrás tratar funciones como valores, crear funciones de orden superior, utilizar `sorted()`, `map()`, `filter()`, comprensiones, `any()`, `all()`, `zip()`, `enumerate()` y `reduce()`, y reconocer efectos secundarios.

---

## 📋 Antes de comenzar

Utilizaremos funciones, lambda y colecciones. No estudiaremos todavía `yield`, decoradores, closures avanzados, iteradores en profundidad, `itertools` ni programación funcional purista.

---

# 1. ¿Qué significa “funcional” en Python?

Python es multiparadigma: admite POO, instrucciones imperativas e ideas funcionales. No es un lenguaje funcional puro.

Nos concentraremos en funciones como valores, transformaciones pequeñas y combinables, y control de efectos secundarios innecesarios. Ningún estilo es siempre superior.

---

# 2. Funciones como valores

```python
def saludar():
    return "Hola"

otra_funcion = saludar

print(otra_funcion())
```

`saludar` representa la función; `saludar()` la ejecuta. La asignación no usa paréntesis, por lo que no ejecuta nada.

---

# 3. Funciones en colecciones

```python
def sumar(numero_1, numero_2):
    return numero_1 + numero_2

def multiplicar(numero_1, numero_2):
    return numero_1 * numero_2

operaciones = [sumar, multiplicar]

for operacion in operaciones:
    print(operacion(3, 4))
```

Cada elemento es una función que podemos invocar con argumentos compatibles.

---

# 4. Pasar funciones como argumentos

```python
def aplicar_operacion(numero_1, numero_2, operacion):
    return operacion(numero_1, numero_2)

def restar(numero_1, numero_2):
    return numero_1 - numero_2

print(aplicar_operacion(10, 4, restar))
```

Una función de orden superior recibe funciones, devuelve funciones o hace ambas cosas. Aquí priorizaremos las que reciben otras funciones.

`restar` actúa como **callback**: se entrega para que `aplicar_operacion` la invoque cuando corresponda. No necesitamos GUI ni asincronía para comprender el concepto.

---

# 5. Lambda: repaso y uso adecuado

```python
doble = lambda numero: numero * 2

print(doble(5))
```

Lambda crea una función anónima de una sola expresión. Para lógica con varios pasos, decisiones complejas o ciclos, `def` suele ser más legible:

```python
def calcular_total(precio, cantidad):
    subtotal = precio * cantidad
    return subtotal
```

---

# 6. Ordenar con `sorted()` y `key`

```python
estudiantes = [
    {"nombre": "Ana", "nota": 4.5},
    {"nombre": "Luis", "nota": 3.8},
    {"nombre": "Marta", "nota": 4.2}
]

ordenados = sorted(estudiantes, key=lambda estudiante: estudiante["nota"])
descendentes = sorted(estudiantes, key=lambda estudiante: estudiante["nota"], reverse=True)

print([estudiante["nombre"] for estudiante in ordenados])
print([estudiante["nombre"] for estudiante in descendentes])
```

`key` recibe una función que produce el criterio para cada elemento. `sorted()` devuelve una lista nueva y conserva la original. En cambio, `lista.sort()` modifica la lista y devuelve `None`.

Como alternativa breve, `itemgetter("nota")` pertenece a la biblioteca estándar:

```python
from operator import itemgetter

estudiantes = [{"nombre": "Ana", "nota": 4.5}, {"nombre": "Luis", "nota": 3.8}]
print(sorted(estudiantes, key=itemgetter("nota")))
```

---

# 7. `min()` y `max()` con `key`

```python
estudiantes = [
    {"nombre": "Ana", "nota": 4.5},
    {"nombre": "Luis", "nota": 3.8}
]

mayor = max(estudiantes, key=lambda estudiante: estudiante["nota"])
menor = min(estudiantes, key=lambda estudiante: estudiante["nota"])

print(mayor["nombre"])
print(menor["nombre"])
```

---

# 8. Transformar con `map()`

```python
numeros = [1, 2, 3, 4]
dobles = map(lambda numero: numero * 2, numeros)

print(type(dobles))
print(list(dobles))
```

`map(funcion, iterable)` aplica la función a cada elemento. Devuelve un iterable, no directamente una lista. Lo convertimos para visualizarlo.

Una función con `def` puede ser más clara:

```python
def convertir_celsius_a_fahrenheit(temperatura):
    return temperatura * 9 / 5 + 32

temperaturas = [0, 20, 30]
resultado = list(map(convertir_celsius_a_fahrenheit, temperaturas))

print(resultado)
```

---

# 9. Seleccionar con `filter()`

```python
numeros = [1, 2, 3, 4, 5, 6]
pares = filter(lambda numero: numero % 2 == 0, numeros)

print(list(pares))
```

La función de `filter()` produce un valor evaluable como verdadero o falso.

```text
map    → transforma cada elemento
filter → selecciona algunos elementos
```

Un objeto `map` o `filter` se consume al recorrerlo. No esperes reutilizarlo como una lista; conviértelo si necesitas conservar los resultados.

---

# 10. Comprensiones como alternativa

```python
numeros = [1, 2, 3, 4, 5, 6]

dobles_map = list(map(lambda numero: numero * 2, numeros))
dobles_comprension = [numero * 2 for numero in numeros]

pares_filter = list(filter(lambda numero: numero % 2 == 0, numeros))
pares_comprension = [numero for numero in numeros if numero % 2 == 0]

print(dobles_map == dobles_comprension)
print(pares_filter == pares_comprension)
```

En Python, las comprensiones suelen ser más legibles para transformaciones y filtros simples. `map()` y `filter()` siguen siendo útiles, especialmente con una función ya definida.

---

# 11. Comprensiones con condición

```python
numeros = [1, 2, 3, 4]

pares = [numero for numero in numeros if numero % 2 == 0]
etiquetas = ["par" if numero % 2 == 0 else "impar" for numero in numeros]

print(pares)
print(etiquetas)
```

La condición final filtra elementos. El `if/else` antes de `for` transforma todos los elementos eligiendo uno de dos valores.

---

# 12. Comprensiones de conjunto y diccionario

```python
nombres = [" Ana ", "LUIS", "ana"]
nombres_unicos = {nombre.strip().title() for nombre in nombres}
longitudes = {nombre: len(nombre) for nombre in nombres_unicos}

print(len(nombres_unicos))
print(longitudes)
```

El conjunto elimina duplicados normalizados; el diccionario crea pares clave–valor.

---

# 13. Comprensiones anidadas controladas

Primero con ciclos:

```python
filas = [[1, 2], [3, 4]]
valores = []

for fila in filas:
    for valor in fila:
        valores.append(valor)

print(valores)
```

Equivalente breve:

```python
filas = [[1, 2], [3, 4]]
valores = [valor for fila in filas for valor in fila]

print(valores)
```

Si cuesta leerla, conserva los ciclos. No construiremos comprensiones anidadas crípticas.

---

# 14. `any()` y `all()`

```python
notas = [2.5, 3.0, 4.2]

hay_nota_alta = any(nota >= 4.0 for nota in notas)
todas_validas = all(0.0 <= nota <= 5.0 for nota in notas)

print(hay_nota_alta)
print(todas_validas)
```

`any()` devuelve `True` si al menos un valor es verdadero; `all()`, si todos lo son.

Las expresiones entre paréntesis son **expresiones generadoras**: producen valores de forma perezosa y pueden entregarse a `any()`, `all()` o `sum()`. No estudiaremos aún `next()`, `yield` ni `StopIteration`.

---

# 15. `sum()` con expresiones

```python
estudiantes = [{"nombre": "Ana", "nota": 4.5}, {"nombre": "Luis", "nota": 3.5}]
total = sum(estudiante["nota"] for estudiante in estudiantes)

print(total)
```

---

# 16. Combinar con `zip()`

```python
nombres = ["Ana", "Luis"]
notas = [4.5, 3.8]

for nombre, nota in zip(nombres, notas):
    print(nombre, nota)

datos = dict(zip(nombres, notas))
print(datos)
```

`zip()` combina por posición y se detiene cuando termina el iterable más corto. No rellena faltantes. Al crear un diccionario, las claves deben ser únicas para no reemplazar valores.

---

# 17. Numerar con `enumerate()`

```python
nombres = ["Ana", "Luis", "Marta"]

for posicion, nombre in enumerate(nombres, start=1):
    print(f"{posicion}. {nombre}")
```

Evita administrar un contador manual. `start=1` cambia la numeración mostrada, no los índices reales. `zip()` reemplaza recorridos paralelos por índice cuando solo necesitamos emparejar elementos.

---

# 18. Reducción con `reduce()`

```python
from functools import reduce

numeros = [2, 3, 4]
producto = reduce(lambda acumulado, numero: acumulado * numero, numeros, 1)

print(producto)
```

`functools` es parte de la biblioteca estándar. `reduce()` combina la colección hasta obtener un valor. El `1` es el acumulador inicial.

Para sumar, `sum(numeros)` es más claro. También preferimos `min()` o `max()` cuando expresan directamente el objetivo. Usa `reduce()` solo si no existe una operación integrada más legible.

---

# 19. Efectos secundarios y funciones puras

Imprimir, escribir archivos, modificar una lista recibida o una variable global son efectos secundarios. No siempre son malos; debemos reconocerlos y controlarlos.

```python
def calcular_total(precio, cantidad):
    return precio * cantidad
```

De forma simplificada, esta función es pura: con los mismos argumentos devuelve el mismo resultado y no modifica estado externo. Python no obliga a escribir funciones puras.

Podemos evitar una mutación innecesaria:

```python
def duplicar(numeros):
    return [numero * 2 for numero in numeros]

original = [1, 2, 3]
resultado = duplicar(original)

print(original)
print(resultado)
```

Modificar puede ser correcto si forma parte explícita de la responsabilidad.

---

# 20. Pipeline de transformación

```python
estudiantes = [
    {"nombre": "Marta", "nota": 4.5},
    {"nombre": "Ana", "nota": 2.8},
    {"nombre": "Luis", "nota": 3.8}
]

aprobados = [estudiante for estudiante in estudiantes if estudiante["nota"] >= 3.0]
nombres = [estudiante["nombre"] for estudiante in aprobados]
nombres_ordenados = sorted(nombres)

print(nombres_ordenados)
```

```text
estudiantes → filtrar aprobados → extraer nombres → ordenar → resultado
```

Los pasos nombrados facilitan inspeccionar resultados intermedios. Una línea profundamente anidada puede ser más corta, pero no necesariamente mejor. **Prioriza legibilidad antes que compactación.**

---

# 21. Ejemplo integrador — Procesar estudiantes

```python
estudiantes = [
    {"nombre": "Ana", "nota": 4.5},
    {"nombre": "Luis", "nota": 2.8},
    {"nombre": "Marta", "nota": 4.0}
]

aprobados = list(filter(lambda estudiante: estudiante["nota"] >= 3.0, estudiantes))
nombres = list(map(lambda estudiante: estudiante["nombre"], aprobados))
ordenados = sorted(aprobados, key=lambda estudiante: estudiante["nota"], reverse=True)
mayor = max(estudiantes, key=lambda estudiante: estudiante["nota"])
menor = min(estudiantes, key=lambda estudiante: estudiante["nota"])

print(nombres)
print([estudiante["nombre"] for estudiante in ordenados])
print(mayor["nombre"], menor["nombre"])
print(any(estudiante["nota"] == 5.0 for estudiante in estudiantes))
print(all(0.0 <= estudiante["nota"] <= 5.0 for estudiante in estudiantes))

for posicion, estudiante in enumerate(ordenados, start=1):
    print(posicion, estudiante["nombre"])
```

---

# 22. Funciones como estrategias

```python
def calcular_resultado(notas, estrategia):
    return estrategia(notas)

def promedio(notas):
    return sum(notas) / len(notas)

def nota_maxima(notas):
    return max(notas)

notas = [4.0, 3.5, 4.5]

print(calcular_resultado(notas, promedio))
print(calcular_resultado(notas, nota_maxima))
```

La estrategia cambia sin modificar `calcular_resultado`. No necesitamos introducir formalmente un patrón de diseño.

## 💡 Experimenta

Agrega una estrategia que devuelva la nota mínima y guárdala junto con las otras funciones en una lista.

---

# 23. Errores frecuentes

- Escribir `funcion()` cuando queríamos pasar `funcion`.
- Pasar una función con parámetros incompatibles.
- Crear lambdas complejas en lugar de usar `def`.
- Olvidar que `map()` y `filter()` devuelven iterables consumibles.
- Confundir transformación con selección.
- Construir comprensiones difíciles de leer.
- Creer que `sorted()` modifica la original o que `sort()` devuelve la lista.
- Olvidar `key` al ordenar estructuras complejas.
- Confundir `any()` y `all()`.
- Suponer que `zip()` rellena faltantes.
- Usar `reduce()` cuando `sum()`, `min()` o `max()` son más claros.
- Introducir efectos secundarios en `map()` o `filter()`.
- Modificar una colección mientras se transforma.
- Pensar que el estilo funcional elimina todos los ciclos.
- Buscar una sola línea en lugar de claridad.

---

# 24. Ejercicios

1. Guarda una función en otra variable.
2. Pasa una función como argumento.
3. Recorre una lista de funciones.
4. Escribe una lambda sencilla y su equivalente con `def`.
5. Ordena diccionarios mediante `key`.
6. Repite el orden con `reverse=True`.
7. Encuentra mínimos y máximos con `key`.
8. Transforma temperaturas con `map()`.
9. Filtra notas válidas con `filter()`.
10. Compara `map()` con una comprensión.
11. Compara `filter()` con una comprensión.
12. Normaliza valores únicos con una comprensión de set.
13. Crea un diccionario mediante comprensión.
14. Comprueba una condición con `any()`.
15. Comprueba una condición con `all()`.
16. Empareja códigos y nombres con `zip()`.
17. Numera resultados con `enumerate()`.
18. Usa una expresión generadora dentro de `sum()`.
19. Calcula un producto con `reduce()`.
20. Construye un pipeline con pasos nombrados.
21. Identifica efectos secundarios en tres funciones.
22. Refactoriza una expresión ilegible.

---

# 25. Reto — Analizador académico funcional

Parte de estudiantes con código, nombre, programa y notas. Crea funciones para calcular promedio, filtrar aprobados o promedios superiores a un límite, ordenar, encontrar mayor y menor, obtener nombres y validar notas.

Requisitos:

- Pasa al menos una función como argumento.
- Usa `sorted(..., key=...)`, `any()` o `all()`, y `zip()` o `enumerate()`.
- Incluye comprensiones y compara una con `map()` o `filter()`.
- Verifica si existe un promedio perfecto y si todas las notas son válidas.
- Evita mutación innecesaria y lambdas complejas.
- No uses `yield`, decoradores, generadores definidos como funciones, clases nuevas ni paquetes externos.

No se entrega la solución completa.

---

# 26. Comprobación de aprendizaje

- [ ] Distingo una función de su llamada.
- [ ] Trato funciones como valores, argumentos y callbacks.
- [ ] Creo funciones de orden superior sencillas.
- [ ] Uso lambda solo para expresiones pequeñas.
- [ ] Ordeno y busco extremos mediante `key`.
- [ ] Utilizo `map()`, `filter()` y comprensiones con criterio.
- [ ] Creo comprensiones de lista, set y diccionario.
- [ ] Comprendo superficialmente una expresión generadora.
- [ ] Uso correctamente `any()`, `all()`, `zip()` y `enumerate()`.
- [ ] Utilizo `reduce()` solo cuando aporta claridad.
- [ ] Reconozco efectos secundarios y funciones puras.
- [ ] Evito mutación innecesaria y priorizo legibilidad.

---

# 27. Lo que aprendimos

```text
Datos → funciones → transformación → filtrado → combinación → reducción → resultado
```

Hemos utilizado iterables y valores producidos de forma perezosa sin estudiar aún su mecanismo interno. La Unidad 11 profundizará en iterables, iteradores, `next()`, `StopIteration`, generadores, closures, decoradores y administradores de contexto.

---

# 🧭 Navegación

⬅️ [Volver a la Unidad 9 — Módulos, paquetes y organización de proyectos](../unidad09-modulos-proyectos/)

🏠 [Volver al inicio del curso](../README.md)

➡️ [Continuar a la Unidad 11 — Python avanzado](../unidad11-python-avanzado/)


---

## Continuar el curso

- **Unidad anterior:** [Unidad 9 — Módulos, paquetes y organización de proyectos](../unidad09-modulos-proyectos/README.md)
- **Volver al índice:** [Todas las unidades](../README.md)
- **Siguiente unidad:** [Unidad 11 — Python avanzado](../unidad11-python-avanzado/README.md)
