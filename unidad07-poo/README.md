# Unidad 7 — Programación orientada a objetos

En esta unidad aprenderás a representar entidades mediante objetos que reúnen datos y comportamiento. Estudiaremos POO fundamental; la herencia y otros mecanismos avanzados pertenecen a la Unidad 8.

---

## 🎯 Objetivos de aprendizaje

Al finalizar podrás crear clases y objetos, inicializar atributos, escribir métodos, comprender `self`, aplicar encapsulamiento básico, componer objetos y transformar su información para guardarla en JSON.

---

## 📋 Antes de comenzar

Utilizaremos funciones, colecciones, archivos, JSON y excepciones. No usaremos herencia, polimorfismo, clases abstractas, mixins, `dataclass` ni patrones de diseño.

---

# 1. ¿Por qué programación orientada a objetos?

Hasta ahora podíamos representar un estudiante así:

```python
estudiante = {
    "nombre": "Ana",
    "edad": 20,
    "programa": "Ingeniería de Sistemas"
}
```

El diccionario funciona. Cuando además necesitamos mostrar, calcular, actualizar y validar información, un objeto puede reunir:

```text
datos + comportamiento
```

POO no es siempre mejor que diccionarios y funciones. Es otro enfoque útil cuando datos y operaciones forman una entidad clara.

---

# 2. ¿Qué es una clase?

Una clase define características y comportamientos para determinados objetos:

```python
class Estudiante:
    pass
```

- `class` inicia la definición.
- `Estudiante` usa la convención `PascalCase`.
- `:` abre el bloque indentado.
- `pass` permite un bloque vacío válido.

Una analogía útil es pensar en un modelo, pero una clase es concretamente una definición de Python con la que crearemos objetos.

---

# 3. Objetos e instancias

```python
class Estudiante:
    pass

estudiante_1 = Estudiante()
estudiante_2 = Estudiante()

print(estudiante_1 is estudiante_2)
```

`Estudiante` es la clase. Cada llamada crea un objeto o **instancia** diferente; el resultado es `False`.

---

# 4. Primeros atributos

Un atributo guarda información asociada al objeto:

```python
class Estudiante:
    pass

estudiante = Estudiante()
estudiante.nombre = "Ana"

print(estudiante.nombre)
```

Esto sirve como puente, pero normalmente queremos establecer el estado inicial de forma organizada.

---

# 5. Inicializar con `__init__()`

```python
class Estudiante:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

estudiante = Estudiante("Ana", 20)
print(estudiante.nombre, estudiante.edad)
```

`__init__()` se ejecuta automáticamente al crear la instancia e inicializa sus datos. Informalmente se llama constructor, aunque técnicamente inicializa una instancia que ya fue creada. No necesitamos estudiar `__new__` todavía.

---

# 6. Comprender `self`

`self` representa la instancia sobre la que trabaja el método:

```python
class Estudiante:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

estudiante_1 = Estudiante("Ana", 20)
estudiante_2 = Estudiante("Luis", 22)

print(estudiante_1.nombre)
print(estudiante_2.nombre)
```

Cada objeto conserva sus propios atributos. Al llamar mediante un objeto, Python proporciona esa instancia como primer argumento del método.

`self` no es una palabra reservada, pero es la convención universal y debemos utilizarla.

---

# 7. Atributos de instancia

```python
class Estudiante:
    def __init__(self, nombre, edad, programa):
        self.nombre = nombre
        self.edad = edad
        self.programa = programa

estudiante = Estudiante("Ana", 20, "Sistemas")
print(estudiante.nombre)

estudiante.edad = 21
print(estudiante.edad)
```

Hasta este punto son accesibles y modificables directamente.

---

# 8. Métodos de instancia

Un método es una función definida dentro de una clase y trabaja en el contexto de sus objetos:

```python
class Estudiante:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def mostrar_informacion(self):
        print(f"{self.nombre}: {self.edad} años")

estudiante = Estudiante("Ana", 20)
estudiante.mostrar_informacion()
```

No pasamos `self` manualmente en la llamada normal.

