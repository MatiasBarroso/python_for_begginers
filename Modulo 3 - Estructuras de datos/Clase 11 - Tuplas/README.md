# Clase 3: Tuplas: características y uso

Segunda parte: Uso de tuplas y operaciones básicas

En la segunda parte de esta clase, exploraremos el uso de las tuplas y las operaciones básicas que se pueden realizar con ellas. A continuación, se detallan los puntos clave:

1. **Creación de tuplas:**

   - Las tuplas se crean utilizando paréntesis ( ) y separando los elementos por comas.
   - Ejemplo:
     ```python
     tupla1 = (1, 2, 3)
     tupla2 = ('manzana', 'naranja', 'plátano')
     tupla3 = ()
     ```

2. **Acceso a elementos de una tupla (Indexación y rebanado):**

   - Las tuplas admiten la indexación y el rebanado, al igual que las listas y otras secuencias en Python.
   - La indexación se utiliza para acceder a elementos individuales de una tupla utilizando un índice numérico.
   - El rebanado se utiliza para acceder a un rango de elementos de una tupla utilizando la notación `[inicio:fin]`.
   - Ejemplo:
     ```python
     tupla = ('a', 'b', 'c', 'd', 'e')
     print(tupla[2])      # Salida: 'c'
     print(tupla[1:4])    # Salida: ('b', 'c', 'd')
     print(tupla[:3])     # Salida: ('a', 'b', 'c')
     print(tupla[2:])     # Salida: ('c', 'd', 'e')
     print(tupla[-1])     # Salida: 'e' (índice negativo)
     ```

3. **Longitud de una tupla:**

   - La función `len()` se utiliza para obtener la longitud de una tupla (es decir, el número de elementos).
   - Ejemplo:
     ```python
     tupla = (1, 2, 3, 4, 5)
     print(len(tupla))  # Salida: 5
     ```

4. **Concatenación de tuplas:**

   - Las tuplas se pueden concatenar utilizando el operador de concatenación `+`.
   - El resultado es una nueva tupla que contiene todos los elementos de las tuplas originales.
   - Ejemplo:
     ```python
     tupla1 = (1, 2)
     tupla2 = (3, 4)
     tupla_concatenada = tupla1 + tupla2
     print(tupla_concatenada)  # Salida: (1, 2, 3, 4)
     ```

5. **Repetición de tuplas:**

   - Las tuplas se pueden repetir utilizando el operador de repetición `*`.
   - El resultado es una nueva tupla que contiene múltiples repeticiones de la tupla original.
   - Ejemplo:
     ```python
     tupla = ('a', 'b')
     tupla_repetida = tupla * 3
     print(tupla_repetida)  # Salida: ('a', 'b', 'a', 'b', 'a', 'b')
     ```

6. **Verificación de existencia de elementos:**

   - Se puede utilizar el operador `in` para verificar si un elemento está presente en una tupla.
   - El resultado es un valor booleano (True o False).
   - Ejemplo:
     ```python
     tupla = ('manzana', 'naranja', 'plátano')
     print('manzana' in tupla)  # Salida: True
     print('pera' in tupla)     # Salida: False
     ```

7. **Desempaquetado de tuplas:**

   - El desempaquetado de tuplas permite asignar los elementos individuales de una tupla a variables separadas.
   - Se utiliza una sintaxis especial con la cantidad correspondiente de variables a la izquierda del operador de asignación (`=`) y una tupla a la derecha.
   - Ejemplo:
     ```python
     tupla = ('Juan', 25, 'México')
     nombre, edad, pais = tupla
     print(nombre)   # Salida: 'Juan'
     print(edad)     # Salida: 25
     print(pais)     # Salida: 'México'
     ```

8. **Comparación de tuplas:**

   - Las tuplas se pueden comparar utilizando los operadores de comparación (`<`, `<=`, `>`, `>=`, `==`, `!=`).
   - La comparación se realiza elemento por elemento en orden de izquierda a derecha.
   - Si los elementos son comparables, se devuelve el resultado de la comparación. Si no son comparables, se generará un error.
   - Ejemplo:
     ```python
     tupla1 = (1, 2, 3)
     tupla2 = (1, 2, 4)
     print(tupla1 < tupla2)   # Salida: True
     print(tupla1 == tupla2)  # Salida: False
     ```

9. **Uso de tuplas como claves de diccionarios:**

   - Las tuplas se pueden utilizar como claves en un diccionario debido a su inmutabilidad.
   - Esto significa que las tuplas pueden contener elementos que no se pueden modificar y, por lo tanto, se pueden utilizar como claves.
   - Ejemplo:
     ```python
     diccionario = {('manzana', 'roja'): 10, ('plátano', 'amarillo'): 5}
     print(diccionario[('manzana', 'roja')])     # Salida: 10
     print(diccionario[('plátano', 'amarillo')])  # Salida: 5
     ```

Las tuplas son una herramienta poderosa en Python, especialmente en situaciones en las que se requiere una secuencia inmutable de elementos. Pueden utilizarse para agrupar valores relacionados, devolver múltiples valores en una función y representar datos que no deben modificarse. Aprovecha estas características y operaciones para mejorar tus habilidades en Python.
