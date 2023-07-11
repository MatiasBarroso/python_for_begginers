# Clase 17: Funciones predefinidas y bibliotecas

En esta clase, nos centraremos en explorar las funciones predefinidas de Python y cómo utilizar bibliotecas externas en nuestros programas. Las funciones predefinidas son aquellas que están integradas en Python y se pueden utilizar directamente sin necesidad de importar ninguna biblioteca adicional. A continuación, se detallan los aspectos clave:

1. **Funciones predefinidas comunes:**

   - Python ofrece una variedad de funciones predefinidas que son ampliamente utilizadas en la programación. Algunas de las funciones más comunes incluyen `print()`, `len()`, `type()`, `input()`, `range()`, `int()`, `float()`, `str()`, `list()` y `dict()`, entre otras.
   - Estas funciones nos permiten realizar tareas comunes como imprimir en la consola, obtener la longitud de una cadena o lista, convertir entre tipos de datos, solicitar entrada del usuario y generar secuencias de números.

2. **Importación de bibliotecas:**

   - Las bibliotecas (también conocidas como módulos o paquetes) son conjuntos de funciones y clases adicionales que no están incluidas en la biblioteca estándar de Python. Estas bibliotecas amplían la funcionalidad de Python y nos permiten realizar tareas más especializadas.
   - Para utilizar una biblioteca en nuestro programa, primero debemos importarla utilizando la instrucción `import`. Por ejemplo:
     ```python
     import math
     ```
   - Después de importar una biblioteca, podemos acceder a sus funciones y clases utilizando la sintaxis `nombre_biblioteca.nombre_funcion()` o `nombre_biblioteca.nombre_clase()`.
   - Algunas bibliotecas populares en Python incluyen `math` para funciones matemáticas, `random` para generación de números aleatorios, `datetime` para manipulación de fechas y horas, y `csv` para trabajar con archivos CSV, entre muchas otras.

3. **Uso de funciones y clases de bibliotecas:**

   - Después de importar una biblioteca, podemos utilizar sus funciones y clases para realizar tareas específicas.
   - Para utilizar una función de una biblioteca, podemos llamarla directamente utilizando la sintaxis `nombre_biblioteca.nombre_funcion()`. Por ejemplo:

     ```python
     import math

     raiz_cuadrada = math.sqrt(16)
     ```

   - Para utilizar una clase de una biblioteca, primero debemos crear una instancia de la clase utilizando la sintaxis `nombre_clase()`. Luego, podemos utilizar los métodos y atributos de la instancia. Por ejemplo:

     ```python
     import datetime

     fecha_actual = datetime.datetime.now()
     anio_actual = fecha_actual.year
     ```

4. **Alias de bibliotecas:**

   - En algunos casos, las bibliotecas tienen nombres largos o complicados de escribir repetidamente. Para facilitar su uso, podemos asignarles un alias utilizando la palabra clave `as`.
   - Por ejemplo, en lugar de escribir `import math`, podemos asignarle un alias y escribir `import math as m` para utilizar las funciones de la biblioteca.
   - De manera similar, también podemos asignar un alias a una función o clase específica dentro de una biblioteca. Por ejemplo:
     ```python
     from math import sqrt as raiz_cuadrada
     ```

5. **Documentación de bibliotecas y funciones:**

   - Muchas bibliotecas y funciones proporcionan documentación detallada sobre su uso. Puedes consultar la documentación oficial en línea o utilizar la función `help()` para obtener información sobre una función o biblioteca específica. Por ejemplo:

     ```python
     import math

     help(math.sqrt)
     ```

Al utilizar funciones predefinidas y bibliotecas en Python, podemos aprovechar la funcionalidad existente para realizar tareas complejas y ahorrar tiempo en la implementación de soluciones. A medida que avancemos en la clase, exploraremos diferentes bibliotecas populares y aprenderemos cómo utilizarlas de manera efectiva en nuestros programas.