---

# 9. Métodos con parámetros adicionales

```python
class Estudiante:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def actualizar_edad(self, nueva_edad):
        self.edad = nueva_edad

estudiante = Estudiante("Ana", 20)
estudiante.actualizar_edad(21)
print(estudiante.edad)
```

`self` identifica el objeto y `nueva_edad` recibe el argumento adicional.

---

# 10. Métodos que devuelven valores

```python
class Estudiante:
    def __init__(self, edad):
        self.edad = edad

    def es_mayor_edad(self):
        return self.edad >= 18

estudiante = Estudiante(20)
resultado = estudiante.es_mayor_edad()
print(resultado)
```

`return` entrega el resultado; `print()` solo lo muestra.

---

# 11. Estado y comportamiento

```text
Estudiante
├── estado: nombre, edad, notas
└── comportamiento: agregar_nota(), calcular_promedio(), mostrar_informacion()
```

Los atributos forman el estado actual. Los métodos describen operaciones relacionadas con ese estado.

---

# 12. Colecciones como atributos

```python
class Estudiante:
    def __init__(self, nombre):
        self.nombre = nombre
        self.notas = []

    def agregar_nota(self, nota):
        self.notas.append(nota)

    def calcular_promedio(self):
        if not self.notas:
            return 0.0
        return sum(self.notas) / len(self.notas)

estudiante = Estudiante("Ana")
estudiante.agregar_nota(4.0)
estudiante.agregar_nota(4.5)
print(estudiante.calcular_promedio())
```

---

# 13. Cuidado con valores mutables predeterminados

No utilices este patrón:

```text
def __init__(self, notas=[]):
    self.notas = notas
```

La misma lista predeterminada podría compartirse entre instancias. Usa `None` y crea una lista para cada objeto:

```python
class Estudiante:
    def __init__(self, nombre, notas=None):
        self.nombre = nombre
        self.notas = [] if notas is None else list(notas)

estudiante_1 = Estudiante("Ana")
estudiante_2 = Estudiante("Luis")
estudiante_1.notas.append(4.5)

print(estudiante_1.notas)
print(estudiante_2.notas)
```

`is None` comprueba específicamente la identidad del objeto único `None`. `list(notas)` crea una copia básica de los valores recibidos.

---

# 14. Atributos de clase

```python
class Estudiante:
    institucion = "Universidad Central"

    def __init__(self, nombre):
        self.nombre = nombre

estudiante_1 = Estudiante("Ana")
estudiante_2 = Estudiante("Luis")

print(estudiante_1.institucion)
print(estudiante_2.institucion)
```

`institucion` pertenece a la clase y se comparte como valor común. `nombre` pertenece a cada instancia.

---

# 15. Modificar atributos de clase

```python
class Estudiante:
    institucion = "Universidad Central"

    def __init__(self, nombre):
        self.nombre = nombre

estudiante_1 = Estudiante("Ana")
estudiante_2 = Estudiante("Luis")

Estudiante.institucion = "Nueva Universidad"
estudiante_1.institucion = "Institución particular"

print(estudiante_1.institucion)
print(estudiante_2.institucion)
print(Estudiante.institucion)
```

Asignar mediante la clase cambia el valor compartido. Asignar mediante `estudiante_1` crea un atributo de instancia que **sombrea** el de clase solo para ese objeto.

---

# 16. Contador de instancias

```python
class Estudiante:
    cantidad = 0

    def __init__(self, nombre):
        self.nombre = nombre
        Estudiante.cantidad += 1

estudiante_1 = Estudiante("Ana")
estudiante_2 = Estudiante("Luis")

print(Estudiante.cantidad)
```

Es un ejemplo pedagógico de estado compartido, no un patrón obligatorio.

---

# 17. Encapsulamiento

El encapsulamiento busca organizar y controlar cómo se consulta o modifica el estado interno. Python utiliza convenciones y propiedades; no ofrece aquí privacidad estricta equivalente a la de algunos lenguajes.

---

# 18. Convención de atributo interno `_`

