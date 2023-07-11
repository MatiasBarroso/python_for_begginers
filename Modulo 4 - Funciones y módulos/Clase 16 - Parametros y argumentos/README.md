# Clase 16: Parámetros y argumentos

En esta clase, nos enfocaremos en comprender los conceptos de parámetros y argumentos en Python. Al definir y llamar a una función, utilizamos parámetros para recibir valores que se utilizarán dentro de la función. Aquí tienes los aspectos clave a tener en cuenta:

1. **Definición de parámetros:**

   - Los parámetros son variables declaradas en la definición de una función que permiten recibir valores cuando se llama a la función.
   - Los parámetros se definen dentro de los paréntesis de la definición de la función.
   - Puedes especificar uno o más parámetros separados por comas.
   - Ejemplo:
     ```python
     def saludar(nombre):
         print("¡Hola,", nombre + "!")
     ```

2. **Argumentos en la llamada de función:**

   - Los argumentos son los valores reales que se pasan a una función cuando se la llama.
   - Los argumentos se proporcionan dentro de los paréntesis en la llamada de la función.
   - Los argumentos deben coincidir en orden y cantidad con los parámetros definidos en la función.
   - Ejemplo:
     ```python
     saludar("Juan")
     ```

3. **Tipos de parámetros:**

   - Parámetros posicionales: Son aquellos que se asignan a los argumentos basándose en su posición en la llamada de función. Los argumentos se asignan en orden.
   - Parámetros de palabras clave: Son aquellos que se asignan a los argumentos utilizando su nombre. Esto permite cambiar el orden o incluso omitir argumentos.
   - Ejemplo:

     ```python
     def calcular_descuento(precio, descuento):
         precio_final = precio - descuento
         return precio_final

     calcular_descuento(100, descuento=20)
     ```

4. **Valores predeterminados de parámetros:**

   - Puedes asignar un valor predeterminado a un parámetro en la definición de la función. Esto significa que si no se proporciona un argumento correspondiente, se utilizará el valor predeterminado.
   - Los parámetros con valores predeterminados deben estar al final de la lista de parámetros.
   - Ejemplo:
     ```python
     def saludar(nombre, saludo="¡Hola,"):
         print(saludo, nombre + "!")
     ```

5. **Argumentos arbitrarios:**

   - Puedes definir una función que acepte un número variable de argumentos utilizando los parámetros `*args` y `**kwargs`.
   - `*args` permite pasar una lista de argumentos posicionales adicionales.
   - `**kwargs` permite pasar un diccionario de argumentos de palabras clave adicionales.
   - Ejemplo:
     ```python
     def imprimir_argumentos(*args, **kwargs):
         for arg in args:
             print(arg)
         for key, value in kwargs.items():
             print(key, ":", value)
     ```

6. **Desempaquetado de argumentos:**

   - Puedes pasar una lista o tupla de argumentos a una función utilizando el operador `*` para desempaquetarlos.
   - Puedes pasar un diccionario de argumentos a una función utilizando el operador `**` para desempaquetarlo.
   - Ejemplo:

     ```python
     numeros = [1, 2, 3]
     suma(*numeros)

     datos = {"nombre": "Juan", "edad": 30}
     saludar(**datos)
     ```

Entender cómo funcionan los parámetros y argumentos es fundamental para aprovechar al máximo la flexibilidad y reusabilidad de las funciones en Python. A medida que avancemos en la clase, exploraremos más conceptos relacionados con los parámetros y argumentos, como la asignación de valores predeterminados, la manipulación de argumentos arbitrarios y el desempaquetado de argumentos.
