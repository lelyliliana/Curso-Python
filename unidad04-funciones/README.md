# Unidad 4 — Funciones

Nuestros programas ya pueden tomar decisiones, repetir acciones y organizar varios datos. Sin embargo, cuando crecen, es frecuente encontrar instrucciones repetidas o bloques que realizan demasiadas tareas.

En esta unidad aprenderás a dividir un programa en bloques reutilizables llamados **funciones**.

---

## 🎯 Objetivos de aprendizaje

Al finalizar esta unidad podrás:

- Definir y llamar funciones.
- Diferenciar parámetros y argumentos.
- Devolver valores mediante `return`.
- Distinguir entre mostrar y devolver un resultado.
- Utilizar parámetros predeterminados y argumentos por nombre.
- Comprender el alcance básico de las variables.
- Recibir, devolver y modificar colecciones de forma consciente.
- Dividir un problema entre funciones con responsabilidades claras.
- Escribir docstrings y type hints sencillos.
- Comprender los usos básicos de `*args`, `**kwargs` y lambda.
- Explicar el concepto de recursión y la necesidad de un caso base.

---

## 📋 Antes de comenzar

Necesitas haber completado la Unidad 3. Utilizaremos condicionales, ciclos y colecciones sin explicarlos nuevamente en profundidad.

No utilizaremos clases, archivos, excepciones, módulos propios, pruebas automatizadas ni bibliotecas externas.

> **Recomendación:** ejecuta cada ejemplo completo antes de modificarlo. Presta atención al orden en que se definen y llaman las funciones.

---

# 1. ¿Por qué necesitamos funciones?

Imagina que queremos mostrar el mismo encabezado varias veces:

```python
print("=" * 25)
print("REGISTRO DE ESTUDIANTES")
print("=" * 25)

print("Aquí se registraría un estudiante")

print("=" * 25)
print("REGISTRO DE ESTUDIANTES")
print("=" * 25)
```

La repetición hace que el programa sea más largo. Además, cualquier cambio debe aplicarse en varios lugares.

Una función permite:

- Agrupar instrucciones relacionadas.
- Asignarles un nombre descriptivo.
- Reutilizarlas sin copiar el código.
- Dividir un problema grande en tareas pequeñas.
- Mejorar la lectura y el mantenimiento del programa.

Comenzaremos con una función sencilla, sin recibir datos.

---

# 2. Definir una función

Utilizamos `def` para definir una función:

```python
def saludar():
    print("Hola")
```

Cada parte cumple una función:

- `def` indica que comienza una definición.
- `saludar` es el nombre de la función y utiliza `snake_case`.
- Los paréntesis `()` contendrán información de entrada más adelante.
- Los dos puntos `:` anuncian el comienzo del bloque.
- La instrucción indentada pertenece a la función.

Definir la función solamente enseña a Python qué debe hacer. **Todavía no la ejecuta.**

---

# 3. Llamar una función

Para ejecutar una función escribimos su nombre seguido de paréntesis:

```python
def saludar():
    print("Hola")

saludar()
```

Resultado:

```text
Hola
```

Esta parte define la función:

```python
def saludar():
    print("Hola")
```

Esta parte la llama:

```text
saludar()
```

Podemos llamarla varias veces:

```python
def mostrar_encabezado():
    print("=" * 25)
    print("REGISTRO DE ESTUDIANTES")
    print("=" * 25)

mostrar_encabezado()
print("Primer registro")
mostrar_encabezado()
```

## 💡 Experimenta

Cambia el texto y la cantidad de símbolos dentro de `mostrar_encabezado()`. Observa cómo una sola modificación afecta las dos llamadas.

---

# 4. Orden de definición y llamada

El flujo debe encontrar la definición antes de intentar llamar la función:

```python
def mostrar_mensaje():
    print("La función ya está definida")

mostrar_mensaje()
```

No ejecutes este ejemplo incorrecto:

```text
mostrar_mensaje()

def mostrar_mensaje():
    print("La función todavía no estaba definida al llamarla")
```

Python ejecuta el archivo de arriba hacia abajo. En la primera línea aún no conoce `mostrar_mensaje`.