```python
class Cuenta:
    def __init__(self, saldo):
        self._saldo = saldo

    def consultar_saldo(self):
        return self._saldo

cuenta = Cuenta(50000)
print(cuenta.consultar_saldo())
```

El guion bajo inicial comunica “uso interno”. No impide técnicamente `cuenta._saldo`.

---

# 19. *Name mangling* con `__`

```python
class Cuenta:
    def __init__(self, saldo):
        self.__saldo = saldo

    def consultar_saldo(self):
        return self.__saldo

cuenta = Cuenta(50000)
print(cuenta.consultar_saldo())
```

Python transforma internamente el nombre para reducir colisiones y accesos accidentales. No es seguridad ni privacidad absoluta.

---

# 20. Getters y setters tradicionales

```python
class Estudiante:
    def __init__(self, edad):
        self._edad = edad

    def obtener_edad(self):
        return self._edad

    def establecer_edad(self, edad):
        if edad < 0:
            raise ValueError("La edad no puede ser negativa")
        self._edad = edad
```

Funcionan, pero Python ofrece una interfaz más idiomática mediante propiedades.

---

# 21. `@property`

```python
class Estudiante:
    def __init__(self, edad):
        self._edad = edad

    @property
    def edad(self):
        return self._edad

estudiante = Estudiante(20)
print(estudiante.edad)
```

Consultamos `estudiante.edad` sin llamar explícitamente `obtener_edad()`.

---

# 22. Setter con `@property`

```python
class Estudiante:
    def __init__(self, edad):
        self._edad = edad

    @property
    def edad(self):
        return self._edad

    @edad.setter
    def edad(self, valor):
        if valor < 0:
            raise ValueError("La edad no puede ser negativa")
        self._edad = valor

estudiante = Estudiante(20)
estudiante.edad = 21
print(estudiante.edad)
```

El setter controla la asignación y aprovecha `raise` de la Unidad 6.

---

# 23. Validar desde `__init__()`

Podemos evitar duplicar la regla usando la propiedad al inicializar:

```python
class Estudiante:
    def __init__(self, edad):
        self.edad = edad

    @property
    def edad(self):
        return self._edad

    @edad.setter
    def edad(self, valor):
        if valor < 0:
            raise ValueError("La edad no puede ser negativa")
        self._edad = valor

estudiante = Estudiante(20)
print(estudiante.edad)
```

Tanto la creación como cambios posteriores pasan por la misma validación.

---

# 24. Representación con `__str__()`

Sin personalización, `print(estudiante)` muestra una representación técnica que incluye clase e identidad. Podemos definir una representación amigable:

```python
class Estudiante:
    def __init__(self, nombre, programa):
        self.nombre = nombre
        self.programa = programa

    def __str__(self):
        return f"{self.nombre} - {self.programa}"

estudiante = Estudiante("Ana", "Sistemas")
print(estudiante)
```

`print()` utiliza `__str__()` y este debe devolver una cadena.

---

# 25. Métodos especiales

Nombres como `__init__` y `__str__` se denominan métodos especiales o *dunder methods*. Python los utiliza en operaciones concretas. Estudiaremos más en POO avanzada.

Dejaremos `__repr__` para la Unidad 8: conceptualmente, `__str__` busca una presentación amigable y `__repr__` una representación más útil para desarrollo.

---

# 26. Composición básica

Un objeto puede contener otros objetos:

```python
class Estudiante:
    def __init__(self, nombre):
        self.nombre = nombre

class Curso:
    def __init__(self, nombre):
        self.nombre = nombre
        self.estudiantes = []

    def agregar_estudiante(self, estudiante):
        self.estudiantes.append(estudiante)

curso = Curso("Python")
curso.agregar_estudiante(Estudiante("Ana"))

print(curso.estudiantes[0].nombre)
```

Un curso “tiene” estudiantes. No necesitamos herencia para expresar esta relación.

---

# 27. Listas de objetos

```python
class Estudiante:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

estudiantes = [Estudiante("Ana", 20), Estudiante("Luis", 22)]

for estudiante in estudiantes:
    print(estudiante.nombre)
```

