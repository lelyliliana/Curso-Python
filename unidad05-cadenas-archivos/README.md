# Unidad 5 — Cadenas y archivos

Hasta ahora hemos utilizado textos y hemos almacenado datos mientras el programa se encuentra en ejecución. En esta unidad aprenderás a procesar cadenas con mayor profundidad y a conservar información en archivos para recuperarla posteriormente.

---

## 🎯 Objetivos de aprendizaje

Al finalizar esta unidad podrás:

- Consultar, recorrer y obtener partes de una cadena.
- Explicar la inmutabilidad de `str`.
- Transformar, buscar, dividir y unir texto.
- Validar características básicas de una cadena.
- Utilizar f-strings y caracteres de escape.
- Explicar qué significa que los datos sean persistentes.
- Trabajar con rutas relativas y `with open()`.
- Escribir, leer y agregar contenido en archivos TXT.
- Guardar y recuperar registros en CSV y JSON.
- Utilizar `pathlib` para construir rutas y comprobar su existencia.
- Organizar operaciones de texto y archivos mediante funciones.

---

## 📋 Antes de comenzar

Necesitas haber completado la Unidad 4. Utilizaremos colecciones y funciones para organizar los ejemplos.

No utilizaremos clases, manejo de excepciones, pandas, expresiones regulares ni bibliotecas externas.

> **Importante:** varios ejemplos crean archivos en la carpeta desde la que ejecutas el programa. Utiliza una carpeta de práctica y revisa el contenido antes y después de cada ejecución.

---

# Parte I — Cadenas

# 1. Profundizar en `str`

Una cadena de tipo `str` representa texto. Puede delimitarse con comillas simples o dobles:

```python
curso = "Python"
ciudad = 'Bogotá'
texto_vacio = ""

print(curso)
print(ciudad)
print(len(texto_vacio))
```

Una cadena multilínea se delimita con tres comillas:

```python
mensaje = """Primera línea
Segunda línea
Tercera línea"""

print(mensaje)
```

Una cadena con triple comilla puede almacenar texto de varias líneas. Una **docstring**, estudiada en la Unidad 4, utiliza esa sintaxis en una posición especial —por ejemplo, al comienzo de una función— para documentar código. No toda cadena multilínea es una docstring.

---

# 2. Las cadenas son secuencias

Al igual que las listas y tuplas, las cadenas tienen posiciones ordenadas:

```text
Texto:   P y t h o n
Índice:  0 1 2 3 4 5
Negativo:-6-5-4-3-2-1
```

```python
texto = "Python"

print(texto[0])
print(texto[-1])
print(len(texto))
```

Resultado:

```text
P
n
6
```

Podemos recorrer sus caracteres:

```python
texto = "Python"

for caracter in texto:
    print(caracter)
```

---

# 3. Inmutabilidad de `str`

Las cadenas son **inmutables**: no podemos reemplazar directamente uno de sus caracteres después de crearlas. Esto se parece a la inmutabilidad de las tuplas.

No ejecutes este ejemplo:

```text
texto = "Python"
texto[0] = "J"
```

Para obtener un texto diferente debemos construir una cadena nueva:

```python
texto = "Python"
nuevo_texto = "J" + texto[1:]

print(texto)
print(nuevo_texto)
```

Resultado:

```text
Python
Jython
```

---

# 4. Slicing

El slicing obtiene una parte de la cadena:

```text
texto[inicio:fin]
texto[inicio:fin:paso]
```

El límite inicial se incluye y el final no:

```python
texto = "Programación"

print(texto[:])
print(texto[3:])
print(texto[:4])
print(texto[::2])
print(texto[::-1])
```

- `[:]` obtiene una copia completa.
- `[3:]` obtiene desde el índice `3`.
- `[:4]` obtiene hasta antes del índice `4`.
- `[::2]` avanza de dos en dos.
- `[::-1]` invierte el orden.

## 💡 Experimenta

Con `texto = "estudiante"`, obtén `"est"`, `"diante"` y el texto invertido.

---

# 5. Concatenación y repetición

`+` une cadenas y `*` repite una cadena:

```python
nombre = "Ana"
apellido = "Pérez"
nombre_completo = nombre + " " + apellido

print(nombre_completo)
print("-" * 20)
```

No podemos concatenar directamente `str` con `int` o `float`. Podemos convertir o utilizar una f-string:

```python
edad = 20

print("Edad: " + str(edad))
print(f"Edad: {edad}")
```

---

# 6. Pertenencia

`in` comprueba si un fragmento aparece en el texto y `not in` comprueba lo contrario:

```python
mensaje = "Estoy aprendiendo Python"

print("Python" in mensaje)
print("Java" not in mensaje)
```