---

# 5. Parámetros y argumentos

Una función resulta más reutilizable cuando puede recibir información:

```python
def saludar(nombre):
    print(f"Hola, {nombre}")

saludar("Ana")
saludar("Luis")
```

Resultado:

```text
Hola, Ana
Hola, Luis
```

Es importante distinguir dos términos:

- **Parámetro:** variable escrita en la definición. En el ejemplo es `nombre`.
- **Argumento:** valor proporcionado en la llamada. En la primera llamada es `"Ana"`.

El parámetro recibe un argumento diferente en cada llamada.

---

# 6. Varios parámetros

Los parámetros se separan con comas:

```python
def mostrar_suma(numero_1, numero_2):
    suma = numero_1 + numero_2
    print(f"Suma: {suma}")

mostrar_suma(8, 5)
mostrar_suma(12, 3)
```

Resultado:

```text
Suma: 13
Suma: 15
```

Por ahora la función muestra el resultado. A continuación aprenderemos a entregarlo para que otras instrucciones puedan utilizarlo.

---

# 7. Devolver valores con `return`

`return` entrega un valor al lugar donde se llamó la función:

```python
def sumar(numero_1, numero_2):
    return numero_1 + numero_2

resultado = sumar(5, 3)

print(resultado)
```

Resultado:

```text
8
```

El valor devuelto puede:

- Guardarse en una variable.
- Mostrarse con `print()`.
- Utilizarse en otra expresión.
- Enviarse como argumento a otra función.

```python
def sumar(numero_1, numero_2):
    return numero_1 + numero_2

resultado_doble = sumar(5, 3) * 2

print(resultado_doble)
print(sumar(10, 4))
```

Cuando Python ejecuta `return`, la función termina inmediatamente. Las instrucciones posteriores de ese bloque no se ejecutan.

---

# 8. `print()` no es `return`

Mostrar un valor y devolverlo son operaciones diferentes:

```python
def sumar_mostrando(numero_1, numero_2):
    print(numero_1 + numero_2)

def sumar_devolviendo(numero_1, numero_2):
    return numero_1 + numero_2

resultado_mostrado = sumar_mostrando(2, 3)
resultado_devuelto = sumar_devolviendo(2, 3)

print(f"Valor de resultado_mostrado: {resultado_mostrado}")
print(f"Valor de resultado_devuelto: {resultado_devuelto}")
```

Resultado:

```text
5
Valor de resultado_mostrado: None
Valor de resultado_devuelto: 5
```

La primera función imprime `5`, pero no lo entrega. La segunda devuelve `5`, que puede almacenarse y reutilizarse.

> Utiliza `print()` cuando la responsabilidad sea mostrar información. Utiliza `return` cuando otra parte del programa necesite recibir el resultado.

---

# 9. Funciones sin `return` explícito

Si una función llega al final sin ejecutar `return`, Python devuelve `None` implícitamente:

```python
def mostrar_curso():
    print("Curso de Python")

resultado = mostrar_curso()

print(resultado)
```

Resultado:

```text
Curso de Python
None
```

En la Unidad 3 vimos un comportamiento relacionado: métodos como `append()`, `remove()` y `sort()` modifican una colección, pero devuelven `None`.

---

# 10. Diferentes rutas de `return`

Una función puede devolver valores distintos según una condición:

```python
def clasificar_nota(nota):
    if nota >= 3.0:
        return "Aprobado"

    return "No aprobado"

resultado = clasificar_nota(4.2)
print(resultado)
```

Si la condición es verdadera, el primer `return` termina la función. Si es falsa, el flujo continúa hasta el segundo.

```python
def describir_numero(numero):
    if numero > 0:
        return "Positivo"
    elif numero < 0:
        return "Negativo"
    else:
        return "Cero"

print(describir_numero(-4))
```

Aunque aparecen varios `return`, cada llamada ejecuta solamente uno.

---

# 11. Parámetros con valores predeterminados

Un parámetro puede tener un valor que se utiliza cuando no recibe argumento:

```python
def saludar(nombre, mensaje="Hola"):
    print(f"{mensaje}, {nombre}")

saludar("Ana")
saludar("Luis", "Buenos días")
```

Resultado:

```text
Hola, Ana
Buenos días, Luis
```

`nombre` es obligatorio. `mensaje` es opcional porque tiene el valor predeterminado `"Hola"`.

Los parámetros obligatorios deben aparecer antes de los parámetros con valor predeterminado:

```python
def calcular_total(precio, cantidad=1):
    return precio * cantidad

print(calcular_total(5000))
print(calcular_total(5000, 3))
```

---

# 12. Argumentos posicionales

En una llamada posicional, el orden relaciona cada argumento con su parámetro:

```python
def presentar(nombre, edad):
    print(f"{nombre} tiene {edad} años")

presentar("Ana", 20)
```

`"Ana"` corresponde a `nombre` y `20` corresponde a `edad`. Intercambiarlos cambiaría el significado.

---

# 13. Argumentos por nombre

Podemos indicar explícitamente el parámetro de cada argumento:

```python
def presentar(nombre, edad):
    print(f"{nombre} tiene {edad} años")

presentar(edad=20, nombre="Ana")
```

Los argumentos por nombre mejoran la legibilidad y pueden escribirse en un orden diferente.

---

# 14. Mezclar argumentos posicionales y por nombre

Podemos combinar ambas formas si los argumentos posicionales aparecen primero:

```python
def registrar_producto(nombre, precio, cantidad=1):
    total = precio * cantidad
    print(f"{nombre}: {cantidad} unidades, total {total}")

registrar_producto("Cuaderno", precio=5000, cantidad=3)
```

No debemos volver a proporcionar un parámetro que ya recibió un valor posicional. Tampoco debemos colocar un argumento posicional después de uno por nombre.

## 💡 Experimenta

Llama `registrar_producto` utilizando solo argumentos posicionales y después utilizando únicamente argumentos por nombre.

---

# 15. Alcance de variables

El **alcance** indica en qué parte del programa puede utilizarse una variable.

## 15.1 Variable local

Una variable creada dentro de una función es local:

```python
def mostrar_mensaje():
    mensaje_local = "Mensaje local"
    print(mensaje_local)

mostrar_mensaje()
```

`mensaje_local` existe durante la ejecución de la función. Intentar utilizarla fuera produce un error.

## 15.2 Variable global

Una variable creada fuera de las funciones es global y puede consultarse dentro de ellas:

```python
mensaje = "Mensaje global"

def mostrar_mensajes():
    mensaje_local = "Mensaje local"
    print(mensaje)
    print(mensaje_local)

mostrar_mensajes()
print(mensaje)
```

Las variables locales de funciones diferentes pueden utilizar el mismo nombre sin ser la misma variable.

---

# 16. Evitar dependencias globales innecesarias

Esta función depende de una variable externa:

```python
precio = 5000

def calcular_total_global():
    return precio * 3

print(calcular_total_global())
```

Una alternativa más clara recibe la información y devuelve el resultado:

```python
def calcular_total(precio, cantidad):
    return precio * cantidad

total = calcular_total(5000, 3)
print(total)
```

La segunda función puede reutilizarse con distintos precios y cantidades. Sus entradas y su salida son visibles, lo que facilita comprenderla y comprobarla.

---

# 17. La palabra `global`

`global` permite indicar que una asignación dentro de una función debe modificar una variable global:

```python
contador = 0

def aumentar_contador():
    global contador
    contador = contador + 1

aumentar_contador()
print(contador)
```

Resultado:

```text
1
```

Esta característica existe, pero crea una dependencia difícil de seguir cuando se usa con frecuencia. Durante el curso preferiremos parámetros y `return`:

```python
def aumentar_contador(contador_actual):
    return contador_actual + 1

contador = 0
contador = aumentar_contador(contador)

print(contador)
```

---

# 18. Retornar varios valores

Python puede agrupar varios valores devueltos en una tupla:

```python
def calcular(numero_1, numero_2):
    suma = numero_1 + numero_2
    resta = numero_1 - numero_2
    return suma, resta

resultados = calcular(10, 5)

print(resultados)
print(type(resultados))
```

