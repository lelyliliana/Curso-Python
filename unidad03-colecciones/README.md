# Unidad 3 — Colecciones

[Volver al índice del curso](../README.md) · [Ver el curso en Aprende con Leli](https://lelyliliana.github.io/aprende-con-leli/cursos/python/)

Hasta ahora hemos guardado cada dato en una variable independiente. En esta unidad aprenderás a reunir varios datos relacionados para consultarlos, modificarlos y recorrerlos de forma organizada.

Estudiaremos las cuatro colecciones integradas principales de Python: listas, tuplas, conjuntos y diccionarios.

---

## 🎯 Objetivos de aprendizaje

Al finalizar esta unidad podrás:

- Crear y recorrer listas.
- Consultar, agregar, modificar y eliminar elementos.
- Trabajar con índices, `len()`, `enumerate()` y slicing.
- Diferenciar una asignación de una copia independiente.
- Construir listas anidadas y comprensiones sencillas.
- Utilizar tuplas para datos que no deben cambiar.
- Utilizar conjuntos para pertenencia, valores únicos y operaciones entre grupos.
- Crear, consultar, modificar y recorrer diccionarios.
- Combinar listas y diccionarios para representar varios registros.
- Elegir una colección apropiada para un problema sencillo.

---

## 📋 Antes de comenzar

Necesitas haber completado la Unidad 2. Aprovecharemos variables, operadores, condicionales, `match`, ciclos, contadores y acumuladores.

No utilizaremos funciones definidas por el usuario, clases, archivos, excepciones ni bibliotecas externas.

> **Recomendación:** copia los ejemplos en archivos `.py`, ejecútalos y realiza las propuestas de experimentación.

---

# 1. ¿Por qué necesitamos colecciones?

Podemos guardar tres notas en tres variables:

```python
nota_1 = 4.0
nota_2 = 3.5
nota_3 = 4.7

print(nota_1)
print(nota_2)
print(nota_3)
```

Esta solución funciona, pero obliga a crear otra variable y otra instrucción por cada nota. Una **colección** permite agrupar varios valores:

```python
notas = [4.0, 3.5, 4.7]

for nota in notas:
    print(nota)
```

Python ofrece colecciones con características diferentes:

- `list`: secuencia ordenada que puede modificarse.
- `tuple`: secuencia ordenada que no puede modificarse después de crearla.
- `set`: grupo de elementos únicos, sin posiciones por índice.
- `dict`: relación de claves con valores.

Comenzaremos con la colección más flexible para nuestros primeros programas: la lista.

---

# 2. Listas

Una **lista** guarda varios elementos en un orden determinado. Se escribe entre corchetes `[]` y sus elementos se separan con comas.

```python
estudiantes = ["Ana", "Luis", "Carlos"]
notas = [4.0, 3.5, 4.7]

print(estudiantes)
print(notas)
```

Resultado:

```text
['Ana', 'Luis', 'Carlos']
[4.0, 3.5, 4.7]
```

Una lista vacía no contiene elementos:

```python
estudiantes = []

print(estudiantes)
```

Las listas:

- Mantienen el orden de sus elementos.
- Admiten elementos repetidos.
- Son **mutables**: pueden cambiar después de crearse.
- Pueden contener tipos diferentes.

```python
datos = ["Ana", 20, 4.5, True]
print(datos)
```

Aunque esto es válido, normalmente conviene agrupar datos relacionados de forma consistente. Por ejemplo, una lista de nombres o una lista de notas resulta más fácil de procesar.

---

# 3. Índices

Cada elemento de una lista ocupa una posición identificada por un **índice**. Los índices comienzan en `0`:

```text
Elementos: ["Ana", "Luis", "Carlos"]
Índices:      0       1        2
```

```python
estudiantes = ["Ana", "Luis", "Carlos"]

print(estudiantes[0])
print(estudiantes[1])
print(estudiantes[2])
```

Resultado:

```text
Ana
Luis
Carlos
```

## 3.1 Índices negativos

Los índices negativos cuentan desde el final. `-1` representa el último elemento:

```python
estudiantes = ["Ana", "Luis", "Carlos"]

print(estudiantes[-1])
print(estudiantes[-2])
```

Resultado:

```text
Carlos
Luis
```

## 💡 Experimenta

Agrega un cuarto nombre y predice qué valores tendrán los índices `3`, `-1` y `-4`.

---

# 4. Modificar elementos

Podemos asignar un valor nuevo a una posición existente:

```python
estudiantes = ["Ana", "Luis", "Carlos"]
estudiantes[1] = "Laura"

print(estudiantes)
```

Resultado:

```text
['Ana', 'Laura', 'Carlos']
```

La lista original cambió. Por eso decimos que las listas son mutables.

---

# 5. Cantidad de elementos con `len()`

`len()` devuelve la cantidad de elementos:

```python
estudiantes = ["Ana", "Laura", "Carlos"]
cantidad = len(estudiantes)

print(f"Cantidad: {cantidad}")
```

Resultado:

```text
Cantidad: 3
```

Si una lista tiene `3` elementos, sus índices válidos son `0`, `1` y `2`. El último índice positivo es `len(estudiantes) - 1`:

```python
estudiantes = ["Ana", "Laura", "Carlos"]
ultimo_indice = len(estudiantes) - 1

print(estudiantes[ultimo_indice])
```

---

# 6. Agregar elementos

## 6.1 `append()`

`append()` agrega un elemento al final y modifica la lista existente:

```python
estudiantes = ["Ana", "Luis"]
resultado = estudiantes.append("Carlos")

print(estudiantes)
print(resultado)
```

Resultado:

```text
['Ana', 'Luis', 'Carlos']
None
```

`append()` devuelve `None`. Por eso debemos usar `estudiantes.append("Carlos")`, no `estudiantes = estudiantes.append("Carlos")`.

## 6.2 `insert()`

`insert(indice, valor)` agrega un elemento en una posición específica y desplaza los siguientes:

```python
estudiantes = ["Ana", "Carlos"]
estudiantes.insert(1, "Luis")

print(estudiantes)
```

Resultado:

```text
['Ana', 'Luis', 'Carlos']
```

`insert()` también modifica la lista y devuelve `None`. Utiliza `append()` para agregar al final e `insert()` cuando la posición sea importante.

---

# 7. Eliminar elementos

## 7.1 `remove()` elimina por valor

```python
estudiantes = ["Ana", "Luis", "Carlos"]
resultado = estudiantes.remove("Luis")

print(estudiantes)
print(resultado)
```

Resultado:

```text
['Ana', 'Carlos']
None
```

`remove()` elimina la primera aparición del valor, modifica la lista y devuelve `None`. Si el valor no existe, produce un error.

## 7.2 `pop()` elimina por posición

`pop(indice)` modifica la lista y devuelve el elemento eliminado:

```python
estudiantes = ["Ana", "Luis", "Carlos"]
estudiante_eliminado = estudiantes.pop(1)

print(estudiante_eliminado)
print(estudiantes)
```

Resultado:

```text
Luis
['Ana', 'Carlos']
```

Sin indicar un índice, `pop()` elimina y devuelve el último elemento.

## 7.3 `del` elimina mediante un índice

`del` es una instrucción del lenguaje:

```python
estudiantes = ["Ana", "Luis", "Carlos"]
del estudiantes[0]

print(estudiantes)
```

Resultado:

```text
['Luis', 'Carlos']
```

---

# 8. Buscar y contar

## 8.1 Pertenencia con `in` y `not in`

```python
estudiantes = ["Ana", "Luis", "Carlos"]

print("Luis" in estudiantes)
print("Laura" not in estudiantes)
```

Resultado:

```text
True
True
```

Podemos aprovecharlo en una decisión:

```python
estudiantes = ["Ana", "Luis", "Carlos"]
nombre_buscado = input("Nombre que deseas buscar: ")

if nombre_buscado in estudiantes:
    print("El estudiante está registrado")
else:
    print("El estudiante no está registrado")
```

## 8.2 `count()`

`count(valor)` devuelve cuántas veces aparece un valor y no modifica la lista:

```python
notas = [4.0, 3.5, 4.0, 2.8]

print(notas.count(4.0))
```

Resultado:

```text
2
```

## 8.3 `index()`

`index(valor)` devuelve el índice de la primera aparición. Produce un error si el valor no existe, así que primero podemos comprobarlo con `in`:

```python
estudiantes = ["Ana", "Luis", "Carlos"]
nombre_buscado = "Luis"

if nombre_buscado in estudiantes:
    posicion = estudiantes.index(nombre_buscado)
    print(f"Índice: {posicion}")
else:
    print("El nombre no existe")
```

---

# 9. Ordenar listas

## 9.1 `sort()` modifica la lista

```python
notas = [3.5, 4.8, 2.9, 4.0]
resultado = notas.sort()

print(notas)
print(resultado)
```

Resultado:

```text
[2.9, 3.5, 4.0, 4.8]
None
```

`sort()` modifica la lista existente y devuelve `None`.

## 9.2 `sorted()` crea una lista nueva

```python
notas = [3.5, 4.8, 2.9, 4.0]
notas_ordenadas = sorted(notas)

print(notas)
print(notas_ordenadas)
```

Resultado:

```text
[3.5, 4.8, 2.9, 4.0]
[2.9, 3.5, 4.0, 4.8]
```

Ambas opciones admiten `reverse=True` para ordenar de mayor a menor:

```python
notas = [3.5, 4.8, 2.9, 4.0]
notas_ordenadas = sorted(notas, reverse=True)

print(notas_ordenadas)
```

---

# 10. Recorrer listas

Cuando no necesitamos el índice, normalmente resulta más claro recorrer directamente los elementos:

```python
estudiantes = ["Ana", "Luis", "Carlos"]

for estudiante in estudiantes:
    print(estudiante)
```

La variable `estudiante` recibe un elemento diferente en cada iteración.

---

# 11. Recorrer mediante índices

Un índice resulta útil cuando necesitamos consultar o modificar una posición:

```python
estudiantes = ["Ana", "Luis", "Carlos"]

for indice in range(len(estudiantes)):
    print(indice, estudiantes[indice])
```

Resultado:

```text
0 Ana
1 Luis
2 Carlos
```

`range(len(estudiantes))` produce exactamente los índices válidos desde `0` hasta uno antes de la cantidad de elementos.

---

# 12. Posición y elemento con `enumerate()`

`enumerate()` permite obtener una posición y un elemento durante el recorrido:

```python
estudiantes = ["Ana", "Luis", "Carlos"]

for posicion, estudiante in enumerate(estudiantes):
    print(posicion, estudiante)
```

Para mostrar una numeración más natural al usuario podemos comenzar en `1`:

```python
estudiantes = ["Ana", "Luis", "Carlos"]

for numero, estudiante in enumerate(estudiantes, start=1):
    print(f"{numero}. {estudiante}")
```

Resultado:

```text
1. Ana
2. Luis
3. Carlos
```

`start=1` solo cambia la numeración producida por `enumerate()`. El índice real de `"Ana"` continúa siendo `0`.

---

# 13. Slicing de listas

El **slicing** permite obtener una parte de una lista y produce una lista nueva.

```text
lista[inicio:fin]
lista[inicio:fin:paso]
```

El índice inicial se incluye y el final no se incluye:

```python
numeros = [0, 1, 2, 3, 4, 5, 6]

print(numeros[:3])
print(numeros[2:])
print(numeros[::2])
print(numeros[::-1])
```

Resultado:

```text
[0, 1, 2]
[2, 3, 4, 5, 6]
[0, 2, 4, 6]
[6, 5, 4, 3, 2, 1, 0]
```

- `[:3]`: desde el comienzo hasta antes del índice `3`.
- `[2:]`: desde el índice `2` hasta el final.
- `[::2]`: toda la lista avanzando de dos en dos.
- `[::-1]`: toda la lista en orden inverso.

## 💡 Experimenta

Utiliza la misma lista para obtener `[1, 2, 3]` y `[5, 3, 1]`.

---

# 14. Copiar listas y el problema de la asignación

Asignar una lista a otra variable no crea una colección independiente. Ambas variables se refieren al mismo objeto:

```python
original = [1, 2, 3]
copia = original
copia.append(4)

print(original)
print(copia)
```

Resultado:

```text
[1, 2, 3, 4]
[1, 2, 3, 4]
```

Para crear una lista independiente utilizamos `copy()`:

```python
original = [1, 2, 3]
copia = original.copy()
copia.append(4)

print(original)
print(copia)
```

Resultado:

```text
[1, 2, 3]
[1, 2, 3, 4]
```

El slicing `original[:]` también crea una copia básica, pero utilizaremos `copy()` como forma principal por su claridad.

---

# 15. Listas anidadas

Una lista puede contener otras listas:

```python
notas = [
    [4.0, 3.5],
    [4.5, 4.2]
]

print(notas[0])
print(notas[0][1])
```

Resultado:

```text
[4.0, 3.5]
3.5
```

`notas[0]` obtiene la primera lista y el segundo `[1]` obtiene su segundo elemento.

Podemos recorrer todos los valores con ciclos anidados:

```python
notas = [
    [4.0, 3.5],
    [4.5, 4.2]
]

for notas_estudiante in notas:
    for nota in notas_estudiante:
        print(nota)
```

---

# 16. Comprensiones de listas

Primero recordemos cómo construir una lista mediante un ciclo:

```python
cuadrados = []

for numero in range(1, 6):
    cuadrados.append(numero ** 2)

print(cuadrados)
```

Una **comprensión de lista** expresa el mismo patrón de forma breve:

```python
cuadrados = [numero ** 2 for numero in range(1, 6)]

print(cuadrados)
```

Su estructura es:

```text
[valor_que_se_agrega for elemento in recorrido]
```

Puede incluir una condición sencilla:

```python
numeros_pares = [numero for numero in range(1, 11) if numero % 2 == 0]

print(numeros_pares)
```

Resultado:

```text
[2, 4, 6, 8, 10]
```

Utiliza comprensiones cuando la transformación sea corta y clara. Un ciclo tradicional es preferible cuando se necesitan varios pasos.

---

# 17. Tuplas

Una **tupla** es una secuencia ordenada e inmutable. Se escribe normalmente entre paréntesis:

```python
coordenada = (10, 20)

print(coordenada[0])
print(coordenada[-1])
```

Resultado:

```text
10
20
```

Admite índices, recorridos y elementos repetidos, pero no permite cambiar sus elementos después de crearla.

No ejecutes esta modificación, porque produce un error:

```text
coordenada = (10, 20)
coordenada[0] = 15
```

## 17.1 Tupla de un elemento

La coma permite distinguir una tupla de un valor entre paréntesis:

```python
valor = (5)
tupla_un_elemento = (5,)

print(type(valor))
print(type(tupla_un_elemento))
```

Resultado:

```text
<class 'int'>
<class 'tuple'>
```

---

# 18. Desempaquetado de tuplas

El desempaquetado asigna cada elemento a una variable:

```python
coordenada = (10, 20)
x, y = coordenada

print(x)
print(y)
```

Debe existir la misma cantidad de variables que de elementos.

Python también permite intercambiar dos valores mediante una asignación:

```python
primer_valor = 10
segundo_valor = 20

primer_valor, segundo_valor = segundo_valor, primer_valor

print(primer_valor)
print(segundo_valor)
```

Los valores de la derecha se preparan antes de asignarse a las variables de la izquierda.

---

# 19. Conjuntos — `set`

Un **conjunto** almacena elementos únicos. Puede escribirse entre llaves cuando contiene valores:

```python
numeros = {1, 2, 2, 3}

print(len(numeros))
print(2 in numeros)
```

Resultado:

```text
3
True
```

El segundo `2` no crea otro elemento. No mostramos directamente el conjunto como resultado esperado porque su orden de presentación no debe formar parte de la lógica del programa.

Los conjuntos no se consultan mediante índices. Son especialmente útiles para verificar pertenencia y eliminar duplicados:

```python
nombres = ["Ana", "Luis", "Ana", "Carlos"]
nombres_unicos = set(nombres)

print(len(nombres_unicos))
```

Resultado:

```text
3
```

> `{}` crea un diccionario vacío, no un conjunto. Para crear un conjunto vacío utiliza `set()`.

```python
conjunto_vacio = set()
diccionario_vacio = {}

print(type(conjunto_vacio))
print(type(diccionario_vacio))
```

---

# 20. Modificar conjuntos

## 20.1 `add()`

`add()` agrega un elemento, modifica el conjunto y devuelve `None`:

```python
codigos = {101, 102}
resultado = codigos.add(103)

print(103 in codigos)
print(resultado)
```

## 20.2 `remove()` y `discard()`

Ambos eliminan un elemento y devuelven `None`. La diferencia aparece cuando el elemento no existe:

- `remove()` produce un error.
- `discard()` no produce un error.

```python
codigos = {101, 102, 103}

if 102 in codigos:
    codigos.remove(102)

codigos.discard(999)

print(102 in codigos)
print(len(codigos))
```

No llamamos `remove(102)` sin comprobar su existencia porque todavía no hemos estudiado el manejo de excepciones.

---

# 21. Operaciones entre conjuntos

Supongamos que tenemos estudiantes inscritos en dos actividades:

```python
programacion = {"Ana", "Luis", "Marta"}
robotica = {"Luis", "Carlos", "Marta"}

union = programacion | robotica
interseccion = programacion & robotica
diferencia = programacion - robotica

print(len(union))
print("Luis" in interseccion)
print("Ana" in diferencia)
```

Resultado:

```text
4
True
True
```

- Unión `|`: estudiantes que están en al menos una actividad.
- Intersección `&`: estudiantes que están en ambas.
- Diferencia `-`: estudiantes de la primera que no están en la segunda.

También existen los métodos `union()`, `intersection()` y `difference()`. Los operadores anteriores expresan las mismas operaciones de forma compacta.

---

# 22. Diccionarios — `dict`

Un **diccionario** relaciona claves con valores:

```text
clave → valor
```

```python
estudiante = {
    "nombre": "Ana",
    "edad": 20,
    "programa": "Ingeniería de Sistemas"
}

print(estudiante)
```

Las claves `"nombre"`, `"edad"` y `"programa"` son únicas. Cada una permite localizar su valor. Los diccionarios son mutables.

---

# 23. Consultar valores

Podemos acceder mediante corchetes:

```python
estudiante = {"nombre": "Ana", "edad": 20}

print(estudiante["nombre"])
```

Si la clave no existe, esta forma produce un error. `get()` resulta útil cuando la clave podría faltar:

```python
estudiante = {"nombre": "Ana", "edad": 20}

print(estudiante.get("nombre"))
print(estudiante.get("semestre"))
print(estudiante.get("semestre", "Sin registrar"))
```

Resultado:

```text
Ana
None
Sin registrar
```

`get()` no modifica el diccionario. Devuelve `None` o el valor predeterminado indicado cuando la clave no existe.

---

# 24. Agregar y modificar pares

La misma sintaxis sirve para ambas operaciones:

```python
estudiante = {"nombre": "Ana", "edad": 20}

estudiante["semestre"] = 3
estudiante["edad"] = 21

print(estudiante)
```

`"semestre"` se agrega porque no existía. El valor de `"edad"` se reemplaza porque la clave ya existía.

---

# 25. Eliminar pares

`pop(clave)` elimina el par y devuelve su valor:

```python
estudiante = {"nombre": "Ana", "edad": 20, "semestre": 3}
semestre_eliminado = estudiante.pop("semestre")

print(semestre_eliminado)
print(estudiante)
```

`del` elimina el par mediante su clave:

```python
estudiante = {"nombre": "Ana", "edad": 20}
del estudiante["edad"]

print(estudiante)
```

Ambas formas producen un error si la clave indicada no existe. Podemos comprobar primero con `in` cuando exista esa posibilidad.

---

# 26. Recorrer diccionarios

Un recorrido directo obtiene las claves:

```python
estudiante = {"nombre": "Ana", "edad": 20}

for clave in estudiante:
    print(clave, estudiante[clave])
```

Los métodos de consulta permiten elegir qué recorrer:

```python
estudiante = {"nombre": "Ana", "edad": 20}

for clave in estudiante.keys():
    print(clave)

for valor in estudiante.values():
    print(valor)

for clave, valor in estudiante.items():
    print(clave, valor)
```

- `keys()` permite recorrer las claves.
- `values()` permite recorrer los valores.
- `items()` permite desempaquetar cada par en `clave` y `valor`.

---

# 27. Diccionarios con colecciones

Un valor de un diccionario puede ser una colección:

```python
estudiante = {
    "nombre": "Ana",
    "notas": [4.0, 3.5, 4.5]
}

print(estudiante["nombre"])

for nota in estudiante["notas"]:
    print(nota)
```

Esta estructura representa datos relacionados de una misma persona sin utilizar clases.

---

# 28. Lista de diccionarios

Una lista puede almacenar varios registros, cada uno representado por un diccionario:

```python
estudiantes = [
    {"nombre": "Ana", "nota": 4.2},
    {"nombre": "Luis", "nota": 3.8}
]

for estudiante in estudiantes:
    print(f"{estudiante['nombre']}: {estudiante['nota']}")
```

La lista organiza varios estudiantes. Cada diccionario relaciona los campos de un estudiante con sus valores.

---

# 29. ¿Qué colección debo utilizar?

| Colección | Orden de recorrido | ¿Mutable? | Duplicados | Acceso principal | Uso típico |
|---|---|---|---|---|---|
| `list` | Conserva el orden de inserción | Sí | Sí | Índice | Secuencia que puede cambiar |
| `tuple` | Conserva el orden de inserción | No | Sí | Índice | Datos ordenados que deben permanecer fijos |
| `set` | No depender de él | Sí | No | Pertenencia | Valores únicos y operaciones entre grupos |
| `dict` | Conserva el orden de inserción | Sí | Claves únicas; valores pueden repetirse | Clave | Datos relacionados por nombre o identificador |

No existe una colección universalmente mejor. La elección depende de cómo necesitas guardar, consultar y modificar los datos.

---

# 30. Ejemplos integradores

## 30.1 Registrar nombres

```python
estudiantes = []
cantidad = int(input("¿Cuántos estudiantes registrarás? "))

for numero in range(1, cantidad + 1):
    nombre = input(f"Nombre {numero}: ")
    estudiantes.append(nombre)

for numero, nombre in enumerate(estudiantes, start=1):
    print(f"{numero}. {nombre}")
```

## 30.2 Promedio de notas con `sum()`

`sum()` devuelve la suma de los valores numéricos de una colección y no la modifica:

```python
notas = [4.0, 3.5, 4.5]
promedio = sum(notas) / len(notas)

print(f"Promedio: {promedio}")
```

Resultado:

```text
Promedio: 4.0
```

Antes de dividir, debemos asegurarnos de que la lista no esté vacía:

```python
notas = []

if len(notas) > 0:
    promedio = sum(notas) / len(notas)
    print(f"Promedio: {promedio}")
else:
    print("No hay notas registradas")
```

## 30.3 Eliminar duplicados

```python
codigos = [101, 102, 101, 103, 102]
codigos_unicos = set(codigos)

print(f"Cantidad original: {len(codigos)}")
print(f"Cantidad sin duplicados: {len(codigos_unicos)}")
```

No dependemos del orden del conjunto.

## 30.4 Información de un estudiante

```python
estudiante = {
    "nombre": "Ana",
    "edad": 20,
    "programa": "Ingeniería de Sistemas",
    "nota": 4.2
}

for campo, valor in estudiante.items():
    print(f"{campo}: {valor}")
```

## 30.5 Buscar entre varios estudiantes

```python
estudiantes = [
    {"nombre": "Ana", "nota": 4.2},
    {"nombre": "Luis", "nota": 3.8},
    {"nombre": "Marta", "nota": 4.5}
]

nombre_buscado = input("Nombre que deseas buscar: ")
encontrado = False

for estudiante in estudiantes:
    if estudiante["nombre"] == nombre_buscado:
        print(f"Nota: {estudiante['nota']}")
        encontrado = True
        break

if not encontrado:
    print("El estudiante no está registrado")
```

---

# 31. Errores frecuentes

## 31.1 Acceder a un índice inexistente

No ejecutes este ejemplo; la lista solo tiene índices `0`, `1` y `2`:

```text
estudiantes = ["Ana", "Luis", "Carlos"]
print(estudiantes[3])
```

Recuerda que el último índice positivo es `len(estudiantes) - 1`.

## 31.2 Modificar una tupla

Las tuplas son inmutables. `coordenada[0] = 15` produce un error; utiliza una lista si los elementos deben cambiar.

## 31.3 Tratar un conjunto como una secuencia indexada

`codigos[0]` no funciona cuando `codigos` es un `set`. Utiliza `in` para consultar pertenencia o recórrelo sin depender del orden.

## 31.4 Confundir colecciones vacías

```python
diccionario_vacio = {}
conjunto_vacio = set()

print(type(diccionario_vacio))
print(type(conjunto_vacio))
```

`{}` es un diccionario vacío; `set()` es un conjunto vacío.

## 31.5 Consultar directamente una clave inexistente

No ejecutes `estudiante["semestre"]` si la clave podría faltar. Comprueba con `in` o utiliza `estudiante.get("semestre")`.

## 31.6 Modificar una lista mientras se recorre

Eliminar elementos de la misma lista que se está recorriendo puede saltar valores y producir resultados inesperados. En esta etapa, realiza las modificaciones antes o después del recorrido.

## 31.7 Guardar el resultado de `append()` o `remove()`

Esto reemplaza la lista por `None`:

```text
estudiantes = ["Ana"]
estudiantes = estudiantes.append("Luis")
```

`append()` y `remove()` modifican la lista existente y devuelven `None`. Llámalos sin reasignar la variable.

## 31.8 Confundir `sort()` y `sorted()`

`lista.sort()` modifica la lista y devuelve `None`. `sorted(lista)` devuelve una lista nueva y deja la original sin cambios.

## 31.9 Copiar mediante asignación

`copia = original` hace que ambas variables se refieran a la misma lista. Utiliza `original.copy()` cuando necesites una copia básica independiente.

---

# 32. Ejercicios

Resuelve cada ejercicio sin consultar soluciones completas.

## Ejercicio 1 — Primera lista

Crea una lista con cinco nombres. Muestra el primero, el último y la cantidad total.

## Ejercicio 2 — Modificar posiciones

Cambia el segundo nombre de la lista y muestra el resultado.

## Ejercicio 3 — Agregar estudiantes

Agrega un nombre al final con `append()` y otro en el índice `1` con `insert()`.

## Ejercicio 4 — Eliminar elementos

Practica `remove()`, `pop()` y `del` sobre copias independientes de una misma lista. Muestra el valor devuelto por cada método cuando corresponda.

## Ejercicio 5 — Buscar y contar

Solicita un nombre, comprueba si existe y muestra cuántas veces aparece. Usa `index()` solo después de verificar su existencia.

## Ejercicio 6 — Recorridos

Muestra una lista de productos primero mediante recorrido directo, después mediante índices y finalmente con `enumerate(..., start=1)`.

## Ejercicio 7 — Slicing

A partir de `[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]`, obtén los tres primeros, los cuatro últimos, los elementos de índices pares y una copia invertida.

## Ejercicio 8 — Copias

Demuestra la diferencia entre asignar una lista y copiarla con `copy()`.

## Ejercicio 9 — Lista anidada

Crea una lista con las notas de tres estudiantes. Cada estudiante tendrá dos notas. Muestra una nota específica y después recorre todas.

## Ejercicio 10 — Comprensión

Crea mediante comprensiones una lista con los cuadrados del `1` al `10` y otra con los múltiplos de `3` entre `1` y `30`.

## Ejercicio 11 — Tupla

Crea una tupla con una ciudad y sus dos coordenadas. Consulta sus elementos y desempaquétalos en variables.

## Ejercicio 12 — Conjuntos

Crea dos conjuntos de estudiantes inscritos en actividades. Obtén unión, intersección y diferencia sin depender del orden al mostrar resultados.

## Ejercicio 13 — Eliminar duplicados

Parte de una lista con códigos repetidos, conviértela en conjunto y compara las cantidades con `len()`.

## Ejercicio 14 — Diccionario

Crea un diccionario de un producto con nombre, precio y cantidad. Consulta, modifica, agrega y elimina un par.

## Ejercicio 15 — Recorrer un diccionario

Muestra por separado sus claves, valores y pares mediante `keys()`, `values()` e `items()`.

## Ejercicio 16 — Diccionario con notas

Representa un estudiante mediante un diccionario que contenga una lista de notas. Calcula el promedio con `sum()` y `len()`.

## Ejercicio 17 — Lista de diccionarios

Crea tres registros de productos y recórrelos para mostrar nombre y precio. Después busca uno por nombre.

---

# 33. Reto de la unidad — Gestión de estudiantes

Crea un archivo llamado:

```text
gestion_estudiantes.py
```

Construye un programa con una lista llamada `estudiantes`. Cada elemento será un diccionario con:

- Nombre.
- Edad.
- Programa académico.
- Nota entre `0.0` y `5.0`.

El programa debe repetir este menú hasta elegir la opción `6`:

```text
1. Registrar estudiante
2. Mostrar estudiantes
3. Buscar estudiante por nombre
4. Mostrar cantidad de estudiantes
5. Calcular promedio general
6. Salir
```

## Requisitos

- Utiliza `while` para mantener activo el menú.
- Utiliza `match/case` o `if/elif` para procesar la opción.
- En el registro, crea un diccionario y agrégalo con `append()`.
- Valida con `while` que la nota esté entre `0.0` y `5.0`.
- Recorre la lista para mostrar y buscar estudiantes.
- Usa una variable booleana para indicar si la búsqueda encontró el nombre.
- Si la lista está vacía, muestra un mensaje antes de intentar calcular el promedio.
- Para el promedio, recorre los registros y acumula sus notas. También puedes crear una lista de notas y usar `sum()` y `len()`.
- Muestra una respuesta para las opciones no válidas.

No utilices funciones propias, clases, archivos, excepciones ni módulos. Escribe la lógica directamente dentro del ciclo principal.

Desarrolla el reto por etapas: primero el menú, después el registro, luego la visualización, la búsqueda y finalmente el promedio. Ejecuta el programa después de cada etapa.

---

# 34. Comprobación de aprendizaje

Antes de continuar, comprueba que puedes:

- [ ] Crear listas vacías y listas con elementos.
- [ ] Consultar y modificar elementos mediante índices.
- [ ] Utilizar índices positivos y negativos.
- [ ] Agregar y eliminar elementos con métodos apropiados.
- [ ] Explicar qué devuelven `append()`, `remove()`, `pop()`, `sort()` y `sorted()`.
- [ ] Buscar valores con `in`, `count()` e `index()` de forma segura.
- [ ] Recorrer listas directamente, mediante índices y con `enumerate()`.
- [ ] Obtener partes de una lista mediante slicing.
- [ ] Diferenciar una asignación de una copia con `copy()`.
- [ ] Crear listas anidadas y comprensiones sencillas.
- [ ] Crear, consultar y desempaquetar tuplas.
- [ ] Explicar por qué una tupla es inmutable.
- [ ] Crear conjuntos sin depender de su orden ni de índices.
- [ ] Agregar y eliminar elementos de conjuntos.
- [ ] Calcular unión, intersección y diferencia.
- [ ] Crear, consultar, modificar y recorrer diccionarios.
- [ ] Elegir entre acceso por clave y `get()`.
- [ ] Trabajar con diccionarios que contienen listas.
- [ ] Representar varios registros mediante una lista de diccionarios.
- [ ] Elegir una colección adecuada según el problema.

---

# 35. Lo que aprendimos

En esta unidad pasamos de trabajar con valores aislados a procesar grupos de datos:

```text
Dato individual
      ↓
Colección
      ↓
Recorrido
      ↓
Procesamiento de múltiples datos
      ↓
Estructuras combinadas
```

Las listas permiten mantener secuencias mutables; las tuplas representan secuencias que no deben cambiar; los conjuntos ofrecen elementos únicos y operaciones entre grupos; y los diccionarios relacionan claves con valores.

Al combinar listas y diccionarios ya podemos representar varios registros. Sin embargo, a medida que los programas crecen, algunas instrucciones comienzan a repetirse.

En la Unidad 4 aprenderemos a organizar y reutilizar esa lógica mediante funciones.

---

# 🧭 Navegación

⬅️ [Volver a la Unidad 2 — Control de flujo](../unidad02-control-flujo/)

🏠 [Volver al inicio del curso](../README.md)

➡️ [Continuar a la Unidad 4 — Funciones](../unidad04-funciones/)


---

## Continuar el curso

- **Unidad anterior:** [Unidad 2 — Control de flujo](../unidad02-control-flujo/README.md)
- **Volver al índice:** [Todas las unidades](../README.md)
- **Siguiente unidad:** [Unidad 4 — Funciones](../unidad04-funciones/README.md)
