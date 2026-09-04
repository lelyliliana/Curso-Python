# Unidad 15 — Consumo de APIs REST con Python

Hasta ahora nuestros programas han trabajado principalmente con datos locales. En esta unidad aprenderás a solicitar información a servicios web, interpretar respuestas JSON y construir un cliente HTTP robusto y comprobable.

---

## 🎯 Objetivos de aprendizaje

Al finalizar podrás comprender API, REST, cliente, servidor, URL, endpoint, métodos y códigos HTTP; enviar solicitudes con `requests`; utilizar timeout, headers, parámetros y JSON; manejar errores; proteger credenciales; separar responsabilidades y probar clientes sin red real.

---

## 📋 Antes de comenzar

Necesitas conocer JSON, excepciones, módulos, entornos virtuales, pytest, mocks, dataclasses y type hints. No crearemos APIs, ni usaremos FastAPI, Flask, `async`, OAuth profundo, JWT o microservicios.

`requests` es una dependencia externa. Los ejemplos de red son conceptuales y usan un dominio ficticio; no los ejecutes sin reemplazarlo por una API real y consultar su documentación actual.

---

# 1. API, cliente y servidor

Una API es una interfaz definida para que dos sistemas se comuniquen. No toda API utiliza la web, aunque aquí estudiaremos APIs web.

```text
Aplicación Python (cliente)
          ↓ petición HTTP
       API del servidor
          ↓ respuesta HTTP
Aplicación Python (cliente)
```

REST es un estilo arquitectónico común para servicios web. Suele representar recursos mediante URLs, operaciones mediante métodos HTTP y datos mediante JSON. No todas las APIs llamadas “REST” siguen exactamente las mismas decisiones.

---

# 2. URL, rutas y endpoints

En `https://api.ejemplo.com/estudiantes/10`:

- `https` es el esquema.
- `api.ejemplo.com` es el host.
- `/estudiantes/10` es la ruta.

Un endpoint combina una ruta y una operación disponible:

```text
GET /estudiantes       → consultar colección
GET /estudiantes/10    → consultar un recurso
```

El `10` es un parámetro de ruta. En el cliente puede incorporarse como `f"{base_url}/estudiantes/{estudiante_id}"` después de validar el identificador.

---

# 3. Métodos HTTP

| Método | Uso típico |
|---|---|
| `GET` | Consultar |
| `POST` | Crear |
| `PUT` | Reemplazar un recurso completo |
| `PATCH` | Actualizar parcialmente |
| `DELETE` | Eliminar |

Son convenciones habituales y el contrato real lo define cada API. `GET` normalmente es idempotente; `PUT` y `DELETE` suelen diseñarse así; no debemos asumir que repetir un `POST` sea seguro.

---

# 4. Códigos de estado

```text
2xx → éxito
3xx → redirección
4xx → problema relacionado con la solicitud o cliente
5xx → problema del servidor
```

Algunos códigos importantes son `200 OK`, `201 Created`, `204 No Content`, `400 Bad Request`, `401 Unauthorized`, `403 Forbidden`, `404 Not Found`, `409 Conflict`, `422 Unprocessable Content` y `500 Internal Server Error`. No es necesario memorizarlos todos.

Un éxito no siempre es `200`. Un `DELETE` correcto puede devolver `204`, cuyo cuerpo está vacío.

---

# 5. JSON en HTTP

HTTP transporta datos textuales o binarios. JSON es una representación frecuente:

```json
{
  "id": 1,
  "nombre": "Ana"
}
```

Como vimos en la Unidad 5, JSON y los diccionarios Python están relacionados, pero no son el mismo objeto.

---

# 6. Instalar `requests`

Activa un entorno virtual y ejecuta:

```bash
python -m pip install requests
```

No fijamos una versión concreta. Comprueba que el intérprete activo corresponde al entorno del proyecto.

---

# 7. Primer GET y timeout

Este ejemplo es **conceptual** y no debe ejecutarse contra el dominio ficticio:

```text
import requests

response = requests.get(
    "https://api.ejemplo.com/estudiantes",
    timeout=10,
)
```

`requests.get()` envía la petición y devuelve una respuesta. El timeout limita cuánto estamos dispuestos a esperar; sin uno explícito, una solicitud puede permanecer bloqueada demasiado tiempo. `10` es solo un ejemplo: la cifra apropiada depende del servicio y del contexto.

---