Podemos desempaquetar la tupla, como aprendimos en la Unidad 3:

```python
def calcular(numero_1, numero_2):
    suma = numero_1 + numero_2
    resta = numero_1 - numero_2
    return suma, resta

suma, resta = calcular(10, 5)

print(suma)
print(resta)
```

---

# 19. Funciones que reciben colecciones

Una colección completa puede enviarse como argumento.

## 19.1 Recibir una lista

```python
def calcular_promedio(notas):
    if len(notas) == 0:
        return None

    return sum(notas) / len(notas)

notas_estudiante = [4.0, 3.5, 4.5]
promedio = calcular_promedio(notas_estudiante)

print(promedio)
```

La comprobación evita dividir entre cero cuando la lista está vacía.

## 19.2 Recibir un diccionario

```python
def mostrar_estudiante(estudiante):
    print(f"Nombre: {estudiante['nombre']}")
    print(f"Nota: {estudiante['nota']}")

datos_estudiante = {"nombre": "Ana", "nota": 4.2}
mostrar_estudiante(datos_estudiante)
```

---

# 20. Mutabilidad y funciones

Las listas y los diccionarios son mutables. Una función que recibe una lista puede modificar el mismo objeto que observa el código exterior:

```python
def agregar_estudiante(estudiantes, nombre):
    estudiantes.append(nombre)

nombres = ["Ana", "Luis"]
agregar_estudiante(nombres, "Carlos")

print(nombres)
```

Resultado:

```text
['Ana', 'Luis', 'Carlos']
```

El parámetro recibe una referencia al mismo objeto. `append()` lo modifica.

Si queremos producir una lista nueva sin modificar la original, podemos copiarla:

```python
def crear_lista_con_estudiante(estudiantes, nombre):
    nuevos_estudiantes = estudiantes.copy()
    nuevos_estudiantes.append(nombre)
    return nuevos_estudiantes

nombres = ["Ana", "Luis"]
nuevos_nombres = crear_lista_con_estudiante(nombres, "Carlos")

print(nombres)
print(nuevos_nombres)
```

Resultado:

```text
['Ana', 'Luis']
['Ana', 'Luis', 'Carlos']
```

Ninguna alternativa es siempre correcta. Lo importante es que el nombre y la explicación de la función permitan saber si modifica la colección recibida o devuelve una nueva.

---

# 21. Funciones que llaman otras funciones

Una función puede utilizar el resultado de otra:

```python
def calcular_promedio(notas):
    if len(notas) == 0:
        return None

    return sum(notas) / len(notas)

def mostrar_resultado(notas):
    promedio = calcular_promedio(notas)

    if promedio is None:
        print("No hay notas registradas")
    else:
        print(f"Promedio: {promedio}")

notas_estudiante = [4.0, 3.5, 4.5]
mostrar_resultado(notas_estudiante)
```

`calcular_promedio()` se concentra en calcular y devolver. `mostrar_resultado()` decide qué mensaje presentar.

> `is None` permite comprobar específicamente si un valor es `None`.

---

# 22. Una responsabilidad clara por función

Una función resulta más fácil de comprender cuando realiza una tarea concreta.

Un nombre general como:

```text
procesar_todo()
```

no explica qué sucederá y puede reunir entrada, cálculos, búsquedas y mensajes en un bloque enorme.

Nombres más específicos comunican mejor las responsabilidades:

```text
registrar_estudiante()
calcular_promedio()
buscar_estudiante()
mostrar_estudiante()
```

Esto no significa que cada función deba tener una sola línea. Significa que sus instrucciones deben colaborar en una tarea clara.

---

# 23. Documentar con docstrings

Una **docstring** es un texto colocado al comienzo del cuerpo de una función para explicar su propósito:

```python
def sumar(numero_1, numero_2):
    """Devuelve la suma de dos números."""
    return numero_1 + numero_2

print(sumar(4, 6))
```

Una docstring forma parte de la documentación de la función. Un comentario con `#` explica decisiones o detalles del código:

```python
def calcular_promedio(notas):
    """Devuelve el promedio o None cuando no hay notas."""
    if len(notas) == 0:
        return None  # Evita una división entre cero

    return sum(notas) / len(notas)
```

En esta unidad utilizaremos docstrings breves. Los formatos profesionales de documentación se estudiarán más adelante.

---

# 24. Introducción a type hints

Los **type hints** permiten comunicar qué tipos de datos espera y devuelve una función:

```python
def sumar(numero_1: float, numero_2: float) -> float:
    return numero_1 + numero_2

resultado = sumar(2.5, 3.0)
print(resultado)
```

- `numero_1: float` y `numero_2: float` describen los argumentos esperados.
- `-> float` describe el valor de retorno esperado.

Los type hints no convierten datos automáticamente ni obligan a Python a rechazar otro tipo durante la ejecución. Son ayudas para comunicar la intención y para algunas herramientas de desarrollo.

La Unidad 12 profundizará en el tipado. Por ahora basta con reconocer esta sintaxis básica.

---

# 25. Argumentos posicionales adicionales con `*args`

`*args` permite recibir una cantidad variable de argumentos posicionales. Dentro de la función se agrupan en una tupla:

```python
def sumar_todos(*numeros):
    print(type(numeros))
    return sum(numeros)

print(sumar_todos(2, 3))
print(sumar_todos(1, 2, 3, 4))
```

Resultado:

```text
<class 'tuple'>
5
<class 'tuple'>
10
```

El nombre `args` es una convención; lo importante es el asterisco. Un nombre descriptivo como `*numeros` comunica mejor el propósito.

Utiliza parámetros normales cuando la cantidad de datos sea conocida. `*args` es útil solamente cuando esa cantidad puede variar.

---

# 26. Argumentos por nombre adicionales con `**kwargs`

`**kwargs` recibe una cantidad variable de argumentos por nombre. Dentro de la función se agrupan en un diccionario:

```python
def mostrar_datos(**datos):
    print(type(datos))

    for clave, valor in datos.items():
        print(f"{clave}: {valor}")

mostrar_datos(nombre="Ana", edad=20, programa="Sistemas")
```

`datos` contiene claves como `"nombre"` y sus valores correspondientes.

El nombre `kwargs` es una convención; `**datos` resulta más descriptivo en este ejemplo.

---

# 27. Diferencia entre `*args` y `**kwargs`

| Sintaxis | Recibe | Dentro de la función |
|---|---|---|
| `*args` | Argumentos posicionales adicionales | Tupla |
| `**kwargs` | Argumentos por nombre adicionales | Diccionario |

```python
def mostrar_resumen(titulo, *valores, **datos):
    print(titulo)
    print(valores)
    print(datos)

mostrar_resumen("Estudiante", 4.0, 3.5, nombre="Ana", edad=20)
```

No todas las funciones necesitan estos mecanismos. Los parámetros normales suelen expresar mejor una interfaz conocida.

---

# 28. Funciones lambda

Una función lambda es una función anónima limitada a una expresión:

```python
doble = lambda numero: numero * 2

print(doble(5))
```

Es equivalente, para este caso sencillo, a:

```python
def doble(numero):
    return numero * 2

print(doble(5))
```

Lambda puede ser apropiada para una operación pequeña usada en un contexto breve. Para lógica con decisiones, ciclos o varios pasos, `def` suele ser más legible.

Más adelante, en Python funcional, estudiaremos contextos donde las funciones pequeñas se pasan a otras operaciones. No necesitamos introducirlos todavía.

---

# 29. Introducción a la recursión

Una función es **recursiva** cuando se llama a sí misma. Debe tener un **caso base** que detenga las llamadas.

```python
def mostrar_cuenta_regresiva(numero):
    if numero == 0:
        print("Inicio")
        return

    print(numero)
    mostrar_cuenta_regresiva(numero - 1)

mostrar_cuenta_regresiva(3)
```

Resultado:

```text
3
2
1
Inicio
```

Cuando `numero` vale `0`, el caso base ejecuta `return` y evita otra llamada. Sin un caso base alcanzable, la función continuaría llamándose hasta que Python detuviera el programa con un error.

