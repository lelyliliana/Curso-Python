# Unidad 8 — Programación orientada a objetos avanzada

[Volver al índice del curso](../README.md) · [Ver el curso en Aprende con Leli](https://lelyliliana.github.io/aprende-con-leli/cursos/python/)

En la Unidad 7 aprendimos a crear objetos con estado y comportamiento. Ahora estudiaremos relaciones entre clases y formas de integrarlas mejor con Python.

---

## 🎯 Objetivos de aprendizaje

Al finalizar podrás aplicar herencia, sobrescritura, polimorfismo, abstracción, composición, métodos de clase y estáticos, métodos especiales y excepciones personalizadas, evaluando cuándo aportan claridad.

---

## 📋 Antes de comenzar

Necesitas dominar POO fundamental y excepciones. No utilizaremos paquetes propios, `dataclass`, testing formal, metaclases, descriptores personalizados, protocolos ni frameworks.

---

# 1. ¿Qué significa POO avanzada?

```text
Clase → Objeto → Estado + comportamiento
                         ↓
Herencia → Sobrescritura → Polimorfismo → Abstracción
                         ↓
             Composición y diseños flexibles
```

Más herencia no significa automáticamente mejor diseño. Cada herramienta debe resolver una necesidad real.

---

# 2. Herencia

```python
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def presentarse(self):
        return f"Soy {self.nombre}"

class Estudiante(Persona):
    pass
```

`Persona` es la clase base y `Estudiante` la derivada. La relación conceptual es “Estudiante **es una** Persona”. La clase derivada hereda atributos y métodos.

---

# 3. Objetos derivados y comportamiento adicional

```python
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def presentarse(self):
        return f"Soy {self.nombre}"

class Estudiante(Persona):
    def estudiar(self):
        return f"{self.nombre} está estudiando"

estudiante = Estudiante("Ana", 20)
print(estudiante.edad)
print(estudiante.presentarse())
print(estudiante.estudiar())
```

`__init__()` y `presentarse()` son heredados; `estudiar()` es propio.

---

# 4. Sobrescritura de métodos

```python
class Persona:
    def presentarse(self):
        return "Soy una persona"

class Estudiante(Persona):
    def presentarse(self):
        return "Soy estudiante"

print(Estudiante().presentarse())
```

La implementación derivada **sobrescribe** la heredada para especializar el comportamiento.

---

# 5. Reutilizar con `super()`

```python
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def presentarse(self):
        return f"Soy {self.nombre}"

class Estudiante(Persona):
    def __init__(self, nombre, edad, programa):
        super().__init__(nombre, edad)
        self.programa = programa

    def presentarse(self):
        informacion_base = super().presentarse()
        return f"{informacion_base}. Estudio {self.programa}"

print(Estudiante("Ana", 20, "Sistemas").presentarse())
```

`super()` sigue el orden de resolución de métodos y permite reutilizar o extender comportamiento sin repetirlo. En herencia simple conduce a la implementación base correspondiente.

---

# 6. `isinstance()` e `issubclass()`

```python
class Persona:
    pass

class Estudiante(Persona):
    pass

estudiante = Estudiante()

print(isinstance(estudiante, Estudiante))
print(isinstance(estudiante, Persona))
print(issubclass(Estudiante, Persona))
```

Los tres resultados son `True`: una instancia derivada también pertenece conceptualmente al tipo base.

---

# 7. Polimorfismo

```python
class Persona:
    def presentarse(self):
        return "Persona"

class Estudiante(Persona):
    def presentarse(self):
        return "Soy estudiante"

class Docente(Persona):
    def presentarse(self):
        return "Soy docente"

personas = [Estudiante(), Docente()]

for persona in personas:
    print(persona.presentarse())
```

La misma operación produce el comportamiento apropiado según el objeto.

---

# 8. Duck typing

Python también permite polimorfismo sin una herencia común:

```python
class Libro:
    def describir(self):
        return "Libro de Python"

class Curso:
    def describir(self):
        return "Curso de Python"

def mostrar_descripcion(objeto):
    print(objeto.describir())

mostrar_descripcion(Libro())
mostrar_descripcion(Curso())
```

Si el objeto ofrece el comportamiento necesario, podemos usarlo. La herencia expresa una relación explícita; duck typing prioriza la capacidad. No siempre necesitamos una jerarquía para compartir una operación.

---

# 9. Clases abstractas y abstracción

Una clase abstracta define **qué** comportamiento deben ofrecer sus derivadas sin decidir todos los detalles de **cómo**:

```python
from abc import ABC, abstractmethod

class Persona(ABC):
    @abstractmethod
    def obtener_rol(self):
        pass

class Estudiante(Persona):
    def obtener_rol(self):
        return "Estudiante"

estudiante = Estudiante()
print(estudiante.obtener_rol())
```

`abc` pertenece a la biblioteca estándar. Una clase con métodos abstractos pendientes no puede instanciarse. Una derivada concreta debe implementarlos.

---

# 10. Herencia múltiple y MRO

Python permite heredar de varias clases, aunque aumenta la complejidad:

```python
class Identificable:
    def describir(self):
        return "Identificable"

class Registrable:
    def describir(self):
        return "Registrable"

class Recurso(Identificable, Registrable):
    pass

recurso = Recurso()
print(recurso.describir())
print([clase.__name__ for clase in Recurso.mro()])
```

El MRO (*Method Resolution Order*) indica dónde busca Python los métodos. `super()` avanza siguiendo ese orden, no significa simplemente “padre directo”. No profundizaremos en el algoritmo C3 ni fomentaremos jerarquías complejas.

---

# 11. Composición

```python
class Motor:
    def encender(self):
        return "Motor encendido"

class Vehiculo:
    def __init__(self):
        self.motor = Motor()

    def iniciar(self):
        return self.motor.encender()

print(Vehiculo().iniciar())
```

Un vehículo **tiene un** motor. En cambio, Estudiante **es una** Persona. Estas frases ayudan, pero no sustituyen el análisis del problema.

Heredar solo para reutilizar líneas genera acoplamiento innecesario. Si una clase simplemente necesita usar otra capacidad, la composición suele ser más natural.

---

# 12. Métodos de clase

```python
class Estudiante:
    institucion = "Universidad"

    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    @classmethod
    def cambiar_institucion(cls, nueva_institucion):
        cls.institucion = nueva_institucion

    @classmethod
    def desde_dict(cls, datos):
        return cls(datos["nombre"], datos["edad"])

Estudiante.cambiar_institucion("Universidad Central")
estudiante = Estudiante.desde_dict({"nombre": "Ana", "edad": 20})

print(estudiante.nombre)
print(Estudiante.institucion)
```

`self` representa una instancia; `cls`, la clase. `desde_dict()` funciona como constructor alternativo y mejora la reconstrucción desde JSON.

---

# 13. Métodos estáticos

```python
class Estudiante:
    @staticmethod
    def nota_valida(nota):
        return 0.0 <= nota <= 5.0

print(Estudiante.nota_valida(4.5))
```

Un método estático no recibe automáticamente `self` ni `cls`; pertenece conceptualmente al dominio de la clase.

| Tipo | Primer valor automático | Uso principal |
|---|---|---|
| Instancia | `self` | Trabajar con un objeto |
| `@classmethod` | `cls` | Trabajar con la clase o crear alternativas |
| `@staticmethod` | Ninguno | Operación relacionada con la clase |

Si no existe relación clara con la clase, una función normal puede ser mejor.

---

# 14. Métodos especiales

Python utiliza métodos especiales para integrar objetos con operaciones del lenguaje:

```python
class Estudiante:
    def __init__(self, codigo, nombre):
        self.codigo = codigo
        self.nombre = nombre

    def __str__(self):
        return f"{self.nombre} ({self.codigo})"

    def __repr__(self):
        return f"Estudiante(codigo={self.codigo!r}, nombre={self.nombre!r})"

estudiante = Estudiante("E001", "Ana")
print(str(estudiante))
print(repr(estudiante))
```

`__str__` busca una representación legible; `__repr__`, una útil para desarrollo.

---

# 15. `__len__`, `__contains__` e `__iter__`

```python
class Curso:
    def __init__(self):
        self.estudiantes = []

    def agregar(self, estudiante):
        self.estudiantes.append(estudiante)

    def __len__(self):
        return len(self.estudiantes)

    def __contains__(self, estudiante):
        return estudiante in self.estudiantes

    def __iter__(self):
        return iter(self.estudiantes)

curso = Curso()
curso.agregar("Ana")

print(len(curso))
print("Ana" in curso)

for estudiante in curso:
    print(estudiante)
```

`__iter__` permite recorrer sin profundizar todavía en el protocolo de iteradores, que veremos en la Unidad 11.

---

# 16. Igualdad y comparación

```python
class Estudiante:
    def __init__(self, codigo, promedio):
        self.codigo = codigo
        self.promedio = promedio

    def __eq__(self, other):
        if not isinstance(other, Estudiante):
            return NotImplemented
        return self.codigo == other.codigo

    def __lt__(self, other):
        if not isinstance(other, Estudiante):
            return NotImplemented
        return self.promedio < other.promedio

estudiante_1 = Estudiante("E001", 4.0)
estudiante_2 = Estudiante("E001", 4.5)

print(estudiante_1 == estudiante_2)
print(estudiante_1 < estudiante_2)
```

Usamos un código, no el nombre, como identidad del dominio. `NotImplemented` indica que la operación no sabe comparar ese otro tipo y permite que Python intente el comportamiento apropiado.

No implementes métodos especiales solo porque existen: la operación debe tener significado natural y devolver el tipo esperado.

---

# 17. Excepciones personalizadas

```python
class NotaInvalidaError(ValueError):
    pass

def validar_nota(nota):
    if not 0.0 <= nota <= 5.0:
        raise NotaInvalidaError("La nota debe estar entre 0.0 y 5.0")

try:
    validar_nota(7.0)
except NotaInvalidaError as error:
    print(error)
```

Una excepción personalizada hereda de una existente y representa un error propio del dominio. No necesitamos una clase distinta para cada pequeño fallo.

---

# 18. Ejemplo integrador — Personas universitarias

```python
from abc import ABC, abstractmethod

class Persona(ABC):
    def __init__(self, codigo, nombre):
        self.codigo = codigo
        self.nombre = nombre

    @abstractmethod
    def obtener_rol(self):
        pass

    def presentarse(self):
        return f"Soy {self.nombre} y mi rol es {self.obtener_rol()}"

class Estudiante(Persona):
    def __init__(self, codigo, nombre, programa, notas=None):
        super().__init__(codigo, nombre)
        self.programa = programa
        self.notas = [] if notas is None else list(notas)

    def obtener_rol(self):
        return "Estudiante"

    def calcular_promedio(self):
        return sum(self.notas) / len(self.notas) if self.notas else 0.0

class Docente(Persona):
    def __init__(self, codigo, nombre, area):
        super().__init__(codigo, nombre)
        self.area = area

    def obtener_rol(self):
        return "Docente"

personas = [
    Estudiante("E001", "Ana", "Sistemas", [4.0, 4.5]),
    Docente("D001", "Laura", "Programación")
]

for persona in personas:
    print(persona.presentarse())
```

El recorrido demuestra abstracción, herencia, `super()`, sobrescritura y polimorfismo.

---

# 19. Ejemplo integrador — Curso por composición

```python
class Curso:
    def __init__(self, codigo, nombre, docente):
        self.codigo = codigo
        self.nombre = nombre
        self.docente = docente
        self.estudiantes = []

    def agregar_estudiante(self, estudiante):
        if estudiante in self.estudiantes:
            raise ValueError("El estudiante ya está registrado")
        self.estudiantes.append(estudiante)

    def __len__(self):
        return len(self.estudiantes)

    def __iter__(self):
        return iter(self.estudiantes)

docente = "Laura"
curso = Curso("PY01", "Python", docente)
curso.agregar_estudiante("Ana")

for estudiante in curso:
    print(estudiante)
print(len(curso))
```

Curso tiene docente y estudiantes; no hereda de ellos.

---

# 20. Persistencia mejorada

```python
import json
from pathlib import Path

class Estudiante:
    def __init__(self, codigo, nombre):
        self.codigo = codigo
        self.nombre = nombre

    def to_dict(self):
        return {"codigo": self.codigo, "nombre": self.nombre}

    @classmethod
    def desde_dict(cls, datos):
        return cls(datos["codigo"], datos["nombre"])

class Curso:
    def __init__(self, codigo, estudiantes=None):
        self.codigo = codigo
        self.estudiantes = [] if estudiantes is None else list(estudiantes)

    def to_dict(self):
        return {
            "codigo": self.codigo,
            "estudiantes": [estudiante.to_dict() for estudiante in self.estudiantes]
        }

    @classmethod
    def desde_dict(cls, datos):
        estudiantes = [Estudiante.desde_dict(item) for item in datos["estudiantes"]]
        return cls(datos["codigo"], estudiantes)

ruta = Path("curso.json")
curso = Curso("PY01", [Estudiante("E001", "Ana")])

with ruta.open("w", encoding="utf-8") as archivo:
    json.dump(curso.to_dict(), archivo, ensure_ascii=False, indent=4)

with ruta.open("r", encoding="utf-8") as archivo:
    curso_recuperado = Curso.desde_dict(json.load(archivo))

print(curso_recuperado.estudiantes[0].nombre)
```

No construimos un sistema de serialización: transformamos explícitamente objetos, diccionarios y JSON.

---

# 21. Principios introductorios de diseño

- Una clase debe tener una responsabilidad comprensible.
- Evita clases gigantes y jerarquías profundas.
- No heredes solo para reutilizar unas líneas.
- Favorece relaciones claras y composición natural.
- Encapsula reglas importantes y usa nombres descriptivos.

---

# 22. Sobrecarga: una aclaración

Python no conserva métodos con el mismo nombre y firmas diferentes como Java o C++. En el mismo ámbito, una segunda definición reemplaza la primera.

**No utilizar como sobrecarga:**

```text
def calcular(a):
    ...

def calcular(a, b):
    ...
```

Podemos usar parámetros predeterminados o `*args`. Existen técnicas de *dispatch* más avanzadas, pero no las veremos aquí. Sobrescritura significa redefinir un método heredado; no es lo mismo que sobrecarga.

---

# 23. Errores frecuentes

- Heredar sin una relación conceptual clara o crear jerarquías profundas.
- Olvidar `super().__init__()` y dejar incompleta la inicialización.
- Repetir inicialización que ya ofrece la base.
- Pensar que `super()` siempre significa “padre directo” e ignorar el MRO.
- Confundir sobrescritura con sobrecarga por firma.
- Instanciar una clase abstracta incompleta u olvidar `@abstractmethod`.
- Abusar de herencia múltiple sin revisar `Clase.mro()`.
- Usar `staticmethod` cuando una función normal es más clara.
- Usar `classmethod` cuando la operación necesita `self`.
- Implementar `__eq__` sin comprobar el tipo ni devolver `NotImplemented`.
- Devolver tipos incorrectos desde métodos especiales.
- Implementar métodos especiales sin significado natural.
- Confundir composición con herencia.
- Crear excepciones personalizadas innecesarias.

---

# 24. Ejercicios

1. Crea herencia simple entre Persona y Estudiante.
2. Usa un método heredado.
3. Agrega comportamiento a la derivada.
4. Sobrescribe `presentarse()`.
5. Extiende inicialización y presentación con `super()`.
6. Comprueba `isinstance()` e `issubclass()`.
7. Recorre objetos polimórficos.
8. Practica duck typing con dos clases independientes.
9. Define una clase base con `ABC`.
10. Implementa un `abstractmethod` en dos derivadas.
11. Compón Vehículo con Motor.
12. Justifica herencia o composición para tres relaciones.
13. Cambia un atributo con `@classmethod`.
14. Crea `desde_dict()` como constructor alternativo.
15. Valida una nota con `@staticmethod`.
16. Implementa `__repr__()`.
17. Integra una clase con `len()`.
18. Compara objetos por código mediante `__eq__()`.
19. Permite recorrer Curso con `__iter__()`.
20. Crea y captura una excepción de dominio.
21. Guarda y recupera objetos usando `desde_dict()`.
22. Refactoriza una jerarquía artificial usando composición.
23. Inspecciona el MRO de una herencia múltiple sencilla.
24. Agrega `__contains__()` solo donde tenga significado natural.

No incluyas soluciones completas; prueba cada cambio.

---

# 25. Reto de la unidad — Sistema académico orientado a objetos

Construye `Persona` abstracta con código, nombre, `obtener_rol()` y `presentarse()`. Deriva `Estudiante` y `Docente`.

`Estudiante` tendrá programa, notas, validación, promedio, rol, `to_dict()` y `desde_dict()`. `Docente` tendrá área, rol y los mismos métodos de persistencia.

`Curso` tendrá código, nombre, docente y estudiantes; incluirá agregar, buscar, promedio general, `__len__`, `__iter__`, `to_dict()` y `desde_dict()`.

Además:

- Crea una excepción específica para notas inválidas.
- Demuestra polimorfismo al presentar personas.
- Usa composición entre Curso, Docente y Estudiantes.
- Guarda y carga JSON con manejo de excepciones.
- No uses paquetes externos, `dataclass`, módulos propios separados ni bases de datos.

Desarrolla una clase cada vez y no consultes una solución completa.

---

# 26. Comprobación de aprendizaje

- [ ] Aplico herencia, sobrescritura y `super()` con criterio.
- [ ] Uso `isinstance()`, `issubclass()` y comprendo el MRO.
- [ ] Explico polimorfismo y duck typing.
- [ ] Creo clases abstractas y métodos abstractos.
- [ ] Distingo “es un” de “tiene un” sin usarlo como regla mecánica.
- [ ] Elijo composición cuando expresa mejor la relación.
- [ ] Distingo métodos de instancia, clase y estáticos.
- [ ] Creo constructores alternativos.
- [ ] Implemento métodos especiales con significado natural.
- [ ] Comprendo `NotImplemented` en comparaciones.
- [ ] Creo excepciones personalizadas solo para errores del dominio.
- [ ] Persisto y reconstruyo objetos mediante diccionarios y JSON.
- [ ] Evito jerarquías y abstracciones innecesarias.

---

# 27. Lo que aprendimos

```text
POO fundamental
      ↓
Relaciones entre clases
      ↓
Polimorfismo y abstracción
      ↓
Composición
      ↓
Objetos integrados con Python
      ↓
Diseños más flexibles
```

La Unidad 9 organizará el código en módulos, paquetes y proyectos. Estas herramientas permitirán distribuir clases y responsabilidades sin mantener todo en un solo archivo.

---

# 🧭 Navegación

⬅️ [Volver a la Unidad 7 — Programación orientada a objetos](../unidad07-poo/)

🏠 [Volver al inicio del curso](../README.md)

➡️ [Continuar a la Unidad 9 — Módulos y proyectos](../unidad09-modulos-proyectos/)


---

## Continuar el curso

- **Unidad anterior:** [Unidad 7 — Programación orientada a objetos](../unidad07-poo/README.md)
- **Volver al índice:** [Todas las unidades](../README.md)
- **Siguiente unidad:** [Unidad 9 — Módulos, paquetes y organización de proyectos](../unidad09-modulos-proyectos/README.md)