Es similar a recorrer una lista de diccionarios, pero cada elemento ofrece atributos y métodos definidos por su clase.

---

# 28. Diccionario frente a objeto

| Aspecto | Diccionario | Objeto |
|---|---|---|
| Acceso | `estudiante["nombre"]` | `estudiante.nombre` |
| Estructura | Flexible | Definida por una clase |
| Comportamiento | Funciones externas | Métodos relacionados |
| Costo inicial | Menor | Requiere diseñar una clase |

Un diccionario puede ser ideal para datos simples o dinámicos. Un objeto puede ayudar cuando existe una entidad estable con reglas y comportamiento. Ninguno es siempre mejor.

---

# 29. Funciones frente a métodos

```text
calcular_promedio(estudiante)
estudiante.calcular_promedio()
```

Una función recibe explícitamente los datos. Un método agrupa el comportamiento con el objeto y recibe la instancia mediante `self`.

---

# 30. Identidad de objetos

`is` pregunta si dos nombres representan exactamente el mismo objeto; `==` compara valores según las reglas del tipo:

```python
class Estudiante:
    def __init__(self, nombre):
        self.nombre = nombre

estudiante_1 = Estudiante("Ana")
estudiante_2 = estudiante_1
estudiante_3 = Estudiante("Ana")

print(estudiante_1 is estudiante_2)
print(estudiante_1 is estudiante_3)
```

No uses `is` para comparar números o cadenas por valor; utiliza `==`. No personalizaremos `__eq__` todavía.

---

# 31. Referencias y copias

```python
class Estudiante:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

estudiante_1 = Estudiante("Ana", 20)
estudiante_2 = estudiante_1
estudiante_2.edad = 21

print(estudiante_1.edad)
print(estudiante_2.edad)
```

Ambos nombres hacen referencia al mismo objeto. `otra_variable = objeto` no crea una copia independiente. Las copias avanzadas se estudiarán después.

---

# 32. Ejemplo integrador — Clase `Estudiante`

```python
class Estudiante:
    def __init__(self, nombre, edad, programa, notas=None):
        self.nombre = nombre.strip().title()
        self.edad = edad
        self.programa = programa.strip().title()
        self.notas = [] if notas is None else list(notas)

    @property
    def edad(self):
        return self._edad

    @edad.setter
    def edad(self, valor):
        if valor < 0:
            raise ValueError("La edad no puede ser negativa")
        self._edad = valor

    def agregar_nota(self, nota):
        if nota < 0.0 or nota > 5.0:
            raise ValueError("La nota debe estar entre 0.0 y 5.0")
        self.notas.append(nota)

    def calcular_promedio(self):
        if not self.notas:
            return 0.0
        return sum(self.notas) / len(self.notas)

    def es_mayor_edad(self):
        return self.edad >= 18

    def esta_aprobado(self):
        return self.calcular_promedio() >= 3.0

    def __str__(self):
        return f"{self.nombre} - {self.programa} - promedio {self.calcular_promedio():.2f}"

estudiante = Estudiante(" ana pérez ", 20, " sistemas ")
estudiante.agregar_nota(4.0)
estudiante.agregar_nota(3.5)

print(estudiante)
print(estudiante.es_mayor_edad())
print(estudiante.esta_aprobado())
```

## 💡 Experimenta

Crea otro objeto y agrega notas diferentes. Después intenta asignar una edad negativa dentro de `try/except`.

---

# 33. Ejemplo integrador — Clase `Curso`

