# Unidad 0 — Preparación del entorno

Antes de comenzar a programar necesitamos preparar las herramientas que utilizaremos durante el curso.

En esta unidad aprenderás qué es Python, cómo instalarlo en tu computador, cómo preparar Visual Studio Code y cómo ejecutar tu primer programa.

No necesitas tener conocimientos previos de programación.

---

## 🎯 Objetivos de aprendizaje

Al finalizar esta unidad podrás:

- Explicar de manera general qué es Python y para qué se utiliza.
- Instalar Python en Windows, Linux o macOS.
- Comprobar desde la terminal que Python está instalado correctamente.
- Instalar y preparar Visual Studio Code para trabajar con Python.
- Seleccionar el intérprete de Python en Visual Studio Code.
- Crear archivos con extensión `.py`.
- Ejecutar programas de Python desde Visual Studio Code y desde la terminal.
- Reconocer la función básica de `pip`.
- Identificar algunos errores frecuentes relacionados con la instalación y ejecución de Python.

---

## 📋 Antes de comenzar

Para realizar esta unidad necesitarás:

- Un computador con Windows, Linux o macOS.
- Conexión a Internet para descargar las herramientas.
- Permisos para instalar programas en el computador.

> **Importante:** no necesitas tener Python instalado previamente. En esta unidad realizaremos todo el proceso.

---

# 1. ¿Qué es Python?

Python es un **lenguaje de programación de propósito general**. Esto significa que puede utilizarse para desarrollar muchos tipos diferentes de soluciones.

Por ejemplo, Python se utiliza en:

- Desarrollo de aplicaciones.
- Automatización de tareas.
- Desarrollo web.
- Análisis y procesamiento de datos.
- Inteligencia artificial y aprendizaje automático.
- Computación científica.
- Pruebas de software.
- Robótica e Internet de las cosas.

Una de las características que hace a Python especialmente apropiado para comenzar a programar es que su sintaxis suele ser clara y permite expresar muchas instrucciones con relativamente pocas líneas de código.

Por ejemplo, para mostrar un mensaje en pantalla podemos escribir:

```python
print("Hola, Python")
```

No necesitas comprender todavía todos los elementos de esta instrucción.

Por ahora observa que podemos pedirle al computador que muestre el mensaje:

```text
Hola, Python
```

A lo largo de las siguientes unidades aprenderás exactamente qué significa cada parte del código.

---

## 🐍 ¿Por qué aprender Python?

Python permite comenzar con programas sencillos y posteriormente utilizar el mismo lenguaje para desarrollar proyectos mucho más complejos.

Durante este curso comenzaremos con instrucciones como:

```python
nombre = "Ana"
print(nombre)
```

y progresivamente aprenderemos a trabajar con estructuras de datos, funciones, objetos, archivos, bases de datos, APIs, pruebas, automatización y otras herramientas utilizadas en proyectos reales.

Por eso, el objetivo no será solamente aprender la sintaxis del lenguaje, sino aprender a **resolver problemas utilizando Python**.

---

## 🔎 Antes de instalar

Es posible que tu computador ya tenga Python instalado.

Antes de descargar cualquier programa, en la siguiente sección comprobaremos si Python se encuentra disponible en tu sistema.

---

# 2. Comprobar si Python ya está instalado

Antes de instalar Python, es conveniente verificar si ya se encuentra disponible en el computador.

La forma de comprobarlo depende del sistema operativo.

---

## 🪟 Windows

Abre **PowerShell** o **Símbolo del sistema**.

Puedes buscar cualquiera de estas herramientas desde el menú Inicio.

Luego escribe:

```bash
python --version
```

Si Python está instalado correctamente, deberías obtener una respuesta similar a:

```text
Python 3.13.0
```

También puedes probar:

```bash
py --version
```

En algunos computadores con Windows, Python se ejecuta utilizando el comando `py`.

### ¿Qué pasa si no aparece la versión?

Si obtienes un mensaje indicando que el comando no existe, Python probablemente no está instalado o no está agregado correctamente a las variables del sistema.

No te preocupes. En la siguiente sección veremos cómo instalarlo.

