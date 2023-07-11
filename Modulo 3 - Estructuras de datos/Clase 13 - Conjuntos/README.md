# Clase 13: Conjuntos: operaciones básicas

En esta clase, exploraremos los conjuntos en Python, una estructura de datos que permite almacenar elementos únicos. A continuación, se detallan los aspectos clave de los conjuntos:

1. **Creación de conjuntos:**

   - Los conjuntos se crean utilizando llaves `{ }` o la función `set()`.
   - Cada elemento en un conjunto es único y no se permite la duplicación.
   - Ejemplo:
     ```python
     conjunto = {1, 2, 3}
     ```

2. **Operaciones básicas con conjuntos:**

   - **Agregar elementos a un conjunto:** Se utiliza el método `add(elemento)` para agregar un elemento al conjunto.

     ```python
     conjunto = {1, 2, 3}
     conjunto.add(4)
     print(conjunto)  # Salida: {1, 2, 3, 4}
     ```

   - **Eliminar elementos de un conjunto:** Se utiliza el método `remove(elemento)` para eliminar un elemento específico del conjunto.

     ```python
     conjunto = {1, 2, 3, 4}
     conjunto.remove(3)
     print(conjunto)  # Salida: {1, 2, 4}
     ```

   - **Verificar la existencia de un elemento en un conjunto:** Se puede utilizar el operador `in` para verificar si un elemento está presente en un conjunto.

     ```python
     conjunto = {1, 2, 3, 4}
     print(3 in conjunto)  # Salida: True
     print(5 in conjunto)  # Salida: False
     ```

   - **Longitud de un conjunto:** Se puede obtener la cantidad de elementos en un conjunto utilizando la función `len()`.
     ```python
     conjunto = {1, 2, 3, 4}
     print(len(conjunto))  # Salida: 4
     ```

3. **Operaciones de conjuntos:**

   - **Unión de conjuntos:** Se puede realizar la unión de dos conjuntos utilizando el operador `|` o el método `union()`.

     ```python
     conjunto1 = {1, 2, 3}
     conjunto2 = {3, 4, 5}
     union = conjunto1 | conjunto2
     print(union)  # Salida: {1, 2, 3, 4, 5}
     ```

   - **Intersección de conjuntos:** Se puede realizar la intersección de dos conjuntos utilizando el operador `&` o el método `intersection()`.

     ```python
     conjunto1 = {1, 2, 3}
     conjunto2 = {3, 4, 5}
     interseccion = conjunto1 & conjunto2
     print(interseccion)  # Salida: {3}
     ```

   - **Diferencia de conjuntos:** Se puede obtener la diferencia entre dos conjuntos utilizando el operador `-` o el método `difference()`.

     ```python
     conjunto1 = {1, 2, 3}
     conjunto2 = {3, 4, 5}
     diferencia = conjunto1 - conjunto2
     print(diferencia)  # Salida: {1, 2}
     ```

   - **Diferencia simétrica de conjuntos:** Se puede obtener la diferencia simétrica entre dos conjuntos utilizando el operador `^` o el método `symmetric_difference()`.
     ```python
     conjunto1 = {1, 2, 3}
     conjunto2 = {3, 4, 5}
     diferencia_simetrica = conjunto1 ^ conjunto2
     print(diferencia_simetrica)  # Salida: {1, 2, 4, 5}
     ```

4. **Iteración sobre un conjunto:**
   - Se puede iterar sobre los elementos de un conjunto utilizando un bucle `for`.
   - No hay un orden específico garantizado en la iteración.
     ```python
     conjunto = {1, 2, 3}
     for elemento in conjunto:
         print(elemento)
     # Salida:
     # 1
     # 2
     # 3
     ```

Los conjuntos en Python son útiles cuando se necesita almacenar elementos únicos y realizar operaciones matemáticas de conjuntos. Aprovecha estos conceptos y operaciones para mejorar tus habilidades en Python y manipular conjuntos de manera eficiente.
