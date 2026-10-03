# Unidad 21 — Proyecto final

[Volver al índice del curso](../README.md) · [Ver el curso en Aprende con Leli](https://lelyliliana.github.io/aprende-con-leli/cursos/python/)

Llegaste a la etapa en la que los conceptos dejan de aparecer como ejercicios aislados y se convierten en decisiones dentro de una solución completa. En esta unidad diseñarás, implementarás, probarás y documentarás un proyecto propio.

No encontrarás una aplicación final resuelta de principio a fin. Esta guía te ofrece preguntas, rutas, criterios, plantillas y controles para que construyas una solución que puedas comprender y defender.

---

## 🎯 Objetivos de aprendizaje

Al finalizar podrás:

- Definir un problema, un usuario y un alcance alcanzable.
- Convertir necesidades en requisitos y criterios de aceptación.
- Elegir tecnologías por su utilidad y no por acumular herramientas.
- Diseñar una estructura de módulos adecuada al problema.
- Construir primero un flujo mínimo funcional.
- Integrar persistencia, APIs, datos o automatización cuando aporten valor.
- Probar reglas, límites y errores relevantes.
- Refactorizar con apoyo de pruebas.
- Documentar instalación, configuración, ejecución y decisiones.
- Verificar el proyecto en un entorno limpio y presentarlo con claridad.

---

## 📋 Antes de comenzar

Esta unidad integra el curso completo. Vuelve a las unidades anteriores cuando necesites recuperar una técnica concreta; no necesitas memorizarlo todo.

> **Principio del proyecto:** un proyecto pequeño, terminado, probado y documentado demuestra más criterio que un sistema enorme e incompleto.

No es obligatorio usar todas las tecnologías estudiadas. Debes seleccionar únicamente las que tengan sentido para el problema.

---

# 1. ¿Qué vamos a construir?

Desarrollarás un proyecto propio desde cero siguiendo este recorrido:

```text
Problema
   ↓
Requisitos
   ↓
Diseño
   ↓
Implementación
   ↓
Pruebas
   ↓
Documentación
   ↓
Entrega
```

El resultado puede ser una aplicación CLI, una API, un análisis de datos, una automatización, un cliente de API o una combinación razonable. Lo importante es resolver un problema concreto y poder explicar cada decisión.

# 2. El proyecto no comienza escribiendo código

Antes de abrir el editor, responde:

- ¿Qué problema quiero resolver?
- ¿Quién utilizará la solución?
- ¿Qué debe hacer?
- ¿Qué no debe hacer en esta versión?
- ¿Qué datos necesita?
- ¿Cómo sabré que funciona?

Estas respuestas evitan construir funcionalidades sin propósito y sirven como base para las pruebas y la documentación.

# 3. Elegir un problema

Puedes crear, entre otras posibilidades:

- Un sistema académico, biblioteca, inventario, reservas o agenda.
- Un gestor de tareas, gastos o seguimiento de proyectos.
- Una herramienta CLI o de procesamiento de archivos.
- Un analizador de datos o generador de reportes.
- Una API REST o un cliente de API.
- Un automatizador de tareas repetitivas.

Son ejemplos, no una lista cerrada. También puedes proponer otro problema que comprendas y puedas delimitar.

# 4. Reducir antes de construir

Propuestas como “una red social completa”, “un sistema bancario completo” o “un ERP” esconden decenas de problemas. Reduce la idea hasta poder entregar un núcleo coherente.

Compara:

```text
Demasiado amplio:
Sistema universitario con pagos, chat, aplicación móvil e IA.

Alcance viable:
CLI local para registrar estudiantes y notas, calcular promedios
y persistir la información en SQLite.
```

La segunda propuesta permite diseñar, probar y documentar un flujo completo.

# 5. Definir el alcance

Escribe dos listas visibles:

## Incluye

- Registrar tareas.
- Mostrar y buscar tareas.
- Marcar una tarea como completada.
- Persistir datos localmente.

## No incluye

- Usuarios múltiples.
- Autenticación.
- Aplicación móvil.
- Sincronización en la nube.

“No incluye” no significa que la idea sea mala; protege la versión actual y convierte otras ideas en posibles mejoras futuras.

# 6. Usuario o actor

Describe quién utilizará la solución y qué necesita:

```text
Usuario: persona que necesita organizar sus tareas personales.
Necesidad: registrar, consultar y completar tareas desde la terminal.
```

Un usuario concreto ayuda a elegir interfaz, mensajes y funcionalidades.

# 7. Requisitos funcionales

Los requisitos funcionales describen qué debe hacer la solución:

```text
RF01 — Registrar una tarea válida.
RF02 — Mostrar las tareas registradas.
RF03 — Marcar una tarea como completada.
RF04 — Eliminar una tarea existente.
```

Usa frases observables. “Tener una buena interfaz” es ambiguo; “mostrar un mensaje claro cuando no existe la tarea” puede comprobarse.

# 8. Requisitos no funcionales

Describen cualidades o restricciones sin entrar en especificaciones empresariales avanzadas:

- Código organizado por responsabilidades.
- Datos persistentes cuando corresponda.
- Mensajes comprensibles.
- Pruebas automatizadas.
- Instalación y ejecución reproducibles.
- Ausencia de secretos y rutas personales.

# 9. Criterios de aceptación

Para las funcionalidades importantes utiliza una condición comprobable:

```text
Dada una tarea válida,
cuando el usuario la registra,
entonces queda disponible para consultas posteriores.
```

También diseña el error:

```text
Dado un identificador inexistente,
cuando el usuario intenta completar la tarea,
entonces recibe un mensaje claro y los datos no cambian.
```

Las historias de usuario son opcionales:

```text
Como persona que organiza tareas,
quiero consultar las pendientes,
para decidir cuál realizar después.
```

No necesitamos convertir el proyecto en un curso de Scrum.

# 10. Diseño inicial

Antes de implementar, prepara:

- Lista priorizada de funcionalidades.
- Entidades principales y sus datos.
- Flujo principal de uso.
- Estructura preliminar de módulos.
- Forma de persistencia, si aplica.
- Interfaz prevista.
- Tecnologías seleccionadas y justificación.

Un diagrama sencillo o Mermaid puede ayudar, pero es opcional.

# 11. Elegir tecnología con criterio

Cada elección debe responder a una necesidad:

```text
SQLite: necesito persistencia local, estructurada y relacional.
FastAPI: consumidores externos necesitan acceder mediante HTTP.
pandas: el objetivo central es limpiar y resumir tablas.
argparse: la solución necesita una interfaz de terminal reproducible.
```

No conviertas cualquier aplicación en API, no uses DataFrames para tres valores triviales y no introduzcas clases donde funciones claras bastan.

# 12. Rutas posibles

Puedes seguir una ruta o combinar dos cuando exista una razón clara.

## Ruta A — Aplicación CLI

Puede utilizar:

- `argparse` para la interfaz.
- JSON, CSV o SQLite para persistencia.
- `logging` para eventos importantes.
- pytest para reglas y flujo principal.

Ejemplo: gestor de inventario con CRUD local.

## Ruta B — API REST

Puede utilizar:

- FastAPI y Pydantic.
- Una capa de servicio.
- SQLite u otra persistencia acorde al alcance.
- `TestClient` para pruebas sin servidor real.

Ejemplo: API de catálogo de biblioteca.

## Ruta C — Análisis de datos

Puede utilizar:

- CSV local, pandas y NumPy.
- Funciones de carga, limpieza y resumen.
- Pruebas de transformaciones con DataFrames pequeños.

Ejemplo: analizador académico con reportes reproducibles.

## Ruta D — Automatización

Puede utilizar:

- `pathlib`, `shutil` y `argparse`.
- Dry run, backups y logging.
- `tmp_path` para probar operaciones de archivos.

Ejemplo: organizador seguro de documentos.

## Ruta E — Cliente de API

Puede utilizar:

- `requests` para HTTP.
- Dataclasses o modelos para datos.
- Variables de entorno y timeouts.
- Mocks para no depender de internet en pruebas.

Ejemplo: cliente que consulta y conserva información de un servicio.

## Ruta F — Proyecto híbrido

Combinaciones razonables incluyen API + SQLite, automatización + análisis de datos o cliente API + almacenamiento local. No combines cinco tecnologías solo para mencionarlas.

# 13. Nivel mínimo esperado

Todo proyecto debe demostrar como mínimo:

- Funciones y estructuras de datos apropiadas.
- Manejo explícito de errores previsibles.
- Módulos y organización del código.
- Type hints en las interfaces importantes.
- Pruebas automatizadas relevantes.
- README y `.gitignore`.
- Entorno y pasos de ejecución reproducibles.
- Buenas prácticas de nombres, responsabilidades y seguridad.

Persistencia, POO, APIs, concurrencia, pandas y automatización se añaden cuando el problema las necesita.

# 14. Cuándo utilizar cada capacidad

## Persistencia

Si la información debe sobrevivir a la ejecución, elige JSON para estructuras sencillas, CSV para intercambio tabular o SQLite para relaciones y consultas. No exijas una base de datos cuando un archivo basta.

## API

Crea o consume una API solamente si existe interacción mediante HTTP o una fuente externa relevante.

## POO

Usa clases cuando ayuden a representar entidades con estado y comportamiento o a intercambiar dependencias. No crees una clase por cada función.

## Análisis de datos

Usa pandas o NumPy ante procesamiento tabular o numérico significativo, no para cumplir una casilla.

## Concurrencia

Threading, multiprocessing y asyncio no son requisitos. Úsalos solo ante un problema real y después de medir o justificar el modelo de espera o cálculo.

# 15. Arquitectura base adaptable

```text
mi_proyecto/
├── README.md
├── pyproject.toml
├── .gitignore
├── src/
│   └── mi_proyecto/
│       ├── __init__.py
│       └── ...
└── tests/
```

El `src` layout es recomendable para practicar una estructura moderna, pero un proyecto pequeño puede justificar otra organización clara.

`pyproject.toml` debe indicar como mínimo nombre, versión, descripción, versión de Python y dependencias. `.gitignore` debe excluir, según corresponda:

```gitignore
.venv/
__pycache__/
*.pyc
.pytest_cache/
.coverage
.env
```

# 16. README del proyecto

Otra persona debe poder comprender y ejecutar la solución sin depender de explicaciones orales. Incluye:

1. Nombre y descripción.
2. Problema y objetivo.
3. Funcionalidades y alcance.
4. Requisitos e instalación.
5. Configuración y ejecución.
6. Pruebas.
7. Estructura.
8. Tecnologías.
9. Decisiones técnicas importantes.
10. Limitaciones y mejoras futuras.

# 17. Configuración, secretos y logging

No hardcodees secretos, credenciales, rutas personales ni URLs cambiantes. Usa argumentos, configuración o variables de entorno cuando corresponda.

Si el proyecto realiza operaciones relevantes, utiliza logging para inicio, errores y eventos útiles. No llenes los logs de ruido ni registres tokens, contraseñas o datos sensibles.

Un `.env` local puede ser útil, pero debe estar en `.gitignore`. Si documentas variables, utiliza nombres y valores ficticios.

# 18. Manejo y validación de errores

Anticipa situaciones previsibles:

- Archivo inexistente o formato inválido.
- Registro no encontrado.
- Entrada CLI incorrecta.
- Restricción de datos incumplida.
- API no disponible o respuesta inesperada.

Valida en la capa adecuada: parsing en la interfaz, reglas en dominio o servicio, Pydantic en una API y restricciones en SQLite. Evita este patrón:

```text
try:
    ejecutar_todo()
except Exception:
    pass
```

Capturar y silenciar cualquier error impide saber si el proyecto funciona.

# 19. Separación de responsabilidades

Evita un `main.py` de mil líneas. Divide según el problema:

```text
interfaz → servicio → modelo / persistencia / cliente externo
```

Un módulo `utils.py` no debe convertirse en un cajón de funciones sin relación. Prefiere nombres con propósito, como `validacion.py`, `rutas.py` o `formato_reportes.py`, solo si esas responsabilidades existen.

Funciones y métodos necesitan nombres, entradas, retornos y responsabilidad comprensibles. Usa type hints en interfaces importantes y docstrings en módulos, clases y funciones públicas; no comentes código obvio.

# 20. Pruebas automatizadas obligatorias

Usa pytest. Prueba al menos:

- Funcionalidad principal.
- Reglas de negocio.
- Casos límite.
- Errores esperados.

Diez casos relevantes pueden servir como referencia inicial, pero calidad y selección importan más que una cifra.

- Usa fixtures cuando reduzcan preparación repetida.
- Parametriza entradas equivalentes.
- Usa `tmp_path` para filesystem.
- Usa mocks para APIs, servicios o comandos externos.
- Con SQLite, usa `:memory:` o un archivo temporal.
- Con FastAPI, usa `TestClient`.
- Evita internet real cuando una dependencia puede simularse.

La cobertura ayuda a encontrar zonas no ejecutadas, pero 100 % no garantiza buenas expectativas.

# 21. Calidad del código

Antes de entregar revisa nombres, duplicación, complejidad, imports, tipos, tests y estructura. Ruff y mypy pueden ayudar si forman parte de tu entorno, pero no son obligatorios. Ninguna herramienta sustituye comprender el diseño.

# 22. Git como historial del trabajo

Desarrolla con control de versiones y commits progresivos, por ejemplo:

```text
estructura inicial
modelo de datos
persistencia
pruebas
documentación
```

No necesitas un commit por línea ni un único commit final. Las feature branches son opcionales en un proyecto individual pequeño. Nunca subas `.env`, tokens, contraseñas o claves.

# Parte II — Proceso de desarrollo

# 23. Fase 1 — Problema y alcance

Entregable: una sección del README o `problema.md` con situación, usuario, necesidad, objetivo, incluye y no incluye. No crees un archivo adicional si el README resulta suficiente.

# 24. Fase 2 — Requisitos

Escribe requisitos funcionales numerados, criterios de aceptación y restricciones. Prioriza cuáles forman parte del flujo central.

# 25. Fase 3 — Diseño

Define entidades, módulos, flujo, interfaz, persistencia e integraciones. Dibuja las dependencias importantes y justifica las tecnologías.

# 26. Fase 4 — MVP

El **producto mínimo viable** es aquí la menor versión que demuestra el flujo principal de extremo a extremo. Si construyes un inventario, comienza por registrar y consultar; no por temas visuales o exportaciones secundarias.

# 27. Fase 5 — Persistencia e integraciones

Agrega persistencia o comunicación externa si forma parte del alcance. Aísla estas dependencias para poder probar la lógica sin recursos reales.

# 28. Fase 6 — Pruebas

No dejes todas las pruebas para el final. Añádelas mientras implementas reglas, límites y errores. Ejecuta una prueba específica durante el desarrollo y la suite completa antes de integrar cambios.

# 29. Fase 7 — Refactorización

Con las pruebas pasando:

- Elimina duplicación significativa.
- Mejora nombres.
- Divide responsabilidades demasiado amplias.
- Ajusta type hints y manejo de errores.
- Elimina dependencias y código no utilizados.

# 30. Fase 8 — Documentación

Comprueba que otra persona pueda entender, instalar, configurar, ejecutar y probar usando solo el README.

# 31. Fase 9 — Entrega limpia

Prueba desde un clon o copia limpia:

1. Sigue literalmente el README.
2. Crea el entorno indicado.
3. Instala únicamente las dependencias declaradas.
4. Ejecuta el flujo principal.
5. Ejecuta todas las pruebas.
6. Verifica que no depende de archivos personales o no versionados.

Esta prueba detecta muchos casos de “funciona en mi máquina”.

# 32. Plan adaptable de seis etapas

Si necesitas una vista más compacta:

1. Problema y alcance.
2. Estructura y núcleo.
3. Persistencia o integraciones.
4. Pruebas.
5. Refactorización y calidad.
6. README y entrega.

No asignamos días obligatorios: ajusta el plan al contexto sin omitir las verificaciones.

# Parte III — Opciones concretas

# 33. Opción A — Gestor de inventario CLI

Alcance sugerido:

- Registrar, consultar, actualizar y eliminar productos.
- Interfaz con `argparse`.
- Persistencia SQLite.
- Logging y pytest.

Decide reglas de stock, errores y criterios de aceptación. No añadas usuarios, ventas y facturación si no caben en el alcance.

# 34. Opción B — API de biblioteca

Alcance sugerido:

- Registrar y consultar libros.
- Gestionar préstamos y devoluciones sencillas.
- FastAPI y Pydantic.
- Persistencia local y pruebas con `TestClient`.

No necesitas autenticación, pagos ni despliegue para demostrar el núcleo.

# 35. Opción C — Analizador académico

Alcance sugerido:

- Cargar un CSV local.
- Limpiar tipos y faltantes con reglas justificadas.
- Calcular indicadores y reportes.
- Probar transformaciones sobre DataFrames pequeños.

Conserva el dataset original y documenta qué significa cada resultado.

# 36. Opción D — Organizador de documentos

Alcance sugerido:

- Clasificar archivos por extensión.
- CLI con dry run.
- Backup y control de colisiones.
- Logging y pruebas con `tmp_path`.

Ninguna prueba debe tocar carpetas reales.

# 37. Opción E — Cliente de servicio externo

Alcance sugerido:

- Consultar una API mediante `requests`.
- Configurar URL y credenciales fuera del código.
- Aplicar timeout y manejar respuestas inválidas.
- Convertir respuestas en modelos y probar mediante mocks.

La suite no debe depender de internet.

# 38. Opción F — Proyecto híbrido

Puedes unir API + SQLite, automatización + análisis o cliente API + almacenamiento local. Cada conexión añade fallos y pruebas: combina solo lo necesario.

# 39. Ejemplo de alcance bien definido

```text
Proyecto: gestor de biblioteca local

Incluye:
- libros, préstamos y devoluciones
- persistencia SQLite
- interfaz CLI

No incluye:
- usuarios web
- pagos
- notificaciones
- múltiples sedes
```

En cambio, “sistema universitario completo con IA, aplicación móvil, pagos, chats y reconocimiento facial” mezcla demasiados dominios e integraciones. El primer trabajo técnico consiste en reducirlo.

# 40. Matriz de decisiones tecnológicas

| Necesidad | Herramienta posible |
|---|---|
| Datos simples locales | JSON |
| Datos tabulares intercambiables | CSV |
| Datos relacionales | SQLite |
| API propia | FastAPI |
| Consumir una API | requests |
| Análisis tabular | pandas |
| Cálculo numérico | NumPy |
| CLI | argparse |
| Archivos y rutas | pathlib |
| Concurrencia real | threading, multiprocessing o asyncio según el problema |
| Pruebas | pytest |

“Posible” no significa obligatoria. Documenta por qué la elección encaja mejor que una alternativa más simple.

# Parte IV — Evaluación y entrega

# 41. Rúbrica orientativa — 100 puntos

| Criterio | Puntos | Evidencia esperada |
|---|---:|---|
| Problema y alcance | 10 | Usuario, necesidad, incluye y no incluye |
| Diseño y estructura | 15 | Módulos y dependencias coherentes |
| Funcionalidad | 20 | Flujo principal completo y verificable |
| Calidad de código | 15 | Claridad, tipos y responsabilidades |
| Manejo de errores | 10 | Fallos previsibles tratados explícitamente |
| Pruebas | 15 | Casos principales, límites y errores |
| Documentación | 10 | README suficiente para usar el proyecto |
| Reproducibilidad y entrega | 5 | Instalación limpia y suite aprobada |
| **Total** | **100** | |

## Nivel excelente

Problema y alcance claros; solución coherente; código organizado; decisiones justificadas; pruebas relevantes; documentación suficiente y ejecución reproducible.

## Nivel aceptable

El flujo principal funciona, la estructura es razonable, existen pruebas básicas y el README permite instalar y ejecutar.

## Señales de problema

- Código copiado sin comprender.
- Dependencias innecesarias o no documentadas.
- Un `main` gigante y lógica mezclada con interfaz.
- Ausencia de pruebas o errores no probados.
- Secretos, rutas personales o datos reales sensibles.
- README incompleto o archivos necesarios no versionados.
- Funcionamiento exclusivo en el computador del autor.

# 42. Checklist de entrega

- [ ] El problema y el usuario están definidos.
- [ ] El alcance incluye límites explícitos.
- [ ] Las funcionalidades principales están terminadas.
- [ ] La estructura corresponde al tamaño del proyecto.
- [ ] `pyproject.toml` declara Python y dependencias.
- [ ] `.gitignore` cubre entorno, caches, cobertura y secretos locales.
- [ ] Las interfaces importantes tienen type hints.
- [ ] Los errores previsibles se manejan sin silenciarlos.
- [ ] La configuración variable no está hardcodeada.
- [ ] Las pruebas cubren núcleo, límites y errores.
- [ ] El README permite instalar, ejecutar y probar.
- [ ] No existen claves, tokens, contraseñas ni datos personales reales.
- [ ] El proyecto funciona desde una copia limpia.
- [ ] La suite completa termina correctamente.

# 43. Checklist de calidad

- [ ] Cada módulo tiene una responsabilidad reconocible.
- [ ] No existe estado global mutable innecesario.
- [ ] La lógica central está separada de `input()`, `print()` o HTTP.
- [ ] Las funciones públicas tienen nombres y contratos claros.
- [ ] Las validaciones están en la capa apropiada.
- [ ] No hay imports circulares ni dependencias sin usar.
- [ ] No existe duplicación importante sin justificación.
- [ ] Las pruebas son independientes y deterministas.
- [ ] Filesystem, bases y APIs usan recursos temporales o simulados.
- [ ] Los logs aportan contexto y no contienen secretos.
- [ ] Las dependencias son mínimas y están documentadas.
- [ ] La versión actual y las mejoras futuras están separadas.

# Parte V — Uso responsable de IA

# 44. IA como apoyo, no como garantía

Puedes utilizar IA para explicar errores, revisar código, generar ideas, proponer pruebas o mejorar documentación. Su respuesta puede contener errores, dependencias inexistentes, APIs desactualizadas o decisiones que no encajan con tu proyecto.

Debes:

- Comprender el código entregado.
- Ejecutarlo y probarlo.
- Corregirlo y adaptarlo.
- Poder explicar cada módulo y decisión.
- Declarar el uso cuando la actividad o institución lo requiera.

# 45. Verificar código generado

- [ ] ¿Entiendo cada módulo y su responsabilidad?
- [ ] ¿Ejecuté el flujo principal y los tests?
- [ ] ¿Revisé imports y APIs utilizadas?
- [ ] ¿Revisé seguridad y manejo de errores?
- [ ] ¿Revisé dependencias y su necesidad?
- [ ] ¿Revisé licencias cuando aplica?
- [ ] ¿Puedo explicar y defender las decisiones?

Código generado no equivale a código correcto. La responsabilidad de la entrega sigue siendo de quien la presenta.

# Parte VI — Plantillas copiables

# 46. Plantilla de propuesta

Copia esta estructura en tu documento de planificación o README y reemplaza las indicaciones:

```markdown
# Nombre del proyecto

## Problema

Describe la situación concreta que deseas mejorar.

## Usuario

Indica quién utilizará la solución.

## Objetivo

Expresa el resultado principal esperado.

## Alcance

### Incluye

- Funcionalidad incluida.

### No incluye

- Funcionalidad fuera de esta versión.

## Funcionalidades

- RF01 — ...
- RF02 — ...

## Tecnologías

Enumera cada tecnología y justifica su necesidad.

## Estructura propuesta

Muestra el árbol preliminar y responsabilidades.

## Estrategia de persistencia

Indica si aplica, qué opción usarás y por qué.

## Estrategia de pruebas

Describe núcleo, límites, errores y dependencias aisladas.

## Criterios de aceptación

- Dado..., cuando..., entonces...
```

# 47. Plantilla de README final

```markdown
# Nombre

## Descripción

## Características

## Tecnologías

## Requisitos

## Instalación

## Configuración

## Ejecución

## Pruebas

## Estructura

## Decisiones técnicas

## Limitaciones

## Mejoras futuras
```

# 48. Plantilla de retrospectiva

Al finalizar responde con evidencia:

- ¿Qué aprendí?
- ¿Qué fue difícil y cómo lo resolví?
- ¿Qué decisión cambiaría?
- ¿Qué mejoraría con más tiempo?
- ¿Qué quedó deliberadamente fuera del alcance?

# 49. Portafolio y demostración

El proyecto puede formar parte de tu portafolio. Su README debe ser comprensible para una docente, un compañero, una posible persona empleadora y para ti meses después.

Prepara una demostración breve:

1. Problema y usuario.
2. Arquitectura.
3. Funcionalidad principal.
4. Pruebas.
5. Una decisión técnica importante.
6. Principal aprendizaje.

Separa claramente la versión actual del trabajo futuro. Una lista honesta de limitaciones es mejor que funcionalidades incompletas presentadas como terminadas.

# 50. Errores frecuentes

- Empezar a programar sin definir el problema.
- Elegir un alcance demasiado grande.
- Usar todas las tecnologías por obligación.
- Diseñar arquitectura compleja para un proyecto pequeño.
- No construir primero un MVP.
- Empezar por funciones secundarias.
- No usar Git progresivamente o hacer un único commit final.
- Dejar pruebas para el final o no probar errores.
- Hardcodear rutas, URLs o configuración.
- Guardar secretos o datos personales reales.
- Omitir dependencias o archivos necesarios del README.
- Usar bases reales o APIs de internet en pruebas.
- Mezclar lógica, persistencia e interfaz.
- Perseguir sofisticación en lugar de resolver el problema.
- Entregar código que no puedes explicar.

# 51. Relación con las unidades anteriores

| Necesito revisar… | Unidad |
|---|---|
| Fundamentos, control, colecciones y funciones | [Unidad 1](../unidad01-fundamentos/), [Unidad 2](../unidad02-control-flujo/), [Unidad 3](../unidad03-colecciones/) y [Unidad 4](../unidad04-funciones/) |
| Cadenas y archivos | [Unidad 5](../unidad05-cadenas-archivos/) |
| Errores y excepciones | [Unidad 6](../unidad06-excepciones/) |
| POO | [Unidad 7](../unidad07-poo/) y [Unidad 8](../unidad08-poo-avanzada/) |
| Módulos y proyectos | [Unidad 9](../unidad09-modulos-proyectos/) |
| Programación funcional | [Unidad 10](../unidad10-python-funcional/) |
| Python avanzado | [Unidad 11](../unidad11-python-avanzado/) |
| Tipado y calidad | [Unidad 12](../unidad12-tipado-buenas-practicas/) |
| Pruebas automatizadas | [Unidad 13](../unidad13-pruebas/) |
| Bases de datos | [Unidad 14](../unidad14-bases-datos/) |
| Consumir APIs | [Unidad 15](../unidad15-consumo-apis/) |
| Crear APIs | [Unidad 16](../unidad16-creacion-apis/) |
| Concurrencia | [Unidad 17](../unidad17-concurrencia/) |
| Análisis de datos | [Unidad 18](../unidad18-datos/) |
| Automatización | [Unidad 19](../unidad19-automatizacion/) |
| Estructura profesional | [Unidad 20](../unidad20-python-profesional/) |

# 52. Autoevaluación final del curso

- [ ] Puedo leer y explicar código Python acorde a mi nivel.
- [ ] Puedo escribir programas y dividir problemas en partes.
- [ ] Selecciono colecciones y estructuras apropiadas.
- [ ] Manejo errores y depuro con evidencia.
- [ ] Leo, transformo y valido datos.
- [ ] Elijo una persistencia proporcional al problema.
- [ ] Escribo pruebas útiles y aisladas.
- [ ] Organizo módulos y proyectos reproducibles.
- [ ] Puedo consumir servicios externos de forma controlada.
- [ ] Puedo crear una API cuando el problema lo requiere.
- [ ] Automatizo tareas con controles de seguridad.
- [ ] Documento instalación, uso, pruebas y decisiones.
- [ ] Mantengo secretos fuera del repositorio.
- [ ] Puedo refactorizar y mantener una solución existente.

# 53. ¿Qué aprender después?

Estas son rutas posibles, no una secuencia obligatoria:

## Desarrollo backend

FastAPI con mayor profundidad, SQLAlchemy, PostgreSQL y más adelante Docker.

## Datos

pandas avanzado, visualización, estadística y, después de las bases necesarias, scikit-learn.

## Automatización

Integración con APIs, herramientas del sistema y pipelines controlados.

## Calidad y plataforma

CI/CD, packaging, profiling y observabilidad.

## Inteligencia artificial

NumPy y pandas sólidos, fundamentos matemáticos y machine learning.

# 54. Cierre del curso

Completar las unidades no significa conocer todo Python. Significa haber construido una base para leer documentación, aprender bibliotecas nuevas, comprender proyectos existentes y resolver problemas con criterio.

Tu proyecto final no necesita ser perfecto. Debe ser coherente, verificable y comprensible, y debe mostrar las decisiones que ahora eres capaz de tomar.

---

# 🧭 Navegación

⬅️ [Volver a la Unidad 20 — Python profesional](../unidad20-python-profesional/)

🏠 [Volver al inicio del curso](../README.md)

## 🎓 Curso completado

Has recorrido la ruta completa. Conserva la práctica de ejecutar, observar, probar, documentar y mejorar: ahí continúa el aprendizaje.


---

## Continuar el curso

- **Unidad anterior:** [Unidad 20 — Python profesional](../unidad20-python-profesional/README.md)
- **Volver al índice:** [Todas las unidades](../README.md)

Llegaste a la última unidad. Revisa tu proyecto y la lista de comprobación antes de dar por terminado el curso.