```python
class Estudiante:
    def __init__(self, nombre, nota):
        self.nombre = nombre
        self.nota = nota

    def __str__(self):
        return f"{self.nombre}: {self.nota}"

class Curso:
    def __init__(self, nombre):
        self.nombre = nombre
        self.estudiantes = []

    def agregar_estudiante(self, estudiante):
        self.estudiantes.append(estudiante)

    def buscar_estudiante(self, nombre):
        for estudiante in self.estudiantes:
            if estudiante.nombre == nombre:
                return estudiante
        return None

    def calcular_promedio_general(self):
        if not self.estudiantes:
            return 0.0
        suma = 0.0
        for estudiante in self.estudiantes:
            suma += estudiante.nota
        return suma / len(self.estudiantes)

    def mostrar_estudiantes(self):
        for estudiante in self.estudiantes:
            print(estudiante)

curso = Curso("Python")
curso.agregar_estudiante(Estudiante("Ana", 4.5))
curso.agregar_estudiante(Estudiante("Luis", 3.8))

curso.mostrar_estudiantes()
print(curso.buscar_estudiante("Ana"))
print(f"Promedio: {curso.calcular_promedio_general():.2f}")
```

---

# 34. Persistencia de objetos

`json.dump()` no guarda directamente cualquier objeto personalizado. Debemos transformarlo a tipos compatibles:

```python
class Estudiante:
    def __init__(self, nombre, edad, notas=None):
        self.nombre = nombre
        self.edad = edad
        self.notas = [] if notas is None else list(notas)

    def to_dict(self):
        return {"nombre": self.nombre, "edad": self.edad, "notas": self.notas.copy()}

estudiante = Estudiante("Ana", 20, [4.0, 4.5])
print(estudiante.to_dict())
```

Para reconstruir sin introducir `@classmethod`:

```python
class Estudiante:
    def __init__(self, nombre, edad, notas=None):
        self.nombre = nombre
        self.edad = edad
        self.notas = [] if notas is None else list(notas)

datos = {"nombre": "Ana", "edad": 20, "notas": [4.0, 4.5]}
estudiante = Estudiante(datos["nombre"], datos["edad"], datos["notas"])

print(estudiante.nombre)
```

---

# 35. Guardar y cargar objetos con JSON

```python
import json
from pathlib import Path

class Estudiante:
    def __init__(self, nombre, edad, notas=None):
        self.nombre = nombre
        self.edad = edad
        self.notas = [] if notas is None else list(notas)

    def to_dict(self):
        return {"nombre": self.nombre, "edad": self.edad, "notas": self.notas.copy()}

ruta = Path("estudiantes.json")
estudiantes = [
    Estudiante("Ana", 20, [4.0, 4.5]),
    Estudiante("Luis", 22, [3.5, 3.8])
]
datos = [estudiante.to_dict() for estudiante in estudiantes]

with ruta.open("w", encoding="utf-8") as archivo:
    json.dump(datos, archivo, ensure_ascii=False, indent=4)

with ruta.open("r", encoding="utf-8") as archivo:
    datos_recuperados = json.load(archivo)

estudiantes_recuperados = []
for datos_estudiante in datos_recuperados:
    estudiante = Estudiante(
        datos_estudiante["nombre"],
        datos_estudiante["edad"],
        datos_estudiante["notas"]
    )
    estudiantes_recuperados.append(estudiante)

for estudiante in estudiantes_recuperados:
    print(estudiante.nombre)
```

```text
objetos → diccionarios → JSON
JSON → diccionarios → objetos
```

---

# 36. Errores frecuentes

- Confundir la clase con sus objetos.
- Olvidar `self` en la definición de un método o pasarlo manualmente en una llamada normal.
- Omitir `__init__` o escribirlo incorrectamente, por ejemplo `_init_`.
- Nombrar clases con `snake_case` en lugar de `PascalCase`.
- Compartir una lista usando `notas=[]` como valor predeterminado.
- Confundir atributos de clase con atributos de instancia.
- Modificar directamente un atributo que debería validarse mediante una propiedad.
- Creer que `_atributo` es privado o que `__atributo` ofrece seguridad absoluta.
- Olvidar `return` en un método de cálculo o sustituirlo por `print()`.
- Crear clases sin una razón clara y asumir que siempre superan a un diccionario.
- Utilizar `is` para comparar valores en lugar de `==`.
- Creer que `otra_variable = objeto` crea una copia independiente.

---

# 37. Ejercicios