Las comparaciones distinguen mayúsculas de minúsculas: `"python"` y `"Python"` no son iguales.

---

# 7. Cambiar mayúsculas y minúsculas

Los métodos de cadena producen cadenas nuevas; no modifican la original:

```python
texto = "curso DE python"

print(texto.upper())
print(texto.lower())
print(texto.capitalize())
print(texto.title())
print(texto.swapcase())
print(texto)
```

| Método | Resultado general |
|---|---|
| `upper()` | Todo en mayúsculas |
| `lower()` | Todo en minúsculas |
| `capitalize()` | Primera letra del texto en mayúscula |
| `title()` | Primera letra de cada palabra en mayúscula |
| `swapcase()` | Intercambia mayúsculas y minúsculas |

Para conservar una transformación debemos asignar el resultado:

```python
nombre = "ana pérez"
nombre = nombre.title()

print(nombre)
```

---

# 8. Eliminar espacios exteriores

`strip()` elimina espacios al comienzo y al final. `lstrip()` actúa solo a la izquierda y `rstrip()` solo a la derecha:

```python
texto = "   Python   "

print(f">{texto.strip()}<")
print(f">{texto.lstrip()}<")
print(f">{texto.rstrip()}<")
```

Es útil al recibir datos:

```python
nombre = input("Escribe tu nombre: ").strip().title()

print(f"Nombre normalizado: {nombre}")
```

Estos métodos no eliminan los espacios interiores entre palabras.

---

# 9. Buscar texto

## 9.1 `find()` y `rfind()`

`find()` devuelve el índice de la primera aparición. `rfind()` busca desde la derecha y devuelve el índice de la última:

```python
mensaje = "Python permite aprender Python"

print(mensaje.find("Python"))
print(mensaje.rfind("Python"))
print(mensaje.find("Java"))
```

Resultado:

```text
0
23
-1
```

`find()` devuelve `-1` cuando no encuentra el fragmento. No devuelve directamente un booleano.

El método `index()` también busca una posición, pero produce un error si no encuentra el texto. Como el manejo de excepciones se estudiará en la siguiente unidad, preferiremos `find()` o una comprobación con `in` cuando la búsqueda pueda fallar.

## 9.2 `count()`, `startswith()` y `endswith()`

```python
archivo = "notas_finales.csv"
mensaje = "Python Python Python"

print(mensaje.count("Python"))
print(archivo.startswith("notas"))
print(archivo.endswith(".csv"))
```

Resultado:

```text
3
True
True
```

---

# 10. Reemplazar texto

`replace(anterior, nuevo)` produce una cadena con los reemplazos:

```python
mensaje = "Aprendo Python con ejemplos de Python"
nuevo_mensaje = mensaje.replace("Python", "programación")

print(mensaje)
print(nuevo_mensaje)
```

La cadena original no cambia debido a la inmutabilidad de `str`.

---

# 11. Dividir cadenas con `split()`

`split()` divide una cadena y devuelve una lista:

```python
mensaje = "Curso de Python"
palabras = mensaje.split()

print(palabras)
print(type(palabras))
```

Podemos indicar un separador:

```python
registro = "Ana,20,4.5"
datos = registro.split(",")

print(datos)
print(datos[0])
```

---

# 12. Unir cadenas con `join()`

`join()` une textos de una colección. El método pertenece al texto que actuará como separador:

```python
palabras = ["Curso", "de", "Python"]
texto = " ".join(palabras)
ruta_textual = "/".join(["datos", "estudiantes", "notas.txt"])

print(texto)
print(ruta_textual)
```

Resultado:

```text
Curso de Python
datos/estudiantes/notas.txt
```

Los elementos que se unen deben ser cadenas.

---

# 13. Validación básica del contenido

Algunos métodos responden con `True` o `False`:

```python
print("2026".isdigit())
print("Python".isalpha())
print("Python3".isalnum())
print("   ".isspace())
```

- `isdigit()`: todos los caracteres representan dígitos y existe al menos uno.
- `isalpha()`: todos son letras y existe al menos una.
- `isalnum()`: todos son letras o números y existe al menos uno.
- `isspace()`: todos son caracteres de espacio y existe al menos uno.

`isdigit()` no es una validación universal de números decimales o negativos:

```python
print("25".isdigit())
print("-25".isdigit())
print("4.5".isdigit())
```

Resultado:

```text
True
False
False
```

En la Unidad 6 aprenderemos a manejar de forma segura conversiones que pueden fallar.

---

# 14. f-strings con formato

Las llaves de una f-string pueden contener variables y expresiones:

```python
precio = 12500
cantidad = 3

print(f"Total: {precio * cantidad}")
```

Podemos controlar la cantidad de decimales:

```python
promedio = 4.2567
precio = 1234567.5

print(f"Promedio: {promedio:.2f}")
print(f"Precio: {precio:,.2f}")
```

Resultado:

```text
Promedio: 4.26
Precio: 1,234,567.50
```

`.2f` muestra dos decimales. `,.2f` añade separadores de miles y dos decimales.

---

# 15. Caracteres de escape

Una barra invertida introduce caracteres especiales dentro de una cadena:

| Secuencia | Significado |
|---|---|
| `\n` | Nueva línea |
| `\t` | Tabulación |
| `\\` | Barra invertida |
| `\"` | Comilla doble |
| `\'` | Comilla simple |

```python
print("Nombre:\tAna\nNota:\t4.5")
print("Una barra invertida: \\")
print("Ella dijo: \"Hola\"")
print('La palabra \'Python\' está entre comillas')
```

---

# 16. Cadenas crudas

Una cadena cruda o *raw string* utiliza el prefijo `r` y trata las barras invertidas como caracteres normales en la mayoría de los casos:

```python
ruta_ejemplo = r"carpeta\datos\notas.txt"

print(ruta_ejemplo)
```

Esto puede ayudar al representar rutas con barras invertidas. Para construir rutas reales de forma portable utilizaremos `pathlib` más adelante. No introduciremos expresiones regulares en esta unidad.

---

# 17. Ejemplo integrador de texto

Este programa normaliza un nombre, separa sus palabras y crea un resumen:

```python
def normalizar_nombre(nombre):
    """Elimina espacios exteriores y ajusta la presentación."""
    return nombre.strip().title()

def crear_resumen(nombre):
    """Devuelve un resumen básico del nombre recibido."""
    palabras = nombre.split()
    cantidad_letras = len(nombre.replace(" ", ""))

    return f"Nombre: {nombre}\nPalabras: {len(palabras)}\nLetras: {cantidad_letras}"

nombre_ingresado = input("Escribe tu nombre completo: ")
nombre_normalizado = normalizar_nombre(nombre_ingresado)
resumen = crear_resumen(nombre_normalizado)

print(resumen)
```

## 💡 Experimenta

Escribe el nombre con espacios al comienzo y al final, o mezclando mayúsculas y minúsculas. Después agrega al resumen la primera y la última letra.

---

# Parte II — Archivos

# 18. ¿Por qué necesitamos archivos?

Durante la ejecución podemos crear una lista:

```python
estudiantes = [
    {"nombre": "Ana", "nota": 4.5},
    {"nombre": "Luis", "nota": 3.8}
]

print(estudiantes)
```

Cuando el programa termina, esa lista deja de estar disponible. La **persistencia** permite conservar datos para utilizarlos en ejecuciones posteriores:

```text
Datos en memoria durante la ejecución
                 ↓
              Archivo
                 ↓
Información disponible posteriormente
```

---

# 19. Rutas y archivos

Un archivo tiene un nombre y normalmente una extensión:

```text
mensaje.txt
estudiantes.csv
datos.json
```

Una **ruta** indica su ubicación:

- Ruta relativa: parte de la carpeta de trabajo, por ejemplo `datos/estudiantes.json`.
- Ruta absoluta: describe la ubicación completa desde la raíz del sistema.

Los ejemplos usarán rutas relativas. Así pueden ejecutarse en diferentes computadores sin incluir rutas personales.

> La ruta relativa se interpreta a partir de la carpeta actual desde la que ejecutas Python, que no siempre coincide con la carpeta donde está el archivo `.py`.

---

# 20. Abrir archivos con `open()`

Utilizaremos desde el comienzo el patrón recomendado `with open(...)`:

```python
with open("mensaje.txt", "w", encoding="utf-8") as archivo:
    archivo.write("Hola, Python")
```

- `open()` abre el archivo.
- `"mensaje.txt"` es la ruta relativa.
- `"w"` es el modo de escritura.
- `encoding="utf-8"` indica la codificación del texto.
- `as archivo` asigna el archivo abierto a una variable.
- El bloque indentado indica dónde se utiliza.

`with` administra el cierre del archivo al terminar el bloque, incluso si no escribimos manualmente `close()`. No necesitamos estudiar todavía el funcionamiento interno de los administradores de contexto.

---

# 21. Escribir un archivo TXT

El método `write()` escribe una cadena:

```python
with open("mensaje.txt", "w", encoding="utf-8") as archivo:
    archivo.write("Hola, Python")

print("Archivo escrito")
```

El modo `"w"` crea el archivo si no existe. Si ya existe, **reemplaza todo su contenido**. Revisa siempre la ruta antes de utilizarlo.

`write()` devuelve la cantidad de caracteres escritos, aunque normalmente no necesitamos guardar ese resultado.

---

