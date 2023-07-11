# Clase 4: Variables y tipos de datos básicos: números, cadenas, booleanos

En este módulo, aprenderemos sobre las variables y los tipos de datos básicos en Python. Las variables nos permiten almacenar y manipular información, y los tipos de datos nos ayudan a categorizar y trabajar con diferentes tipos de valores.

### Variables

En Python, una variable es un nombre que representa un valor almacenado en la memoria. Puedes asignar un valor a una variable utilizando el operador de asignación `=`. Por ejemplo:

```python
nombre = "Ana"
edad = 25
```

En este ejemplo, hemos creado dos variables: `nombre` y `edad`. La variable `nombre` almacena el valor de una cadena de texto, mientras que la variable `edad` almacena un número entero.

### Tipos de datos básicos

Python tiene varios tipos de datos básicos incorporados que nos permiten trabajar con diferentes tipos de valores. A continuación, veremos los tipos de datos más comunes:

1. **Números**: Python admite diferentes tipos de números, como enteros (`int`), números de punto flotante (`float`) y números complejos (`complex`). Por ejemplo:

   ```python
   edad = 25       # Entero
   altura = 1.75   # Punto flotante
   complejo = 2 + 3j  # Complejo
   ```

2. **Cadenas de texto**: Una cadena de texto es una secuencia de caracteres encerrada entre comillas simples (`'`) o comillas dobles (`"`). Por ejemplo:

   ```python
   nombre = "Ana"
   mensaje = '¡Hola, mundo!'
   ```

3. **Booleanos**: Un booleano representa uno de dos valores: `True` (verdadero) o `False` (falso). Estos valores son útiles para expresar condiciones y realizar operaciones lógicas. Por ejemplo:

   ```python
   es_mayor_edad = True
   es_estudiante = False
   ```

### Operadores de Comparación

Los operadores de comparación se utilizan para comparar dos valores y evaluar si una determinada condición es verdadera o falsa. A continuación, se muestran algunos operadores de comparación comunes:

- `==` - Igual a: verifica si dos valores son iguales.
- `!=` - Diferente de: verifica si dos valores no son iguales.
- `>` - Mayor que: verifica si el valor de la izquierda es mayor que el de la derecha.
- `<` - Menor que: verifica si el valor de la izquierda es menor que el de la derecha.
- `>=` - Mayor o igual que: verifica si el valor de la izquierda es mayor o igual que el de la derecha.
- `<=` - Menor o igual que: verifica si el valor de la izquierda es menor o igual que el de la derecha.

Veamos algunos ejemplos de uso de operadores de comparación:

```python
numero1 = 10
numero2 = 5

print(numero1 == numero2)  # False
print(numero1 != numero2)  # True
print(numero1 > numero2)   # True
print(numero1 < numero2)   # False
print(numero1 >= numero2)  # True
print(numero1 <= numero2)  # False
```

### Operadores Lógicos

Los operadores lógicos se utilizan para combinar o negar condiciones y evaluar expresiones lógicas. Los operadores lógicos más comunes son:

- `and` - Y lógico: devuelve `True` si ambas condiciones son verdaderas.
- `or` - O lógico: devuelve `True` si al menos una de las condiciones es verdadera.
- `not` - Negación lógica: invierte el valor de verdad de una condición.

Aquí tienes algunos ejemplos de uso de operadores lógicos:

```python
numero = 10

# Verificar si el número está entre 0 y 20
print(numero > 0 and numero < 20)  # True

# Verificar si el número es menor que 0 o mayor que 100
print(numero < 0 or numero > 100)  # False

# Negar la condición "el número es igual a 10"
print(not numero == 10)  # False
```

### Uso de variables y tipos de datos

Podemos realizar diversas operaciones y manipulaciones utilizando variables y tipos de datos en Python. A continuación, se presentan algunos ejemplos:

```python
# Operaciones con números
a = 10
b = 5
suma = a + b
resta = a - b
multiplicacion = a * b
division = a / b

# Concatenación de cadenas de texto
nombre = "Ana"
apellido = "García"
nombre_completo = nombre + " " + apellido

# Operaciones lógicas con booleanos
es_mayor_edad = True
es_estudiante = False
puede_votar = es_mayor_edad and not es_estudiante

```

Recuerda que Python es un lenguaje de programación dinámicamente tipado, lo que significa que no es necesario declarar explícitamente el tipo de una variable. Python infiere automáticamente el tipo de datos en función del valor asignado.

¡Ahora estás listo para utilizar variables y tipos de datos básicos en Python!

Continúa practicando y experimentando con diferentes operaciones y manipulaciones utilizando variables y tipos de datos. En las próximas clases, exploraremos más
