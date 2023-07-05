# Clase 1: Instalación de Python y entorno de desarrollo

En este módulo, aprenderemos cómo instalar Python en tu sistema y configurar un entorno de desarrollo adecuado para programar en Python.

### Instalación de Python

1. **Descarga Python:** Ve al sitio web oficial de Python en https://www.python.org/downloads/ y descarga la última versión estable de Python según tu sistema operativo.

2. **Ejecuta el instalador:** Una vez que se haya completado la descarga, ejecuta el archivo de instalación y sigue las instrucciones del instalador.

3. **Configuración de Python:** Durante el proceso de instalación, asegúrate de marcar la opción "Agregar Python al PATH" o "Agregar Python a la variable de entorno". Esto permitirá acceder a Python desde cualquier ubicación en la línea de comandos.

4. **Verificación de la instalación:** Abre la línea de comandos (Terminal en macOS/Linux, Command Prompt en Windows) y escribe el siguiente comando:

   ```shell
   python --version
   ```

   Deberías ver la versión de Python instalada en tu sistema.

### Entorno de desarrollo

Un entorno de desarrollo es una herramienta que te permite escribir y ejecutar programas de manera más eficiente. A continuación, te mostraremos cómo configurar un entorno de desarrollo básico utilizando el editor de texto Visual Studio Code (VS Code).

1. **Descarga e instala VS Code:** Ve al sitio web oficial de Visual Studio Code en https://code.visualstudio.com/ y descarga el instalador según tu sistema operativo. Ejecuta el archivo de instalación y sigue las instrucciones.

2. **Extensiones de VS Code:** Abre VS Code y ve a la sección de extensiones en el menú lateral izquierdo. Busca e instala las siguientes extensiones:

   - Python: Ofrecida por Microsoft, esta extensión proporciona herramientas esenciales para el desarrollo en Python, como el resaltado de sintaxis y la depuración.

3. **Configuración de la terminal integrada:** Abre VS Code y presiona `` Ctrl+`  `` (tecla de acento grave) para abrir la terminal integrada. Asegúrate de que esté configurada para usar Python escribiendo el siguiente comando:

   ```shell
   python --version
   ```

   Esto mostrará la versión de Python en la terminal. Si no aparece nada o muestra un mensaje de error, es posible que necesites configurar la ruta de Python en la variable de entorno PATH.

### Ejemplo de programa en Python

Ahora que tienes Python y VS Code configurados, vamos a escribir un programa sencillo para verificar que todo funciona correctamente.

1. **Crea un archivo nuevo:** Abre VS Code, crea un archivo nuevo y guárdalo con el nombre "hola.py".

2. **Escribe el código:** En el archivo "hola.py", escribe el siguiente código:

   ```python
   print("¡Hola, mundo!")
   ```

3. **Ejecuta el programa:** Para ejecutar el programa, ve al menú de VS Code y selecciona "Run" > "Run Without Debugging" (o presiona `Ctrl+F5`). Verás el resultado en la terminal integrada de VS Code.

¡Felicidades! Has completado la instalación de Python y la configuración de un entorno de desarrollo básico con VS