# 22. Leer un archivo TXT

El modo `"r"` abre para lectura y `read()` recupera todo el contenido:

```python
with open("mensaje.txt", "w", encoding="utf-8") as archivo:
    archivo.write("Hola, Python")

with open("mensaje.txt", "r", encoding="utf-8") as archivo:
    contenido = archivo.read()

print(contenido)
```

Primero creamos el archivo para garantizar que exista. Intentar leer un archivo inexistente produce un error que aprenderemos a manejar en la Unidad 6.

---

# 23. Agregar información

El modo `"a"` agrega al final sin borrar el contenido existente:

```python
with open("registro.txt", "w", encoding="utf-8") as archivo:
    archivo.write("Ana\n")

with open("registro.txt", "a", encoding="utf-8") as archivo:
    archivo.write("Luis\n")

with open("registro.txt", "r", encoding="utf-8") as archivo:
    print(archivo.read())
```

```text
"w" → escribe desde el comienzo y reemplaza el contenido.
"a" → agrega al final.
```

---

# 24. Escribir varias líneas

`write()` no agrega `\n` automáticamente:

```python
with open("notas.txt", "w", encoding="utf-8") as archivo:
    archivo.write("Ana: 4.5\n")
    archivo.write("Luis: 3.8\n")
```

`writelines()` recibe una colección de cadenas, pero tampoco agrega saltos automáticamente:

```python
lineas = ["Ana: 4.5\n", "Luis: 3.8\n", "Marta: 4.2\n"]

with open("notas.txt", "w", encoding="utf-8") as archivo:
    archivo.writelines(lineas)
```

Cada cadena incluye `\n` porque queremos que ocupe una línea diferente.

---

# 25. Leer líneas

## 25.1 `readline()`

Lee una línea cada vez:

```python
with open("notas.txt", "w", encoding="utf-8") as archivo:
    archivo.write("Ana: 4.5\nLuis: 3.8\n")

with open("notas.txt", "r", encoding="utf-8") as archivo:
    primera_linea = archivo.readline()
    segunda_linea = archivo.readline()

print(primera_linea.strip())
print(segunda_linea.strip())
```

## 25.2 `readlines()`

Devuelve una lista con todas las líneas:

```python
with open("notas.txt", "w", encoding="utf-8") as archivo:
    archivo.write("Ana: 4.5\nLuis: 3.8\n")

with open("notas.txt", "r", encoding="utf-8") as archivo:
    lineas = archivo.readlines()

print(lineas)
```

## 25.3 Recorrido directo

Cuando queremos procesar las líneas una por una, podemos recorrer el archivo:

```python
with open("notas.txt", "w", encoding="utf-8") as archivo:
    archivo.write("Ana: 4.5\nLuis: 3.8\n")

with open("notas.txt", "r", encoding="utf-8") as archivo:
    for linea in archivo:
        print(linea.strip())
```

`read()` es útil para todo el contenido, `readline()` para una línea, `readlines()` cuando necesitamos una lista y el recorrido directo para procesar progresivamente.

---

# 26. Modos de apertura

| Modo | Uso | Si el archivo no existe | Si existe |
|---|---|---|---|
| `"r"` | Leer | Produce un error | Conserva el contenido |
| `"w"` | Escribir | Lo crea | Reemplaza el contenido |
| `"a"` | Agregar | Lo crea | Conserva y escribe al final |
| `"x"` | Crear exclusivamente | Lo crea | Produce un error |

En esta unidad utilizaremos principalmente `r`, `w` y `a`. No trabajaremos todavía con archivos binarios.

---

# 27. Codificación UTF-8

La codificación establece cómo se representan los caracteres en el archivo. Utilizaremos explícitamente `encoding="utf-8"` para trabajar de forma consistente con tildes, `ñ` y otros caracteres:

```python
with open("saludo.txt", "w", encoding="utf-8") as archivo:
    archivo.write("¡Hola desde Bogotá! Año: 2026")

with open("saludo.txt", "r", encoding="utf-8") as archivo:
    print(archivo.read())
```

Debemos usar una codificación compatible tanto al escribir como al leer.

---

# 28. Organizar datos de texto

Podemos representar registros separados por comas:

```text
Ana,20,4.5
Luis,22,3.8
```

Después podemos separar cada línea:

```python
linea = "Ana,20,4.5"
datos = linea.split(",")

nombre = datos[0]
edad = int(datos[1])
nota = float(datos[2])

print(nombre, edad, nota)
```

Esta estrategia manual tiene limitaciones. Por ejemplo, un valor podría contener una coma. Para archivos CSV utilizaremos una herramienta especializada de Python.

---

# 29. Introducción a CSV

CSV significa *valores separados por comas*. Es un formato tabular de texto:

```text
nombre,edad,nota
Ana,20,4.5
Luis,22,3.8
```

Cada línea representa una fila y los separadores dividen sus campos. Aunque suele utilizar comas, el formato admite otras configuraciones mediante herramientas apropiadas.

---

# 30. El módulo `csv`

Python incluye un módulo especializado para CSV:

```python
import csv

print("El módulo csv está disponible")
```

`import` permite utilizar herramientas incluidas en un módulo. `csv` pertenece a la biblioteca estándar de Python y no requiere `pip`. El estudio detallado de módulos llegará más adelante.

---

# 31. Escribir CSV

`csv.writer()` crea un escritor y `writerow()` escribe una fila:

```python
import csv

with open("estudiantes.csv", "w", encoding="utf-8", newline="") as archivo:
    escritor = csv.writer(archivo)
    escritor.writerow(["nombre", "edad", "nota"])
    escritor.writerow(["Ana", 20, 4.5])
    escritor.writerow(["Luis", 22, 3.8])
```

`newline=""` permite que el módulo `csv` administre correctamente los finales de línea, especialmente entre sistemas operativos.

También podemos escribir varias filas con `writerows()`:

```python
import csv

filas = [
    ["nombre", "edad", "nota"],
    ["Ana", 20, 4.5],
    ["Luis", 22, 3.8]
]

with open("estudiantes.csv", "w", encoding="utf-8", newline="") as archivo:
    escritor = csv.writer(archivo)
    escritor.writerows(filas)
```

---

# 32. Leer CSV

`csv.reader()` permite recorrer las filas. Los valores leídos son cadenas:

```python
import csv

with open("estudiantes.csv", "w", encoding="utf-8", newline="") as archivo:
    escritor = csv.writer(archivo)
    escritor.writerow(["Ana", 20, 4.5])
    escritor.writerow(["Luis", 22, 3.8])

with open("estudiantes.csv", "r", encoding="utf-8", newline="") as archivo:
    lector = csv.reader(archivo)

    for fila in lector:
        nombre = fila[0]
        edad = int(fila[1])
        nota = float(fila[2])
        print(nombre, edad, nota)
```

Aunque se escribieron números, CSV es texto. Por eso convertimos `edad` y `nota` al leer.

---

# 33. CSV con encabezados

`DictWriter` escribe diccionarios utilizando nombres de campos:

```python
import csv

campos = ["nombre", "edad", "nota"]
estudiantes = [
    {"nombre": "Ana", "edad": 20, "nota": 4.5},
    {"nombre": "Luis", "edad": 22, "nota": 3.8}
]

with open("estudiantes.csv", "w", encoding="utf-8", newline="") as archivo:
    escritor = csv.DictWriter(archivo, fieldnames=campos)
    escritor.writeheader()
    escritor.writerows(estudiantes)
```

`DictReader` utiliza la primera fila como claves. Sus valores continúan siendo cadenas:

```python
import csv

campos = ["nombre", "edad", "nota"]
estudiantes = [
    {"nombre": "Ana", "edad": 20, "nota": 4.5},
    {"nombre": "Luis", "edad": 22, "nota": 3.8}
]

with open("estudiantes.csv", "w", encoding="utf-8", newline="") as archivo:
    escritor = csv.DictWriter(archivo, fieldnames=campos)
    escritor.writeheader()
    escritor.writerows(estudiantes)

with open("estudiantes.csv", "r", encoding="utf-8", newline="") as archivo:
    lector = csv.DictReader(archivo)

    for estudiante in lector:
        nombre = estudiante["nombre"]
        edad = int(estudiante["edad"])
        nota = float(estudiante["nota"])
        print(f"{nombre}: {edad} años, nota {nota}")
```

---

# 34. Introducción a JSON

JSON es un formato de texto que representa datos estructurados. Puede contener objetos, arreglos, textos, números, booleanos y valores nulos.

```text
{
    "nombre": "Ana",
    "edad": 20,
    "notas": [4.0, 3.5, 4.5]
}
```

Existe una relación conceptual:

```text
dict de Python ↔ objeto JSON
list de Python ↔ arreglo JSON
```

No son exactamente el mismo tipo: el diccionario y la lista existen durante la ejecución de Python; JSON es una representación textual con sus propias reglas.

---

# 35. El módulo `json`

El módulo `json` pertenece a la biblioteca estándar y no requiere instalación:

```python
import json

print("El módulo json está disponible")
```

---

# 36. Guardar datos en JSON

`json.dump()` transforma datos compatibles de Python y los escribe en un archivo:

```python
import json

estudiantes = [
    {"nombre": "Ana Pérez", "edad": 20, "nota": 4.5},
    {"nombre": "Muñoz", "edad": 22, "nota": 3.8}
]

with open("estudiantes.json", "w", encoding="utf-8") as archivo:
    json.dump(estudiantes, archivo, ensure_ascii=False, indent=4)
```

- `estudiantes`: datos que se guardarán.
- `archivo`: destino abierto para escritura.
- `ensure_ascii=False`: conserva caracteres como tildes y `ñ` de forma legible.
- `indent=4`: presenta el archivo con una indentación de cuatro espacios.

JSON admite tipos básicos como diccionarios, listas, cadenas, números, booleanos y `None`. Otros objetos de Python pueden no ser serializables directamente.

---

# 37. Leer datos JSON

`json.load()` lee desde un archivo y reconstruye estructuras de Python:

```python
import json

estudiantes = [
    {"nombre": "Ana", "edad": 20, "nota": 4.5},
    {"nombre": "Luis", "edad": 22, "nota": 3.8}
]

with open("estudiantes.json", "w", encoding="utf-8") as archivo:
    json.dump(estudiantes, archivo, ensure_ascii=False, indent=4)

with open("estudiantes.json", "r", encoding="utf-8") as archivo:
    estudiantes_recuperados = json.load(archivo)

for estudiante in estudiantes_recuperados:
    print(estudiante["nombre"], estudiante["nota"])
```

El ejemplo crea primero el archivo, así que la lectura no intenta abrir una ruta inexistente.

---

# 38. `dump()` frente a `dumps()`

Las funciones con `s` final trabajan con cadenas:

```python
import json

estudiante = {"nombre": "Ana", "nota": 4.5}
texto_json = json.dumps(estudiante, ensure_ascii=False, indent=4)
datos_recuperados = json.loads(texto_json)

print(type(texto_json))
print(type(datos_recuperados))
```

| Operación | Fuente o destino |
|---|---|
| `json.dump()` | Escribe JSON en un archivo |
| `json.load()` | Lee JSON desde un archivo |
| `json.dumps()` | Produce una cadena JSON |
| `json.loads()` | Interpreta una cadena JSON |

La `s` puede recordarnos que la operación trabaja con un *string*.

---

# 39. Introducción básica a `pathlib`

`pathlib` pertenece a la biblioteca estándar. Su clase `Path` permite representar y combinar rutas:

```python
from pathlib import Path

ruta = Path("datos") / "estudiantes.json"

print(ruta)
print(ruta.exists())
```

El operador `/` combina las partes de manera apropiada para el sistema operativo. `exists()` devuelve `True` si la ruta existe.

En los ejemplos sencillos guardaremos archivos en la carpeta actual. La ruta combinada muestra cómo organizaríamos una subcarpeta ya existente; no intentaremos abrirla sin crearla primero.

---

# 40. Ejemplo integrador — Estudiantes persistentes

Este ejemplo carga un archivo solamente si existe, agrega un registro y guarda la lista actualizada:

```python
import json
from pathlib import Path

def cargar_estudiantes(ruta):
    """Devuelve los estudiantes guardados o una lista vacía."""
    if not ruta.exists():
        return []

    with ruta.open("r", encoding="utf-8") as archivo:
        return json.load(archivo)

def guardar_estudiantes(ruta, estudiantes):
    """Guarda la lista de estudiantes en formato JSON."""
    with ruta.open("w", encoding="utf-8") as archivo:
        json.dump(estudiantes, archivo, ensure_ascii=False, indent=4)

def registrar_estudiante(estudiantes, nombre, edad, nota):
    """Agrega un estudiante a la lista recibida."""
    estudiante = {
        "nombre": nombre.strip().title(),
        "edad": edad,
        "nota": nota
    }
    estudiantes.append(estudiante)

ruta_datos = Path("estudiantes.json")
estudiantes = cargar_estudiantes(ruta_datos)

registrar_estudiante(estudiantes, "ana pérez", 20, 4.5)
guardar_estudiantes(ruta_datos, estudiantes)

print(f"Estudiantes guardados: {len(estudiantes)}")
```

`Path.open()` cumple el mismo propósito que `open()` y conserva el patrón `with`. No se intenta leer hasta comprobar `exists()`.

> Si ejecutas el ejemplo varias veces, agregará otro registro de Ana en cada ejecución. Modifícalo para solicitar datos o utiliza un archivo de práctica nuevo cuando quieras comenzar de nuevo.

---

# 41. Errores frecuentes

## 41.1 Intentar modificar un carácter

`texto[0] = "J"` produce un error porque `str` es inmutable. Construye una cadena nueva.

## 41.2 Olvidar que los índices comienzan en `0`

Para un texto de longitud `6`, el último índice positivo es `5`, no `6`.

## 41.3 Confundir `find()` con un booleano

