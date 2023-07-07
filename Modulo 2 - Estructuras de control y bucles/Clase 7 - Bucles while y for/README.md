# Clase 7: Condicionales: Bucles while y for

En este módulo, exploraremos dos tipos de bucles en Python: `while` y `for`. Estos bucles nos permiten repetir una secuencia de instrucciones múltiples veces, lo cual es especialmente útil cuando necesitamos realizar tareas repetitivas.

## Bucle while

El bucle `while` ejecuta un bloque de código siempre que se cumpla una condición. La estructura del bucle `while` es la siguiente:

```python
while condición:
    # Bloque de código a ejecutar mientras se cumpla la condición
```

Este bucle ofrece varias posibilidades de uso. A continuación, veremos diferentes formas de utilizar un bucle `while`:

1. Bucle while con una condición: La forma más común de utilizar un bucle `while` es proporcionando una condición que se evalúa en cada iteración. Mientras la condición sea verdadera, el bloque de código del bucle `while` se ejecutará repetidamente. Aquí tienes un ejemplo:

   ```python
   contador = 0
   while contador < 5:
       print(contador)
       contador += 1
   ```

   En este caso, el bucle `while` se ejecuta mientras la variable `contador` sea menor que 5. En cada iteración, se imprime el valor de `contador` y se incrementa en 1.

2. Bucle while con `break`: Puedes utilizar la instrucción `break` dentro de un bucle `while` para salir del bucle antes de que la condición se vuelva falsa. Esto puede ser útil cuando se alcanza una determinada condición de salida. Aquí tienes un ejemplo:

   ```python
   contador = 0
   while True:
       print(contador)
       contador += 1
       if contador == 5:
           break
   ```

   En este caso, el bucle `while` se ejecuta infinitamente (`while True`) hasta que se encuentra la instrucción `break` cuando el contador alcanza el valor de 5. Esto permite salir del bucle antes de que la condición se vuelva falsa.

3. Bucle while con `continue`: La instrucción `continue` se utiliza para omitir el resto del bloque de código en una iteración particular y pasar a la siguiente iteración del bucle. Esto puede ser útil cuando se desea saltar ciertas iteraciones según una condición. Aquí tienes un ejemplo:

   ```python
   contador = 0
   while contador < 5:
       contador += 1
       if contador == 3:
           continue
       print(contador)
   ```

   En este caso, cuando el contador tiene un valor de 3, se encuentra la instrucción `continue`, lo que hace que se omita la impresión de ese valor en esa iteración en particular. El bucle `while` continúa ejecutándose hasta que la condición sea falsa.

Recuerda que en cada iteración del bucle `while`, la condición se evalúa. Si la condición es verdadera, el bloque de código se ejecuta y luego se vuelve a evaluar la condición. Si la condición es falsa, el bucle `while` se detiene y el programa continúa con el resto del código.

¡El bucle `while` es una herramienta útil para ejecutar un bloque de código repetidamente mientras se cumple una condición en Python!

## Bucle for

El bucle `for` se utiliza para iterar sobre una secuencia de elementos, como una lista, una cadena de texto o un rango de números. La estructura del bucle `for` es la siguiente:

```python
for elemento in secuencia:
    # Bloque de código a ejecutar para cada elemento de la secuencia
```

En cada iteración del bucle, la variable `elemento` toma el valor del siguiente elemento en la secuencia y se ejecuta el bloque de código. El bucle `for` se detiene cuando se han recorrido todos los elementos de la secuencia.

El bucle `for` en Python ofrece varias posibilidades de uso, lo que lo convierte en una estructura muy versátil. A continuación, se explican las diferentes formas de utilizar un bucle `for`:

1. Recorrer una secuencia: El uso más común del bucle `for` es recorrer una secuencia, como una lista, una cadena de texto o un rango de números. En cada iteración, la variable de control del bucle tomará el valor de un elemento de la secuencia. Aquí tienes un ejemplo:

   ```python
   frutas = ["manzana", "banana", "cereza"]
   for fruta in frutas:
       print(fruta)
   ```

   En este caso, el bucle `for` recorre la lista `frutas` y en cada iteración la variable `fruta` toma el valor de cada elemento de la lista.

2. Recorrer un rango de números: El bucle `for` se puede utilizar para iterar sobre un rango de números utilizando la función `range()`. Esto es útil cuando se necesita ejecutar un bloque de código un número específico de veces. Aquí tienes un ejemplo:

   ```python
   for i in range(1, 6):
       print(i)
   ```

   En este caso, el bucle `for` itera sobre el rango de números del 1 al 5, y en cada iteración la variable `i` toma el valor del número correspondiente.

3. Utilizar un índice: A veces, puede ser necesario acceder a los elementos de una secuencia utilizando un índice. En estos casos, se puede utilizar la función `enumerate()` para obtener tanto el índice como el elemento en cada iteración. Aquí tienes un ejemplo:

   ```python
   frutas = ["manzana", "banana", "cereza"]
   for indice, fruta in enumerate(frutas):
       print(indice, fruta)
   ```

   En este caso, el bucle `for` utiliza `enumerate(frutas)` para obtener tanto el índice como la fruta en cada iteración.

4. Bucle for vacío: A veces, se puede necesitar un bucle `for` que no realiza ninguna acción en su bloque de código. Esto se puede lograr utilizando la instrucción `pass`. Aquí tienes un ejemplo:

   ```python
   for i in range(5):
       pass
   ```

   En este caso, el bucle `for` itera sobre el rango de números, pero no realiza ninguna acción en cada iteración.

Recuerda que en cada iteración del bucle `for`, el bloque de código indentado se ejecuta una vez. Las diferentes formas de utilizar el bucle `for` permiten adaptarlo a diferentes necesidades y tareas en tus programas.

¡El bucle `for` es una herramienta poderosa para recorrer secuencias y realizar tareas repetitivas en Python!

## Ejemplo de uso de bucles

Aquí tienes un ejemplo que muestra cómo utilizar los bucles `while` y `for` en Python:

```python
# Ejemplo de uso de bucles
i = 0
while i < 5:
    print("Iteración", i)
    i += 1

frutas = ["manzana", "banana", "cereza"]
for fruta in frutas:
    print("Me gusta comer", fruta)
```

En este ejemplo, el bucle `while` se ejecuta mientras el valor de `i` sea menor que 5. En cada iteración, se imprime el mensaje "Iteración" seguido del valor de `i`, y luego se incrementa `i` en 1.

El bucle `for` se utiliza para recorrer la lista de frutas. En cada iteración, la variable `fruta` toma el valor de cada elemento de la lista, y se imprime el mensaje "Me gusta comer" seguido del nombre de la fruta.

¡Los bucles nos permiten repetir tareas de manera eficiente y automatizada en nuestros programas!