# 8. Inspeccionar y validar una respuesta

```text
print(response.status_code)
print(response.text)
response.raise_for_status()
datos = response.json()
```

- `status_code` contiene el código HTTP.
- `text` presenta el cuerpo como texto.
- `raise_for_status()` lanza `HTTPError` para determinados errores HTTP.
- `json()` intenta interpretar el cuerpo y puede fallar si no contiene JSON válido.

No llames automáticamente a `json()` después de un `204 No Content`.

---

# 9. Manejo robusto de errores

Patrón conceptual, sin solicitud real durante la validación:

```text
try:
    response = requests.get(url, timeout=10)
    response.raise_for_status()
    datos = response.json()
except requests.Timeout:
    print("La API tardó demasiado")
except requests.HTTPError:
    print("La API respondió con un error")
except requests.RequestException:
    print("Falló la comunicación")
```

`Timeout`, `ConnectionError` y `HTTPError` derivan de `RequestException`. Coloca las capturas específicas antes de la general y no ocultes errores mediante `except Exception: pass`.

---

# 10. Query parameters y path parameters

Para filtros, páginas o límites usa `params`:

```text
response = requests.get(
    url,
    params={"pagina": 2, "limite": 10},
    timeout=10,
)
```

Requests construye y codifica la query string. No concatenes manualmente `?pagina=...`. En cambio, `/estudiantes/10` contiene un id como parte de la ruta.

La paginación evita que APIs grandes entreguen todo de una vez. Algunos servicios usan páginas y otros cursores; siempre sigue su documentación.

---

# 11. Headers y cuerpos JSON

Los headers transportan metadatos:

```text
headers = {"Accept": "application/json"}
```

`Accept` comunica el formato esperado. `Content-Type: application/json` describe un cuerpo JSON.

Para crear datos:

```text
payload = {"nombre": "Ana", "edad": 20}
response = requests.post(url, json=payload, timeout=10)
```

`json=` serializa el diccionario y configura el tipo de contenido adecuado. `data=` se utiliza para otras representaciones, como formularios, según el contrato. `PUT` y `PATCH` se envían de manera similar; su significado depende de la API.

---

# 12. Autenticación sin secretos en el código

Algunas APIs usan API keys, Basic Auth o bearer tokens:

```text
headers = {"X-API-Key": api_key}
headers = {"Authorization": f"Bearer {token}"}
requests.get(url, auth=(usuario, contrasena), timeout=10)
```

Nunca escribas una clave real en el repositorio. El proceso puede proporcionarla mediante una variable de entorno:

```python
import os

api_key = os.getenv("API_KEY")
if api_key is None:
    print("No se configuró API_KEY")
```

Algunas herramientas cargan archivos `.env`, pero no agregaremos `python-dotenv`. Un `.env` con secretos normalmente pertenece a `.gitignore`.

---

# 13. Reutilizar una `Session`

Una `Session` puede reutilizar conexiones y conservar headers o configuración:

```text
with requests.Session() as session:
    session.headers.update({"Accept": "application/json"})
    response = session.get(url, timeout=10)
```

El context manager garantiza el cierre. No profundizaremos en cookies.

---

# 14. JSON a dataclass

El proyecto representa la respuesta con:

```python
from dataclasses import dataclass

@dataclass
class Estudiante:
    id: int
    nombre: str
    edad: int
    programa: str
```

El mapeo básico es:

```python
from modelos import Estudiante

datos = {"id": 1, "nombre": "Ana", "edad": 20, "programa": "Sistemas"}
estudiante = Estudiante.desde_dict(datos)
print(estudiante)
```

Los type hints no validan el JSON. `desde_dict()` comprueba campos y tipos básicos; una API real todavía puede devolver valores inesperados que debemos tratar según su contrato.

---

# 15. Separar responsabilidades

```text
api_client.py → comunicación HTTP
modelos.py    → estructuras y validación de datos
main.py       → flujo e interacción
```

No coloques `input()` dentro de la capa HTTP ni realices solicitudes al importar. Esta separación facilita reutilización y pruebas.

---

# 16. El cliente real

`APIClient` recibe `base_url`, timeout y una `Session` opcional. `base_url.rstrip("/")` evita dobles barras. Su método interno `_request()` centraliza URL, timeout y `raise_for_status()` sin crear un framework propio.

Ofrece:

```text
listar_estudiantes()     → GET con params
obtener_estudiante(id)   → GET con path parameter
crear_estudiante(datos)  → POST con json
actualizar_estudiante()  → PATCH con json
eliminar_estudiante(id)  → DELETE
```

La estrategia elegida para 404 es consistente: `obtener_estudiante()` devuelve `None`. Otros errores HTTP se propagan como excepciones de requests. `eliminar_estudiante()` no intenta interpretar JSON, por lo que acepta correctamente un `204`.

---

# 17. Ejecutar la demostración

Desde la raíz del ejemplo:

```bash
cd unidad15-consumo-apis/ejemplos/proyecto_api_client
python main.py
```

Antes debes reemplazar `https://api.ejemplo.com` por una API cuya documentación hayas consultado. Las APIs públicas cambian campos, endpoints, autenticación y límites; los patrones de esta unidad son estables, pero el proveedor define el contrato actual.

`main.py` tiene main guard y no solicita nada al importarse.

---

# 18. Rate limits, reintentos e idempotencia

Un servicio puede responder `429 Too Many Requests` al superar sus límites. Algunos fallos temporales admiten reintentos, pero una política correcta considera tiempos, límites e idempotencia.

Reintentar automáticamente un `POST` puede crear duplicados. No implementaremos todavía reintentos complejos. Clientes reales también suelen registrar información relevante; el logging formal llegará más adelante.

---

# 19. Por qué probar sin red

Una API pública puede caerse, cambiar, responder lentamente, limitar solicitudes o requerir credenciales. Una prueba que depende de ella deja de ser rápida, determinista y aislada.

Las pruebas del proyecto inyectan una `Session` simulada. Ninguna conexión real se abre.

---

# 20. Mock de respuesta

```python
from unittest.mock import Mock

import requests

response = Mock(spec=requests.Response)
response.status_code = 200
response.json.return_value = {"id": 1, "nombre": "Ana"}
response.raise_for_status.return_value = None

assert response.json()["nombre"] == "Ana"
response.raise_for_status.assert_not_called()
```

El mock simula únicamente el contrato necesario. En las pruebas reales también comprobamos método, URL, `params`, `json` y timeout.

---

# 21. Simular errores reales

```python
from unittest.mock import Mock

import pytest
import requests

session = Mock(spec=requests.Session)
session.request.side_effect = requests.Timeout("Tiempo agotado")

with pytest.raises(requests.Timeout):
    session.request("GET", "https://api.ejemplo.com", timeout=3)
```

No usamos `sleep()` para probar un timeout. Para un error HTTP, configuramos `response.raise_for_status.side_effect = requests.HTTPError(...)`.

`Response.json()` puede lanzar una excepción de decodificación cuando el cuerpo no es JSON válido. La excepción concreta puede depender de la configuración de requests; el cliente también valida que la estructura resultante sea lista o diccionario y las pruebas simulan respuestas inesperadas de forma controlada.

Si utilizas `patch`, intercepta el nombre donde el código lo consulta, por ejemplo `patch("api_client.requests.Session")`. Parchear la ubicación equivocada puede permitir una llamada real.

---

# 22. Ejecutar las pruebas

Con requests y pytest instalados:

```bash
python -m pytest -v
```

La suite cubre URLs, GET, parámetros, path ids, POST, PATCH, DELETE 204, timeout aplicado, HTTPError, Timeout, 404, formato inesperado, dataclass y cierre de sesión. Todas las llamadas HTTP están interceptadas.

---

# 23. Errores frecuentes

- Olvidar timeout o creer que un único valor sirve para todo contexto.
- Suponer que `200` es el único éxito o llamar `json()` sobre `204`.
- Omitir `raise_for_status()` cuando el contrato necesita detectar errores HTTP.
- Capturar `Exception` y ocultar la causa.
- Concatenar query parameters en lugar de usar `params`.
- Enviar JSON mediante `data=` sin comprender la representación.
- Hardcodear API keys, subir secretos o usar HTTP cuando el servicio ofrece HTTPS.
- Confiar en que JSON siempre contiene claves y tipos esperados.
- No definir qué significa un 404 para la capa cliente.
- Mezclar `input()` con HTTP o hacer solicitudes al importar.
- Ejecutar pruebas contra internet o usar esperas reales.
- Crear mocks que verifican detalles irrelevantes o parchear donde no se usa la dependencia.
- Asumir que todas las APIs REST tienen el mismo contrato e ignorar la documentación.

---

