# Unidad 1 — Fundamentos de Python

[Volver al índice del curso](../README.md) · [Ver el curso en Aprende con Leli](https://lelyliliana.github.io/aprende-con-leli/cursos/python/)

En esta unidad comenzaremos a estudiar formalmente el lenguaje Python.

Aprenderás a escribir instrucciones básicas, utilizar variables, trabajar con diferentes tipos de datos, recibir información del usuario y realizar operaciones.

---

## 🎯 Objetivos de aprendizaje

Al finalizar esta unidad podrás:

- Reconocer la estructura básica de un programa en Python.
- Escribir comentarios en el código.
- Crear y utilizar variables.
- Identificar los principales tipos de datos.
- Mostrar información con `print()`.
- Solicitar datos con `input()`.
- Convertir datos entre diferentes tipos.
- Explicar el comportamiento de `bool()` al convertir distintos valores.
- Utilizar operadores aritméticos.
- Utilizar operadores de comparación.
- Utilizar operadores lógicos.
- Aplicar buenas prácticas básicas al nombrar variables.

---

# 1. Sintaxis básica

La **sintaxis** corresponde a las reglas que debemos seguir para escribir instrucciones válidas en un lenguaje de programación.

Python utiliza una sintaxis sencilla y legible.

Por ejemplo:

```python
print("Hola, Python")
```

Esta instrucción muestra un mensaje en pantalla.

Python distingue entre mayúsculas y minúsculas.

Por ejemplo:

```python
print("Hola")
```

es correcto.

Pero:

```python
Print("Hola")
```

generará un error porque `Print` y `print` son identificadores diferentes.

También es importante escribir correctamente símbolos como paréntesis y comillas. Por ejemplo, esta instrucción está completa:

```python
print("Hola")
```

En cambio, si falta la comilla final, Python no podrá interpretar la instrucción:

```text
print("Hola)
```

Python mostrará un mensaje de error. Estos mensajes pueden parecer difíciles al principio, pero ayudan a encontrar qué parte del código debemos revisar.

---

## 1.1 Una instrucción por línea

Normalmente escribimos una instrucción por línea:

```python
print("Primera línea")
print("Segunda línea")
print("Tercera línea")
```

Resultado:

```text
Primera línea
Segunda línea
Tercera línea
```

---

# 2. Comentarios

Los comentarios permiten agregar explicaciones dentro del código.

Python ignora los comentarios durante la ejecución.

Para escribir un comentario utilizamos:

```python
#
```

Por ejemplo:

```python
# Este programa muestra un mensaje

print("Hola")
```

También podemos escribir comentarios al final de una instrucción:

```python
edad = 20  # Edad del estudiante
```

Los comentarios deben utilizarse para explicar información útil.

Un comentario también puede servir para dejar temporalmente una indicación durante una práctica:

```python
# Cambia el nombre y ejecuta nuevamente el programa
nombre_estudiante = "Laura"

print(nombre_estudiante)
```

---

# 3. Variables

Una **variable** permite almacenar información para utilizarla posteriormente.

Por ejemplo:

```python
nombre = "Laura"
```

Aquí:

```text
nombre
```

es el nombre de la variable.

Y:

```text
"Laura"
```

es el valor almacenado.

Podemos mostrar su contenido:

```python
nombre = "Laura"

print(nombre)
```

Resultado:

```text
Laura
```

---

## 3.1 Cambiar el valor de una variable

Una variable puede recibir un nuevo valor:

```python
edad = 20

print(edad)

edad = 21

print(edad)
```

Resultado:

```text
20
21
```

El valor anterior es reemplazado.

---

## 3.2 Varias variables

Podemos utilizar muchas variables en un mismo programa:

```python
nombre = "Carlos"
edad = 22
ciudad = "Montería"

print(nombre)
print(edad)
print(ciudad)
```

---

# 4. Buenas prácticas para nombrar variables

Los nombres de variables deben ser claros.

Ejemplo recomendable:

```python
nombre_estudiante = "Ana"
edad_estudiante = 19
```

Ejemplo poco recomendable:

```python
x = "Ana"
y = 19
```

Aunque ambos funcionan, los primeros nombres facilitan la comprensión del programa.

---

## 4.1 Reglas básicas

Un nombre de variable:

- Puede contener letras.
- Puede contener números.
- Puede utilizar guion bajo `_`.
- No puede comenzar con un número.
- No debe contener espacios.
- No debe contener guiones `-` ni otros símbolos especiales.
- No puede utilizar palabras reservadas de Python.

Ejemplos válidos:

```python
nombre
edad1
nombre_estudiante
total_compra
```

Ejemplos inválidos:

```text
1nombre
nombre estudiante
precio-total
class
```

> `class` es una palabra que Python reserva para una característica del lenguaje que estudiaremos más adelante. Por eso no puede utilizarse como nombre de variable.

---

## 4.2 Convención snake_case

En Python es habitual utilizar la convención:

```text
snake_case
```

Por ejemplo:

```python
nombre_completo = "Ana Pérez"
total_compra = 35000
cantidad_estudiantes = 25
```

Las palabras se separan utilizando guion bajo.

Python permite otros estilos, pero durante el curso utilizaremos `snake_case` para mantener nombres consistentes y fáciles de leer.

## 💡 Experimenta

Ejecuta este programa y después cambia los valores de las variables:

```python
nombre_producto = "Cuaderno"
precio_producto = 5000

print(nombre_producto)
print(precio_producto)
```

Prueba también a reemplazar `nombre_producto` por `nombre producto`. Observa el error y luego corrige el nombre utilizando `snake_case`.

---

# 5. Tipos de datos

Python permite trabajar con diferentes tipos de información.

Algunos de los tipos básicos son:

```text
str    → texto
int    → números enteros
float  → números decimales
bool   → verdadero o falso
```

---

## 5.1 Texto — `str`

Los textos se escriben utilizando comillas:

```python
nombre = "Laura"
ciudad = "Medellín"
```

También pueden utilizarse comillas simples:

```python
nombre = 'Laura'
```

---

## 5.2 Números enteros — `int`

Los números enteros no tienen parte decimal.

```python
edad = 25
cantidad = 10
temperatura = -3
```

---

## 5.3 Números decimales — `float`

Los números decimales utilizan punto:

```python
altura = 1.72
precio = 3500.50
temperatura = 28.7
```

> En Python se utiliza punto `.` como separador decimal.

---

## 5.4 Valores booleanos — `bool`

Un dato booleano puede tener solamente dos valores:

```python
True
False
```

Ejemplo:

```python
activo = True
matriculado = False
```

Observa que comienzan con mayúscula.

---

# 6. Conocer el tipo de un dato

Python dispone de la función:

```python
type()
```

que permite consultar el tipo de un valor.

Ejemplo:

```python
nombre = "Ana"
edad = 20
altura = 1.65
activo = True

print(type(nombre))
print(type(edad))
print(type(altura))
print(type(activo))
```

Podrías obtener:

```text
<class 'str'>
<class 'int'>
<class 'float'>
<class 'bool'>
```

---

# 7. Mostrar información con `print()`

Ya hemos utilizado varias veces:

```python
print()
```

Esta función permite mostrar información en pantalla.

Ejemplo:

```python
print("Curso de Python")
```

También podemos mostrar variables:

```python
nombre = "Daniel"

print(nombre)
```

---

## 7.1 Mostrar texto y variables

Podemos separar varios valores utilizando comas:

```python
nombre = "Daniel"
edad = 21

print("Nombre:", nombre)
print("Edad:", edad)
```

Resultado:

```text
Nombre: Daniel
Edad: 21
```

---

## 7.2 f-strings

Otra forma muy útil de combinar texto y variables son las **f-strings**.

Ejemplo:

```python
nombre = "Daniel"
edad = 21

print(f"Mi nombre es {nombre} y tengo {edad} años")
```

Resultado:

```text
Mi nombre es Daniel y tengo 21 años
```

Las variables se colocan dentro de:

```text
{}
```

La letra `f` antes de las comillas indica que el texto es una f-string. Python reemplaza cada nombre escrito entre llaves por el valor de la variable correspondiente.

---

# 8. Entrada de datos con `input()`

Hasta ahora los valores han sido escritos directamente en el código.

También podemos permitir que el usuario introduzca información.

Para ello utilizamos:

```python
input()
```

Ejemplo:

```python
nombre = input("Escribe tu nombre: ")

print("Hola", nombre)
```

Cuando el programa se ejecute, esperará que el usuario escriba una respuesta.

---

## 8.1 Ejemplo completo

```python
nombre = input("Nombre: ")
ciudad = input("Ciudad: ")

print(f"Hola {nombre}")
print(f"Vives en {ciudad}")
```

---

# 9. Un detalle importante sobre `input()`

La función `input()` siempre devuelve texto.

Observa:

```python
edad = input("Escribe tu edad: ")

print(type(edad))
```

Aunque el usuario escriba:

```text
20
```

el tipo será:

```text
str
```

Esto será importante cuando necesitemos realizar operaciones matemáticas.

---

# 10. Conversión de tipos

Podemos convertir datos utilizando funciones como:

```text
int()
float()
str()
bool()
```

---

## 10.1 Convertir a entero

```python
edad = input("Escribe tu edad: ")

edad = int(edad)

print(type(edad))
```

Ahora `edad` será de tipo:

```text
int
```

---

## 10.2 Forma abreviada

También podemos convertir directamente:

```python
edad = int(input("Escribe tu edad: "))
```

---

## 10.3 Convertir a decimal

```python
altura = float(input("Escribe tu altura: "))
```

Por ejemplo:

```text
1.72
```

---

## 10.4 Convertir a texto

```python
edad = 20

texto_edad = str(edad)

print(texto_edad)
print(type(texto_edad))
```

Resultado:

```text
20
<class 'str'>
```

## 10.5 Convertir a booleano con `bool()`

La función `bool()` convierte un valor en `True` o `False`, pero su comportamiento requiere atención.

Los números `0` y `0.0` se convierten en `False`. Otros números, incluidos los negativos, se convierten en `True`:

```python
print(bool(0))
print(bool(0.0))
print(bool(1))
print(bool(-5))
```

Resultado:

```text
False
False
True
True
```

En los textos, una cadena vacía `""` se convierte en `False`. Cualquier texto que contenga al menos un carácter se convierte en `True`:

```python
print(bool(""))
print(bool("Hola"))
print(bool("False"))
```

Resultado:

```text
False
True
True
```

> **Importante:** `bool("False")` produce `True`, no `False`, porque `"False"` es un texto que contiene caracteres. `bool()` no interpreta el significado de la palabra.

Por la misma razón, convertir directamente una respuesta de `input()` puede producir un resultado inesperado:

```python
respuesta = input("Escribe algo y presiona Enter: ")

print(bool(respuesta))
```

Si el usuario escribe `False`, el resultado será `True`. Solo será `False` si presiona Enter sin escribir ningún carácter.

## 💡 Experimenta

Antes de ejecutar el siguiente código, intenta predecir cada resultado:

```python
print(int("25"))
print(float("3.5"))
print(str(100))
print(bool("0"))
print(bool(0))
```

Después ejecútalo y compara tus predicciones con los resultados.

---

# 11. Operadores aritméticos

Python permite realizar operaciones matemáticas.

| Operador | Operación |
|---|---|
| `+` | Suma |
| `-` | Resta |
| `*` | Multiplicación |
| `/` | División |
| `//` | División entera |
| `%` | Módulo o residuo |
| `**` | Potencia |

---

## 11.1 Suma

```python
a = 10
b = 5

resultado = a + b

print(resultado)
```

Resultado:

```text
15
```

---

## 11.2 Resta

```python
resultado = 10 - 4

print(resultado)
```

Resultado:

```text
6
```

---

## 11.3 Multiplicación

```python
resultado = 6 * 5

print(resultado)
```

Resultado:

```text
30
```

---

## 11.4 División

```python
resultado = 10 / 4

print(resultado)
```

Resultado:

```text
2.5
```

---

## 11.5 División entera

```python
resultado = 10 // 4

print(resultado)
```

Resultado:

```text
2
```

---

## 11.6 Módulo

El operador `%` devuelve el residuo de una división.

```python
resultado = 10 % 3

print(resultado)
```

Resultado:

```text
1
```

Este operador será muy útil más adelante.

---

## 11.7 Potencia

```python
resultado = 2 ** 3

print(resultado)
```

Resultado:

```text
8
```

## 11.8 Combinar operaciones

Podemos utilizar varios operadores en una misma expresión. Los paréntesis permiten indicar con claridad qué operación debe realizarse primero:

```python
nota_1 = 4.0
nota_2 = 3.5
nota_3 = 4.5

promedio = (nota_1 + nota_2 + nota_3) / 3

print(f"Promedio: {promedio}")
```

Resultado:

```text
Promedio: 4.0
```

## 💡 Experimenta

Cambia las tres notas y vuelve a ejecutar el programa. Después elimina los paréntesis de la fórmula y observa cómo cambia el resultado.

---

# 12. Ejemplo práctico — Calcular el total de una compra

Supongamos que queremos calcular el valor total de varios productos iguales.

```python
producto = input("Nombre del producto: ")
precio = float(input("Precio del producto: "))
cantidad = int(input("Cantidad: "))

total = precio * cantidad

print(f"Producto: {producto}")
print(f"Cantidad: {cantidad}")
print(f"Total: {total}")
```

Ejemplo de ejecución:

```text
Nombre del producto: Cuaderno
Precio del producto: 5000
Cantidad: 3

Producto: Cuaderno
Cantidad: 3
Total: 15000.0
```

Aquí ya estamos combinando:

```text
Variables
+
input()
+
Conversión de tipos
+
Operadores
+
print()
```

---

# 13. Operadores de comparación

Los operadores de comparación permiten comparar valores.

El resultado será:

```text
True
```

o:

```text
False
```

| Operador | Significado |
|---|---|
| `==` | Igual a |
| `!=` | Diferente de |
| `>` | Mayor que |
| `<` | Menor que |
| `>=` | Mayor o igual que |
| `<=` | Menor o igual que |

---

## 13.1 Ejemplos

```python
print(10 > 5)
print(10 < 5)
print(10 == 10)
print(10 != 7)
print(8 >= 8)
print(6 <= 4)
```

Resultado:

```text
True
False
True
True
True
False
```

---

## ⚠️ `=` no es lo mismo que `==`

Este símbolo:

```text
=
```

se utiliza para asignar valores:

```python
edad = 20
```

Mientras que:

```text
==
```

se utiliza para comparar:

```python
edad == 20
```

Esta diferencia es muy importante.

---

# 14. Operadores lógicos

Python dispone de tres operadores lógicos principales:

```text
and
or
not
```

---

## 14.1 Operador `and`

Devuelve `True` cuando ambas condiciones son verdaderas.

```python
edad = 20

resultado = edad >= 18 and edad <= 60

print(resultado)
```

Resultado:

```text
True
```

---

## 14.2 Operador `or`

Devuelve `True` cuando al menos una condición es verdadera.

```python
dia = "sábado"

resultado = dia == "sábado" or dia == "domingo"

print(resultado)
```

Resultado:

```text
True
```

---

## 14.3 Operador `not`

Invierte un valor booleano.

```python
activo = True

print(not activo)
```

Resultado:

```text
False
```

## 14.4 Combinar operadores lógicos y comparaciones

Podemos conectar comparaciones para responder preguntas más completas:

```python
nota = 4.2
asistencia = 85

cumple_requisitos = nota >= 3.0 and asistencia >= 80
necesita_revision = nota < 3.0 or asistencia < 80

print(f"Cumple los requisitos: {cumple_requisitos}")
print(f"Necesita revisión: {necesita_revision}")
print(f"No cumple los requisitos: {not cumple_requisitos}")
```

Resultado:

```text
Cumple los requisitos: True
Necesita revisión: False
No cumple los requisitos: False
```

El programa calcula resultados booleanos, pero todavía no elige qué instrucciones ejecutar. Esa capacidad se estudiará en la Unidad 2.

## 💡 Experimenta

Cambia `nota` a `2.8` y ejecuta nuevamente el ejemplo. Antes de hacerlo, intenta predecir los tres resultados.

---

# 15. Ejemplo integrador — Información de un estudiante

Crea un archivo llamado:

```text
estudiante.py
```

Escribe:

```python
nombre = input("Nombre del estudiante: ")
edad = int(input("Edad: "))
nota = float(input("Nota final: "))

es_mayor_edad = edad >= 18
nota_valida = nota >= 0 and nota <= 5

print()
print("--- INFORMACIÓN DEL ESTUDIANTE ---")
print(f"Nombre: {nombre}")
print(f"Edad: {edad}")
print(f"Nota final: {nota}")
print(f"Mayor de edad: {es_mayor_edad}")
print(f"Nota dentro del rango esperado: {nota_valida}")
```

Este programa todavía no toma decisiones.

Solamente calcula expresiones cuyo resultado puede ser `True` o `False`.

En la siguiente unidad utilizaremos esos resultados para hacer que el programa tome decisiones mediante `if`, `elif` y `else`.

---

# 16. Errores frecuentes

## 16.1 Intentar sumar texto y números

Este código:

```python
edad = input("Edad: ")

resultado = edad + 1
```

generará un error porque `input()` devuelve texto.

Debemos convertir:

```python
edad = int(input("Edad: "))

resultado = edad + 1
```

---

## 16.2 Utilizar coma como separador decimal

Esto no es correcto:

```text
1,75
```

Para un valor decimal debemos utilizar:

```text
1.75
```

---

## 16.3 Confundir `=` con `==`

Asignación:

```python
edad = 20
```

Comparación:

```python
edad == 20
```

---

## 16.4 Escribir una variable diferente

Ejemplo:

```python
nombre = "Ana"

print(nombres)
```

Python mostrará un error porque la variable creada fue:

```text
nombre
```

y no:

```text
nombres
```

---

## 16.5 Utilizar una variable antes de crearla

Este código dará error:

```python
print(edad)

edad = 20
```

Primero debemos crear la variable:

```python
edad = 20

print(edad)
```

## 16.6 Pensar que `bool("False")` produce `False`

Este código muestra `True`:

```python
resultado = bool("False")

print(resultado)
```

El texto `"False"` no está vacío. `bool()` comprueba si el texto contiene caracteres; no convierte la palabra según su significado.

## 16.7 Convertir texto que no representa un número

Este código generará un error:

```python
edad = int("veinte")
```

`int()` puede convertir el texto `"20"`, pero no la palabra `"veinte"`:

```python
edad = int("20")

print(edad)
```

## 16.8 Olvidar las comillas en un texto

Este código intenta buscar una variable llamada `Bogotá`:

```text
ciudad = Bogotá
```

Para guardar texto debemos utilizar comillas:

```python
ciudad = "Bogotá"
```

---

# 17. Ejercicios

Intenta resolver los siguientes ejercicios sin copiar directamente los ejemplos anteriores.

---

## Ejercicio 1 — Datos personales

Solicita:

- Nombre.
- Edad.
- Ciudad.

Después muestra una frase con toda la información.

---

## Ejercicio 2 — Suma de dos números

Solicita dos números enteros y muestra:

- La suma.
- La resta.
- La multiplicación.

---

## Ejercicio 3 — Área de un rectángulo

Solicita:

```text
base
altura
```

Calcula:

```text
área = base × altura
```

y muestra el resultado.

---

## Ejercicio 4 — Edad futura

Solicita la edad actual del usuario.

Calcula cuántos años tendrá dentro de 10 años.

---

## Ejercicio 5 — Precio total

Solicita:

- Nombre de un producto.
- Precio.
- Cantidad.

Calcula el valor total de la compra.

---

## Ejercicio 6 — Conversión de temperatura

Solicita una temperatura en grados Celsius.

Utiliza:

```text
F = (C × 9 / 5) + 32
```

para convertirla a Fahrenheit.

---

## Ejercicio 7 — Comparaciones

Solicita dos números y muestra el resultado de:

```text
primer número > segundo número
primer número < segundo número
primer número == segundo número
```

## Ejercicio 8 — División y residuo

Solicita una cantidad de estudiantes y una cantidad de grupos.

Muestra:

- Cuántos estudiantes completos quedarían en cada grupo utilizando `//`.
- Cuántos estudiantes quedarían sin repartir utilizando `%`.

## Ejercicio 9 — Validación mediante expresiones

Solicita una edad y una nota. Después calcula y muestra:

- Si la edad es mayor o igual a `18`.
- Si la nota se encuentra entre `0` y `5`, utilizando `and`.
- Si la edad es menor de `18` o la nota es menor de `3.0`, utilizando `or`.
- La negación del resultado de la primera comparación, utilizando `not`.

No utilices `if`, `elif` ni `else`.

## Ejercicio 10 — Predicciones con `bool()`

Antes de ejecutar el código, escribe qué resultado esperas en cada línea. Después comprueba tus respuestas:

```python
print(bool(""))
print(bool("False"))
print(bool("0"))
print(bool(0))
print(bool(2.5))
```

---

# 18. Reto de la unidad — Registro básico de estudiante

Crea un archivo llamado:

```text
registro_estudiante.py
```

El programa debe solicitar:

- Nombre.
- Edad.
- Programa académico.
- Semestre.
- Nota 1.
- Nota 2.
- Nota 3.

Luego debe calcular:

```text
promedio = (nota1 + nota2 + nota3) / 3
```

También debe determinar mediante expresiones booleanas:

- Si el estudiante es mayor de edad.
- Si el promedio es mayor o igual a `3.0`.

> Todavía no utilices `if`. Eso lo aprenderemos en la siguiente unidad.

Finalmente muestra un resumen similar a:

```text
----- REGISTRO DEL ESTUDIANTE -----

Nombre: Laura Pérez
Edad: 20
Programa: Ingeniería de Sistemas
Semestre: 3
Promedio: 4.1
Mayor de edad: True
Promedio igual o superior a 3.0: True
```

---

# 19. Comprobación de aprendizaje

Antes de continuar, comprueba que puedes:

- [ ] Crear variables.
- [ ] Diferenciar `str`, `int`, `float` y `bool`.
- [ ] Utilizar `type()`.
- [ ] Mostrar información mediante `print()`.
- [ ] Utilizar f-strings.
- [ ] Solicitar datos mediante `input()`.
- [ ] Explicar por qué `input()` devuelve texto.
- [ ] Convertir datos utilizando `int()`, `float()` y `str()`.
- [ ] Explicar qué valores básicos convierte `bool()` en `False` y por qué `bool("False")` produce `True`.
- [ ] Realizar operaciones aritméticas.
- [ ] Utilizar operadores de comparación.
- [ ] Diferenciar `=` de `==`.
- [ ] Utilizar `and`, `or` y `not`.
- [ ] Utilizar nombres de variables descriptivos.

---

# 20. Lo que aprendimos

En esta unidad comenzamos a trabajar formalmente con Python.

Ahora podemos representar el funcionamiento de nuestros programas así:

```text
Entrada
   ↓
Variables
   ↓
Operaciones
   ↓
Resultado
```

Por ejemplo:

```python
precio = float(input("Precio: "))
cantidad = int(input("Cantidad: "))

total = precio * cantidad

print(f"Total: {total}")
```

Ya podemos recibir información, procesarla y mostrar resultados.

También aprendimos a distinguir `str`, `int`, `float` y `bool`, a convertir valores con cuidado y a producir resultados booleanos mediante comparaciones y operadores lógicos.

En la siguiente unidad agregaremos algo fundamental:

**la capacidad de tomar decisiones y repetir instrucciones.**

---

# ➡️ Siguiente unidad

Continúa con:

👉 [Unidad 2 — Control de flujo](../unidad02-control-flujo/)

En la siguiente unidad aprenderás sobre:

- `if`.
- `elif`.
- `else`.
- Condiciones.
- Condiciones anidadas.
- `match`.
- Ciclo `while`.
- Ciclo `for`.
- `range()`.
- `break`.
- `continue`.

---

# 🧭 Navegación

⬅️ [Volver a la Unidad 0 — Preparación del entorno](../unidad00-entorno/)

🏠 [Volver al inicio del curso](../README.md)

➡️ [Continuar a la Unidad 2 — Control de flujo](../unidad02-control-flujo/)


---

## Continuar el curso

- **Unidad anterior:** [Unidad 0 — Preparación del entorno](../unidad00-entorno/README.md)
- **Volver al índice:** [Todas las unidades](../README.md)
- **Siguiente unidad:** [Unidad 2 — Control de flujo](../unidad02-control-flujo/README.md)
