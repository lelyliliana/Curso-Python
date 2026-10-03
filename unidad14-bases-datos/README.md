# Unidad 14 — Bases de datos con Python y SQLite

[Volver al índice del curso](../README.md) · [Ver el curso en Aprende con Leli](https://lelyliliana.github.io/aprende-con-leli/cursos/python/)

Hasta ahora hemos guardado información en TXT, CSV y JSON. En esta unidad aprenderás a conservar y consultar datos estructurados mediante una base de datos relacional, SQL, SQLite y el módulo `sqlite3` de Python.

---

## 🎯 Objetivos de aprendizaje

Al finalizar podrás:

- Explicar tablas, filas, columnas, claves primarias y relaciones básicas.
- Crear una base SQLite y ejecutar SQL desde Python.
- Realizar operaciones `INSERT`, `SELECT`, `UPDATE` y `DELETE`.
- Filtrar, ordenar y resumir información.
- Utilizar parámetros SQL para datos dinámicos.
- Controlar transacciones con `commit()` y `rollback()`.
- Mapear filas a dataclasses sin utilizar un ORM.
- Separar persistencia, modelo y flujo principal.
- Probar operaciones con bases temporales y aisladas.

---

## 📋 Antes de comenzar

Necesitas haber completado la Unidad 13. Utilizaremos archivos, excepciones, módulos, context managers, type hints, dataclasses y pytest.

SQLite y `sqlite3` no requieren un servidor ni una instalación mediante `pip`. No estudiaremos todavía ORM, SQLAlchemy, PostgreSQL, MySQL, migraciones, concurrencia de base de datos, APIs ni frameworks web.

---

# 1. Archivos y bases de datos

Con un archivo solemos cargar y procesar datos manualmente:

```text
Archivo → datos completos → procesamiento en Python
```

Una base permite pedir solo los registros necesarios:

```text
Base de datos → consulta → datos seleccionados
```

Una base de datos facilita búsquedas, filtros, orden, actualizaciones, eliminaciones y restricciones estructurales. No siempre es mejor: un TXT pequeño de configuración o un JSON de intercambio pueden ser más simples. La elección depende del volumen, las consultas y las reglas de persistencia.

---

# 2. Modelo relacional

Una base relacional organiza información en tablas:

```text
Base de datos
└── tablas
    ├── filas
    └── columnas
```

Tabla `estudiantes`:

| id | nombre | edad | programa |
|---:|---|---:|---|
| 1 | Ana | 20 | Ingeniería |
| 2 | Luis | 22 | Sistemas |

- Una **fila** representa un registro.
- Una **columna** representa un atributo o campo.
- Una **clave primaria** identifica cada fila de manera única.

Una fila puede recordarnos un diccionario, dataclass u objeto, pero no son equivalentes: la tabla vive en la base y Python crea representaciones durante la ejecución.

---

# 3. SQL y SQLite

SQL es el lenguaje utilizado para definir estructuras y consultar o modificar datos relacionales. Sus instrucciones principales en esta unidad serán:

```text
CREATE TABLE → crear una tabla
INSERT       → agregar filas
SELECT       → consultar filas
UPDATE       → modificar filas
DELETE       → eliminar filas
```

SQLite es un motor embebido que normalmente guarda una base completa en un archivo y no necesita servidor separado. Resulta adecuado para aprender, crear prototipos y muchas aplicaciones locales. Motores cliente-servidor ofrecen otras capacidades para sistemas distribuidos y alta concurrencia, temas que no abordaremos aquí.

---

# 4. El módulo `sqlite3`

`sqlite3` pertenece a la biblioteca estándar:

```python
import sqlite3

print(sqlite3.sqlite_version)
```

No requiere `pip`. Una conexión representa una sesión con la base:

```python
import sqlite3

conexion = sqlite3.connect(":memory:")
print(type(conexion))
conexion.close()
```

`:memory:` crea una base temporal que existe mientras esa conexión permanece abierta. Es útil para demostraciones y ciertas pruebas.

---

# 5. Conexiones y `with`: una precisión importante

El objeto conexión funciona como context manager:

```python
import sqlite3

conexion = sqlite3.connect(":memory:")
try:
    with conexion:
        conexion.execute("CREATE TABLE ejemplo (id INTEGER PRIMARY KEY)")
finally:
    conexion.close()
```

El bloque `with conexion:` confirma la transacción si termina correctamente y la revierte ante una excepción. **No garantiza por sí mismo cerrar la conexión al salir**, a diferencia de `with open(...)`. Por eso el ejemplo llama `close()` en `finally`.

Más adelante construiremos un context manager propio que controle `commit`, `rollback` y cierre.

---

# 6. Cursores y primera tabla

Un cursor ejecuta sentencias y recupera resultados:

```python
import sqlite3

conexion = sqlite3.connect(":memory:")
try:
    cursor = conexion.cursor()
    cursor.execute(
        """
        CREATE TABLE estudiantes (
            id INTEGER PRIMARY KEY,
            nombre TEXT NOT NULL,
            edad INTEGER NOT NULL,
            programa TEXT NOT NULL
        )
        """
    )
    conexion.commit()
finally:
    conexion.close()
```

- `CREATE TABLE` define una tabla.
- `INTEGER`, `TEXT` y otras palabras declaran afinidades de tipo.
- `NOT NULL` impide ausencia en una columna.
- `PRIMARY KEY` exige una identificación única.

Para una inicialización repetible utilizamos `IF NOT EXISTS`:

```sql
CREATE TABLE IF NOT EXISTS estudiantes (
    id INTEGER PRIMARY KEY,
    nombre TEXT NOT NULL
)
```

---

# 7. Tipos de datos en SQLite

SQLite utiliza cinco clases de almacenamiento principales:

- `INTEGER`: enteros.
- `REAL`: números de punto flotante.
- `TEXT`: texto.
- `BLOB`: datos binarios.
- `NULL`: ausencia de valor.

SQLite tiene tipado dinámico y afinidad de tipos; no se comporta exactamente como motores más estrictos. `NULL` en SQL suele convertirse en `None` al llegar a Python. La cadena `"NULL"` es texto y no representa ausencia.

---

# 8. Insertar datos con parámetros

`INSERT` agrega una fila. Los signos `?` son placeholders:

```python
import sqlite3

conexion = sqlite3.connect(":memory:")
try:
    conexion.execute(
        """
        CREATE TABLE estudiantes (
            id INTEGER PRIMARY KEY,
            nombre TEXT NOT NULL,
            edad INTEGER NOT NULL,
            programa TEXT NOT NULL
        )
        """
    )
    cursor = conexion.execute(
        """
        INSERT INTO estudiantes (nombre, edad, programa)
        VALUES (?, ?, ?)
        """,
        ("Ana", 20, "Ingeniería"),
    )
    conexion.commit()
    print(cursor.lastrowid)
finally:
    conexion.close()
```

La sentencia SQL y los valores viajan separados. La tupla tiene un elemento por placeholder. `lastrowid` permite consultar el id generado tras el `INSERT`.

En SQLite, `INTEGER PRIMARY KEY` se vincula al `rowid` y genera un valor cuando omitimos el id. `AUTOINCREMENT` modifica reglas de reutilización y normalmente no es necesario.

---

# 9. No concatenar datos dentro del SQL

Este patrón es **inseguro y no debe ejecutarse como solución**:

```text
sql = "SELECT * FROM estudiantes WHERE nombre = '" + nombre + "'"
```

Concatenar input o usar f-strings para valores puede romper la consulta con caracteres especiales y permite **SQL injection**: datos manipulados alteran la estructura prevista de la sentencia.

La prevención básica consiste en parametrizar:

```python
import sqlite3

conexion = sqlite3.connect(":memory:")
try:
    conexion.execute("CREATE TABLE estudiantes (nombre TEXT NOT NULL)")
    conexion.execute(
        "INSERT INTO estudiantes (nombre) VALUES (?)",
        ("Ana",),
    )
    fila = conexion.execute(
        "SELECT nombre FROM estudiantes WHERE nombre = ?",
        ("Ana",),
    ).fetchone()
    print(fila)
finally:
    conexion.close()
```

Los parámetros protegen **valores**, no nombres de tablas o columnas. En este curso esos identificadores permanecerán escritos en el código, no vendrán directamente del usuario.

---

# 10. Transacciones, `commit()` y `rollback()`

Una transacción agrupa operaciones que deben confirmarse juntas:

```text
inicio → operaciones → ¿todo correcto?
                       ↙            ↘
                     sí              no
                      ↓               ↓
                   commit          rollback
```

`commit()` confirma cambios. `rollback()` revierte la transacción pendiente:

```python
import sqlite3

conexion = sqlite3.connect(":memory:")
try:
    conexion.execute("CREATE TABLE productos (nombre TEXT NOT NULL)")
    try:
        conexion.execute(
            "INSERT INTO productos (nombre) VALUES (?)",
            ("Teclado",),
        )
        raise ValueError("Operación incompleta")
    except ValueError:
        conexion.rollback()
    cantidad = conexion.execute("SELECT COUNT(*) FROM productos").fetchone()[0]
    print(cantidad)
finally:
    conexion.close()
```

El resultado es `0`: la inserción no quedó confirmada. Las transacciones contribuyen a mantener cambios coherentes; no profundizaremos aún en todas las propiedades ACID.

---

# 11. Consultar con `SELECT`

Prefiere nombrar las columnas cuando conoces lo que necesitas:

```sql
SELECT id, nombre, edad, programa
FROM estudiantes
```

`SELECT *` es útil para exploración, pero puede traer datos innecesarios y oculta qué columnas espera el código.

```python
import sqlite3

conexion = sqlite3.connect(":memory:")
try:
    conexion.execute("CREATE TABLE estudiantes (id INTEGER PRIMARY KEY, nombre TEXT)")
    conexion.executemany(
        "INSERT INTO estudiantes (nombre) VALUES (?)",
        [("Ana",), ("Luis",)],
    )
    conexion.commit()

    cursor = conexion.execute("SELECT id, nombre FROM estudiantes ORDER BY id")
    primera_fila = cursor.fetchone()
    filas_restantes = cursor.fetchall()
    print(primera_fila)
    print(filas_restantes)
finally:
    conexion.close()
```

- `fetchone()` devuelve una fila o `None` si no queda ninguna.
- `fetchall()` devuelve una lista con las filas restantes.

Para grandes resultados podemos recorrer el cursor progresivamente:

```python
import sqlite3

conexion = sqlite3.connect(":memory:")
try:
    conexion.execute("CREATE TABLE numeros (valor INTEGER)")
    conexion.executemany("INSERT INTO numeros (valor) VALUES (?)", [(1,), (2,), (3,)])
    for fila in conexion.execute("SELECT valor FROM numeros ORDER BY valor"):
        print(fila[0])
finally:
    conexion.close()
```

---

# 12. Filtrar con `WHERE`

`WHERE` limita las filas según una condición:

```sql
SELECT id, nombre, edad, programa
FROM estudiantes
WHERE id = ?
```

Operadores básicos: `=`, `!=`, `>`, `<`, `>=` y `<=`. Podemos combinar condiciones con `AND` y `OR`:

```sql
SELECT id, nombre
FROM estudiantes
WHERE edad >= ? AND programa = ?
```

Los valores siguen siendo parámetros, aunque sean números.

---

# 13. Búsqueda, orden y límite

`LIKE` permite búsquedas textuales. `%` representa cualquier secuencia de caracteres:

```python
import sqlite3

conexion = sqlite3.connect(":memory:")
try:
    conexion.execute("CREATE TABLE estudiantes (id INTEGER PRIMARY KEY, nombre TEXT)")
    conexion.executemany(
        "INSERT INTO estudiantes (nombre) VALUES (?)",
        [("Ana",), ("Mariana",), ("Luis",)],
    )
    filas = conexion.execute(
        """
        SELECT id, nombre
        FROM estudiantes
        WHERE nombre LIKE ?
        ORDER BY nombre ASC
        LIMIT ?
        """,
        ("%Ana%", 2),
    ).fetchall()
    print(filas)
finally:
    conexion.close()
```

`ASC` ordena ascendentemente y `DESC` descendentemente. SQLite admite un parámetro para `LIMIT`; conviene validar en la aplicación que la cantidad tenga sentido.

---

# 14. Agregaciones básicas

Las funciones agregadas resumen varias filas:

```python
import sqlite3

conexion = sqlite3.connect(":memory:")
try:
    conexion.execute("CREATE TABLE notas (valor REAL)")
    conexion.executemany(
        "INSERT INTO notas (valor) VALUES (?)",
        [(4.0,), (3.5,), (4.5,)],
    )
    fila = conexion.execute(
        "SELECT COUNT(*), AVG(valor), MIN(valor), MAX(valor) FROM notas"
    ).fetchone()
    print(fila)
finally:
    conexion.close()
```

- `COUNT(*)` cuenta filas.
- `AVG()` calcula un promedio.
- `MIN()` y `MAX()` obtienen extremos.

Este es solo un primer contacto con SQL, no un recorrido exhaustivo.

---

# 15. Actualizar con `UPDATE`

```python
import sqlite3

conexion = sqlite3.connect(":memory:")
try:
    conexion.execute("CREATE TABLE estudiantes (id INTEGER PRIMARY KEY, edad INTEGER)")
    conexion.execute("INSERT INTO estudiantes (edad) VALUES (?)", (20,))
    conexion.execute(
        "UPDATE estudiantes SET edad = ? WHERE id = ?",
        (21, 1),
    )
    conexion.commit()
    print(conexion.execute("SELECT edad FROM estudiantes WHERE id = ?", (1,)).fetchone())
finally:
    conexion.close()
```

El `WHERE` selecciona qué filas cambiar. Esta sentencia, mostrada solo como advertencia, afectaría **todas** las filas:

```text
UPDATE estudiantes
SET edad = 20
```

Antes de actualizar, comprueba siempre si el alcance es el esperado.

---

# 16. Eliminar con `DELETE`

```python
import sqlite3

conexion = sqlite3.connect(":memory:")
try:
    conexion.execute("CREATE TABLE estudiantes (id INTEGER PRIMARY KEY, nombre TEXT)")
    conexion.execute("INSERT INTO estudiantes (nombre) VALUES (?)", ("Ana",))
    conexion.execute("DELETE FROM estudiantes WHERE id = ?", (1,))
    conexion.commit()
    print(conexion.execute("SELECT COUNT(*) FROM estudiantes").fetchone()[0])
finally:
    conexion.close()
```

`DELETE FROM estudiantes` sin `WHERE` eliminaría todas las filas. No lo ejecutes accidentalmente.

---

# 17. CRUD y separación de responsabilidades

CRUD reúne cuatro operaciones:

```text
Create → INSERT
Read   → SELECT
Update → UPDATE
Delete → DELETE
```

En el proyecto real, la persistencia se expresa mediante funciones:

```text
crear_estudiante()
listar_estudiantes()
buscar_estudiante_por_id()
actualizar_estudiante()
eliminar_estudiante()
```

`database.py` contiene SQL; `estudiantes.py` contiene el modelo; `main.py` coordina una demostración. La interacción con el usuario no debe mezclarse con cada consulta.

---

# 18. Filas con nombres mediante `sqlite3.Row`

Los índices como `fila[1]` dependen de recordar el orden. Podemos configurar:

```python
import sqlite3

conexion = sqlite3.connect(":memory:")
conexion.row_factory = sqlite3.Row
try:
    conexion.execute("CREATE TABLE estudiantes (id INTEGER PRIMARY KEY, nombre TEXT)")
    conexion.execute("INSERT INTO estudiantes (nombre) VALUES (?)", ("Ana",))
    fila = conexion.execute("SELECT id, nombre FROM estudiantes").fetchone()
    if fila is not None:
        print(fila["nombre"])
finally:
    conexion.close()
```

`sqlite3.Row` permite acceso por nombre sin perder el acceso por posición.

---

# 19. Mapear una fila a una dataclass

El proyecto define:

```python
from dataclasses import dataclass

@dataclass
class Estudiante:
    id: int | None
    nombre: str
    edad: int
    programa: str
```

Después realiza el mapeo manual:

```python
from estudiantes import Estudiante

fila = {
    "id": 1,
    "nombre": "Ana",
    "edad": 20,
    "programa": "Ingeniería",
}

estudiante = Estudiante(
    id=fila["id"],
    nombre=fila["nombre"],
    edad=fila["edad"],
    programa=fila["programa"],
)

print(estudiante)
```

Al crear un objeto antes de insertarlo, `id` es `None`; la base genera el entero. Esto no es un ORM: escribimos SQL y conversión explícitamente. Los ORM, como SQLAlchemy, automatizan parte de ese trabajo, pero aprender SQL primero ayuda a comprender lo que ocurre.

---

# 20. Restricciones e integridad

Las restricciones protegen reglas también en la base:

```sql
CREATE TABLE notas (
    id INTEGER PRIMARY KEY,
    valor REAL NOT NULL CHECK (valor >= 0 AND valor <= 5),
    codigo TEXT UNIQUE
)
```

- `NOT NULL` impide ausencia.
- `UNIQUE` evita valores repetidos.
- `CHECK` exige una condición.

La validación de aplicación ofrece mensajes y experiencia de uso; las restricciones defienden la integridad aunque otro código acceda a la base. Se complementan.

Una violación puede producir `sqlite3.IntegrityError`:

```python
import sqlite3

conexion = sqlite3.connect(":memory:")
try:
    conexion.execute("CREATE TABLE notas (valor REAL CHECK (valor BETWEEN 0 AND 5))")
    try:
        conexion.execute("INSERT INTO notas (valor) VALUES (?)", (6.0,))
        conexion.commit()
    except sqlite3.IntegrityError as error:
        conexion.rollback()
        print(f"Dato rechazado: {error}")
finally:
    conexion.close()
```

`sqlite3.Error` agrupa errores del módulo, pero captura una excepción más específica cuando puedas responder a ella. No ocultes el fallo con `except sqlite3.Error: pass`.

---

# 21. Relaciones y claves foráneas

Una relación uno a muchos apropiada puede ser:

```text
Programa 1 ───── N Estudiantes
```

La columna `programa_id` de estudiantes puede referirse a la clave primaria de programas. Una **foreign key** ayuda a impedir referencias inexistentes.

En SQLite, la comprobación debe habilitarse en **cada conexión**:

```python
import sqlite3

conexion = sqlite3.connect(":memory:")
try:
    conexion.execute("PRAGMA foreign_keys = ON")
    estado = conexion.execute("PRAGMA foreign_keys").fetchone()[0]
    print(estado)
finally:
    conexion.close()
```

Estudiante y curso suelen formar una relación muchos a muchos:

```text
estudiantes ──< matriculas >── cursos
```

La tabla intermedia contiene las claves de ambos. Evitar datos redundantes mediante tablas y relaciones se relaciona con **normalización**; no estudiaremos todavía sus formas normales.

---

# 22. Context manager propio

El proyecto controla el ciclo completo de la conexión:

```python
import sqlite3
from collections.abc import Iterator
from contextlib import contextmanager
from pathlib import Path

@contextmanager
def obtener_conexion(
    ruta_db: str | Path,
) -> Iterator[sqlite3.Connection]:
    conexion = sqlite3.connect(ruta_db)
    conexion.row_factory = sqlite3.Row
    conexion.execute("PRAGMA foreign_keys = ON")
    try:
        yield conexion
        conexion.commit()
    except Exception:
        conexion.rollback()
        raise
    finally:
        conexion.close()
```

Si el bloque termina bien, confirma; si falla, revierte y vuelve a propagar; al final, cierra siempre. Una conexión global complicaría el ciclo de vida, las pruebas y la recuperación ante errores, por eso pasamos la ruta a cada función. No es una prohibición universal, sino una decisión clara para este proyecto.

---

# 23. Proyecto SQLite real

```text
proyecto_sqlite/
├── database.py
├── estudiantes.py
├── main.py
└── tests/
    └── test_database.py
```

El esquema utiliza `INTEGER PRIMARY KEY`, columnas explícitas y un `CHECK` para edad. Todas las funciones CRUD usan parámetros para valores dinámicos, `WHERE` en actualizaciones y eliminaciones, y `sqlite3.Row` para mapear resultados.

Ejecuta manualmente desde la raíz del ejemplo:

```bash
cd unidad14-bases-datos/ejemplos/proyecto_sqlite
python main.py
```

Esto crea `estudiantes.db` en esa carpeta y demuestra crear, listar, buscar, actualizar y eliminar. El archivo solo aparece cuando tú ejecutas `main.py`; importarlo no hace nada porque utiliza `if __name__ == "__main__":`.

Para comenzar nuevamente, elimina únicamente tu base de práctica después de comprobar su ruta. La validación de esta unidad no ejecuta `main.py` dentro del repositorio.

---

# 24. Pruebas con una base temporal

Las pruebas utilizan `tmp_path`:

```python
from pathlib import Path

import pytest

from database import inicializar_db

@pytest.fixture
def ruta_db(tmp_path: Path) -> Path:
    ruta = tmp_path / "test.db"
    inicializar_db(ruta)
    return ruta
```

Cada prueba recibe una ruta aislada y no toca `estudiantes.db`. La suite comprueba inicialización, id generado, lista, búsquedas, actualización, eliminación, restricciones, rollback y persistencia entre conexiones.

Desde `proyecto_sqlite/`:

```bash
python -m pytest -v
```

No compartas una base real entre pruebas ni hagas que una dependa de la ejecución anterior.

## Base en memoria o archivo temporal

`:memory:` es excelente si toda la prueba usa la misma conexión. Si una función abre y cierra conexiones independientes, cada `sqlite3.connect(":memory:")` recibe normalmente una base distinta. `tmp_path / "test.db"` permite comprobar persistencia entre conexiones manteniendo aislamiento.

---

# 25. Seguridad básica

- Parametriza siempre los valores dinámicos.
- No insertes input mediante concatenación o f-strings SQL.
- No guardes contraseñas en texto plano.
- No incluyas credenciales en código o repositorios.
- Revisa el alcance de `UPDATE` y `DELETE` antes de ejecutarlos.

SQLite local no necesita credenciales en este ejemplo. La seguridad completa de una aplicación incluye más aspectos que no abordaremos todavía.

---

# 26. Rendimiento, índices y evolución

Un índice puede acelerar búsquedas frecuentes:

```sql
CREATE INDEX idx_estudiantes_nombre
ON estudiantes(nombre)
```

También ocupa espacio y añade costo a escrituras. No crees índices innecesarios ni optimices antes de medir. SQLite ofrece `EXPLAIN QUERY PLAN` para inspeccionar planes como ampliación opcional.

Cuando cambia un proyecto real, su esquema necesita evolucionar de forma controlada mediante **migraciones**. Solo anticipamos el concepto; no utilizaremos Alembic ni otra herramienta en esta unidad.

---

# 27. Errores frecuentes

- Olvidar `commit()` y perder cambios pendientes.
- Olvidar cerrar conexiones o creer que `with sqlite3.connect(...)` las cierra automáticamente.
- Mantener una conexión global que dificulta pruebas y ciclo de vida.
- Construir SQL con input, concatenación o f-strings en lugar de parámetros.
- Creer que parametrizar nombres de tablas funciona igual que parametrizar valores.
- Usar siempre `SELECT *` sin considerar las columnas necesarias.
- Confundir `fetchone()` con `fetchall()` o asumir que `fetchone()` nunca devuelve `None`.
- Omitir `WHERE` en `UPDATE` o `DELETE`.
- Usar rutas relativas distintas y crear varias bases sin advertirlo.
- Confundir `None` de Python con el texto `"NULL"`.
- Esperar el mismo tipado estricto de otros motores.
- Usar `AUTOINCREMENT` sin necesitar sus reglas particulares.
- Olvidar `PRAGMA foreign_keys = ON` en cada conexión que use claves foráneas.
- Capturar `sqlite3.Error` y ocultarlo sin recuperar ni propagar.
- Usar la base real en pruebas, compartir estado o dejar conexiones abiertas.
- Saltar directamente a un ORM sin comprender SQL básico.

---

# 28. Ejercicios

## Ejercicio 1 — Crear una base

Abre una base de práctica en una carpeta temporal, imprime el tipo de conexión y ciérrala explícitamente.

## Ejercicio 2 — Crear una tabla

Crea `productos` con id, nombre, precio y cantidad. Añade `NOT NULL` donde corresponda.

## Ejercicio 3 — Primer `INSERT`

Inserta un producto con placeholders y una tupla de parámetros. Confirma la transacción.

## Ejercicio 4 — Primer `SELECT`

Consulta columnas explícitas de los productos y recorre el cursor.

## Ejercicio 5 — `fetchone()`

Busca un id existente y otro inexistente; maneja correctamente el posible `None`.

## Ejercicio 6 — `fetchall()`

Recupera los productos restantes y explica cuándo no convendría cargar todas las filas.

## Ejercicio 7 — `WHERE`

Filtra productos cuyo precio sea mayor o igual a un valor parametrizado.

## Ejercicio 8 — `LIKE`

Busca nombres que contengan un texto y pasa el patrón con `%` como parámetro.

## Ejercicio 9 — `ORDER BY` y `LIMIT`

Obtén los tres productos más costosos usando `DESC` y un límite parametrizado.

## Ejercicio 10 — `COUNT()`

Cuenta los registros y recupera el único valor de la fila resultante.

## Ejercicio 11 — `AVG()`, `MIN()` y `MAX()`

Resume precios y explica qué representa cada columna agregada.

## Ejercicio 12 — `UPDATE`

Actualiza la cantidad de un producto por id y comprueba `rowcount`.

## Ejercicio 13 — `DELETE`

Elimina un registro por id y verifica mediante `SELECT` que ya no existe.

## Ejercicio 14 — Funciones CRUD

Separa crear, listar, buscar, actualizar y eliminar en funciones de persistencia.

## Ejercicio 15 — Parámetros SQL

Revisa todas tus consultas y separa de la sentencia cada valor dinámico.

## Ejercicio 16 — Detectar SQL inseguro

Identifica por qué una consulta construida con concatenación es riesgosa y reescríbela sin ensayar entradas dañinas.

## Ejercicio 17 — `rollback()`

Realiza dos inserciones dentro de una transacción, provoca una excepción controlada antes del commit y comprueba que ninguna persiste.

## Ejercicio 18 — Restricciones

Agrega `UNIQUE` o `CHECK`, intenta violar la regla y maneja `sqlite3.IntegrityError` sin silenciarla.

## Ejercicio 19 — `sqlite3.Row`

Configura `row_factory` y reemplaza índices numéricos por nombres de columnas.

## Ejercicio 20 — Fila a dataclass

Mapea un resultado a `Estudiante` y conserva `None` para objetos todavía no insertados.

## Ejercicio 21 — Prueba con `:memory:`

Prueba una operación completa manteniendo una sola conexión abierta y explica por qué una segunda conexión no ve esa base.

## Ejercicio 22 — Prueba con `tmp_path`

Comprueba persistencia entre dos conexiones usando una base exclusiva de la prueba.

## Ejercicio 23 — Foreign key

Crea programas y estudiantes relacionados, habilita claves foráneas por conexión y comprueba una referencia inválida.

## Ejercicio 24 — Eliminar una conexión global

Refactoriza un módulo para pasar una ruta o conexión controlada, añadir rollback y garantizar cierre.

No consultes soluciones completas. Ejecuta cada práctica sobre una base temporal o desechable cuya ruta hayas verificado.

---

# 29. Reto — Sistema académico con SQLite

Transforma el sistema académico anterior para persistir información en SQLite.

## Tablas mínimas sugeridas

```text
estudiantes
├── id
├── codigo UNIQUE
├── nombre
├── edad
└── programa

notas
├── id
├── estudiante_id
└── valor CHECK entre 0 y 5
```

`notas.estudiante_id` debe ser una foreign key hacia estudiantes.

## Menú

```text
1. Registrar estudiante
2. Agregar nota
3. Mostrar estudiantes
4. Buscar estudiante
5. Mostrar notas
6. Calcular promedio
7. Actualizar estudiante
8. Eliminar estudiante
9. Salir
```

## Requisitos

- Usa `sqlite3` y SQL parametrizado.
- Separa persistencia, modelos e interacción.
- Utiliza dataclasses cuando aporten claridad.
- Controla `commit`, `rollback` y cierre de conexiones.
- Activa foreign keys en cada conexión.
- Maneja excepciones específicas sin ocultarlas.
- Prueba CRUD, restricciones y persistencia con bases temporales.
- No utilices ORM, paquetes externos de base de datos, red ni credenciales.

No se entrega una solución completa. Diseña primero el esquema y prueba cada función de persistencia antes de conectar el menú.

---

# 30. Comprobación de aprendizaje

- [ ] Distingo archivos y bases de datos según el problema.
- [ ] Comprendo modelo relacional, tabla, fila, columna y clave primaria.
- [ ] Uso SQLite mediante el módulo estándar `sqlite3`.
- [ ] Abro y cierro conexiones y utilizo cursores.
- [ ] Creo tablas con `CREATE TABLE IF NOT EXISTS`.
- [ ] Realizo `INSERT`, `SELECT`, `UPDATE` y `DELETE`.
- [ ] Utilizo `WHERE`, `LIKE`, `ORDER BY` y agregaciones básicas.
- [ ] Parametrizo valores y explico la prevención básica de SQL injection.
- [ ] Comprendo `commit()`, `rollback()` y transacciones.
- [ ] Distingo `fetchone()`, `fetchall()` y recorrido de cursor.
- [ ] Accedo a columnas mediante `sqlite3.Row`.
- [ ] Utilizo `lastrowid` y comprendo `INTEGER PRIMARY KEY`.
- [ ] Aplico `NOT NULL`, `UNIQUE`, `CHECK` y claves foráneas.
- [ ] Mapeo filas a dataclasses sin confundirlo con un ORM.
- [ ] Separo persistencia, lógica y flujo principal.
- [ ] Pruebo con `:memory:` o `tmp_path` según el ciclo de conexiones.
- [ ] Mantengo pruebas aisladas y conexiones cerradas.

---

# 31. Lo que aprendimos

```text
Aplicación Python
       ↓
    sqlite3
       ↓
      SQL
       ↓
    SQLite
       ↓
    tablas
       ↓
datos persistentes
```

```text
Create → INSERT
Read   → SELECT
Update → UPDATE
Delete → DELETE
```

Ahora podemos almacenar información estructurada. La Unidad 15 enseñará a obtener datos desde sistemas externos mediante HTTP y APIs REST.

---

# 🧭 Navegación

⬅️ [Volver a la Unidad 13 — Pruebas](../unidad13-pruebas/)

🏠 [Volver al inicio del curso](../README.md)

➡️ [Continuar a la Unidad 15 — Consumo de APIs](../unidad15-consumo-apis/)


---

## Continuar el curso

- **Unidad anterior:** [Unidad 13 — Pruebas automatizadas con Python](../unidad13-pruebas/README.md)
- **Volver al índice:** [Todas las unidades](../README.md)
- **Siguiente unidad:** [Unidad 15 — Consumo de APIs REST con Python](../unidad15-consumo-apis/README.md)