1. Define una primera clase vacía y crea dos objetos.
2. Agrega atributos manualmente y consúltalos.
3. Define `__init__()` para un producto.
4. Demuestra con dos instancias cómo actúa `self`.
5. Crea un método sin parámetros adicionales que muestre información.
6. Crea un método que actualice un precio.
7. Crea un método que devuelva el total de una compra.
8. Crea una clase con una lista propia por instancia.
9. Agrega y valida notas entre `0.0` y `5.0`.
10. Crea un atributo de clase compartido.
11. Compara ese atributo con uno de instancia.
12. Utiliza `_saldo` como convención de estado interno.
13. Crea una propiedad de lectura para una edad.
14. Agrega un setter que rechace edades negativas.
15. Reutiliza el setter desde `__init__()`.
16. Implementa `__str__()` en una clase Producto.
17. Recorre una lista de objetos y llama un método.
18. Compón una clase Biblioteca que contenga objetos Libro.
19. Implementa `to_dict()` en Estudiante.
20. Reconstruye un objeto desde un diccionario.
21. Guarda una lista de objetos transformados en JSON.
22. Carga JSON y reconstruye los objetos.

No consultes soluciones completas; prueba cada paso antes de continuar.

---

# 38. Reto de la unidad — Sistema de estudiantes orientado a objetos

Crea al menos las clases `Estudiante` y `Curso`.

`Estudiante` tendrá nombre, edad, programa y notas; validará sus datos e incluirá `agregar_nota()`, `calcular_promedio()`, `esta_aprobado()`, `to_dict()` y `__str__()`.

`Curso` tendrá nombre y estudiantes, con `agregar_estudiante()`, `buscar_estudiante()`, `mostrar_estudiantes()` y `calcular_promedio_general()`.

El menú debe permitir registrar estudiantes, agregar notas, mostrar, buscar, calcular el promedio general, guardar en JSON, cargar desde JSON y salir.

Requisitos:

- Utiliza objetos y listas de objetos.
- Aplica propiedades donde una asignación necesite validación.
- Evita listas mutables como argumentos predeterminados.
- Transforma objetos a diccionarios antes de guardar.
- Reconstruye objetos explícitamente al cargar.
- Maneja errores de entrada y archivos con conocimientos de la Unidad 6.
- No utilices herencia, `@classmethod`, `dataclass`, clases abstractas ni bibliotecas externas.

Construye y prueba una clase cada vez. No se entrega la solución completa.

---

# 39. Comprobación de aprendizaje

- [ ] Distingo clase, objeto e instancia.
- [ ] Utilizo `PascalCase`, `__init__()` y `self` correctamente.
- [ ] Creo atributos y métodos de instancia.
- [ ] Distingo estado y comportamiento.
- [ ] Uso listas como atributos sin compartir valores predeterminados.
- [ ] Diferencio atributos de clase e instancia.
- [ ] Explico encapsulamiento, `_` y *name mangling* sin hablar de privacidad absoluta.
- [ ] Creo propiedades y setters con validación.
- [ ] Implemento `__str__()`.
- [ ] Trabajo con listas de objetos y composición básica.
- [ ] Comparo diccionarios, objetos, funciones y métodos.
- [ ] Distingo identidad con `is` de comparación por valor con `==`.
- [ ] Comprendo que una asignación no copia un objeto.
- [ ] Transformo objetos a diccionarios y los reconstruyo desde JSON.

---

# 40. Lo que aprendimos

```text
Datos separados
      ↓
Clase
      ↓
Objetos con estado
      ↓
Métodos con comportamiento
      ↓
Encapsulamiento básico
      ↓
Composición y persistencia
```

Ahora podemos representar entidades mediante clases y objetos sin asumir que este enfoque sustituye todas las demás herramientas.

En la Unidad 8 profundizaremos en POO con herencia, polimorfismo, composición avanzada y otros mecanismos.

---

# 🧭 Navegación

⬅️ [Volver a la Unidad 6 — Errores y excepciones](../unidad06-excepciones/)

🏠 [Volver al inicio del curso](../README.md)

➡️ [Continuar a la Unidad 8 — POO avanzada](../unidad08-poo-avanzada/)
