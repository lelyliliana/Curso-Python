# Unidad 2 — Control de flujo

[Volver al índice del curso](../README.md) · [Ver el curso en Aprende con Leli](https://lelyliliana.github.io/aprende-con-leli/cursos/python/)

Hasta ahora nuestros programas se han ejecutado principalmente de arriba hacia abajo: cada instrucción se realiza una vez y luego comienza la siguiente.

En esta unidad aprenderás a controlar **qué instrucciones se ejecutan** y **cuántas veces se ejecutan**. Para lograrlo utilizaremos condicionales y ciclos.

---

## 🎯 Objetivos de aprendizaje

Al finalizar esta unidad podrás:

- Explicar qué es el control de flujo.
- Tomar decisiones con `if`, `elif` y `else`.
- Construir condiciones con operadores de comparación y operadores lógicos.
- Utilizar correctamente la indentación de Python.
- Elegir entre `if` y `match` según el problema.
- Repetir instrucciones mediante `while` y `for`.
- Utilizar las tres formas básicas de `range()`.
- Diferenciar contadores y acumuladores.
- Recorrer los caracteres de un texto.
- Interrumpir o saltar iteraciones con `break` y `continue`.
- Construir ciclos anidados sencillos.
- Combinar entradas, conversiones, decisiones y repeticiones en programas pequeños.

---

## 📋 Antes de comenzar

Para realizar esta unidad necesitas haber completado la Unidad 1. Utilizaremos variables, tipos de datos básicos, `print()`, `input()`, conversiones, operadores y f-strings.

No necesitas conocer listas, funciones propias, clases ni ningún otro concepto posterior.

> **Recomendación:** copia cada ejemplo en un archivo `.py`, ejecútalo y después modifica sus valores. La mejor forma de comprender el flujo de un programa es observar cómo cambia su comportamiento.

---

# 1. ¿Qué es el control de flujo?

El **flujo** de un programa es el orden en el que se ejecutan sus instrucciones.

Observa este ejemplo:

```python
print("Inicio")
print("Preparando el ejercicio")
print("Fin")
```

Resultado:

```text
Inicio
Preparando el ejercicio
Fin
```

Python ejecuta las instrucciones de arriba hacia abajo. Sin embargo, muchos problemas necesitan comportamientos más flexibles.

Por ejemplo, un programa puede necesitar:

- Mostrar un mensaje solamente si una persona es mayor de edad.
- Elegir una respuesta diferente según una calificación.
- Solicitar un dato nuevamente mientras no sea válido.
- Repetir una operación una cantidad determinada de veces.

Las estructuras de control permiten cambiar el recorrido del programa:

```text
Decisiones  →  if, elif, else y match
Repeticiones → while y for
```

Comenzaremos aprendiendo a tomar decisiones.

---

# 2. Condicional `if`

La palabra `if` significa **si**. Permite ejecutar un bloque de instrucciones solamente cuando una condición es `True`.

Su estructura básica es:

```python
if condicion:
    instruccion
```

Observa tres elementos importantes:

1. La condición se escribe después de `if`.
2. La línea termina con dos puntos `:`.
3. La instrucción controlada por `if` tiene una sangría de cuatro espacios.

## 2.1 Una condición booleana

Una condición es una expresión cuyo resultado es `True` o `False`.

```python
edad = 20

if edad >= 18:
    print("La persona es mayor de edad")
```

Resultado:

```text
La persona es mayor de edad
```

La comparación `edad >= 18` produce `True`, por eso se ejecuta el `print()` indentado.

Si cambiamos la edad:

```python
edad = 16

if edad >= 18:
    print("La persona es mayor de edad")

print("Consulta terminada")
```

Resultado:

```text
Consulta terminada
```

El primer mensaje no aparece porque la condición es `False`. La última instrucción no pertenece al `if`, ya que no está indentada.

## 2.2 La indentación define el bloque

La **indentación** es el espacio que aparece al inicio de una línea. En Python no es decorativa: indica cuáles instrucciones pertenecen a una estructura.

```python
nota = 4.0

if nota >= 3.0:
    print("La nota alcanzó el valor requerido")
    print("Puedes continuar")

print("Programa finalizado")
```

Los dos primeros mensajes están dentro del `if`. El último está fuera y siempre se ejecuta.

Durante el curso utilizaremos **cuatro espacios** para cada nivel de indentación. Visual Studio Code puede insertarlos al presionar la tecla Tab.

## 💡 Experimenta

Cambia `nota` por `2.5`. Antes de ejecutar el código, predice cuáles mensajes aparecerán.

---

# 3. `if` y `else`: dos caminos posibles

A veces necesitamos elegir entre dos caminos. `else` significa **de lo contrario** y se ejecuta cuando la condición del `if` es `False`.

```python
edad = int(input("Escribe tu edad: "))

if edad >= 18:
    print("Eres mayor de edad")
else:
    print("Eres menor de edad")
```

Solamente se mostrará uno de los dos mensajes.

La estructura general es:

```python
if condicion:
    instrucciones_si_es_true
else:
    instrucciones_si_es_false
```

## 3.1 Ejemplo con una nota

En este curso utilizaremos calificaciones entre `0.0` y `5.0`.

```python
nota = float(input("Escribe la nota final: "))

if nota >= 3.0:
    print("La nota alcanzó el valor requerido")
else:
    print("La nota no alcanzó el valor requerido")
```

> Por ahora asumimos que el usuario escribe una nota numérica entre `0.0` y `5.0`. Más adelante aprenderemos otras técnicas para manejar entradas incorrectas.

---

# 4. `if`, `elif` y `else`: varias alternativas

Cuando existen más de dos alternativas podemos utilizar `elif`, que permite comprobar otra condición si las anteriores fueron falsas.

```python
nota = float(input("Escribe una nota entre 0.0 y 5.0: "))

if nota >= 4.5:
    print("Desempeño excelente")
elif nota >= 4.0:
    print("Desempeño alto")
elif nota >= 3.0:
    print("Desempeño básico")
else:
    print("Desempeño bajo")
```

Python evalúa las condiciones **de arriba hacia abajo** y ejecuta solamente el primer bloque cuya condición sea `True`. Después ignora las alternativas restantes.

Por eso el orden es importante. Primero comprobamos el límite más alto y descendemos progresivamente.

Si `nota` vale `4.7`:

```text
Desempeño excelente
```

Aunque `4.7` también es mayor que `4.0` y `3.0`, esas condiciones ya no se evalúan como caminos alternativos porque la primera fue verdadera.

## 💡 Experimenta

Ejecuta el programa con `4.7`, `4.2`, `3.5` y `2.8`. Después cambia el orden de las dos primeras condiciones y observa por qué una clasificación puede resultar incorrecta.

---

# 5. Comparaciones dentro de condiciones

Los operadores aprendidos en la Unidad 1 permiten formular diferentes preguntas:

| Operador | Pregunta que permite formular |
|---|---|
| `==` | ¿Los valores son iguales? |
| `!=` | ¿Los valores son diferentes? |
| `>` | ¿El primero es mayor? |
| `<` | ¿El primero es menor? |
| `>=` | ¿El primero es mayor o igual? |
| `<=` | ¿El primero es menor o igual? |

```python
temperatura = 30.0

if temperatura == 30.0:
    print("La temperatura es exactamente 30 grados")

if temperatura != 20.0:
    print("La temperatura es diferente de 20 grados")

if temperatura > 25.0:
    print("La temperatura supera los 25 grados")

if temperatura < 35.0:
    print("La temperatura es menor que 35 grados")

if temperatura >= 30.0:
    print("La temperatura es de 30 grados o más")

if temperatura <= 30.0:
    print("La temperatura es de 30 grados o menos")
```

Recuerda que `=` asigna un valor y `==` compara dos valores:

```python
ciudad = "Cali"

if ciudad == "Cali":
    print("La ciudad registrada es Cali")
```

---

# 6. Condiciones con `and`, `or` y `not`

Los operadores lógicos permiten combinar o negar condiciones.

## 6.1 `and`: todas las condiciones deben cumplirse

```python
nota = 4.2
asistencia = 85

if nota >= 3.0 and asistencia >= 80:
    print("Cumple los dos requisitos")
else:
    print("No cumple todos los requisitos")
```

## 6.2 `or`: al menos una condición debe cumplirse

```python
dia = "sábado"

if dia == "sábado" or dia == "domingo":
    print("Es fin de semana")
else:
    print("Es un día entre semana")
```

## 6.3 `not`: invertir un valor booleano

```python
activo = False

if not activo:
    print("La cuenta no está activa")
```

## 6.4 Validar un rango

Para comprobar que una nota se encuentra entre `0.0` y `5.0`, ambos límites deben cumplirse:

```python
nota = float(input("Escribe una nota: "))

if nota >= 0.0 and nota <= 5.0:
    print("La nota está dentro del rango")
else:
    print("La nota está fuera del rango")
```

---

# 7. Condicionales anidados

Un condicional está **anidado** cuando se encuentra dentro de otro condicional.

Puede ser útil cuando una segunda pregunta solo tiene sentido después de cumplir la primera:

```python
nota = 4.0
asistencia = 75

if nota >= 3.0:
    print("La nota alcanzó el valor requerido")

    if asistencia >= 80:
        print("También cumple la asistencia")
    else:
        print("Debe revisar su asistencia")
else:
    print("La nota no alcanzó el valor requerido")
```

Cada nivel adicional requiere cuatro espacios más.

No conviene crear muchos niveles anidados porque el código se vuelve difícil de seguir. Cuando solamente necesitamos comprobar que dos requisitos se cumplen al mismo tiempo, una condición con `and` suele ser más clara:

```python
nota = 4.0
asistencia = 85

if nota >= 3.0 and asistencia >= 80:
    print("Cumple la nota y la asistencia")
else:
    print("No cumple todos los requisitos")
```

---

# 8. Valores booleanos directamente en condiciones

Una variable booleana ya contiene `True` o `False`, por lo que puede utilizarse directamente:

```python
activo = True

if activo:
    print("La cuenta está activa")
```

También podemos negarla:

```python
matriculado = False

if not matriculado:
    print("El estudiante no está matriculado")
```

Evita comparaciones innecesarias como:

```python
activo = True

if activo == True:
    print("La cuenta está activa")
```

La forma `if activo:` expresa la misma idea de manera más directa.

---

# 9. Elegir alternativas con `match` y `case`

`match` permite comparar un valor con varias alternativas concretas. Puede resultar más legible que una cadena extensa de `elif` cuando todas las condiciones comparan la misma variable con valores específicos.

> **Importante:** `match` y `case` están disponibles desde Python 3.10. Si utilizas una versión anterior, este código no funcionará.

## 9.1 Sintaxis básica

```python
opcion = input("Elige una opción (1, 2 o 3): ")

match opcion:
    case "1":
        print("Consultar estudiante")
    case "2":
        print("Registrar nota")
    case "3":
        print("Salir")
    case _:
        print("Opción no válida")
```

`match opcion` indica el valor que queremos comparar. Cada `case` representa una alternativa. `case _` funciona como alternativa predeterminada cuando ninguna opción anterior coincide.

El mismo problema podría escribirse con `elif`:

```python
opcion = input("Elige una opción (1, 2 o 3): ")

if opcion == "1":
    print("Consultar estudiante")
elif opcion == "2":
    print("Registrar nota")
elif opcion == "3":
    print("Salir")
else:
    print("Opción no válida")
```

`match` no sustituye siempre a `if`. Para rangos como `nota >= 3.0`, condiciones combinadas o preguntas diferentes, `if` suele ser la opción apropiada.

## 💡 Experimenta

Agrega una opción `"4"` al menú para mostrar el mensaje `"Ver promedio"`. Comprueba también qué sucede al escribir `8`.

---

# 10. Introducción a los ciclos

Supongamos que queremos mostrar cinco números. Podríamos repetir manualmente la instrucción:

```python
print(1)
print(2)
print(3)
print(4)
print(5)
```

Esta solución es repetitiva y resulta difícil de mantener si después necesitamos mostrar cien números.

Un **ciclo** permite ejecutar un bloque varias veces. Python dispone de dos ciclos principales:

- `while`: repite mientras una condición sea `True`.
- `for`: recorre una secuencia de valores.

---

# 11. Ciclo `while`

`while` significa **mientras**. Su bloque se repite mientras la condición sea verdadera.

```python
numero = 1

while numero <= 5:
    print(numero)
    numero = numero + 1
```

Resultado:

```text
1
2
3
4
5
```

Este ciclo tiene tres partes fundamentales:

1. **Valor inicial:** `numero = 1`.
2. **Condición:** `numero <= 5`.
3. **Actualización:** `numero = numero + 1`.

En cada repetición, llamada **iteración**, el valor aumenta. Cuando llega a `6`, la condición se vuelve `False` y el ciclo termina.

## 11.1 Validar una entrada

`while` es útil cuando no sabemos cuántas veces será necesario repetir una pregunta:

```python
nota = float(input("Escribe una nota entre 0.0 y 5.0: "))

while nota < 0.0 or nota > 5.0:
    print("La nota está fuera del rango")
    nota = float(input("Escribe nuevamente la nota: "))

print(f"Nota registrada: {nota}")
```

La variable `nota` se actualiza dentro del ciclo. El programa sale cuando el valor se encuentra dentro del rango.

> Este ejemplo valida el rango, pero supone que el usuario escribe un número. El manejo de entradas no numéricas se estudiará en una unidad posterior.

## 11.2 Riesgo de ciclo infinito

Un ciclo infinito ocurre cuando su condición nunca llega a ser `False`.

No ejecutes este ejemplo:

```text
numero = 1

while numero <= 5:
    print(numero)
```

Como `numero` nunca cambia, siempre vale `1`. El ciclo no puede terminar.

Si ejecutas accidentalmente un ciclo infinito desde la terminal, normalmente puedes detenerlo con `Ctrl + C`.

## 💡 Experimenta

En el primer ejemplo de `while`, cambia el valor inicial a `3` y el aumento a `numero = numero + 2`. Predice la salida antes de ejecutarlo.

---

# 12. Contadores

Un **contador** es una variable que registra cuántas veces ocurre algo. Normalmente comienza en `0` y aumenta en una cantidad fija.

```python
contador = 0
numero = 1

while numero <= 5:
    if numero > 2:
        contador = contador + 1

    numero = numero + 1

print(f"Cantidad de números mayores que 2: {contador}")
```

Resultado:

```text
Cantidad de números mayores que 2: 3
```

El contador aumenta una unidad cuando encuentra `3`, `4` y `5`.

---

# 13. Acumuladores

Un **acumulador** guarda un resultado que crece al agregar valores. A diferencia de un contador, no necesariamente aumenta de uno en uno.

```python
acumulador = 0
numero = 1

while numero <= 5:
    acumulador = acumulador + numero
    numero = numero + 1

print(f"Suma total: {acumulador}")
```

Resultado:

```text
Suma total: 15
```

La diferencia principal es:

```text
Contador   → registra cuántas veces ocurre algo.
Acumulador → reúne o suma valores.
```

## 13.1 Sumar valores ingresados

```python
cantidad_notas = 3
contador = 1
suma_notas = 0.0

while contador <= cantidad_notas:
    nota = float(input(f"Escribe la nota {contador}: "))
    suma_notas = suma_notas + nota
    contador = contador + 1

promedio = suma_notas / cantidad_notas

print(f"Promedio: {promedio}")
```

Aquí `contador` controla cuántas notas se solicitan y `suma_notas` acumula sus valores.

---

# 14. Ciclo `for`

El ciclo `for` permite recorrer, uno por uno, los valores de una secuencia.

En esta unidad lo utilizaremos con `range()` y con textos. Las colecciones como listas y diccionarios se estudiarán en la siguiente unidad.

```python
for numero in range(5):
    print(numero)
```

Resultado:

```text
0
1
2
3
4
```

En cada iteración, `numero` recibe el siguiente valor producido por `range(5)`.

Cuando conocemos de antemano cuántas repeticiones necesitamos, `for` suele ser más directo que `while`.

---

# 15. Crear secuencias numéricas con `range()`

`range()` produce una secuencia de números enteros que `for` puede recorrer. El límite final **no se incluye**.

## 15.1 `range(fin)`

Comienza en `0` y se detiene antes de `fin`:

```python
for numero in range(5):
    print(numero)
```

Produce los números de `0` a `4`.

## 15.2 `range(inicio, fin)`

Permite elegir el valor inicial:

```python
for numero in range(1, 6):
    print(numero)
```

Resultado:

```text
1
2
3
4
5
```

El límite `6` no aparece.

## 15.3 `range(inicio, fin, paso)`

El tercer valor indica cuánto cambia el número en cada iteración:

```python
for numero in range(2, 11, 2):
    print(numero)
```

Resultado:

```text
2
4
6
8
10
```

El paso también puede ser negativo:

```python
for numero in range(5, 0, -1):
    print(numero)

print("Inicio")
```

Resultado:

```text
5
4
3
2
1
Inicio
```

## 15.4 Tabla de multiplicar

```python
numero = int(input("¿Qué tabla deseas consultar? "))

for multiplicador in range(1, 11):
    resultado = numero * multiplicador
    print(f"{numero} × {multiplicador} = {resultado}")
```

## 💡 Experimenta

Modifica el rango para mostrar la tabla desde `0` hasta `12`. Recuerda ajustar el límite final para que `12` sí se incluya.

---

# 16. Recorrer texto con `for`

Un dato `str` es un texto formado por caracteres. `for` puede recorrerlos uno por uno:

```python
palabra = "Python"

for caracter in palabra:
    print(caracter)
```

Resultado:

```text
P
y
t
h
o
n
```

También podemos contar caracteres sin utilizar colecciones:

```python
palabra = input("Escribe una palabra: ")
cantidad_caracteres = 0

for caracter in palabra:
    cantidad_caracteres = cantidad_caracteres + 1

print(f"Cantidad de caracteres: {cantidad_caracteres}")
```

La variable `caracter` recibe cada carácter, aunque no sea necesario mostrarlo.

---

# 17. Interrumpir un ciclo con `break`

`break` termina inmediatamente el ciclo que lo contiene. Debe utilizarse cuando existe una razón clara para dejar de repetir.

```python
numero = 1

while numero <= 10:
    print(numero)

    if numero == 5:
        break

    numero = numero + 1

print("Ciclo terminado")
```

Resultado:

```text
1
2
3
4
5
Ciclo terminado
```

Aunque la condición permitía llegar hasta `10`, `break` termina el ciclo al encontrar `5`.

## 17.1 Detener una búsqueda en un texto

```python
palabra = "programacion"

for caracter in palabra:
    if caracter == "m":
        print("Se encontró la letra m")
        break

    print(f"Revisando: {caracter}")
```

La búsqueda deja de continuar cuando encuentra el carácter esperado.

---

# 18. Saltar una iteración con `continue`

`continue` no termina el ciclo. Omite el resto de la iteración actual y continúa con la siguiente.

```python
for numero in range(1, 6):
    if numero == 3:
        continue

    print(numero)
```

Resultado:

```text
1
2
4
5
```

La diferencia es:

```text
break    → termina todo el ciclo.
continue → salta solamente la iteración actual.
```

## 18.1 Cuidado con `continue` dentro de `while`

En un `while`, la variable de control debe actualizarse antes de llegar a `continue`. Este ejemplo termina correctamente:

```python
numero = 0

while numero < 5:
    numero = numero + 1

    if numero == 3:
        continue

    print(numero)
```

Si la actualización estuviera después de `continue`, el ciclo podría quedar detenido para siempre en el mismo valor.

---

# 19. Ciclos anidados

Un ciclo anidado se encuentra dentro de otro. Por cada iteración del ciclo exterior, el ciclo interior realiza todas sus iteraciones.

```python
for fila in range(1, 3):
    for columna in range(1, 4):
        print(f"Fila {fila}, columna {columna}")
```

Resultado:

```text
Fila 1, columna 1
Fila 1, columna 2
Fila 1, columna 3
Fila 2, columna 1
Fila 2, columna 2
Fila 2, columna 3
```

Los ciclos anidados son útiles para trabajar con combinaciones o estructuras por filas y columnas. Conviene mantenerlos sencillos porque cada nivel adicional hace más difícil seguir el flujo.

---

# 20. Ejemplos integradores

## 20.1 Contar notas que alcanzan el valor requerido

Este programa solicita cuatro notas, comprueba su rango, acumula sus valores y cuenta cuántas son mayores o iguales a `3.0`:

```python
cantidad_notas = 4
contador_notas = 1
notas_suficientes = 0
suma_notas = 0.0

while contador_notas <= cantidad_notas:
    nota = float(input(f"Escribe la nota {contador_notas}: "))

    while nota < 0.0 or nota > 5.0:
        print("La nota debe estar entre 0.0 y 5.0")
        nota = float(input("Escribe nuevamente la nota: "))

    suma_notas = suma_notas + nota

    if nota >= 3.0:
        notas_suficientes = notas_suficientes + 1

    contador_notas = contador_notas + 1

promedio = suma_notas / cantidad_notas

print(f"Promedio: {promedio}")
print(f"Notas iguales o superiores a 3.0: {notas_suficientes}")
```

## 20.2 Menú sencillo con repetición

```python
opcion = ""

while opcion != "3":
    print()
    print("1. Mostrar saludo")
    print("2. Mostrar mensaje de estudio")
    print("3. Salir")

    opcion = input("Elige una opción: ")

    match opcion:
        case "1":
            print("¡Hola!")
        case "2":
            print("La práctica constante fortalece tu aprendizaje")
        case "3":
            print("Programa finalizado")
        case _:
            print("Opción no válida")
```

El ciclo termina cuando `opcion` recibe el texto `"3"`. No se necesita una lista ni una función propia.

---

# 21. Errores frecuentes

## 21.1 Olvidar los dos puntos

Esto es incorrecto:

```text
if edad >= 18
    print("Mayor de edad")
```

La línea del `if`, `elif`, `else`, `match`, `case`, `while` o `for` debe terminar con `:` cuando corresponda.

## 21.2 Errores de indentación

Esto es incorrecto:

```text
if nota >= 3.0:
print("Nota suficiente")
```

La instrucción que pertenece al bloque debe estar indentada:

```python
if nota >= 3.0:
    print("Nota suficiente")
```

## 21.3 Utilizar `=` en lugar de `==`

Esto es incorrecto:

```text
if opcion = "1":
    print("Opción uno")
```

Para comparar utilizamos `==`:

```python
if opcion == "1":
    print("Opción uno")
```

## 21.4 Crear una condición imposible

Una nota no puede ser menor que `0.0` y mayor que `5.0` al mismo tiempo:

```python
nota = 6.0

if nota < 0.0 and nota > 5.0:
    print("Nota fuera del rango")
```

Para detectar cualquiera de los dos extremos debemos utilizar `or`:

```python
nota = 6.0

if nota < 0.0 or nota > 5.0:
    print("Nota fuera del rango")
```

## 21.5 Construir incorrectamente una condición con `or`

Esto no compara `dia` dos veces:

```text
if dia == "sábado" or "domingo":
    print("Fin de semana")
```

La comparación completa debe aparecer a ambos lados de `or`:

```python
if dia == "sábado" or dia == "domingo":
    print("Fin de semana")
```

## 21.6 Crear un `while` infinito

No ejecutes este código:

```text
contador = 1

while contador <= 5:
    print(contador)
```

Falta actualizar `contador`. Revisa siempre qué hará que la condición llegue a ser `False`.

## 21.7 Confundir el límite final de `range()`

`range(1, 5)` produce `1`, `2`, `3` y `4`. El `5` no se incluye.

Para recorrer de `1` a `5` utiliza:

```python
for numero in range(1, 6):
    print(numero)
```

## 21.8 Utilizar `break` fuera de un ciclo

`break` solamente puede aparecer dentro de `while` o `for`. Fuera de un ciclo produce un error.

Además, no debe utilizarse para ocultar una condición de ciclo mal diseñada. Antes de agregarlo, identifica con claridad por qué el ciclo debe terminar en ese punto.

## 21.9 Utilizar `continue` sin actualizar el control de un `while`

Si `continue` evita que se ejecute la actualización, la condición puede permanecer verdadera para siempre. Actualiza primero la variable de control o reorganiza el ciclo.

---

# 22. Ejercicios

Resuelve los ejercicios en archivos separados. No necesitas utilizar conceptos diferentes a los estudiados hasta esta sección.

## Ejercicio 1 — Mayoría de edad

Solicita la edad y muestra si la persona es mayor o menor de edad.

## Ejercicio 2 — Comparar dos números

Solicita dos números. Indica si el primero es mayor, el segundo es mayor o ambos son iguales.

## Ejercicio 3 — Clasificar una nota

Solicita una nota entre `0.0` y `5.0` y clasifícala como desempeño excelente, alto, básico o bajo. Antes de clasificarla, indica si está fuera del rango permitido.

## Ejercicio 4 — Múltiples requisitos

Solicita una nota y un porcentaje de asistencia. Indica si ambos alcanzan los valores `3.0` y `80`, respectivamente. Utiliza `and`.

## Ejercicio 5 — Menú con `match`

Muestra un menú con opciones para consultar una nota, registrar un nombre y salir. Solicita una opción y muestra un mensaje relacionado. Incluye `case _`.

## Ejercicio 6 — Contar con `while`

Muestra los números del `1` al `10` mediante `while`. Después modifícalo para mostrar solamente los números pares.

## Ejercicio 7 — Validar una temperatura

Solicita una temperatura entre `-20.0` y `50.0`. Mientras esté fuera del rango, vuelve a solicitarla.

## Ejercicio 8 — Acumular compras

Solicita cuántos productos se registrarán. Después solicita el precio de cada uno y muestra el total acumulado.

## Ejercicio 9 — Practicar `range()`

Utiliza `for` y `range()` para mostrar:

- Los números de `0` a `9`.
- Los números de `5` a `15`.
- Los números pares de `2` a `20`.
- Una cuenta regresiva de `10` a `1`.

## Ejercicio 10 — Tabla de multiplicar

Solicita un número y muestra su tabla de multiplicar del `1` al `10`.

## Ejercicio 11 — Contar caracteres

Solicita una palabra, recorre sus caracteres y cuenta cuántas veces aparece la letra `a`.

## Ejercicio 12 — `break` y `continue`

Realiza dos programas:

- Recorre los números del `1` al `20` y detén el ciclo cuando llegues a `12`.
- Recorre los números del `1` al `10` y omite el número `5`.

Antes de programar, decide cuál requiere `break` y cuál requiere `continue`.

## Ejercicio 13 — Ciclo anidado

Muestra las combinaciones de fila y columna de una cuadrícula de `3` filas y `3` columnas.

---

# 23. Reto de la unidad — Registro y análisis de notas

Crea un archivo llamado:

```text
analisis_notas.py
```

El programa administrará un registro pequeño de notas sin utilizar listas.

## Requisitos

1. Solicita el nombre del estudiante.
2. Solicita cuántas notas se registrarán. La cantidad debe ser mayor que `0`; utiliza `while` para volver a solicitarla mientras no sea válida.
3. Solicita cada nota mediante un ciclo.
4. Cada nota debe estar entre `0.0` y `5.0`. Si está fuera del rango, vuelve a solicitarla antes de continuar.
5. Acumula la suma de todas las notas.
6. Cuenta cuántas notas son mayores o iguales a `3.0` y cuántas son menores.
7. Calcula el promedio.
8. Clasifica el promedio mediante `if`, `elif` y `else`:

```text
4.5 a 5.0 → Excelente
4.0 a menos de 4.5 → Alto
3.0 a menos de 4.0 → Básico
0.0 a menos de 3.0 → Bajo
```

9. Muestra un resumen con el nombre, la cantidad de notas, el promedio, la clasificación y ambos contadores.

Una salida posible es:

```text
Nombre del estudiante: Laura
¿Cuántas notas deseas registrar? 3
Nota 1: 4.5
Nota 2: 3.8
Nota 3: 2.7

----- RESUMEN -----
Estudiante: Laura
Cantidad de notas: 3
Promedio: 3.6666666666666665
Clasificación: Básico
Notas iguales o superiores a 3.0: 2
Notas inferiores a 3.0: 1
```

> El número de decimales del promedio puede ser extenso. Más adelante aprenderás otras herramientas para controlar su presentación.

El reto puede resolverse únicamente con variables, entrada y salida, conversiones, operadores, condicionales, ciclos, contadores y acumuladores.

---

# 24. Comprobación de aprendizaje

Antes de continuar, comprueba que puedes:

- [ ] Explicar cómo cambia el flujo de un programa mediante decisiones y repeticiones.
- [ ] Escribir un condicional con `if` y una condición booleana.
- [ ] Utilizar correctamente `if`, `elif` y `else`.
- [ ] Explicar por qué el orden de las condiciones puede cambiar el resultado.
- [ ] Indentar correctamente los bloques de código.
- [ ] Combinar condiciones con `and`, `or` y `not`.
- [ ] Utilizar una variable booleana directamente en una condición.
- [ ] Reconocer cuándo un condicional anidado es útil y cuándo `and` resulta más claro.
- [ ] Crear un menú sencillo con `match` y `case _` en Python 3.10 o superior.
- [ ] Elegir entre `if` y `match` según el tipo de comparación.
- [ ] Construir un `while` que termine correctamente.
- [ ] Diferenciar un contador de un acumulador.
- [ ] Utilizar `for` con `range()` y con un texto.
- [ ] Explicar por qué el límite final de `range()` no se incluye.
- [ ] Utilizar `break` y `continue` con una finalidad clara.
- [ ] Construir un ciclo anidado sencillo.
- [ ] Combinar conceptos de las unidades 1 y 2 en un programa completo.

---

# 25. Lo que aprendimos

En esta unidad nuestros programas dejaron de seguir un único camino.

Ahora podemos representar su funcionamiento así:

```text
Entrada
   ↓
Decisión con if o match
   ↓
Repetición con while o for
   ↓
Contadores y acumuladores
   ↓
Resultado
```

Aprendimos que:

- `if`, `elif` y `else` eligen qué bloque ejecutar.
- `match` organiza alternativas basadas en valores concretos.
- `while` repite mientras una condición sea verdadera.
- `for` recorre los valores de `range()` o los caracteres de un texto.
- Los contadores registran cantidades y los acumuladores reúnen valores.
- `break` termina un ciclo y `continue` salta una iteración.
- La indentación forma parte de la sintaxis de Python.

En la siguiente unidad aprenderemos a guardar y organizar varios valores mediante colecciones.

---

# 🧭 Navegación

⬅️ [Volver a la Unidad 1 — Fundamentos de Python](../unidad01-fundamentos/)

🏠 [Volver al inicio del curso](../README.md)

➡️ [Continuar a la Unidad 3 — Colecciones](../unidad03-colecciones/)


---

## Continuar el curso

- **Unidad anterior:** [Unidad 1 — Fundamentos de Python](../unidad01-fundamentos/README.md)
- **Volver al índice:** [Todas las unidades](../README.md)
- **Siguiente unidad:** [Unidad 3 — Colecciones](../unidad03-colecciones/README.md)
