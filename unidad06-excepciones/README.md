# Unidad 6 — Errores y excepciones

[Volver al índice del curso](../README.md) · [Ver el curso en Aprende con Leli](https://lelyliliana.github.io/aprende-con-leli/cursos/python/)

Los programas reciben datos, leen archivos y realizan operaciones que no siempre pueden completarse. En esta unidad aprenderás a reconocer errores y responder de forma controlada ante situaciones excepcionales.

---

## 🎯 Objetivos de aprendizaje

Al finalizar esta unidad podrás:

- Diferenciar errores de sintaxis, ejecución y lógica.
- Manejar excepciones específicas con `try` y `except`.
- Utilizar `else` y `finally` cuando correspondan.
- Validar entradas mediante ciclos y excepciones.
- Manejar errores en archivos, CSV y JSON.
- Lanzar excepciones con `raise`.
- Explicar la propagación entre funciones.
- Evitar capturas generales que oculten problemas.

---

## 📋 Antes de comenzar

Necesitas haber completado la Unidad 5. Retomaremos funciones, colecciones, archivos, JSON y `pathlib`.

No utilizaremos clases, excepciones personalizadas, módulos propios, testing, logging ni bibliotecas externas.

> Los fragmentos inválidos estarán marcados como **NO ejecutar — ejemplo de error** y se mostrarán como texto.

---

# 1. Los errores forman parte de la programación

Encontrar y corregir errores es una parte normal del desarrollo. Podemos distinguir:

- **Error de sintaxis:** el código no respeta las reglas del lenguaje.
- **Error de ejecución:** la sintaxis es válida, pero una operación falla al ejecutarse.
- **Error lógico:** el programa termina, pero su resultado no corresponde al objetivo.

`try/except` responde a determinadas excepciones durante la ejecución. No corrige automáticamente errores de sintaxis ni de lógica.

---

# 2. Errores de sintaxis

Python debe interpretar la estructura antes de ejecutar el programa.

**NO ejecutar — ejemplo de error:**

```text
edad = 20

if edad >= 18
    print("Mayor de edad")
```

Faltan los dos puntos. Python informa un `SyntaxError`. La solución es corregir el código:

```python
edad = 20

if edad >= 18:
    print("Mayor de edad")
```

No debemos conservar código mal escrito y envolverlo en `try/except` como estrategia normal.

---

# 3. Errores durante la ejecución

Un programa sintácticamente válido también puede fallar:

| Excepción | Situación típica |
|---|---|
| `ZeroDivisionError` | Dividir entre cero |
| `ValueError` | Convertir `"hola"` con `int()` |
| `TypeError` | Operar tipos incompatibles |
| `IndexError` | Consultar una posición inexistente |
| `KeyError` | Consultar una clave inexistente |
| `FileNotFoundError` | Leer un archivo que no existe |

**NO ejecutar — ejemplos de error:**

```text
10 / 0
int("hola")
"Edad: " + 20
["Ana", "Luis"][5]
{"nombre": "Ana"}["nota"]
open("inexistente.txt", "r")
```

---

# 4. Errores lógicos

```python
precio = 100
descuento = 20
total = precio + descuento

print(total)
```

El programa muestra `120`, aunque probablemente queríamos restar el descuento. No ocurre una excepción: Python ejecuta la operación escrita. `try/except` no detecta este tipo de problema.

---

# 5. ¿Qué es una excepción?

Una **excepción** representa una situación que interrumpe el flujo normal durante la ejecución. Por ejemplo, `int("hola")`, una división entre cero, un índice inexistente o un archivo ausente.

Si no la manejamos, Python detiene el programa y muestra información técnica. Si el problema es esperado, podemos responder mediante `try/except`.

---

# 6. Primer `try/except`

```python
try:
    edad = int(input("Edad: "))
except ValueError:
    print("Debes escribir un número entero")
```

- `try` intenta ejecutar el bloque protegido.
- `except ValueError` identifica el problema que sabemos manejar.
- Si la conversión funciona, se omite el `except`.
- Si falla, se abandona el resto del `try` y se ejecuta `except`.

---

# 7. Flujo de ejecución

```text
try
 ↓
operación
 ↓
¿ocurre la excepción esperada?
 ↙                         ↘
sí                          no
 ↓                           ↓
except                    continúa
```

```python
try:
    numero = int(input("Escribe un entero: "))
    print("La conversión terminó")
except ValueError:
    print("No fue posible convertir el dato")

print("El programa continúa")
```

---

# 8. Capturar excepciones específicas

```python
try:
    divisor = float(input("Divisor: "))
    resultado = 10 / divisor
except ValueError:
    print("Debes escribir un número")
except ZeroDivisionError:
    print("El divisor no puede ser cero")
```

Cada nombre documenta qué puede fallar. Las capturas específicas evitan ocultar otros defectos.

---

# 9. Evitar `except` desnudo

**NO ejecutar como patrón recomendado:**

```text
try:
    numero = int(input("Número: "))
except:
    print("Algo falló")
```

Un `except:` desnudo puede ocultar errores inesperados y dificulta diagnosticarlos. Captura excepciones específicas siempre que conozcas el problema esperado.

---

# 10. Varios bloques `except`

```python
try:
    numero_1 = float(input("Primer número: "))
    numero_2 = float(input("Segundo número: "))
    resultado = numero_1 / numero_2
except ValueError:
    print("Ambos valores deben ser números")
except ZeroDivisionError:
    print("No se puede dividir entre cero")
else:
    print(f"Resultado: {resultado}")
```

Python ejecuta el primer `except` compatible con la excepción.

---

# 11. Obtener información con `as error`

```python
try:
    edad = int("veinte")
except ValueError as error:
    print(f"Ocurrió un error: {error}")
```

`error` contiene información para diagnosticar el problema. En una aplicación real no siempre mostraremos detalles técnicos al usuario final; suele necesitar un mensaje comprensible.

---

# 12. `except Exception as error`

```python
try:
    resultado = 10 / 0
except Exception as error:
    print(f"No pudo completarse: {type(error).__name__}")
```

`Exception` agrupa muchas excepciones habituales. Una captura general puede justificarse en un límite concreto del programa si sabemos cómo responder, pero una captura específica comunica mejor el problema esperado. No utilizaremos `BaseException`.

---

# 13. No silenciar errores

Este patrón suele ser peligroso:

```text
try:
    realizar_operacion()
except Exception:
    pass
```

El programa oculta el fallo y continúa. Si capturas una excepción, responde de manera útil: informa, solicita otro dato, devuelve un resultado documentado o vuelve a propagarla.

---

# 14. La cláusula `else`

`else` se ejecuta solamente cuando `try` termina sin excepción:

```python
try:
    nota = float(input("Nota: "))
except ValueError:
    print("La nota debe ser numérica")
else:
    print(f"Nota registrada: {nota}")
```

Así separamos la operación que puede fallar de la lógica que depende de su éxito.

---

# 15. La cláusula `finally`

`finally` normalmente se ejecuta haya ocurrido o no una excepción:

```python
try:
    numero = int(input("Escribe un entero: "))
except ValueError:
    print("Entrada inválida")
finally:
    print("Intento de lectura terminado")
```

Sirve para limpieza necesaria en ambos caminos. Para archivos seguiremos prefiriendo `with open(...)`, que administra el cierre con claridad. La lógica que depende del éxito pertenece a `else`, no a `finally`.

---

# 16. Estructura completa

```python
try:
    divisor = float(input("Divisor: "))
    resultado = 20 / divisor
except ValueError:
    print("Debes escribir un número")
except ZeroDivisionError:
    print("No puedes dividir entre cero")
else:
    print(f"Resultado: {resultado}")
finally:
    print("Operación finalizada")
```

No todos los casos necesitan las cuatro cláusulas. Utiliza solo las que aporten al problema.

## 💡 Experimenta

Ejecuta el ejemplo con `4`, `0` y `hola`. Predice cuándo se ejecutarán `else` y `finally`.

---

# 17. Validación con ciclos y excepciones

```python
while True:
    try:
        edad = int(input("Edad: "))
        break
    except ValueError:
        print("Entrada inválida. Debes escribir un entero")

print(f"Edad registrada: {edad}")
```

El ciclo termina únicamente después de una conversión válida. Esto admite enteros negativos y es más robusto que depender de `isdigit()`.

---

# 18. Función para leer un entero

```python
def leer_entero(mensaje):
    """Solicita datos hasta obtener un entero."""
    while True:
        try:
            return int(input(mensaje))
        except ValueError:
            print("Debes escribir un entero")

edad = leer_entero("Edad: ")
cantidad = leer_entero("Cantidad: ")
print(edad, cantidad)
```

Cuando la conversión funciona, `return` entrega el entero y termina la función y su ciclo.

---

# 19. Función para leer un decimal

```python
def leer_decimal(mensaje):
    """Solicita datos hasta obtener un número decimal."""
    while True:
        try:
            return float(input(mensaje))
        except ValueError:
            print("Debes escribir un número válido")

temperatura = leer_decimal("Temperatura: ")
print(f"Temperatura registrada: {temperatura}")
```

Acepta valores como `-3.5`, aunque `"-3.5".isdigit()` sea `False`.

---

# 20. Excepciones y archivos

```python
try:
    with open("datos.txt", "r", encoding="utf-8") as archivo:
        contenido = archivo.read()
except FileNotFoundError:
    print("El archivo no existe")
else:
    print(contenido)
```

`with` administra el cierre. `FileNotFoundError` identifica específicamente la ausencia del archivo.

---

# 21. `pathlib` y excepciones

Podemos comprobar antes:

```python
from pathlib import Path

ruta = Path("datos.txt")

if ruta.exists():
    with ruta.open("r", encoding="utf-8") as archivo:
        print(archivo.read())
else:
    print("El archivo no existe")
```

O intentar la operación:

```python
from pathlib import Path

ruta = Path("datos.txt")

try:
    with ruta.open("r", encoding="utf-8") as archivo:
        print(archivo.read())
except FileNotFoundError:
    print("El archivo no existe")
```

Ninguna estrategia es universalmente superior. Incluso después de `exists()`, otro proceso podría eliminar el archivo antes de abrirlo; capturar responde al fallo real.

---

# 22. Excepciones en JSON

```python
import json

try:
    with open("estudiantes.json", "r", encoding="utf-8") as archivo:
        estudiantes = json.load(archivo)
except FileNotFoundError:
    print("No existe el archivo de estudiantes")
except json.JSONDecodeError:
    print("El archivo no contiene JSON válido")
else:
    print(f"Registros cargados: {len(estudiantes)}")
```

Un archivo puede existir y contener JSON inválido. `JSONDecodeError` pertenece al módulo `json`, por eso usamos `json.JSONDecodeError`.

---

# 23. Excepciones en CSV

Los campos de CSV son cadenas y sus conversiones pueden fallar:

```python
import csv

with open("estudiantes.csv", "w", encoding="utf-8", newline="") as archivo:
    escritor = csv.DictWriter(archivo, fieldnames=["nombre", "edad", "nota"])
    escritor.writeheader()
    escritor.writerow({"nombre": "Ana", "edad": "veinte", "nota": "4.5"})

with open("estudiantes.csv", "r", encoding="utf-8", newline="") as archivo:
    for fila in csv.DictReader(archivo):
        try:
            edad = int(fila["edad"])
            nota = float(fila["nota"])
        except ValueError:
            print(f"Datos numéricos inválidos para {fila['nombre']}")
        else:
            print(f"{fila['nombre']}: {edad} años, nota {nota}")
```

El ejemplo crea primero el archivo y se concentra en `ValueError`.

---

# 24. Lanzar una excepción con `raise`

```python
def calcular_promedio(notas):
    if len(notas) == 0:
        raise ValueError("La lista de notas no puede estar vacía")

    return sum(notas) / len(notas)

print(calcular_promedio([4.0, 3.5, 4.5]))
```

Nuestro programa detecta una condición inválida. `raise` interrumpe la función y el mensaje explica por qué no puede completar su responsabilidad.

---

# 25. ¿Por qué lanzar una excepción?

- `return None` comunica ausencia de resultado mediante una convención que debe comprobarse.
- `return False` puede ser una respuesta normal o señalar un fallo, según la documentación.
- `raise ValueError(...)` comunica que la función no puede completarse normalmente por un valor inválido.

Ninguna opción es siempre superior. `raise` ayuda a impedir que un problema pase inadvertido.

---

# 26. Capturar una excepción lanzada

```python
def calcular_promedio(notas):
    if len(notas) == 0:
        raise ValueError("La lista de notas no puede estar vacía")

    return sum(notas) / len(notas)

try:
    promedio = calcular_promedio([])
except ValueError as error:
    print(f"No fue posible calcular: {error}")
else:
    print(f"Promedio: {promedio}")
```

La función produce la excepción y quien la llama decide cómo comunicarla.

---

# 27. `raise` sin argumentos

Dentro de `except`, `raise` vuelve a propagar la excepción actual:

```python
def convertir_edad(texto):
    try:
        return int(texto)
    except ValueError:
        print("La función no pudo convertir la edad")
        raise

try:
    edad = convertir_edad("veinte")
except ValueError:
    print("El programa principal decidió cómo continuar")
```

Evita informar el mismo problema en muchos niveles; este ejemplo solo muestra el mecanismo.

---

# 28. Propagación de excepciones

```text
función A
   ↓
función B
   ↓
ocurre una excepción
   ↓
B no la maneja
   ↓
la excepción regresa hacia A
```

```python
def dividir(dividendo, divisor):
    return dividendo / divisor

def calcular_resultado(divisor):
    return dividir(100, divisor)

try:
    resultado = calcular_resultado(0)
except ZeroDivisionError:
    print("No fue posible calcular: el divisor es cero")
```

No es obligatorio colocar `try/except` dentro de cada función. Puede manejarse donde exista contexto para decidir la respuesta.

---

# 29. No capturar demasiado pronto

```python
def calcular_total(precio, cantidad):
    if precio < 0 or cantidad < 0:
        raise ValueError("Precio y cantidad no pueden ser negativos")

    return precio * cantidad
```

La función calcula o lanza. El flujo que interactúa con el usuario puede capturar y presentar el mensaje. Una función debe capturar cuando realmente puede recuperarse o añadir información útil.

---

# 30. Bloques `try` pequeños y precisos

```python
texto_edad = input("Edad: ")

try:
    edad = int(texto_edad)
except ValueError:
    print("La edad debe ser un entero")
else:
    print(f"Edad registrada: {edad}")
```

Un `try` con muchas operaciones dificulta identificar cuál produjo `ValueError`. Protege la operación susceptible y coloca en `else` la lógica que depende del éxito.

---

# 31. Las excepciones no sustituyen todo control de flujo

```python
edad = 20

if edad >= 18:
    print("Mayor de edad")
else:
    print("Menor de edad")
```

Una clasificación normal pertenece a `if`. Las excepciones representan situaciones que impiden completar una operación como se esperaba.

---

# 32. Jerarquía de excepciones

Vista simplificada:

```text
Exception
├── ValueError
├── TypeError
├── LookupError
│   ├── IndexError
│   └── KeyError
├── OSError
│   └── FileNotFoundError
└── ArithmeticError
    └── ZeroDivisionError
```

`except Exception` puede capturar muchas excepciones derivadas. Cuando combinamos capturas relacionadas, las específicas deben escribirse antes de las generales.

---

# 33. Excepciones personalizadas: un anticipo

Después de estudiar clases aprenderemos a crear excepciones propias. No definiremos clases de excepción en esta unidad; las integradas son suficientes.

---

# 34. Ejemplo integrador — Lectura segura de estudiantes

El ejemplo crea JSON válido, lo carga y valida los registros:

```python
import json
from pathlib import Path

def cargar_estudiantes(ruta):
    """Carga registros válidos o devuelve una lista vacía."""
    try:
        with ruta.open("r", encoding="utf-8") as archivo:
            datos = json.load(archivo)
    except FileNotFoundError:
        print("No existe el archivo de estudiantes")
        return []
    except json.JSONDecodeError:
        print("El archivo contiene JSON inválido")
        return []

    estudiantes_validos = []

    for registro in datos:
        try:
            nombre = str(registro["nombre"])
            edad = int(registro["edad"])
            nota = float(registro["nota"])
        except (KeyError, TypeError, ValueError):
            print("Se omitió un registro inválido")
            continue

        estudiantes_validos.append({"nombre": nombre, "edad": edad, "nota": nota})

    return estudiantes_validos

ruta_datos = Path("estudiantes.json")
datos_iniciales = [
    {"nombre": "Ana", "edad": 20, "nota": 4.5},
    {"nombre": "Luis", "edad": 22, "nota": 3.8}
]

with ruta_datos.open("w", encoding="utf-8") as archivo:
    json.dump(datos_iniciales, archivo, ensure_ascii=False, indent=4)

estudiantes = cargar_estudiantes(ruta_datos)
print(f"Registros válidos: {len(estudiantes)}")
```

La tupla de excepciones reúne únicamente problemas esperados para un registro.

## 💡 Experimenta

Cambia una edad por `"veinte"` o elimina la clave `"nota"`. Se omitirá solo ese registro.

---

# 35. Ejemplo integrador — Guardado seguro

`OSError` agrupa problemas del sistema operativo relacionados, entre otros casos, con rutas o permisos:

```python
import json
from pathlib import Path

def guardar_estudiantes(ruta, estudiantes):
    """Guarda los registros y devuelve si tuvo éxito."""
    try:
        with ruta.open("w", encoding="utf-8") as archivo:
            json.dump(estudiantes, archivo, ensure_ascii=False, indent=4)
    except OSError:
        print("No fue posible guardar el archivo")
        return False
    else:
        return True

ruta_datos = Path("estudiantes.json")
estudiantes = [{"nombre": "Ana", "edad": 20, "nota": 4.5}]

if guardar_estudiantes(ruta_datos, estudiantes):
    print("Datos guardados correctamente")
```

No provocamos artificialmente un error del sistema.

---

# 36. Errores frecuentes

## 36.1 Ocultar todos los errores

`except:` y `except Exception: pass` esconden defectos. Captura problemas específicos y responde visiblemente.

## 36.2 Capturar una excepción incorrecta

`except ZeroDivisionError` no maneja `int("hola")`. Identifica la operación y su excepción.

## 36.3 Crear un `try` demasiado grande

Protege solo operaciones relacionadas con el fallo esperado; utiliza `else` para el camino exitoso.

## 36.4 Suponer que `except` siempre se ejecuta

Solo se ejecuta cuando ocurre una excepción compatible dentro de `try`.

## 36.5 Confundir `else` y `finally`

`else` requiere éxito; `finally` normalmente se ejecuta con éxito o error.

## 36.6 Colocar lógica de éxito en `finally`

No muestres “operación exitosa” allí, pues también aparecería después de un error.

## 36.7 Utilizar `raise` sin comprenderlo

`raise` interrumpe el flujo. Si nadie maneja la excepción, el programa termina.

## 36.8 Devolver silenciosamente datos incorrectos

No ocultes un fallo devolviendo un valor aparentemente válido sin documentarlo.

## 36.9 Mostrar detalles técnicos innecesarios

`as error` ayuda a diagnosticar, pero el usuario suele necesitar un mensaje claro.

## 36.10 Intentar manejar código mal escrito

Un `SyntaxError` del código fuente se corrige antes de ejecutar; no es una estrategia de ejecución normal.

## 36.11 Reemplazar cualquier `if`

Las decisiones normales continúan expresándose mediante condicionales.

---

# 37. Ejercicios

No se incluyen soluciones completas.

## Ejercicio 1 — Clasificar errores

Clasifica casos como sintaxis, ejecución o lógica.

## Ejercicio 2 — `ValueError`

Solicita un entero y maneja una conversión inválida.

## Ejercicio 3 — `ZeroDivisionError`

Solicita dos números y maneja la división entre cero.

## Ejercicio 4 — Varios `except`

Distingue conversión inválida y división por cero.

## Ejercicio 5 — `as error`

Muestra tipo y mensaje de una excepción en una práctica de diagnóstico.

## Ejercicio 6 — `else`

Muestra el resultado solo si `try` termina correctamente.

## Ejercicio 7 — `finally`

Agrega un mensaje final en los dos caminos y explica su significado.

## Ejercicio 8 — Validación repetida

Solicita una edad hasta recibir un entero.

## Ejercicio 9 — `leer_entero()`

Crea una función y úsala con edad y cantidad.

## Ejercicio 10 — `leer_decimal()`

Acepta decimales y negativos para una temperatura.

## Ejercicio 11 — `FileNotFoundError`

Lee una ruta solicitada y responde si no existe.

## Ejercicio 12 — TXT seguro

Devuelve contenido o `None` si la ruta no existe.

## Ejercicio 13 — `JSONDecodeError`

Crea JSON inválido en una carpeta de práctica y maneja su lectura.

## Ejercicio 14 — JSON seguro

Distingue archivo inexistente y JSON inválido.

## Ejercicio 15 — `raise ValueError`

Rechaza notas fuera de `0.0` a `5.0`.

## Ejercicio 16 — Capturar una excepción lanzada

Captura el `ValueError` anterior y comunica su mensaje.

## Ejercicio 17 — Propagación

Usa dos funciones y maneja `ZeroDivisionError` solo en el flujo principal.

## Ejercicio 18 — Reducir un `try`

Refactoriza un bloque que proteja demasiadas operaciones.

## Ejercicio 19 — CSV inválido

Omite con un mensaje registros cuya conversión falle.

## Ejercicio 20 — Guardado JSON

Maneja `OSError` y devuelve un booleano documentado.

---

# 38. Reto de la unidad — Sistema de estudiantes robusto

Evoluciona el sistema de la Unidad 5 con este menú:

```text
1. Registrar estudiante
2. Mostrar estudiantes
3. Buscar estudiante
4. Calcular promedio
5. Guardar datos
6. Cargar datos
7. Salir
```

## Requisitos

- Mantén una lista de diccionarios y funciones con responsabilidades claras.
- Crea `leer_entero()` y `leer_decimal()`.
- Valida edad no negativa y nota entre `0.0` y `5.0`.
- Utiliza `ValueError` y `raise` para valores inválidos.
- Maneja `FileNotFoundError`, `json.JSONDecodeError` y, al guardar, `OSError`.
- Usa `else` o `finally` solo cuando expresen su propósito.
- No silencies excepciones ni uses `except:` desnudo.
- Evita que una entrada incorrecta cierre el menú completo.
- Mantén bloques `try` pequeños y mensajes comprensibles.
- Evita variables globales innecesarias.
- No utilices clases, excepciones personalizadas ni bibliotecas externas.

Construye primero las funciones de validación, después carga y guardado, y finalmente integra el menú. No se entrega la solución completa.

---

# 39. Comprobación de aprendizaje

- [ ] Distingo errores de sintaxis, ejecución y lógica.
- [ ] Puedo explicar qué es una excepción.
- [ ] Utilizo `try` y excepciones específicas.
- [ ] Manejo problemas diferentes con varios `except`.
- [ ] Consulto información mediante `as error`.
- [ ] Evito `except:` desnudo y errores silenciados.
- [ ] Utilizo correctamente `else` y `finally`.
- [ ] Valido entradas con ciclos y excepciones.
- [ ] Creo funciones reutilizables de lectura.
- [ ] Manejo archivos inexistentes, JSON inválido y conversiones CSV.
- [ ] Lanzo una excepción apropiada con `raise`.
- [ ] Capturo excepciones lanzadas y comprendo su propagación.
- [ ] Mantengo bloques `try` pequeños.
- [ ] Elijo entre `if`, un retorno especial y una excepción.

---

# 40. Lo que aprendimos

```text
Operación
   ↓
¿puede fallar?
   ↓
  try
 ↙   ↘
error  éxito
 ↓      ↓
except  else
   \    /
   finally
      ↓
continuación controlada
```

No todos los programas necesitan las cuatro cláusulas. Una captura específica y pequeña suele ser suficiente.

Ahora sabemos representar datos, organizar lógica, persistir información y responder a errores. En la Unidad 7 aprenderemos a representar entidades mediante objetos.

---

# 🧭 Navegación

⬅️ [Volver a la Unidad 5 — Cadenas y archivos](../unidad05-cadenas-archivos/)

🏠 [Volver al inicio del curso](../README.md)

➡️ [Continuar a la Unidad 7 — Programación orientada a objetos](../unidad07-poo/)


---

## Continuar el curso

- **Unidad anterior:** [Unidad 5 — Cadenas y archivos](../unidad05-cadenas-archivos/README.md)
- **Volver al índice:** [Todas las unidades](../README.md)
- **Siguiente unidad:** [Unidad 7 — Programación orientada a objetos](../unidad07-poo/README.md)
