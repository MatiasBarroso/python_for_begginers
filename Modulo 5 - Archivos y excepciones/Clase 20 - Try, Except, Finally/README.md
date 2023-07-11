# Clase 20: Manejo de excepciones: try, except, finally

En este módulo, nos enfocaremos en el manejo de excepciones en Python. Las excepciones son eventos que ocurren durante la ejecución de un programa y pueden interrumpir su flujo normal. Aprenderemos cómo utilizar las cláusulas `try`, `except` y `finally` para manejar estas excepciones de manera adecuada.

1. Bloque `try-except`:

   - El bloque `try` se utiliza para encerrar el código que puede generar una excepción.
   - Dentro del bloque `try`, se puede incluir cualquier cantidad de instrucciones que pueden generar excepciones.
   - Después del bloque `try`, podemos agregar uno o varios bloques `except` para manejar las excepciones específicas que pueden ocurrir.
   - El bloque `except` captura la excepción y ejecuta el código correspondiente para manejarla.
   - Por ejemplo:

   ```python
   try:
       # Código que puede generar una excepción
   except TipoDeExcepcion:
       # Código para manejar la excepción
   ```

2. Manejo de excepciones específicas:

   - Es posible manejar diferentes tipos de excepciones en bloques `except` separados.
   - Cada bloque `except` puede estar asociado con un tipo de excepción específico.
   - Esto permite un manejo más preciso y personalizado de las excepciones.
   - Por ejemplo:

   ```python
   try:
       # Código que puede generar una excepción
   except TypeError:
       # Código para manejar un TypeError
   except ValueError:
       # Código para manejar un ValueError
   ```

3. Bloque `finally`:

   - El bloque `finally` se utiliza para ejecutar código que debe ser ejecutado, independientemente de si se produce o no una excepción.
   - Se coloca después de los bloques `try` y `except`.
   - El código dentro del bloque `finally` se ejecutará siempre, incluso si ocurre una excepción y no se captura.
   - Esto es útil para liberar recursos o realizar tareas de limpieza necesarias.
   - Por ejemplo:

   ```python
   try:
       # Código que puede generar una excepción
   except TipoDeExcepcion:
       # Código para manejar la excepción
   finally:
       # Código que se ejecuta siempre
   ```

4. Excepciones genéricas:

   - Si no se especifica un tipo de excepción en un bloque `except`, se capturarán todas las excepciones.
   - Sin embargo, es recomendable capturar excepciones específicas para un manejo más adecuado.
   - Capturar todas las excepciones puede ocultar errores inesperados y dificultar la depuración del código.
   - Por ejemplo:

   ```python
   try:
       # Código que puede generar una excepción
   except:
       # Código para manejar cualquier excepción (no recomendado)
   ```

En este módulo, hemos aprendido cómo utilizar las cláusulas `try`, `except` y `finally` para manejar excepciones en Python. Este enfoque nos permite controlar el flujo de ejecución de nuestro programa y manejar errores de manera adecuada. Recuerda ser específico en la captura de excepciones y utilizar el bloque `finally` para realizar acciones de limpieza necesarias.
