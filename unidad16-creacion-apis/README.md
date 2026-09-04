# Unidad 16 — Creación de APIs REST con FastAPI

En la unidad anterior nuestro programa era cliente de una API externa. Ahora construiremos el servidor: recibirá peticiones HTTP, validará datos, ejecutará lógica y devolverá respuestas JSON.

---

## 🎯 Objetivos de aprendizaje

Al finalizar podrás crear rutas FastAPI con GET, POST, PATCH y DELETE; utilizar parámetros, cuerpos Pydantic, response models, códigos HTTP y `HTTPException`; separar esquemas, dominio y repositorio; consultar la documentación automática y probar localmente con `TestClient`.

---

## 📋 Antes de comenzar

Necesitas conocer HTTP, JSON, APIs REST, type hints, dataclasses, módulos, excepciones, pytest y persistencia. No estudiaremos todavía ORM, SQLAlchemy, JWT, OAuth, despliegue, Docker, WebSockets, tareas en segundo plano ni arquitectura distribuida.

---

# 1. De cliente a servidor

```text
Cliente → HTTP → nuestra API FastAPI → lógica/repositorio → respuesta
```

FastAPI es un framework web externo orientado a APIs. Aprovecha type hints, integra validación y genera documentación. Una aplicación FastAPI cumple la interfaz ASGI; Uvicorn es un servidor ASGI habitual que la ejecuta. Framework y servidor no son lo mismo.

---

# 2. Instalación y ejecución

Dentro de un entorno virtual:

```bash
python -m pip install fastapi uvicorn
```

Desde `unidad16-creacion-apis/ejemplos/proyecto_fastapi/`:

```bash
python -m uvicorn app.main:app --reload
```

`app.main` identifica el módulo y el último `app` la aplicación. `--reload` reinicia ante cambios y se usa solo durante desarrollo, no como configuración de producción.

---

# 3. Primera aplicación y ruta

```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def inicio() -> dict[str, str]:
    return {"mensaje": "Hola, API"}
```

`app` representa la aplicación. `@app.get("/")` registra una función para GET sobre `/`; el diccionario se convierte en JSON.

FastAPI publica normalmente documentación interactiva en `/docs`, otra vista en `/redoc` y un esquema OpenAPI. Rutas, modelos y tipos alimentan esa documentación; OpenAPI también puede servir a herramientas que generan clientes.

---

# 4. Path y query parameters

```python
from fastapi import FastAPI, Query

app = FastAPI()

@app.get("/estudiantes/{estudiante_id}")
def obtener(estudiante_id: int) -> dict[str, int]:
    return {"id": estudiante_id}

@app.get("/estudiantes")
def listar(
    programa: str | None = None,
    limite: int = Query(default=10, ge=1, le=100),
) -> dict[str, object]:
    return {"programa": programa, "limite": limite}
```

`estudiante_id` forma parte de la ruta y FastAPI valida su tipo. `programa` y `limite` aparecen después de `?` en la URL. `str | None = None` hace opcional el filtro; `Query` exige un límite entre 1 y 100.

Los datos complejos de creación pertenecen normalmente al cuerpo, no a una larga colección de query parameters.

---

# 5. Pydantic y el request body

FastAPI utiliza modelos Pydantic para validar, convertir y documentar datos:

```python
from pydantic import BaseModel, Field

class EstudianteCrear(BaseModel):
    nombre: str = Field(min_length=1)
    edad: int = Field(ge=0)
    programa: str = Field(min_length=1)
```

Si el cuerpo no tiene la estructura esperada, FastAPI responde con un error de validación. `Field(ge=0)` exige edad mayor o igual a cero.

Una dataclass representa cómodamente datos internos; `BaseModel` se orienta aquí a datos que entran o salen de la API. Ninguno sustituye universalmente al otro.

---

# 6. Esquemas de entrada, actualización y respuesta

El proyecto separa:

```python
from pydantic import BaseModel, Field

class EstudianteCrear(BaseModel):
    nombre: str
    edad: int = Field(ge=0)
    programa: str

class EstudianteActualizar(BaseModel):
    nombre: str | None = None
    edad: int | None = Field(default=None, ge=0)
    programa: str | None = None

class EstudianteRespuesta(BaseModel):
    id: int
    nombre: str
    edad: int
    programa: str
```

El id no llega al crear porque lo genera el repositorio; sí aparece al responder. Los campos de PATCH son opcionales porque solo se envían cambios.

