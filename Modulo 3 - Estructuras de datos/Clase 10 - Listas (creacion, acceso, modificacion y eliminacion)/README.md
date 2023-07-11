# Clase 10: Listas: creación, acceso, modificación, eliminación

En este módulo, exploraremos las listas en Python, una estructura de datos versátil y fundamental en la programación. Aprenderemos cómo crear listas, acceder a sus elementos, modificarlos y eliminar elementos de una lista. ¡Comencemos!

1. **¿Qué es una lista?**

   - Una lista es una estructura de datos en Python que permite almacenar múltiples elementos en un solo objeto.
   - Puede contener elementos de diferentes tipos, como números, cadenas, booleanos e incluso otras listas.
   - Se utiliza para almacenar colecciones de elementos relacionados y proporciona métodos y operaciones para manipularlos.

2. **Creación de listas:**

   - Podemos crear una lista utilizando corchetes ([]), colocando los elementos separados por comas.
   - Por ejemplo:
     ```python
     numeros = [1, 2, 3, 4, 5]
     frutas = ['manzana', 'naranja', 'plátano']
     mezclado = [1, 'Hola', True]
     ```

3. **Acceso a elementos de una lista:**

   - Los elementos de una lista se indexan comenzando desde 0.
   - Podemos acceder a un elemento específico utilizando su índice entre corchetes ([]).
   - Por ejemplo:
     ```python
     frutas = ['manzana', 'naranja', 'plátano']
     print(frutas[0])  # Salida: manzana
     print(frutas[1])  # Salida: naranja
     ```

4. **Modificación de elementos de una lista:**

   - Podemos modificar un elemento de una lista utilizando su índice y asignándole un nuevo valor.
   - Por ejemplo:
     ```python
     numeros = [1, 2, 3, 4, 5]
     numeros[2] = 10
     print(numeros)  # Salida: [1, 2, 10, 4, 5]
     ```

5. **Eliminación de elementos de una lista:**

   - Podemos eliminar un elemento de una lista utilizando la instrucción `del` seguida del índice del elemento.
   - Por ejemplo:
     ```python
     frutas = ['manzana', 'naranja', 'plátano']
     del frutas[1]
     print(frutas)  # Salida: ['manzana', 'plátano']
     ```