`find()` devuelve un índice o `-1`. Para una respuesta booleana utiliza `fragmento in texto`.

## 41.4 Ignorar el `-1` de `find()`

Comprobar `if texto.find("Python"):` es problemático: el índice `0` se interpreta como falso y `-1` como verdadero. Compara el resultado con `-1` o usa `in`.

## 41.5 Esperar que `upper()` modifique la cadena

Los métodos de `str` devuelven una cadena nueva. Guarda el resultado: `texto = texto.upper()`.

## 41.6 Utilizar `isdigit()` para cualquier número

`"-5".isdigit()` y `"4.5".isdigit()` son `False`. Este método no valida por sí solo enteros negativos ni decimales.

## 41.7 Confundir `split()` y `join()`

`split()` parte una cadena y devuelve una lista. `join()` se llama desde el separador y une una colección de cadenas.

## 41.8 Olvidar `encoding="utf-8"`

La codificación predeterminada puede variar. Indícala explícitamente en todos los ejemplos de texto.

## 41.9 Utilizar `"w"` por accidente

El modo `w` reemplaza el contenido existente. Utiliza `a` cuando realmente quieras agregar al final y revisa la ruta antes de abrir.

## 41.10 Leer un archivo inexistente

El modo `r` produce un error si el archivo no existe. Hasta estudiar excepciones, créalo primero o comprueba `Path(...).exists()`.

## 41.11 Olvidar saltos de línea

Ni `write()` ni `writelines()` agregan `\n` automáticamente.

## 41.12 Trabajar con una ruta equivocada

Una ruta relativa parte de la carpeta actual de ejecución. Confirma desde qué carpeta ejecutaste Python y evita sobrescribir archivos importantes.

## 41.13 Confundir una ruta relativa con una absoluta

`"datos.json"` es relativa. Una ruta absoluta describe toda la ubicación y cambia entre equipos; por eso no usamos rutas personales en los ejemplos.

## 41.14 Confundir CSV y JSON

CSV representa principalmente filas y columnas. JSON representa estructuras anidadas con objetos y arreglos. Utiliza el módulo correspondiente.

## 41.15 Guardar objetos no serializables

`json.dump()` no puede convertir automáticamente cualquier objeto de Python. En esta unidad utiliza cadenas, números, booleanos, `None`, listas y diccionarios compatibles.

## 41.16 Suponer que CSV recupera números

`csv.reader` y `csv.DictReader` entregan los campos como cadenas. Convierte explícitamente con `int()` o `float()` cuando corresponda.

---

# 42. Ejercicios

No incluyas archivos reales del curso en tus pruebas. Trabaja en una carpeta de práctica.

## Ejercicio 1 — Índices

Solicita una palabra y muestra su primer y último carácter después de comprobar que no esté vacía.

## Ejercicio 2 — Slicing

Obtén distintas partes de `"programacion"`, los caracteres alternos y el texto invertido.

## Ejercicio 3 — Métodos

Normaliza un nombre con espacios y mayúsculas inconsistentes. Conserva también el texto original para compararlos.

## Ejercicio 4 — Búsqueda

Solicita una frase y una palabra. Utiliza `in`, `find()`, `rfind()` y `count()` para describir sus apariciones.

## Ejercicio 5 — Reemplazo

Reemplaza una palabra de una frase sin modificar la variable original.

## Ejercicio 6 — Dividir

Separa `"producto,precio,cantidad"` y accede a cada campo.

## Ejercicio 7 — Unir

Une una lista de palabras primero con espacios y después con guiones.

## Ejercicio 8 — Validaciones

Compara los resultados de `isdigit()`, `isalpha()`, `isalnum()` e `isspace()` con entradas diferentes. Explica sus límites.

## Ejercicio 9 — Formato

Muestra un promedio con dos decimales y un precio con separador de miles.

## Ejercicio 10 — Procesar nombres

Crea funciones para normalizar un nombre completo, contar sus palabras y producir un identificador sencillo.

## Ejercicio 11 — Escribir TXT

Escribe tres mensajes en líneas diferentes usando `with`, modo `w` y UTF-8.

## Ejercicio 12 — Leer TXT

Lee el archivo anterior con `read()` y muestra su contenido.

## Ejercicio 13 — Agregar contenido

Agrega otra línea con modo `a` y comprueba que las anteriores permanezcan.

## Ejercicio 14 — Procesar líneas

Recorre directamente un archivo de nombres, elimina `\n` con `strip()` y muestra una numeración.

## Ejercicio 15 — Escribir CSV

Guarda tres productos mediante `csv.writer()` y agrega una fila de encabezados.

## Ejercicio 16 — Leer CSV

Recorre el archivo anterior y convierte precio y cantidad antes de calcular cada total.