En Pydantic moderno usamos `model_dump()`. Para PATCH, `model_dump(exclude_unset=True)` distingue campos omitidos. El proyecto además excluye `None` para no reemplazar campos requeridos por valores nulos.

---

# 7. Response models y códigos de estado

```python
from fastapi import FastAPI, status

app = FastAPI()

@app.post(
    "/estudiantes",
    response_model=EstudianteRespuesta,
    status_code=status.HTTP_201_CREATED,
)
def crear(datos: EstudianteCrear) -> EstudianteRespuesta:
    ...
```

`response_model` valida y documenta la forma de salida. `201 Created` comunica creación. Las constantes de `status` mejoran legibilidad, aunque un número correcto también es válido.

---

# 8. Recursos inexistentes y conflictos

```python
from fastapi import HTTPException

if estudiante is None:
    raise HTTPException(
        status_code=404,
        detail="Estudiante no encontrado",
    )
```

Un recurso inexistente produce 404. Un código académico duplicado podría producir 409 Conflict si esa regla forma parte del contrato. Los errores también son respuestas diseñadas, no accidentes.

Pydantic valida estructura y reglas sencillas; el repositorio o dominio valida reglas como unicidad.

---

# 9. PUT, PATCH y DELETE

PUT suele representar reemplazo completo y PATCH actualización parcial; el contrato de cada API decide los detalles. El proyecto usa PATCH y aplica solo `model_dump(exclude_unset=True, exclude_none=True)`.

DELETE exitoso puede devolver 204 sin cuerpo:

```python
from fastapi import Response, status

return Response(status_code=status.HTTP_204_NO_CONTENT)
```

No devuelvas un diccionario junto con 204.

---

# 10. Separación del mini proyecto

```text
proyecto_fastapi/
├── app/
│   ├── __init__.py
│   ├── main.py          → rutas y aplicación
│   ├── modelos.py       → dataclass de dominio
│   ├── esquemas.py      → modelos Pydantic
│   └── repositorio.py   → almacenamiento en memoria
└── tests/
    └── test_api.py
```

No es la única arquitectura posible. `APIRouter` permite dividir rutas grandes y `tags=["Estudiantes"]` las agrupa en la documentación. FastAPI también ofrece `Depends`, pero no necesitamos inyección avanzada en este ejemplo.

---

# 11. Repositorio en memoria

`RepositorioEstudiantes` encapsula un `dict[int, Estudiante]`, genera ids y ofrece listar, obtener, crear, actualizar, eliminar y `reset()`.

Este almacenamiento facilita aprender HTTP sin añadir SQLite al centro de la lección. Más adelante podría reemplazarse por un repositorio SQLite conservando rutas similares. El modelo Pydantic describe la frontera HTTP; la dataclass representa la aplicación internamente.

---

# 12. Metadata y documentación

```python
from fastapi import FastAPI

app = FastAPI(
    title="API Académica",
    version="1.0.0",
)
```

La metadata aparece en OpenAPI y las interfaces de documentación. Revisa `/docs` mientras desarrollas para comprobar parámetros, cuerpos, respuestas y códigos.

---

# 13. Pruebas con `TestClient`

`TestClient` ejecuta la aplicación localmente dentro del proceso; no necesita Uvicorn ni un puerto abierto:

```python
from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)

def test_inicio() -> None:
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"mensaje": "API Académica disponible"}
```

Las pruebas con un servidor desplegado serían otro nivel, cercano a extremo a extremo. No lo realizaremos aquí.

---

# 14. Aislamiento del estado

El repositorio vive en memoria, pero ninguna prueba debe depender de otra. Una fixture automática lo restablece:

```python
import pytest

from app.main import repositorio

@pytest.fixture(autouse=True)
def repositorio_limpio() -> None:
    repositorio.reset()
```

Así cada prueba comienza con ids y colección vacíos. La suite cubre inicio, lista, creación, consulta, 404, body inválido, filtro, PATCH, DELETE y ausencia de cuerpo en 204.

Ejecuta desde la raíz del mini proyecto:

```bash
python -m pytest -v
```

No inicies Uvicorn para las pruebas.

---

# 15. `def`, `async def` y temas posteriores

FastAPI admite endpoints con `def` y `async def`. Usaremos `def`: escribir `async` no acelera automáticamente trabajo de CPU ni transforma operaciones bloqueantes. `async`, `await` y concurrencia se estudiarán en la Unidad 17.

APIs reales suelen necesitar autenticación y CORS para determinados frontends. Solo anticipamos esos conceptos; no configuraremos JWT, OAuth ni seguridad compleja.

---