Para recorridos y repeticiones sencillas, los ciclos suelen ser más fáciles de comprender. Esta introducción busca mostrar la idea; no utilizaremos recursión en el reto.

## 💡 Experimenta

Cambia la llamada a `mostrar_cuenta_regresiva(5)`. No utilices valores negativos, porque el caso base actual está diseñado para llegar a `0` desde un entero positivo.

---

# 30. Refactorizar un programa

En el reto de la Unidad 3, toda la gestión de estudiantes podía estar directamente dentro del ciclo del menú. Ese programa **monolítico** comienza a resultar difícil de leer cuando crece.

Podemos separar sus responsabilidades:

```text
Programa monolítico
        ↓
Funciones
        ↓
Responsabilidades separadas
```

Observa una versión pequeña de esa evolución:

```python
def registrar_estudiante(estudiantes, nombre, nota):
    estudiante = {"nombre": nombre, "nota": nota}
    estudiantes.append(estudiante)

def mostrar_estudiantes(estudiantes):
    if len(estudiantes) == 0:
        print("No hay estudiantes registrados")
        return

    for estudiante in estudiantes:
        print(f"{estudiante['nombre']}: {estudiante['nota']}")

def buscar_estudiante(estudiantes, nombre_buscado):
    for estudiante in estudiantes:
        if estudiante["nombre"] == nombre_buscado:
            return estudiante

    return None

def calcular_promedio(estudiantes):
    if len(estudiantes) == 0:
        return None

    suma_notas = 0.0

    for estudiante in estudiantes:
        suma_notas = suma_notas + estudiante["nota"]

    return suma_notas / len(estudiantes)

estudiantes = []
registrar_estudiante(estudiantes, "Ana", 4.2)
registrar_estudiante(estudiantes, "Luis", 3.8)
mostrar_estudiantes(estudiantes)

estudiante_encontrado = buscar_estudiante(estudiantes, "Ana")
promedio = calcular_promedio(estudiantes)

print(estudiante_encontrado)
print(f"Promedio: {promedio}")
```

Cada nombre explica una tarea. Las funciones reciben los datos que necesitan y devuelven información cuando otra parte debe utilizarla.

---

# 31. Errores frecuentes

## 31.1 Definir una función y olvidar llamarla

La definición no ejecuta el cuerpo. Después de `def saludar(): ...` debes llamar `saludar()` cuando quieras realizar la acción.

## 31.2 Llamar antes de definir

Python debe ejecutar la definición antes de llegar a la llamada. Coloca las definiciones antes del flujo principal.

## 31.3 Olvidar los dos puntos o la indentación

No ejecutes este ejemplo incorrecto:

```text
def saludar()
print("Hola")
```

La definición termina con `:` y el cuerpo lleva cuatro espacios.

## 31.4 Confundir parámetros y argumentos

El parámetro aparece en la definición; el argumento aparece en la llamada. Ambos se relacionan, pero no son el mismo concepto.

## 31.5 Olvidar `return`

Una función que calcula un valor pero no lo devuelve entrega `None`:

```python
def calcular_total(precio, cantidad):
    total = precio * cantidad

resultado = calcular_total(5000, 3)
print(resultado)
```

## 31.6 Confundir `print()` con `return`

Si una función solo imprime, asignar su resultado guarda `None`. Mostrar una operación no hace que su valor quede disponible para otras instrucciones.

## 31.7 Utilizar una variable local fuera

No ejecutes este ejemplo incorrecto:

```text
def calcular_total():
    total = 15000

calcular_total()
print(total)
```

`total` es local. Debe devolverse si el código exterior la necesita.

## 31.8 Cantidad u orden incorrectos de argumentos

Si una función requiere dos argumentos, una llamada con uno o tres produce un error. En llamadas posicionales también debes respetar el significado del orden.

## 31.9 Colocar un parámetro obligatorio después de uno opcional

No ejecutes esta definición incorrecta:

```text
def saludar(mensaje="Hola", nombre):
    print(mensaje, nombre)
```