# 24. Ejercicios

1. Identifica cliente, servidor, petición y respuesta en una aplicación académica.
2. Separa esquema, host y ruta de tres URLs.
3. Elige entre GET, POST, PUT, PATCH y DELETE para cinco operaciones.
4. Clasifica códigos 200, 201, 204, 404, 429 y 500.
5. Escribe conceptualmente un GET con URL ficticia y timeout.
6. Inspecciona `status_code` y decide qué resultados representan éxito.
7. Convierte una respuesta simulada con `json()` y valida su estructura.
8. Agrega `raise_for_status()` y explica qué errores detecta.
9. Compara una solicitud con timeout y otra sin él; justifica el valor elegido.
10. Envía página, límite y programa mediante `params`.
11. Configura headers `Accept` y una API key ficticia recibida desde el entorno.
12. Diseña un POST con `json=` para crear un estudiante.
13. Explica y ejemplifica la diferencia contractual entre PUT y PATCH.
14. Maneja un DELETE 204 sin llamar a `json()`.
15. Lee `API_KEY` mediante `os.getenv()` y falla claramente si falta.
16. Usa una `Session` con headers comunes y garantiza su cierre.
17. Convierte un diccionario validado a `Estudiante` mediante `desde_dict()`.
18. Amplía `APIClient` con una consulta filtrada sin duplicar manejo HTTP.
19. Simula un GET con `Mock` y comprueba el objeto devuelto.
20. Simula un POST y verifica exactamente su argumento `json`.
21. Configura `raise_for_status()` para producir `requests.HTTPError`.
22. Simula `requests.Timeout` sin red ni esperas.
23. Comprueba método, URL, params y timeout de una llamada.
24. Refactoriza un cliente que mezcla input, secretos, HTTP y presentación.

No incluyas soluciones completas ni credenciales. Todas las pruebas deben funcionar sin red.

---

# 25. Reto — Cliente de API académica

Diseña un cliente para estos endpoints hipotéticos:

```text
GET    /estudiantes
GET    /estudiantes/{id}
POST   /estudiantes
PATCH  /estudiantes/{id}
DELETE /estudiantes/{id}
```

Debe listar, buscar por id, filtrar por programa mediante query param, crear, actualizar, eliminar, manejar 404 y responder ante timeout.

Requisitos:

- `APIClient`, dataclass `Estudiante` y main separados.
- Timeout, headers, `raise_for_status()`, `params` y `json=`.
- API key desde variable de entorno si el contrato la exige.
- Estrategia documentada y consistente para 404.
- Pytest y `Mock` o `patch`, sin red real.
- Ninguna credencial, API real obligatoria, `async` ni creación de servidor.

No se entrega la solución completa. Define primero el contrato observable de cada método.

---

# 26. Comprobación de aprendizaje

- [ ] Explico API, REST, cliente, servidor, HTTP, URL y endpoint.
- [ ] Distingo métodos HTTP y categorías de códigos de estado.
- [ ] Interpreto JSON sin asumir que sus datos son válidos.
- [ ] Reconozco que requests es externo y utilizo timeout.
- [ ] Uso `status_code`, `text`, `json()` y `raise_for_status()`.
- [ ] Manejo `Timeout`, `HTTPError` y `RequestException` apropiadamente.
- [ ] Distingo query params de path params.
- [ ] Utilizo headers, `Content-Type` y `json=`.
- [ ] Comprendo PUT, PATCH, DELETE y 204.
- [ ] Obtengo secretos desde variables de entorno.
- [ ] Reutilizo y cierro una `Session`.
- [ ] Separo cliente HTTP, modelos y flujo.
- [ ] Comprendo paginación, rate limiting, reintentos e idempotencia básica.
- [ ] Pruebo URL, parámetros, cuerpos y errores mediante mocks sin red.

---

# 27. Lo que aprendimos

```text
Aplicación Python → requests → HTTP → API externa → JSON → objetos Python
```

```text
solicitud → status code → validación → JSON → procesamiento
```

Hasta ahora somos clientes de una API. En la Unidad 16 construiremos nuestro propio servicio web mediante FastAPI.

---

# 🧭 Navegación

⬅️ [Volver a la Unidad 14 — Bases de datos](../unidad14-bases-datos/)

🏠 [Volver al inicio del curso](../README.md)

➡️ [Continuar a la Unidad 16 — Creación de APIs](../unidad16-creacion-apis/)