## Ejercicio 17 — Diccionarios y CSV

Guarda y recupera tres estudiantes con `DictWriter` y `DictReader`.

## Ejercicio 18 — Guardar JSON

Guarda una lista de diccionarios usando `ensure_ascii=False` e `indent=4`.

## Ejercicio 19 — Cargar JSON

Comprueba con `Path.exists()` que el archivo anterior exista, cárgalo y recorre sus registros.

---

# 43. Reto de la unidad — Sistema de estudiantes con persistencia

Amplía el sistema de estudiantes de la Unidad 4 para conservar los datos en `estudiantes.json`.

El menú debe ofrecer:

```text
1. Registrar estudiante
2. Mostrar estudiantes
3. Buscar estudiante
4. Calcular promedio general
5. Guardar datos
6. Cargar datos
7. Salir
```

## Requisitos

- Representa los registros con una lista de diccionarios.
- Separa cada responsabilidad en una función.
- Usa `Path("estudiantes.json")` para representar la ruta.
- Comprueba `exists()` antes de leer.
- Abre los archivos con `with` y `encoding="utf-8"`.
- Guarda mediante `json.dump(..., ensure_ascii=False, indent=4)`.
- Recupera mediante `json.load()`.
- Evita variables globales innecesarias: recibe listas y rutas como parámetros.
- Devuelve datos con `return` cuando otra parte del programa deba utilizarlos.
- Valida con `while` que cada nota esté entre `0.0` y `5.0`.
- Normaliza los nombres con métodos de cadena.
- Informa cuando no haya datos para mostrar o promediar.
- No utilices clases ni `try/except`.

Funciones posibles:

```text
registrar_estudiante(estudiantes)
mostrar_estudiantes(estudiantes)
buscar_estudiante(estudiantes, nombre_buscado)
calcular_promedio_general(estudiantes)
guardar_estudiantes(ruta, estudiantes)
cargar_estudiantes(ruta)
```

Construye y prueba primero las funciones de cálculo y búsqueda. Después agrega el guardado, la carga y finalmente el menú. No se incluye la solución completa para que puedas integrar lo aprendido.

---

# 44. Comprobación de aprendizaje

Antes de continuar, comprueba que puedes:

- [ ] Consultar caracteres mediante índices positivos y negativos.
- [ ] Obtener partes de una cadena mediante slicing.
- [ ] Explicar por qué `str` es inmutable.
- [ ] Transformar cadenas sin esperar que cambie la original.
- [ ] Buscar con pertenencia, `find()`, `rfind()` y `count()`.
- [ ] Dividir con `split()` y unir con `join()`.
- [ ] Explicar los límites de `isdigit()`.
- [ ] Formatear números mediante f-strings.
- [ ] Utilizar caracteres de escape y reconocer cadenas crudas.
- [ ] Explicar la diferencia entre datos en memoria y persistentes.
- [ ] Distinguir rutas relativas y absolutas.
- [ ] Utilizar `with open()` y UTF-8.
- [ ] Diferenciar los modos `r`, `w` y `a`.
- [ ] Escribir y leer contenido completo o por líneas.
- [ ] Explicar el comportamiento de `writelines()`.
- [ ] Escribir y leer CSV mediante la biblioteca estándar.
- [ ] Convertir los campos numéricos leídos desde CSV.
- [ ] Utilizar `DictWriter` y `DictReader`.
- [ ] Relacionar estructuras de Python con JSON sin confundir sus tipos.
- [ ] Guardar y cargar JSON mediante `dump()` y `load()`.
- [ ] Diferenciar `dump()` de `dumps()` y `load()` de `loads()`.
- [ ] Construir rutas y comprobar su existencia con `pathlib`.
- [ ] Guardar y recuperar una lista de diccionarios.

---

# 45. Lo que aprendimos

En esta unidad transformamos datos y aprendimos a conservarlos:

```text
Datos en memoria
       ↓
Procesamiento
       ↓
Texto estructurado
       ↓
Archivo
       ↓
Persistencia
       ↓
Recuperación de datos
```

Ahora podemos manipular cadenas, organizar texto y utilizar TXT, CSV y JSON según la estructura que necesitemos. También podemos comprobar una ruta antes de leerla y separar las operaciones en funciones.

Hasta ahora hemos evitado intencionalmente muchas operaciones que podrían fallar. En la Unidad 6 aprenderemos a responder correctamente ante esos fallos mediante excepciones.

---

# 🧭 Navegación

⬅️ [Volver a la Unidad 4 — Funciones](../unidad04-funciones/)

🏠 [Volver al inicio del curso](../README.md)

➡️ [Continuar a la Unidad 6 — Errores y excepciones](../unidad06-excepciones/)