Los parámetros obligatorios deben escribirse primero: `def saludar(nombre, mensaje="Hola"):`.

## 31.10 Modificar accidentalmente una lista

Antes de usar `append()`, `remove()` o asignaciones por índice dentro de una función, decide si la función debe modificar la lista recibida. Si debe conservarse, crea una copia básica y devuelve la nueva lista.

## 31.11 Utilizar `global` innecesariamente

El uso frecuente de variables globales oculta las entradas y salidas. Prefiere parámetros y `return`.

## 31.12 Olvidar el caso base en recursión

No ejecutes una función recursiva sin un caso base alcanzable. Cada llamada debe acercarse a la condición que termina la recursión.

## 31.13 Asignar el resultado de una función que solo imprime

La variable recibirá `None`. Si necesitas reutilizar el valor, agrega un `return` apropiado en lugar de depender de `print()`.

---

# 32. Ejercicios

No consultes soluciones completas. Ejecuta y comprueba cada función con varias llamadas.

## Ejercicio 1 — Función sin parámetros

Define `mostrar_bienvenida()` para mostrar un encabezado y llámala tres veces.

## Ejercicio 2 — Un parámetro

Define `saludar_estudiante(nombre)` y pruébala con tres nombres.

## Ejercicio 3 — Varios parámetros

Define una función que reciba nombre, edad y programa académico y muestre una presentación.

## Ejercicio 4 — Devolver un resultado

Define `calcular_area_rectangulo(base, altura)` y utiliza su retorno en una f-string.

## Ejercicio 5 — Condicional y `return`

Define una función que reciba una nota y devuelva su clasificación en la escala de `0.0` a `5.0`.

## Ejercicio 6 — Valor predeterminado

Define una función que calcule el precio total y use `cantidad=1` como valor predeterminado.

## Ejercicio 7 — Argumentos por nombre

Llama una función de presentación alterando el orden mediante argumentos por nombre. Después mezcla un argumento posicional con argumentos por nombre válidos.

## Ejercicio 8 — Alcance

Crea una variable global y otra local con nombres diferentes. Muestra desde qué lugares puede consultarse cada una. Después reescribe el programa usando parámetros.

## Ejercicio 9 — Recibir una lista

Define una función que reciba notas y devuelva la nota mayor. Puedes recorrer la lista sin utilizar `max()`.

## Ejercicio 10 — Recibir un diccionario

Define una función que reciba un producto y devuelva `precio * cantidad` usando sus claves.

## Ejercicio 11 — Varios valores

Define una función que reciba dos números y devuelva suma, resta y multiplicación. Desempaqueta la tupla.

## Ejercicio 12 — Composición

Define una función para calcular un promedio y otra que utilice su retorno para mostrar si alcanza `3.0`.

## Ejercicio 13 — Docstring

Agrega una docstring clara a tres funciones anteriores.

## Ejercicio 14 — Type hints

Agrega type hints básicos a una función que reciba dos `float` y devuelva un `float`. Comprueba que no convierten un texto automáticamente.

## Ejercicio 15 — `*args`

Define una función que reciba cualquier cantidad de precios y devuelva la suma.

## Ejercicio 16 — `**kwargs`

Define una función que reciba datos de un producto por nombre y recorra el diccionario resultante.

## Ejercicio 17 — Lambda

Crea una lambda que calcule el cuadrado de un número y compárala con una función equivalente definida con `def`.

## Ejercicio 18 — Mutabilidad

Escribe una función que modifique una lista recibida y otra que devuelva una copia modificada. Comprueba ambas listas después de cada llamada.

---

# 33. Reto de la unidad — Sistema de estudiantes refactorizado

Retoma el reto de gestión de estudiantes de la Unidad 3. El programa continuará usando una lista de diccionarios, pero ahora separarás sus responsabilidades mediante funciones.

El menú debe ofrecer:

```text
1. Registrar estudiante
2. Mostrar estudiantes
3. Buscar estudiante
4. Calcular promedio general
5. Mostrar estudiantes con nota igual o superior a 3.0
6. Salir
```

## Funciones sugeridas

### `registrar_estudiante(estudiantes)`