---

## 🐧 Linux

Abre una terminal y ejecuta:

```bash
python3 --version
```

En muchas distribuciones Linux, Python 3 se utiliza mediante el comando:

```text
python3
```

Si está instalado, deberías ver algo similar a:

```text
Python 3.12.3
```

También puedes comprobar:

```bash
python --version
```

Sin embargo, dependiendo de la distribución, este comando puede no existir.

> **Importante:** en Linux es habitual utilizar `python3` en lugar de `python`.

---

## 🍎 macOS

Abre la aplicación **Terminal** y ejecuta:

```bash
python3 --version
```

Si Python está instalado, aparecerá una versión similar a:

```text
Python 3.12.3
```

En versiones actuales de macOS, normalmente se utiliza el comando:

```text
python3
```

---

## 🔢 ¿Qué versión de Python necesito?

Para este curso utilizaremos **Python 3**.

No es necesario que tengas exactamente la misma versión que aparece en los ejemplos.

Por ejemplo:

```text
Python 3.11.x
Python 3.12.x
Python 3.13.x
```

Lo importante es utilizar una versión moderna de Python 3.

---

## ✅ Si Python ya está instalado

Si el comando muestra correctamente una versión de Python 3, puedes continuar con las siguientes secciones.

No necesitas reinstalar Python.

---

## ❌ Si Python no está instalado

Si el sistema indica que no reconoce el comando, continúa con la siguiente sección:

**3. Instalar Python**

---

# 3. Instalar Python

Si en la sección anterior comprobaste que ya tienes una versión moderna de Python 3 instalada, puedes pasar directamente a la sección 4.

Si Python no está instalado, sigue las instrucciones correspondientes a tu sistema operativo.

---

## 🪟 Windows

### Paso 1. Descargar Python

Ingresa al sitio oficial:

[Descargar Python desde el sitio oficial](https://www.python.org/downloads/)

La página normalmente detectará que estás utilizando Windows y mostrará una opción para descargar una versión actual de Python 3.

Descarga el instalador.

### Paso 2. Ejecutar el instalador

Abre el archivo descargado.

Antes de comenzar la instalación, presta especial atención a la opción:

```text
Add python.exe to PATH
```

Marca esta opción antes de continuar.

> **¿Por qué es importante?**  
> Agregar Python al `PATH` permite ejecutar el comando `python` desde la terminal sin tener que indicar manualmente dónde está instalado.

Luego continúa con la instalación y espera a que finalice.

### Paso 3. Comprobar la instalación

Cierra las terminales que estuvieran abiertas anteriormente y abre una nueva ventana de PowerShell o Símbolo del sistema.

Ejecuta:

```bash
python --version
```

También puedes comprobar el lanzador de Python para Windows:

```bash
py --version
```

Si aparece una versión de Python 3, la instalación fue realizada correctamente.

---

## 🐧 Linux

Muchas distribuciones Linux ya incluyen Python 3.

Primero compruébalo:

```bash
python3 --version
```

Si utilizas **Ubuntu o una distribución basada en Debian** y Python 3 no está instalado, actualiza la información de los paquetes:

```bash
sudo apt update
```

Luego instala Python 3:

```bash
sudo apt install python3
```

Comprueba la instalación:

```bash
python3 --version
```

### Instalar pip y soporte para entornos virtuales

En Ubuntu y distribuciones basadas en Debian puedes instalar las herramientas necesarias mediante:

```bash
sudo apt install python3-pip python3-venv
```

Luego comprueba `pip` con:

```bash
python3 -m pip --version
```

> Más adelante utilizaremos entornos virtuales para instalar paquetes de forma aislada y evitar modificar innecesariamente la instalación principal de Python del sistema.

> **Importante:** otras distribuciones Linux pueden utilizar gestores de paquetes diferentes. Si no utilizas Ubuntu o Debian, consulta la documentación de tu distribución antes de ejecutar comandos de instalación.

---

## 🍎 macOS

Primero comprueba si Python 3 ya está disponible:

```bash
python3 --version
```

Si necesitas instalarlo, utiliza el sitio oficial:

[Descargar Python para macOS](https://www.python.org/downloads/macos/)

Descarga una versión actual de Python 3 compatible con tu equipo y sigue las instrucciones del instalador.

Cuando termine, abre una nueva Terminal y ejecuta:

```bash
python3 --version
```

Si aparece una versión de Python 3, la instalación fue realizada correctamente.

---

## 📦 Comprobar pip

Python dispone de un administrador de paquetes llamado **pip**.

Más adelante utilizaremos `pip` para instalar paquetes desarrollados por terceros.

Por ahora solamente comprobaremos que está disponible.

### Windows

Ejecuta:

```bash
python -m pip --version
```

o:

```bash
py -m pip --version
```

### Linux y macOS

Ejecuta:

```bash
python3 -m pip --version
```

Si todo está correctamente configurado, obtendrás información sobre la versión instalada de `pip`.

No necesitas instalar ningún paquete todavía.

---

## ✅ Comprobación final

Antes de continuar, asegúrate de obtener una respuesta correcta al consultar la versión de Python.

### Windows

```bash
python --version
```

o:

```bash
py --version
```

### Linux y macOS

```bash
python3 --version
```

Si aparece:

```text
Python 3.x.x
```

ya tienes el intérprete de Python preparado.

---

# 4. Preparar Visual Studio Code

Aunque es posible escribir programas de Python utilizando diferentes editores, durante este curso utilizaremos **Visual Studio Code (VS Code)**.

Visual Studio Code es un editor de código que permite trabajar con diferentes lenguajes de programación y ampliar sus funcionalidades mediante extensiones.

---

## 4.1 Instalar Visual Studio Code

Ingresa al sitio oficial:

[Descargar Visual Studio Code](https://code.visualstudio.com/)

Selecciona la descarga correspondiente a tu sistema operativo:

- Windows.
- Linux.
- macOS.

Realiza la instalación siguiendo las instrucciones proporcionadas por el instalador.

> Si ya tienes Visual Studio Code instalado, no necesitas instalarlo nuevamente.

---

## 4.2 Abrir Visual Studio Code

Una vez instalado, inicia Visual Studio Code.

Durante el curso utilizaremos principalmente:

- **Explorador:** permite visualizar las carpetas y archivos del proyecto.
- **Editor:** espacio donde escribiremos el código.
- **Terminal integrada:** permite ejecutar comandos sin salir de Visual Studio Code.
- **Extensiones:** permite agregar herramientas para trabajar con diferentes lenguajes.

No necesitas conocer todas las opciones desde el comienzo.

---

## 4.3 Instalar la extensión de Python

En la barra lateral izquierda, selecciona el icono de **Extensiones**.

También puedes utilizar:

### Windows y Linux

```text
Ctrl + Shift + X
```

### macOS

```text
Cmd + Shift + X
```

En el buscador escribe:

```text
Python
```

Busca la extensión llamada:

```text
Python
```

publicada por:

```text
Microsoft
```

Selecciona **Install** o **Instalar**.

> **Importante:** instalar la extensión de Python en Visual Studio Code no instala Python en el computador. Son elementos diferentes.

---

## 4.4 Seleccionar el intérprete de Python

Visual Studio Code necesita saber qué instalación de Python utilizará para ejecutar tus programas.

Abre la paleta de comandos.

### Windows y Linux

```text
Ctrl + Shift + P
```

### macOS

```text
Cmd + Shift + P
```

Escribe:

```text
Python: Select Interpreter
```

Selecciona una versión de Python 3 instalada en tu computador.

Por ejemplo:

```text
Python 3.12.x
Python 3.13.x
```

Si solamente aparece una instalación de Python 3, puedes seleccionarla.

> Más adelante, cuando trabajemos con entornos virtuales, aprenderemos a seleccionar un intérprete específico para cada proyecto.

---

## 4.5 ¿Para qué sirve la extensión?

La extensión facilita el desarrollo de programas en Python y proporciona herramientas como:

- Reconocimiento de archivos `.py`.
- Resaltado de sintaxis.
- Asistencia al escribir código.
- Detección de algunos errores.
- Ejecución de programas.
- Selección del intérprete de Python.
- Herramientas de depuración.
- Soporte para entornos virtuales.

No necesitas aprender a utilizar todas estas herramientas todavía.

Las iremos incorporando progresivamente.

---

## 4.6 Crear nuestra carpeta de trabajo

Crea una carpeta en una ubicación fácil de encontrar, por ejemplo en **Documentos**.

Puedes llamarla:

```text
curso-python
```

Ahora abre Visual Studio Code y selecciona:

```text
Archivo → Abrir carpeta
```

Busca la carpeta `curso-python` y ábrela.

A partir de este momento, esta carpeta será nuestro espacio de trabajo.

---

## 4.7 Crear el primer archivo de Python

En el Explorador de Visual Studio Code, crea un archivo llamado:

```text
hola.py
```

La extensión:

```text
.py
```

indica que se trata de un archivo de código fuente de Python.

Escribe:

```python
print("Hola, Python")
```

Guarda los cambios.

### Windows y Linux

```text
Ctrl + S
```

### macOS

```text
Cmd + S
```

¡Ya escribiste tu primer programa en Python!

Todavía falta algo importante: **ejecutarlo**.

---

# 5. Ejecutar nuestro primer programa

Antes de utilizar los botones de ejecución de Visual Studio Code, aprenderemos a ejecutar el programa desde la terminal.

Esto te ayudará a comprender qué ocurre realmente cuando se ejecuta un archivo de Python.

---

## 5.1 Abrir la terminal integrada

En Visual Studio Code selecciona:

```text
Terminal → Nueva terminal
```

La terminal aparecerá normalmente en la parte inferior de la ventana.

Comprueba que se encuentre ubicada dentro de la carpeta `curso-python`.

---

## 5.2 Ejecutar el programa en Windows

Escribe:

```bash
python hola.py
```

Si tu instalación utiliza el lanzador de Python para Windows, también puedes ejecutar:

```bash
py hola.py
```

---

## 5.3 Ejecutar el programa en Linux o macOS

Escribe:

```bash
python3 hola.py
```

---

## 5.4 Resultado esperado

Deberías obtener:

```text
Hola, Python
```

Si aparece este mensaje, acabas de completar el ciclo fundamental de programación:

```text
Escribir código
      ↓
Guardar el archivo
      ↓
Ejecutar el programa
      ↓
Observar el resultado
```

Este proceso se repetirá constantemente durante el curso.

---

## 💡 Experimenta

Modifica el programa:

```python
print("Estoy aprendiendo Python")
print("Este es mi primer programa")
```

Guarda nuevamente el archivo y ejecútalo.

Deberías obtener:

```text
Estoy aprendiendo Python
Este es mi primer programa
```

Acabas de comprobar algo muy importante:

**cuando modificas el código, debes guardar el archivo y volver a ejecutarlo para observar el nuevo resultado.**

---

# 6. Python, el intérprete y la terminal

Ya logramos ejecutar nuestro primer programa, pero antes de continuar es importante comprender qué ocurrió cuando escribimos:

```bash
python hola.py
```

o:

```bash
python3 hola.py
```

---

## 6.1 ¿Qué es el intérprete de Python?

El archivo `hola.py` contiene nuestras instrucciones:

```python
print("Hola, Python")
```

El computador necesita un programa capaz de interpretar esas instrucciones.

Ese programa es el **intérprete de Python**.

De manera simplificada:

```text
hola.py
   ↓
Intérprete de Python
   ↓
Ejecución de las instrucciones
   ↓
Resultado
```

Cuando ejecutamos:

```bash
python hola.py
```

estamos indicando:

> Utiliza Python para ejecutar las instrucciones almacenadas en el archivo `hola.py`.

---

## 6.2 ¿Qué es la terminal?

La **terminal** es una herramienta que permite comunicarnos con el sistema mediante comandos escritos.

Por ejemplo:

```bash
python hola.py
```

es un comando.

Más adelante utilizaremos la terminal para:

- Ejecutar programas.
- Instalar paquetes.
- Crear entornos virtuales.
- Ejecutar pruebas.
- Iniciar servidores.
- Administrar dependencias.

No necesitas memorizar todos los comandos desde ahora.

---

## 6.3 ¿Por qué aparecen `python`, `python3` y `py`?

Dependiendo del sistema operativo y de la forma en que Python fue instalado, puedes encontrar diferentes comandos.

### Windows

```bash
python programa.py
```

o:

```bash
py programa.py
```

### Linux

```bash
python3 programa.py
```

### macOS

```bash
python3 programa.py
```

Lo importante es identificar cuál funciona correctamente en tu computador.

---

## 6.4 Comprueba cuál funciona en tu computador

### Windows

```bash
python --version
```

o:

```bash
py --version
```

### Linux y macOS

```bash
python3 --version
```

El comando que muestre correctamente una versión de Python 3 será el que puedas utilizar para ejecutar tus programas.

---

## 6.5 Ejecutar Python sin indicar un archivo

También podemos iniciar directamente el intérprete.

### Windows

```bash
python
```

o:

```bash
py
```

### Linux y macOS

```bash
python3
```

Podrás observar algo similar a:

```text
Python 3.x.x
>>>
```

El símbolo:

```text
>>>
```

indica que Python está esperando una instrucción.

Escribe:

```python
print("Hola desde el intérprete")
```

y presiona Enter.

Python ejecutará inmediatamente:

```text
Hola desde el intérprete
```

---

## 6.6 Modo interactivo y archivos `.py`

Existen dos formas básicas de ejecutar código Python.

### Modo interactivo

Escribimos instrucciones directamente después de:

```text
>>>
```

Python las ejecuta inmediatamente.

Este modo es útil para realizar pequeñas pruebas.

### Archivo de Python

Escribimos instrucciones dentro de un archivo:

```text
hola.py
```

y posteriormente ejecutamos el archivo completo.

Por ejemplo:

```bash
python hola.py
```

o:

```bash
python3 hola.py
```

Durante el curso trabajaremos principalmente con **archivos `.py`**, porque permiten guardar, modificar y organizar nuestros programas.

---

## 6.7 ¿Cómo salir del intérprete?

Si estás viendo:

```text
>>>
```

significa que te encuentras dentro del intérprete de Python.

Puedes salir escribiendo:

```python
exit()
```

y presionando Enter.

Volverás a la terminal normal.

> **Consejo:** observa siempre si estás en la terminal del sistema o dentro del intérprete de Python. Confundir estos dos espacios es uno de los errores más frecuentes cuando se comienza a programar.

---

## 🧪 Prueba rápida

Antes de continuar:

1. Abre la terminal.
2. Inicia el intérprete de Python.
3. Ejecuta:

```python
print("Python está funcionando")
```

4. Sal utilizando:

```python
exit()
```

5. Ejecuta nuevamente tu archivo `hola.py`.

Si puedes realizar ambos procedimientos, ya comprendes la diferencia básica entre **ejecutar instrucciones interactivamente** y **ejecutar un archivo de Python**.

---

# 7. Introducción a pip

Hasta ahora hemos trabajado únicamente con herramientas incluidas en Python.

Sin embargo, existen miles de paquetes desarrollados por otras personas y organizaciones que podemos incorporar a nuestros proyectos.

Para instalar y administrar muchos de estos paquetes utilizaremos **pip**.

---

## 7.1 ¿Qué es pip?

`pip` es el administrador de paquetes utilizado habitualmente en Python.

Nos permite instalar paquetes que no forman parte necesariamente de la biblioteca estándar de Python.

Más adelante utilizaremos paquetes para trabajar con:

- APIs.
- Pruebas automatizadas.
- Análisis de datos.
- Desarrollo de servicios web.

De manera simplificada:

```text
Nuestro programa
      +
Paquetes externos
      ↓
Nuevas funcionalidades
```

---

## 7.2 Comprobar que pip está disponible

### Windows

```bash
python -m pip --version
```

o:

```bash
py -m pip --version
```

### Linux y macOS

```bash
python3 -m pip --version
```

Obtendrás una respuesta similar a:

```text
pip 25.x from ... (python 3.x)
```

Los números exactos pueden ser diferentes.

---

## 7.3 ¿Por qué utilizamos `python -m pip`?

También puedes encontrar en Internet comandos como:

```bash
pip install paquete
```

o:

```bash
pip3 install paquete
```

Sin embargo, durante este curso utilizaremos preferentemente:

```bash
python -m pip
```

o:

```bash
python3 -m pip
```

Esto ayuda a indicar explícitamente qué instalación de Python debe ejecutar `pip`, algo especialmente útil cuando existen varias versiones o entornos de Python en el mismo computador.

---

## 7.4 ¿Cómo se instala un paquete?

La estructura general es:

```bash
python -m pip install nombre-paquete
```

En Linux o macOS:

```bash
python3 -m pip install nombre-paquete
```

Por ejemplo:

```bash
python -m pip install requests
```

Esto solicitaría a `pip` instalar el paquete llamado `requests`.

> **Por ahora no ejecutes este comando.** Lo utilizaremos más adelante cuando aprendamos a consumir APIs y ya conozcamos los entornos virtuales.

---

## 7.5 ¿De dónde obtiene pip los paquetes?

De manera predeterminada, `pip` obtiene paquetes desde **PyPI (Python Package Index)**, un repositorio público de software para Python.

Antes de incorporar una dependencia a un proyecto es conveniente revisar:

- Qué problema resuelve.
- Su documentación.
- Quién la mantiene.
- Si continúa recibiendo mantenimiento.
- Si realmente la necesitamos.

---

## 7.6 Python no es lo mismo que pip

Es importante distinguirlos:

```text
Python
│
└── Ejecuta nuestros programas

pip
│
└── Ayuda a instalar y administrar paquetes de Python
```

Por ejemplo:

```bash
python programa.py
```

ejecuta un programa.

Mientras que:

```bash
python -m pip install nombre-paquete
```

instala un paquete.

Son operaciones diferentes.

---

## 7.7 ¿Debemos instalar todos los paquetes globalmente?

No.

Cuando comencemos a desarrollar proyectos que necesiten paquetes externos aprenderemos a utilizar **entornos virtuales**.

Un entorno virtual permite que cada proyecto tenga sus propias dependencias:

```text
Proyecto A
└── sus paquetes

Proyecto B
└── sus paquetes

Proyecto C
└── sus paquetes
```

Más adelante aprenderemos a crearlos y utilizarlos correctamente.

Por ahora, lo importante es saber que `pip` existe y comprobar que puedes acceder a él.

---

## ✅ Comprobación

Antes de continuar, intenta responder:

1. ¿Qué es `pip`?
2. ¿Para qué sirve?
3. ¿Es lo mismo ejecutar un programa que instalar un paquete?
4. ¿Por qué no es conveniente instalar paquetes innecesariamente?

Si puedes responderlas, ya tienes suficiente conocimiento sobre `pip` para continuar.

---

# 8. Errores frecuentes y cómo solucionarlos

Cuando comenzamos a programar es normal encontrar errores.

Un error puede deberse al código, a la instalación, al comando utilizado, a la ubicación del archivo o incluso a que olvidamos guardar los cambios.

Aprender a leer los mensajes de error y buscar su causa forma parte del aprendizaje de programación.

---

## 8.1 El comando `python` no funciona

Puedes encontrar mensajes similares a:

```text
python: command not found
```

o en Windows:

```text
'python' no se reconoce como un comando interno o externo
```

Esto puede ocurrir porque:

- Python no está instalado.
- Python no está configurado correctamente en el `PATH`.
- Tu sistema utiliza otro comando.

### ¿Qué puedes hacer?

En Windows:

```bash
py --version
```

En Linux o macOS:

```bash
python3 --version
```

Si alguno muestra una versión de Python 3, utiliza ese comando.

---

## 8.2 Windows muestra "Python was not found"

En algunos equipos con Windows, al ejecutar:

```bash
python
```

puede aparecer un mensaje indicando que Python no fue encontrado o puede abrirse Microsoft Store.

Primero comprueba:

```bash
py --version
```

Si funciona, puedes utilizar:

```bash
py hola.py
```

Si tampoco funciona, revisa la instalación de Python.

---

## 8.3 Python está instalado, pero el comando sigue sin funcionar

Una posible causa es que Python no se encuentre correctamente agregado al `PATH`.

El `PATH` permite que el sistema localice programas ejecutables desde la terminal.

En Windows, durante la instalación es recomendable marcar:

```text
Add python.exe to PATH
```

Si acabas de instalar Python, cierra la terminal y abre una nueva antes de probar nuevamente:

```bash
python --version
```

---

## 8.4 Aparece `SyntaxError` al escribir un comando

Imagina que estás viendo:

```text
>>>
```

y escribes:

```text
>>> python hola.py
```

El problema es que:

```bash
python hola.py
```

es un **comando de terminal**, no una instrucción de Python.

Recuerda:

```text
Terminal del sistema
--------------------
python hola.py
python3 hola.py
python -m pip --version
```

Mientras que dentro de:

```text
>>>
```

escribimos código Python:

```python
print("Hola")
```

Si estás dentro del intérprete, sal utilizando:

```python
exit()
```

---

## 8.5 Python no encuentra el archivo

Puedes encontrar:

```text
can't open file 'hola.py'
```

Una causa frecuente es que la terminal se encuentre en una carpeta diferente de aquella donde guardaste el archivo.

Por ejemplo:

```text
curso-python/
└── hola.py
```

La terminal debe estar ubicada en `curso-python` para ejecutar directamente:

```bash
python hola.py
```

o:

```bash
python3 hola.py
```

---

## 8.6 El programa sigue mostrando el resultado anterior

Si modificaste el archivo pero continúa apareciendo el resultado anterior, comprueba que hayas guardado los cambios.

### Windows y Linux

```text
Ctrl + S
```

### macOS

```text
Cmd + S
```

Después vuelve a ejecutar el programa.

---

## 8.7 Escribí `Print` y Python muestra un error

Python distingue entre mayúsculas y minúsculas.

Esto funciona:

```python
print("Hola")
```

Esto no representa la misma instrucción:

```python
Print("Hola")
```

Python es un lenguaje **sensible a mayúsculas y minúsculas** (*case-sensitive*).

---

## 8.8 Olvidé cerrar las comillas

Este código es incorrecto:

```python
print("Hola)
```

La forma correcta es:

```python
print("Hola")
```

Cuando existe un problema de sintaxis, Python suele mostrar información sobre la ubicación aproximada donde detectó el error.

Intenta leer el mensaje antes de modificar el código.

---

## 8.9 Escribí mal el nombre del archivo

Si el archivo se llama:

```text
hola.py
```

debes utilizar exactamente ese nombre:

```bash
python hola.py
```

Escribir:

```bash
python saludo.py
```

no funcionará si `saludo.py` no existe.

---

## 8.10 El archivo terminó como `hola.py.txt`

Este problema puede presentarse especialmente en Windows.

Aunque visualmente parezca llamarse:

```text
hola.py
```

su nombre real podría ser:

```text
hola.py.txt
```

Para evitarlo, crea los archivos directamente desde Visual Studio Code y verifica que tengan extensión:

```text
.py
```

---

## 8.11 `pip` no funciona

Si:

```bash
pip --version
```

no funciona, prueba utilizando Python directamente.

### Windows

```bash
python -m pip --version
```

o:

```bash
py -m pip --version
```

### Linux y macOS

```bash
python3 -m pip --version
```

Esta será la forma que preferiremos durante el curso.

---

## 8.12 ¿Qué hago cuando aparece un error que no conozco?

Sigue este procedimiento:

1. Lee completamente el mensaje de error.
2. Identifica el archivo donde ocurrió.
3. Observa si Python indica un número de línea.
4. Revisa esa línea y las inmediatamente anteriores.
5. Comprueba nombres, paréntesis, comillas y escritura.
6. Verifica que guardaste el archivo.
7. Ejecuta nuevamente el programa.
8. Si el problema continúa, busca el significado del mensaje de error.

---

## 💡 Una buena costumbre

Evita describir un problema únicamente como:

> "Python no funciona".

Intenta ser más específico:

```text
El comando python no es reconocido.
```

```text
Python no encuentra el archivo hola.py.
```

```text
Mi programa muestra un SyntaxError en la línea 3.
```

```text
El programa se ejecuta, pero el resultado no es el esperado.
```

Describir correctamente un problema facilita encontrar su causa y solucionarlo.

---

# 9. Reto de la unidad — Mi primer programa

Ha llegado el momento de comprobar que tu entorno de trabajo está preparado.

Crea un archivo llamado:

```text
presentacion.py
```

El programa debe mostrar:

- Tu nombre.
- Un mensaje indicando que estás aprendiendo Python.
- Algo que te gustaría aprender a desarrollar con este lenguaje.

Puedes utilizar varias instrucciones `print()`.

Por ejemplo:

```python
print("Mi nombre es Laura")
print("Estoy aprendiendo Python")
print("Quiero aprender a desarrollar aplicaciones")
```

> No copies necesariamente el ejemplo. Personaliza los mensajes.

---

## ▶️ Ejecuta tu programa

### Windows

```bash
python presentacion.py
```

o:

```bash
py presentacion.py
```

### Linux y macOS

```bash
python3 presentacion.py
```

Si aparecen correctamente tus tres mensajes, el reto está funcionando.

---

## 🧪 Experimenta

Agrega al menos dos mensajes adicionales.

Por ejemplo:

- Tu ciudad.
- Una tecnología que te interese.
- Una actividad que disfrutes.
- Una expectativa sobre el curso.

Ejecuta nuevamente el programa.

Recuerda el ciclo:

```text
Modificar
   ↓
Guardar
   ↓
Ejecutar
   ↓
Observar
   ↓
Volver a modificar
```

Experimentar con el código será una parte fundamental de tu aprendizaje.

---

# 10. Comprobación de aprendizaje

Antes de avanzar, comprueba que puedes:

- [ ] Identificar qué es Python.
- [ ] Comprobar qué versión de Python está instalada.
- [ ] Abrir Visual Studio Code.
- [ ] Instalar la extensión oficial de Python.
- [ ] Seleccionar un intérprete de Python.
- [ ] Crear una carpeta de trabajo.
- [ ] Crear un archivo con extensión `.py`.
- [ ] Escribir una instrucción `print()`.
- [ ] Guardar un archivo.
- [ ] Abrir la terminal integrada de Visual Studio Code.
- [ ] Ejecutar un archivo de Python desde la terminal.
- [ ] Diferenciar la terminal del intérprete interactivo.
- [ ] Identificar qué comando utilizas: `python`, `python3` o `py`.
- [ ] Explicar de manera general para qué sirve `pip`.
- [ ] Leer un mensaje de error antes de intentar solucionarlo.

Si todavía tienes dificultades con alguno de estos puntos, revisa la sección correspondiente antes de continuar.

---

# 11. Lo que aprendimos

En esta unidad preparaste las herramientas necesarias para comenzar a programar.

Ya sabes que:

```text
Código fuente (.py)
        ↓
Intérprete de Python
        ↓
Ejecución
        ↓
Resultado
```

También aprendiste que la terminal será una herramienta importante durante el curso y conociste por primera vez `pip`.

Lo más importante es que ya puedes escribir:

```python
print("Estoy listo para aprender Python")
```

y ejecutar ese programa en tu computador.

A partir de la siguiente unidad comenzaremos a estudiar formalmente el lenguaje.

---

# ➡️ Siguiente unidad

Continúa con:

👉 [Unidad 1 — Fundamentos de Python](../unidad01-fundamentos/)

En la siguiente unidad aprenderás sobre:

- Sintaxis básica.
- Comentarios.
- Variables.
- Tipos de datos.
- Entrada y salida de información.
- Operadores.
- Conversión de tipos.

---

[⬅️ Volver al inicio del curso](../README.md)