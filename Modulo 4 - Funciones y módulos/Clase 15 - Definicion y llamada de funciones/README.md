# Clase 15: Definición y llamada de funciones

En esta clase, nos centraremos en aprender sobre la definición y llamada de funciones en Python. Las funciones nos permiten agrupar un conjunto de instrucciones en un bloque reutilizable de código. A continuación, se detallan los aspectos clave de las funciones:

1. **Definición de funciones:**

   - Las funciones se definen utilizando la palabra clave `def`, seguida del nombre de la función y paréntesis `()`.
   - Pueden recibir cero o más parámetros (también conocidos como argumentos) dentro de los paréntesis.
   - El cuerpo de la función se define mediante sangría (espacios o tabulaciones) y contiene las instrucciones que se ejecutan cuando se llama a la función.
   - Ejemplo:
     ```python
     def saludar(nombre):
         print("¡Hola,", nombre + "!")
     ```

2. **Llamada de funciones:**

   - Para llamar a una función, se utiliza el nombre de la función seguido de paréntesis `()`. Si la función requiere argumentos, se proporcionan dentro de los paréntesis.
   - Ejemplo:
     ```python
     saludar("Juan")
     ```

3. **Retorno de valores:**

   - Las funciones pueden devolver un valor utilizando la palabra clave `return` seguida del valor que se desea devolver.
   - Si no se especifica un valor de retorno, la función devuelve automáticamente `None`.
   - Ejemplo:
     ```python
     def sumar(a, b):
         return a + b
     ```

4. **Parámetros y argumentos:**

   - Los parámetros son variables que se definen en la declaración de la función y representan los valores que se esperan recibir cuando se llama a la función.
   - Los argumentos son los valores reales que se pasan a la función cuando se la llama.
   - Los argumentos pueden ser valores literales, variables u otras expresiones.
   - Ejemplo:

     ```python
     def multiplicar(x, y):
         return x * y

     a = 2
     b = 3
     resultado = multiplicar(a, b)
     ```

5. **Ámbito de variables:**

   - Las variables definidas dentro de una función son variables locales y solo están disponibles dentro de esa función.
   - Las variables definidas fuera de las funciones se llaman variables globales y están disponibles en todo el programa.
   - Si una variable local tiene el mismo nombre que una variable global, la variable local tiene prioridad dentro de la función.
   - Ejemplo:

     ```python
     pi = 3.1416

     def calcular_area(radio):
         area = pi * radio ** 2
         return area
     ```

6. **Documentación de funciones:**

   - Es una buena práctica documentar las funciones utilizando comentarios llamados docstrings. Los docstrings proporcionan información sobre la función, su propósito y los parámetros que acepta.
   - Ejemplo:

     ```python
     def saludar(nombre):
         """
         Esta función muestra un saludo personalizado.

         Argumentos:
         - nombre (str): El nombre de la persona a saludar.

         Retorna:
         - None
         """
         print("¡Hola,", nombre + "!")
     ```

El uso de funciones nos permite organizar nuestro código, hacerlo más modular y reutilizable. Además, nos ayuda a mejorar la legibilidad y mantenibilidad del programa. A medida que avancemos en la clase, aprenderemos más sobre las funciones y cómo utilizarlas de manera efectiva en Python.
