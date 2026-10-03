# Unidad 17 — Concurrencia en Python

[Volver al índice del curso](../README.md) · [Ver el curso en Aprende con Leli](https://lelyliliana.github.io/aprende-con-leli/cursos/python/)

Algunas tareas calculan continuamente; otras pasan gran parte del tiempo esperando disco, red o temporizadores. En esta unidad aprenderás a coordinar trabajo con threads, procesos y asyncio, y a elegir según el problema.

---

## 🎯 Objetivos de aprendizaje

Al finalizar podrás distinguir concurrencia, paralelismo, I/O-bound y CPU-bound; utilizar `Thread`, executors, futures, `Lock`, procesos, coroutines, `await`, tareas y `gather()`; manejar errores y limitar concurrencia sin asumir que siempre mejora el rendimiento.

---

## 📋 Antes de comenzar

Necesitas conocer funciones, context managers, excepciones, módulos, pytest, APIs y FastAPI introductorio. Usaremos solo la biblioteca estándar, sin red, librerías async externas ni procesamiento pesado.

---

# 1. Secuencial, concurrente y paralelo

```text
Secuencial: tarea 1 → tarea 2 → tarea 3
Concurrente: varias tareas progresan en el mismo intervalo
Paralelo: varias tareas se ejecutan simultáneamente en distintos recursos
```

Concurrencia y paralelismo no son sinónimos. Una sola persona puede avanzar varias tareas alternándolas; varias personas pueden ejecutarlas realmente a la vez.

---

# 2. I/O-bound y CPU-bound

- **I/O-bound:** predomina la espera de red, disco o servicios.
- **CPU-bound:** predominan cálculos intensivos.

```text
I/O bloqueante tradicional → threads
Muchas esperas con APIs async → asyncio
CPU intensiva → procesos
```

Es una guía inicial, no una ley. Primero escribe código correcto, mide e identifica el cuello de botella.

---

# 3. Ejecución secuencial y medición

```python
from time import perf_counter, sleep

def tarea(nombre: str) -> str:
    sleep(0.01)
    return f"{nombre} completada"

inicio = perf_counter()
resultados = [tarea(nombre) for nombre in ["uno", "dos", "tres"]]
duracion = perf_counter() - inicio
print(resultados, duracion)
```

`sleep()` simula espera breve. `perf_counter()` permite observar diferencias, pero una ejecución no constituye un benchmark riguroso.

---

# 4. Primer thread

Un hilo es un flujo de ejecución dentro de un proceso. Los threads comparten memoria.

```python
from threading import Thread

def mostrar(nombre: str) -> None:
    print(nombre)

hilo = Thread(target=mostrar, args=("tarea",))
hilo.start()
hilo.join()
```

`target` recibe la función, `args` sus argumentos, `start()` inicia el hilo y `join()` espera que termine. `Thread` no entrega directamente el retorno como una función normal.

---

# 5. `ThreadPoolExecutor`

Un pool administra workers y futures:

```python
from concurrent.futures import ThreadPoolExecutor
from time import sleep

def procesar(nombre: str) -> str:
    sleep(0.01)
    return f"{nombre} listo"

with ThreadPoolExecutor(max_workers=3) as executor:
    future = executor.submit(procesar, "informe")
    print(future.result())
```

Un `Future` representa un resultado posterior. `result()` devuelve el valor o vuelve a lanzar la excepción; `exception()` permite consultarla.

---

# 6. `executor.map()` y `as_completed()`

```python
from concurrent.futures import ThreadPoolExecutor, as_completed

def duplicar(numero: int) -> int:
    return numero * 2

with ThreadPoolExecutor(max_workers=3) as executor:
    print(list(executor.map(duplicar, [1, 2, 3])))

with ThreadPoolExecutor(max_workers=3) as executor:
    futures = [executor.submit(duplicar, numero) for numero in [1, 2, 3]]
    print([future.result() for future in as_completed(futures)])
```

El `map()` del executor no es el `map()` funcional, aunque ambos aplican una función. `executor.map()` conserva el orden de entrada; `as_completed()` entrega futures según terminan.

---

# 7. Estado compartido y condiciones de carrera

Los threads ven los mismos objetos. Si varios leen y escriben un contador, el resultado puede depender del intercalado: es una **race condition**. Un ejemplo pequeño puede coincidir por casualidad, así que no esperes que falle siempre.

```python
from threading import Lock

contador = 0
lock = Lock()

def incrementar() -> None:
    global contador
    with lock:
        contador += 1

incrementar()
print(contador)
```

El lock protege una sección crítica. Hazla pequeña: un bloqueo demasiado amplio reduce concurrencia. Un deadlock ocurre cuando tareas esperan mutuamente recursos; no construiremos un ejemplo capaz de quedar colgado. Consulta si cada librería u objeto es thread-safe.

---

# 8. El GIL con precisión

En la implementación tradicional de CPython, el GIL limita la ejecución simultánea de bytecode Python por varios threads de un proceso. Esto no significa que “Python no tenga paralelismo”:

- Threads siguen siendo útiles durante esperas I/O.
- Procesos pueden utilizar varios núcleos para CPU.
- Extensiones nativas pueden liberar el GIL.
- Implementaciones y versiones modernas pueden evolucionar.

---

# 9. Procesos y main guard

Los procesos tienen memoria separada y mayor costo de creación, pero pueden ejecutar CPU en varios núcleos.

```python
from multiprocessing import Process

def tarea() -> None:
    print("Proceso iniciado")

if __name__ == "__main__":
    proceso = Process(target=tarea)
    proceso.start()
    proceso.join()
```

El main guard es especialmente importante con el método `spawn`, común en Windows, para no crear procesos recursivamente.

---

# 10. `ProcessPoolExecutor`

```python
from concurrent.futures import ProcessPoolExecutor

def sumar_cuadrados(limite: int) -> int:
    return sum(numero * numero for numero in range(limite))

if __name__ == "__main__":
    with ProcessPoolExecutor() as executor:
        print(list(executor.map(sumar_cuadrados, [100, 200])))
```

Las funciones y argumentos enviados deben poder serializarse según el mecanismo usado. Prefiere funciones de módulo; evita lambdas y funciones locales. Procesos implican overhead, por lo que no convienen para tareas diminutas. `Queue` y `Pipe` permiten comunicación, pero no profundizaremos ni usaremos memoria compartida avanzada.

---

# 11. Coroutines y `async def`

Asyncio coordina tareas cooperativamente en un event loop:

```python
import asyncio

async def saludar() -> str:
    await asyncio.sleep(0.01)
    return "Hola"

resultado = asyncio.run(saludar())
print(resultado)
```

`async def` define una función de coroutine. Llamarla crea un objeto coroutine; no completa el trabajo como una función normal. `await` solo se usa dentro de `async def`, salvo contextos interactivos especiales. `asyncio.run()` crea el punto de entrada.

El event loop ejecuta trabajo listo y cambia de tarea cuando una coroutine espera.

---

# 12. `asyncio.sleep()`, tareas y `gather()`

```python
import asyncio

async def procesar(nombre: str) -> str:
    await asyncio.sleep(0.01)
    return f"{nombre} listo"

async def main() -> None:
    tareas = [
        asyncio.create_task(procesar("uno")),
        asyncio.create_task(procesar("dos")),
    ]
    resultados = await asyncio.gather(*tareas)
    print(resultados)

asyncio.run(main())
```

`create_task()` programa la coroutine y `gather()` espera todas; sus resultados conservan el orden de argumentos, no necesariamente el orden de finalización. Una excepción normalmente se propaga al esperar. No crees tareas para olvidarlas.

---

# 13. Bloqueo, timeouts y cancelación async

Dentro de async, `time.sleep()` bloquea el thread y el event loop. Para espera simulada usa `await asyncio.sleep()`.

`asyncio.wait_for(coroutine, timeout=...)` puede limitar una espera. `task.cancel()` solicita cancelación, que se manifiesta mediante `asyncio.CancelledError`; el código debe conservar limpieza apropiada.

Python 3.11+ ofrece `asyncio.TaskGroup` para concurrencia estructurada y `asyncio.timeout()` para límites de tiempo. Son ampliaciones opcionales, no requisitos de esta unidad.

---

# 14. Código bloqueante y `to_thread()`

`requests`, `sqlite3` y `time.sleep()` son bloqueantes. No se vuelven async por llamarlos desde `async def`.

```python
import asyncio
from time import sleep

def operacion_bloqueante() -> str:
    sleep(0.01)
    return "terminada"

async def main() -> None:
    resultado = await asyncio.to_thread(operacion_bloqueante)
    print(resultado)

asyncio.run(main())
```

`to_thread()` es un puente útil, no sustituto universal de librerías async nativas. `requests` es bloqueante; existen clientes como `httpx.AsyncClient`, pero no los desarrollaremos. FastAPI permite `def` y `async def`: elige según las operaciones reales.

---

# 15. Limitar concurrencia

```python
import asyncio

async def tarea(numero: int, semaforo: asyncio.Semaphore) -> int:
    async with semaforo:
        await asyncio.sleep(0.01)
        return numero

async def main() -> None:
    semaforo = asyncio.Semaphore(2)
    resultados = await asyncio.gather(
        *(tarea(numero, semaforo) for numero in range(4))
    )
    print(resultados)

asyncio.run(main())
```

Un semáforo limita tareas simultáneas. APIs con rate limits, conexiones, archivos y memoria son recursos finitos. Más concurrencia no garantiza más rendimiento.

---

# 16. Comparación

| Modelo | Uso inicial | Memoria | Consideración |
|---|---|---|---|
| Threading | I/O bloqueante | Compartida | Requiere sincronización |
| Multiprocessing | CPU intensiva | Separada | Mayor overhead y serialización |
| Asyncio | Muchas esperas async | Un proceso habitual | Requiere APIs compatibles |

Pueden combinarse, pero la complejidad aumenta. Mide antes de optimizar.

---

# 17. Proyecto real y pruebas

```text
proyecto_concurrencia/
├── threading_demo.py
├── multiprocessing_demo.py
├── asyncio_demo.py
└── tests/test_concurrencia.py
```

Los ejemplos usan esperas menores a una décima de segundo y ninguna red. La suite prueba funciones puras, ThreadPool y coroutines mediante `asyncio.run()`, sin `pytest-asyncio`. No levanta ProcessPool: comprueba su función CPU pura para evitar procesos frágiles en tests.

```bash
cd unidad17-concurrencia/ejemplos/proyecto_concurrencia
python -m pytest -v
```

No afirmes en pruebas que la versión concurrente “debe ser más rápida”; el timing depende de la máquina y su carga.

---

# 18. Errores frecuentes

- Confundir concurrencia y paralelismo.
- Usar threads para CPU intensiva esperando escalado lineal.
- Olvidar `join()` o ignorar errores de `Future.result()`.
- Modificar estado compartido sin sincronización o usar locks enormes.
- Crear ciclos de espera que causan deadlock.
- Omitir main guard en multiprocessing.
- Enviar lambdas o funciones locales a ProcessPool.
- Crear procesos para tareas diminutas.
- Llamar una coroutine sin `await` u olvidar `asyncio.run()`.
- Usar `time.sleep()` o `requests` bloqueante dentro de async sin comprenderlo.
- Crear tareas y no esperarlas.
- Creer que async significa varios núcleos.
- Usar concurrencia ilimitada o medir una sola vez y generalizar.
- Escribir tests dependientes de tiempos exactos.

---

# 19. Ejercicios

1. Ejecuta tres esperas pequeñas secuencialmente.
2. Crea un `Thread` con target y argumento.
3. Inicia dos hilos y espera ambos con `join()`.
4. Coordina varios threads sin asumir su orden de impresión.
5. Repite con `ThreadPoolExecutor` y context manager.
6. Obtén retorno mediante `Future.result()`.
7. Procesa futures con `as_completed()`.
8. Provoca un error controlado y recupéralo desde el future.
9. Explica una race condition sin depender de reproducirla.
10. Protege una sección crítica pequeña con `Lock`.
11. Crea un `Process` mínimo sin carga pesada.
12. Añade el main guard y explica por qué importa.
13. Diseña un ProcessPool con función de módulo.
14. Clasifica cinco tareas como CPU-bound o I/O-bound.
15. Define tu primera coroutine.
16. Espera su resultado mediante `await`.
17. Ejecútala desde código síncrono con `asyncio.run()`.
18. Sustituye un `time.sleep()` async incorrecto.
19. Programa dos coroutines con `create_task()`.
20. Recoge resultados con `gather()` y comprueba su orden.
21. Comprueba la propagación de un error async.
22. Lleva una operación bloqueante pequeña a `to_thread()`.
23. Limita cuatro tareas mediante `Semaphore(2)`.
24. Justifica threading, procesos o asyncio para tres escenarios.

No incluyas soluciones completas ni utilices red o cargas pesadas.

---

# 20. Reto — Procesador concurrente de tareas

Construye tres versiones sobre la misma colección:

- Parte A: secuencial.
- Parte B: esperas I/O simuladas con ThreadPoolExecutor.
- Parte C: las mismas esperas mediante coroutines y asyncio.
- Parte D opcional: cálculo moderado con ProcessPoolExecutor.

Recoge resultados, maneja excepciones, limita concurrencia y mide solo como observación. Explica qué estrategia elegirías y por qué. No uses red ni entregues una solución completa.

---

# 21. Comprobación de aprendizaje

- [ ] Distingo concurrencia, paralelismo, I/O-bound y CPU-bound.
- [ ] Uso Thread, `start()`, `join()` y ThreadPoolExecutor.
- [ ] Comprendo Future, `map()` y `as_completed()`.
- [ ] Reconozco race conditions, Lock, deadlock y thread safety.
- [ ] Explico el GIL sin negar el paralelismo de Python.
- [ ] Uso multiprocessing, ProcessPool y main guard.
- [ ] Mantengo funciones de procesos serializables a nivel de módulo.
- [ ] Comprendo coroutine, `async def`, `await` y event loop.
- [ ] Uso `asyncio.run()`, `sleep()`, `create_task()` y `gather()`.
- [ ] Reconozco timeouts, cancelación, `to_thread()` y Semaphore.
- [ ] Elijo una estrategia después de medir y considerar costos.

---

# 22. Lo que aprendimos

```text
¿CPU-bound? → multiprocessing
¿I/O bloqueante? → threading
¿I/O con ecosistema async? → asyncio
```

La Unidad 18 aplicará Python al análisis y procesamiento de datos.

---

# 🧭 Navegación

⬅️ [Volver a la Unidad 16 — Creación de APIs](../unidad16-creacion-apis/)

🏠 [Volver al inicio del curso](../README.md)

➡️ [Continuar a la Unidad 18 — Análisis de datos](../unidad18-datos/)


---

## Continuar el curso

- **Unidad anterior:** [Unidad 16 — Creación de APIs REST con FastAPI](../unidad16-creacion-apis/README.md)
- **Volver al índice:** [Todas las unidades](../README.md)
- **Siguiente unidad:** [Unidad 18 — Análisis de datos con NumPy y pandas](../unidad18-datos/README.md)
