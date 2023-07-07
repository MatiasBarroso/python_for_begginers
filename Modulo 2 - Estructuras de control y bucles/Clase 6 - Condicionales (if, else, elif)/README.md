# Clase 6: Condicionales: if, else, elif

En este módulo, aprenderemos sobre las estructuras de control de flujo condicionales en Python. Los condicionales nos permiten tomar decisiones y ejecutar diferentes bloques de código según se cumplan ciertas condiciones. En Python, contamos con tres tipos principales de condicionales: `if`, `else` y `elif` (que significa "else if").

### Estructura básica del condicional if

La estructura básica de un condicional `if` es la siguiente:

```python
if condición:
    # Bloque de código a ejecutar si la condición es verdadera
```

En este caso, `condición` representa una expresión que se evalúa como verdadera o falsa. Si la condición es verdadera, se ejecutará el bloque de código indentado que sigue al condicional. Si la condición es falsa, se omitirá ese bloque de código.

### Estructura del condicional if-else

El condicional `if-else` nos permite ejecutar un bloque de código si la condición es verdadera, y otro bloque de código si la condición es falsa. La estructura es la siguiente:

```python
if condición:
    # Bloque de código a ejecutar si la condición es verdadera
else:
    # Bloque de código a ejecutar si la condición es falsa
```

En este caso, si la condición es verdadera, se ejecutará el bloque de código indentado después del `if`. Si la condición es falsa, se ejecutará el bloque de código indentado después del `else`.

### Estructura del condicional if-elif-else

Cuando tenemos múltiples condiciones a evaluar, podemos utilizar el condicional `if-elif-else`. La estructura es la siguiente:

```python
if condición1:
    # Bloque de código a ejecutar si la condición1 es verdadera
elif condición2:
    # Bloque de código a ejecutar si la condición2 es verdadera
else:
    # Bloque de código a ejecutar si ninguna de las condiciones anteriores es verdadera
```

En este caso, se evaluarán las condiciones en orden. Si alguna de las condiciones es verdadera, se ejecutará el bloque de código correspondiente y el condicional se terminará. Si ninguna de las condiciones es verdadera, se ejecutará el bloque de código después del `else`.

### Ejemplo de uso de condicionales

Aquí tienes un ejemplo que muestra cómo utilizar los condicionales `if`, `else` y `elif` en Python:

```python
# Ejemplo de uso de condicionales
x = 10

if x > 0:
    print("x es positivo")
elif x < 0:
    print("x es negativo")
else:
    print("x es cero")
```

En este ejemplo, el valor de `x` se evalúa en cada condición y se imprime un mensaje correspondiente según el resultado.

¡Los condicionales nos permiten tomar decisiones en nuestros programas y ejecutar diferentes acciones según las condiciones establecidas!