6. **Métodos de las listas:**

   Las listas en Python tienen varios métodos incorporados que facilitan su manipulación, como `append()`, `insert()`, `remove()`, `pop()`, `extend()`, entre otros. Estos métodos nos permiten agregar elementos, insertar elementos en una posición específica, eliminar elementos por valor o índice, y más.

   - **`append(elemento)`**

   Agrega un elemento al final de la lista.
   Ejemplo:

   ```python
   frutas = ['manzana', 'naranja']
   frutas.append('plátano')
   print(frutas)  # Salida: ['manzana', 'naranja', 'plátano']
   ```

   - **`insert(posición, elemento)`**

   Inserta un elemento en una posición específica de la lista.
   Ejemplo:

   ```python
   numeros = [1, 2, 3, 4, 5]
   numeros.insert(2, 10)
   print(numeros)  # Salida: [1, 2, 10, 3, 4, 5]
   ```

   - **`remove(elemento)`**

   Elimina la primera aparición de un elemento en la lista.
   Ejemplo:

   ```python
   frutas = ['manzana', 'naranja', 'plátano']
   frutas.remove('naranja')
   print(frutas)  # Salida: ['manzana', 'plátano']
   ```

   - **`pop([índice])`**

   Elimina un elemento de la lista en una posición específica y lo devuelve. Si no se proporciona un índice, elimina y devuelve el último elemento de la lista.
   Ejemplo:

   ```python
   numeros = [1, 2, 3, 4, 5]
   eliminado = numeros.pop(2)
   print(eliminado)  # Salida: 3
   print(numeros)   # Salida: [1, 2, 4, 5]
   ```

   - **`extend(iterable)`**

   Agrega los elementos de un iterable (como otra lista) al final de la lista actual.
   Ejemplo:

   ```python
   numeros = [1, 2, 3]
   otros_numeros = [4, 5, 6]
   numeros.extend(otros_numeros)
   print(numeros)  # Salida: [1, 2, 3, 4, 5, 6]
   ```

   - **`index(elemento[, inicio[, fin]])`**

   Devuelve el índice de la primera aparición de un elemento en la lista. También se puede especificar un rango de búsqueda opcional.
   Ejemplo:

   ```python
   frutas = ['manzana', 'naranja', 'plátano']
   indice = frutas.index('naranja')
   print(indice)  # Salida: 1
   ```

   - **`count(elemento)`**

   Devuelve el número de veces que aparece un elemento en la lista.
   Ejemplo:

   ```python
   numeros = [1, 2, 2, 3, 4, 2]
   conteo = numeros.count(2)
   print(conteo)  # Salida: 3
   ```

   - **`sort(key=None, reverse=False)`**

   Ordena los elementos de la lista de forma ascendente. Se pueden proporcionar argumentos opcionales para personalizar el ordenamiento.
   Ejemplo:

   ```python
   numeros = [3, 1, 4, 2, 5]
   numeros.sort()
   print(numeros)  # Salida: [1, 2, 3, 4, 5]
   ```

   - **`reverse()`**

   Invierte el orden de los elementos en la lista.
   Ejemplo:

   ```python
   letras = ['a', 'b', 'c']
   letras.reverse()
   print(letras)  # Salida: ['c', 'b', 'a']
   ```

   - **`clear()`**

   Elimina todos los elementos de la lista.
   Ejemplo:

   ```python
   numeros = [1, 2, 3, 4, 5]
   numeros.clear()
   print(numeros)  # Salida: []
   ```

   - **`copy()`**

   Crea una copia superficial de la lista.
   Ejemplo:

   ```python
   frutas = ['manzana', 'naranja', 'plátano']
   copia_frutas = frutas.copy()
   print(copia_frutas)  # Salida: ['manzana', 'naranja', 'plátano']
   ```

   - **`len()`**

   Devuelve la longitud (número de elementos) de la lista.
   Ejemplo:

   ```python
   numeros = [1, 2, 3, 4, 5]
   longitud = len(numeros)
   print(longitud)  # Salida: 5
   ```

   - **`max()`**

   Devuelve el elemento máximo de la lista.
   Ejemplo:

   ```python
   numeros = [3, 1, 4, 2, 5]
   maximo = max(numeros)
   print(maximo)  # Salida: 5
   ```

   - **`min()`**

   Devuelve el elemento mínimo de la lista.
   Ejemplo:

   ```python
   numeros = [3, 1, 4, 2, 5]
   minimo = min(numeros)
   print(minimo)  # Salida: 1
   ```

   - **`sum()`**

   Devuelve la suma de todos los elementos numéricos de la lista.
   Ejemplo:

   ```python
   numeros = [1, 2, 3, 4, 5]
   suma = sum(numeros)
   print(suma)  # Salida: 15
   ```

   - **`join(iterable)`**

   Concatena los elementos de un iterable en una sola cadena utilizando la lista como separador.
   Ejemplo:

   ```python
   nombres = ['Juan', 'María', 'Pedro']
   nombres_completos = ', '.join(nombres)
   print(nombres_completos)  # Salida: 'Juan, María, Pedro'
   ```

   - **`reverse()`**

   Invierte el orden de los elementos en la lista.
   Ejemplo:

   ```python
   letras = ['a', 'b', 'c']
   letras.reverse()
   print(letras)  # Salida: ['c', 'b', 'a']
   ```

Recuerda que puedes consultar la documentación oficial de Python para obtener más detalles sobre cada método y su uso.
https://docs.python.org/3/

Con este módulo, has aprendido los conceptos básicos de las listas en Python. Ahora puedes crear listas, acceder a sus elementos, modificarlos y eliminar elementos según sea necesario. ¡Continúa practicando y explorando los diversos métodos de las listas para aprovechar al máximo esta estructura de datos en tus programas!