# 16. Errores frecuentes

- Olvidar `app = FastAPI()` o escribir una ruta sin `/`.
- Confundir parámetros path, query y body.
- No tipar parámetros o colocar estructuras complejas en query sin razón.
- Mezclar APIs de Pydantic v1 y v2; usar `.dict()` como forma central en código moderno en vez de `model_dump()`.
- Crear con 200 cuando el contrato requiere 201.
- Devolver contenido con 204.
- Omitir 404, response models o validaciones de negocio.
- Mezclar rutas, repositorio e `input()`.
- Compartir estado entre pruebas o depender de su orden.
- Levantar Uvicorn o abrir red durante pytest.
- Usar `async` por moda o combinarlo sin comprender llamadas bloqueantes.
- Hardcodear secretos o comenzar autenticación compleja demasiado pronto.
- No revisar `/docs` ni el contrato OpenAPI.

---

# 17. Ejercicios

1. Crea una aplicación FastAPI mínima con título y versión.
2. Agrega un GET `/` que devuelva un diccionario.
3. Crea un path parameter entero y observa la validación.
4. Añade un query parameter opcional `str | None`.
5. Limita un parámetro entero con `Query`, `ge` y `le`.
6. Define tu primer `BaseModel` académico.
7. Recibe ese modelo como request body.
8. Agrega restricciones útiles mediante `Field`.
9. Define un esquema de salida y úsalo como `response_model`.
10. Crea un recurso mediante POST.
11. Configura `status.HTTP_201_CREATED`.
12. Lanza una `HTTPException` con detalle claro.
13. Devuelve 404 para un id inexistente.
14. Diseña un esquema PATCH con campos opcionales.
15. Usa `model_dump(exclude_unset=True)` y explica su propósito.
16. Elimina un recurso con 204 y cuerpo vacío.
17. Implementa un repositorio en memoria con ids generados.
18. Separa esquema Pydantic y modelo interno.
19. Prueba GET `/` mediante `TestClient`.
20. Prueba POST y compara cuerpo y código.
21. Prueba el caso 404.
22. Aísla el repositorio mediante una fixture.
23. Detecta un endpoint marcado `async` sin necesidad y justifica `def`.
24. Diseña un CRUD completo y su matriz de pruebas.

No incluyas soluciones completas ni levantes un servidor para probar.

---

# 18. Reto — API académica

Diseña una API con recursos Estudiantes y Cursos. Para estudiantes implementa GET colección, GET por id, POST, PATCH y DELETE con `id`, `codigo`, `nombre`, `edad` y `programa`.

Requisitos:

- Código único; duplicado produce 409.
- Edad no negativa y recurso inexistente produce 404.
- Modelos Pydantic, response models y `HTTPException`.
- Repositorio separado y pruebas con `TestClient`.
- Fixture que garantice aislamiento.
- Ampliación opcional: repositorio SQLite de la Unidad 14.
- Sin JWT, OAuth, SQLAlchemy, base async ni Docker.

No se entrega la solución completa.

---

# 19. Comprobación de aprendizaje

- [ ] Distingo FastAPI, aplicación ASGI y Uvicorn.
- [ ] Creo rutas y decoradores GET, POST, PATCH y DELETE.
- [ ] Diferencio path parameters, query parameters y body.
- [ ] Uso `BaseModel`, `Field` y Pydantic moderno.
- [ ] Separo modelos de creación, actualización y respuesta.
- [ ] Uso `response_model`, 201, 204, 404 y 409 apropiadamente.
- [ ] Lanzo `HTTPException` con intención.
- [ ] Comprendo `/docs`, `/redoc` y OpenAPI.
- [ ] Separo rutas, esquemas, dominio y repositorio.
- [ ] Pruebo mediante `TestClient` sin servidor ni red.
- [ ] Aíslo estado mediante fixtures.
- [ ] Reconozco `async def` sin utilizarlo por moda.

---

# 20. Lo que aprendimos

```text
Cliente → HTTP → FastAPI → validación Pydantic
                            ↓
                    endpoint → repositorio
                            ↓
                      respuesta JSON
```

Ahora podemos construir servicios web. La Unidad 17 estudiará concurrencia, threading, multiprocessing, `async`, `await` y asyncio.

---

# 🧭 Navegación

⬅️ [Volver a la Unidad 15 — Consumo de APIs](../unidad15-consumo-apis/)

🏠 [Volver al inicio del curso](../README.md)

➡️ [Continuar a la Unidad 17 — Concurrencia](../unidad17-concurrencia/)
