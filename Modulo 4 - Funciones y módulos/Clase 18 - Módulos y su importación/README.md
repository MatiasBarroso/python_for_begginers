# Clase 18: Módulos y su importación

En esta clase, nos enfocaremos en comprender los módulos en Python y cómo importarlos en nuestros programas. Un módulo es un archivo que contiene definiciones y declaraciones de Python, incluyendo funciones, clases y variables. Aquí tienes los aspectos clave a tener en cuenta:

1. **¿Qué es un módulo?**

   - Un módulo es un archivo con extensión `.py` que contiene código de Python.
   - Los módulos se utilizan para organizar y reutilizar el código en Python.
   - Puedes definir tus propios módulos creando archivos `.py` y escribiendo código en ellos.
   - También existen módulos predefinidos en la biblioteca estándar de Python, que proporcionan funcionalidad adicional.

2. **Importación de módulos:**

   - Para utilizar un módulo en tu programa, primero debes importarlo utilizando la instrucción `import`.
   - Puedes importar un módulo completo utilizando la sintaxis `import nombre_modulo`.
   - Por ejemplo, para importar el módulo `math` que proporciona funciones matemáticas, puedes escribir:
     ```python
     import math
     ```

3. **Uso de funciones y clases de un módulo:**

   - Después de importar un módulo, puedes utilizar sus funciones y clases en tu programa.
   - Para acceder a una función o clase de un módulo, utiliza la sintaxis `nombre_modulo.nombre_funcion()` o `nombre_modulo.nombre_clase()`.
   - Por ejemplo, para utilizar la función `sqrt()` del módulo `math` que calcula la raíz cuadrada, puedes escribir:

     ```python
     import math

     resultado = math.sqrt(25)
     ```

4. **Importación selectiva:**

   - Si solo necesitas utilizar algunas funciones o clases de un módulo, puedes importarlas selectivamente en lugar de importar el módulo completo.
   - Utiliza la sintaxis `from nombre_modulo import nombre_funcion` para importar una función específica.
   - Utiliza la sintaxis `from nombre_modulo import nombre_clase` para importar una clase específica.
   - Por ejemplo, para importar solo la función `sqrt()` del módulo `math`, puedes escribir:
     ```python
     from math import sqrt
     ```

5. **Renombrar módulos o funciones:**

   - Puedes asignar un alias a un módulo o función importada utilizando la palabra clave `as`.
   - Esto puede ser útil para simplificar el nombre de un módulo largo o para evitar conflictos de nombres.
   - Por ejemplo, para importar el módulo `math` y asignarle un alias de `m`, puedes escribir:
     ```python
     import math as m
     ```

6. **Importar todo un módulo:**

   - Si quieres importar todas las funciones y clases de un módulo y no quieres utilizar el nombre completo del módulo cada vez que las utilices, puedes importar todo el módulo utilizando la sintaxis `from nombre_modulo import *`.
   - Sin embargo, esta forma de importación puede hacer que sea más difícil de seguir el origen de las funciones y puede generar conflictos de nombres si hay funciones con el mismo nombre en diferentes módulos.
   - Por lo tanto, es generalmente recomendable importar solo las funciones y clases específicas que necesitas en lugar de importar todo el módulo.

7. **Búsqueda de módulos:**
   - Al importar un módulo, Python buscará en varios lugares para encontrar el archivo correspondiente.
   - Python primero buscará en el directorio actual donde se encuentra el archivo `.py` que estás ejecutando.
   - Luego, buscará en los directorios listados en la variable de entorno `PYTHONPATH`.
   - Finalmente, buscará en la biblioteca estándar de Python y otros directorios de búsqueda predeterminados.
   - Si el módulo no se encuentra en ninguna de estas ubicaciones, se producirá un error de importación.

Los módulos son una forma efectiva de organizar y reutilizar el código en Python. Puedes crear tus propios módulos para encapsular funcionalidad específica y también puedes aprovechar los módulos predefinidos en la biblioteca estándar de Python. A medida que avancemos en la clase, exploraremos diferentes módulos y aprenderemos cómo utilizarlos en nuestros programas.
