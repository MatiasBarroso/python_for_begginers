# Clase 12: Diccionarios: pares clave-valor

En esta clase, exploraremos los diccionarios en Python, una estructura de datos muy útil que almacena pares de elementos clave-valor. A continuación, se detallan los aspectos clave de los diccionarios:

1. **Creación de diccionarios:**

   - Los diccionarios se crean utilizando llaves `{ }`.
   - Cada elemento en un diccionario se compone de una clave y su correspondiente valor, separados por `:`. Los pares clave-valor se separan por comas.
   - Ejemplo:
     ```python
     diccionario = {'nombre': 'Juan', 'edad': 25, 'ciudad': 'México'}
     ```

2. **Acceso a elementos de un diccionario:**

   - Los elementos de un diccionario se acceden utilizando su clave.
   - Se utiliza la sintaxis `diccionario[clave]` para obtener el valor asociado a una clave específica.
   - Ejemplo:
     ```python
     diccionario = {'nombre': 'Juan', 'edad': 25, 'ciudad': 'México'}
     print(diccionario['nombre'])  # Salida: 'Juan'
     ```

3. **Modificación de valores en un diccionario:**

   - Los valores en un diccionario se pueden modificar asignando un nuevo valor a una clave existente.
   - Se utiliza la sintaxis `diccionario[clave] = nuevo_valor` para modificar el valor asociado a una clave.
   - Ejemplo:
     ```python
     diccionario = {'nombre': 'Juan', 'edad': 25, 'ciudad': 'México'}
     diccionario['edad'] = 30
     print(diccionario['edad'])  # Salida: 30
     ```

4. **Agregar elementos a un diccionario:**

   - Se puede agregar un nuevo par clave-valor a un diccionario asignando un valor a una nueva clave.
   - Se utiliza la sintaxis `diccionario[nueva_clave] = nuevo_valor` para agregar un nuevo elemento al diccionario.
   - Ejemplo:
     ```python
     diccionario = {'nombre': 'Juan', 'edad': 25}
     diccionario['ciudad'] = 'México'
     print(diccionario)  # Salida: {'nombre': 'Juan', 'edad': 25, 'ciudad': 'México'}
     ```

5. **Eliminar elementos de un diccionario:**

   - Se puede eliminar un par clave-valor de un diccionario utilizando la palabra clave `del` seguida de la clave a eliminar.
   - Ejemplo:
     ```python
     diccionario = {'nombre': 'Juan', 'edad': 25, 'ciudad': 'México'}
     del diccionario['edad']
     print(diccionario)  # Salida: {'nombre': 'Juan', 'ciudad': 'México'}
     ```

6. **Verificación de existencia de claves en un diccionario:**

   - Se puede utilizar el operador `in` para verificar si una clave está presente en un diccionario.
   - El resultado es un valor booleano (True o False).
   - Ejemplo:
     ```python
     diccionario = {'nombre': 'Juan', 'edad': 25, 'ciudad': 'México'}
     print('edad' in diccionario)    # Salida: True
     print('apellido' in diccionario)  # Salida: False
     ```

7. **Métodos comunes de diccionarios:**

   - `keys()`: Devuelve una vista de todas las claves en el diccionario.
   - `values()`: Devuelve una vista de todos los valores en el diccionario.
   - `items()`: Devuelve una vista de todos los pares clave-valor en el diccionario.
   - Ejemplo:
     ```python
     diccionario = {'nombre': 'Juan', 'edad': 25, 'ciudad': 'México'}
     print(diccionario.keys())    # Salida: dict_keys(['nombre', 'edad', 'ciudad'])
     print(diccionario.values())  # Salida: dict_values(['Juan', 25, 'México'])
     print(diccionario.items())   # Salida: dict_items([('nombre', 'Juan'), ('edad', 25), ('ciudad', 'México')])
     ```

8. **Iteración sobre un diccionario:**

   - Se puede iterar sobre un diccionario utilizando un bucle `for`.
   - Por defecto, el bucle `for` itera sobre las claves del diccionario.
   - Ejemplo:
     ```python
     diccionario = {'nombre': 'Juan', 'edad': 25, 'ciudad': 'México'}
     for clave in diccionario:
         print(clave, diccionario[clave])
     # Salida:
     # nombre Juan
     # edad 25
     # ciudad México
     ```

9. **Uso de diccionarios en situaciones prácticas:**
   - Los diccionarios son ideales para almacenar y acceder a datos estructurados utilizando claves significativas.
   - Se pueden utilizar en diversas situaciones como:
     - Almacenar información de usuarios, con claves como 'nombre', 'edad', 'email', etc.
     - Representar información de productos, con claves como 'nombre', 'precio', 'descripción', etc.
     - Organizar datos relacionados, como el diccionario de un estudiante con las claves 'nombre', 'materias', 'calificaciones', etc.
   - Los diccionarios permiten una fácil manipulación y acceso a los datos basados en las claves asociadas.

Los diccionarios son una estructura de datos poderosa en Python que te permite almacenar y acceder eficientemente a información utilizando claves significativas. Aprovecha estos conceptos y operaciones para mejorar tus habilidades en Python y facilitar la manipulación de datos estructurados.