- Recibe la lista.
- Solicita nombre, edad, programa y nota.
- Valida que la nota esté entre `0.0` y `5.0`.
- Agrega el diccionario a la lista.
- Como modifica la lista recibida, no necesita devolverla.

### `mostrar_estudiantes(estudiantes)`

- Recibe la lista.
- Muestra todos los registros o un mensaje si está vacía.

### `buscar_estudiante(estudiantes, nombre_buscado)`

- Recibe la lista y un nombre.
- Devuelve el diccionario encontrado.
- Devuelve `None` si no existe.
- No debe solicitar el nombre; el flujo del menú se lo proporciona.

### `calcular_promedio_general(estudiantes)`

- Recibe la lista.
- Devuelve el promedio de las notas.
- Devuelve `None` si la lista está vacía.
- No imprime el resultado: su responsabilidad es calcularlo.

### `mostrar_aprobados(estudiantes)`

- Recibe la lista.
- Muestra los estudiantes con nota mayor o igual a `3.0`.
- Informa si ninguno cumple la condición.

## Requisitos generales

- Define todas las funciones antes del ciclo principal.
- Mantén el menú dentro de un `while` y procesa la opción con `match/case` o `if/elif`.
- Evita variables globales: entrega los datos mediante parámetros y retornos.
- Separa entrada y salida de los cálculos cuando resulte razonable.
- Usa nombres descriptivos, docstrings breves y funciones con responsabilidades claras.
- No utilices recursión en este reto.
- No utilices clases, archivos, excepciones ni módulos externos.

Construye una función cada vez y compruébala antes de conectarla al menú.

---

# 34. Comprobación de aprendizaje

Antes de continuar, comprueba que puedes:

- [ ] Definir y llamar funciones.
- [ ] Explicar por qué una definición no ejecuta automáticamente su cuerpo.
- [ ] Diferenciar parámetros y argumentos.
- [ ] Recibir uno o varios argumentos.
- [ ] Devolver y reutilizar valores con `return`.
- [ ] Diferenciar claramente `print()` de `return`.
- [ ] Explicar por qué una función sin `return` explícito devuelve `None`.
- [ ] Utilizar diferentes rutas de retorno.
- [ ] Definir parámetros con valores predeterminados válidos.
- [ ] Utilizar argumentos posicionales y por nombre.
- [ ] Explicar el alcance de variables locales y globales.
- [ ] Evitar dependencias globales innecesarias.
- [ ] Retornar y desempaquetar varios valores.
- [ ] Recibir listas y diccionarios.
- [ ] Predecir si una función modificará una colección recibida.
- [ ] Crear funciones que llaman otras funciones.
- [ ] Dividir responsabilidades de forma clara.
- [ ] Escribir docstrings breves.
- [ ] Reconocer type hints básicos y explicar que no fuerzan tipos.
- [ ] Explicar que `*args` forma una tupla.
- [ ] Explicar que `**kwargs` forma un diccionario.
- [ ] Crear una lambda sencilla y reconocer cuándo `def` es más legible.
- [ ] Explicar recursión, caso base y riesgo de recursión infinita.

---

# 35. Lo que aprendimos

En esta unidad pasamos de repetir bloques a organizar responsabilidades:

```text
Código repetido
      ↓
Función
      ↓
Parámetros
      ↓
Procesamiento
      ↓
return
      ↓
Composición
      ↓
Programa organizado
```

Ahora podemos crear funciones reutilizables, comunicar sus entradas mediante parámetros y entregar resultados mediante `return`. También comprendemos el alcance, la mutabilidad básica y algunas formas flexibles de recibir argumentos.

Nuestro código ya puede organizar mejor la lógica. En la Unidad 5 aprenderemos a trabajar con texto con mayor profundidad y a conservar información fuera de la ejecución mediante archivos.

---

# 🧭 Navegación

⬅️ [Volver a la Unidad 3 — Colecciones](../unidad03-colecciones/)

🏠 [Volver al inicio del curso](../README.md)

➡️ [Continuar a la Unidad 5 — Cadenas y archivos](../unidad05-cadenas-archivos/)
