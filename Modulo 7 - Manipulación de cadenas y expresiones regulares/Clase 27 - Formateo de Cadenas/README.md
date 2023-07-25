# Clase 27: Formateo de Cadenas

En este módulo, aprenderemos sobre el formateo de cadenas en Python, una técnica que nos permite combinar variables y texto de manera más eficiente y legible. El formateo de cadenas es especialmente útil cuando queremos crear mensajes dinámicos o mostrar resultados con valores variables.

### Contenido

1. Uso de la función `format()`
2. F-strings (cadenas formateadas)
3. Uso de placeholders

### 1. Uso de la función `format()`

La función `format()` en Python nos permite insertar valores en una cadena utilizando marcadores de posición. Los marcadores de posición son representados por llaves `{}` dentro de la cadena, y los valores a insertar se pasan como argumentos a la función `format()`.

Ejemplo:

```python
nombre = "Juan"
edad = 30

mensaje = "Hola, mi nombre es {} y tengo {} años.".format(nombre, edad)
print(mensaje)  # Salida: "Hola, mi nombre es Juan y tengo 30 años."
```

### 2. F-strings (cadenas formateadas)

A partir de Python 3.6, podemos utilizar F-strings o cadenas formateadas, una sintaxis más sencilla y legible para formatear cadenas. Las F-strings se crean colocando una `f` antes de las comillas que delimitan la cadena, y los valores a insertar se colocan dentro de llaves `{}` directamente en la cadena.

Ejemplo:

```python
nombre = "María"
edad = 25

mensaje = f"Hola, mi nombre es {nombre} y tengo {edad} años."
print(mensaje)  # Salida: "Hola, mi nombre es María y tengo 25 años."
```

### 3. Uso de placeholders

Además de las llaves `{}`, también podemos utilizar placeholders numéricos para referenciar los valores que queremos insertar en la cadena. Los placeholders se representan por llaves con números dentro `{0}`, `{1}`, etc., y los valores se pasan a la función `format()` en el orden correspondiente.

Ejemplo:

```python
nombre = "Pedro"
edad = 35

mensaje = "Hola, mi nombre es {0} y tengo {1} años. {0} es una persona muy amable.".format(nombre, edad)
print(mensaje)  # Salida: "Hola, mi nombre es Pedro y tengo 35 años. Pedro es una persona muy amable."
```

### 4. Ejemplos prácticos

A continuación, algunos ejemplos prácticos donde se utiliza el formateo de cadenas para mostrar mensajes dinámicos con valores variables:

```python
nombre = "Ana"
puntaje = 85.5

# Ejemplo 1: Mensaje de calificación
mensaje_calificacion = f"¡Felicidades, {nombre}! Has obtenido un puntaje de {puntaje:.2f}."
print(mensaje_calificacion)  # Salida: "¡Felicidades, Ana! Has obtenido un puntaje de 85.50."

# Ejemplo 2: Mensaje de bienvenida con placeholders
mensaje_bienvenida = "Hola, {0}. Bienvenido al curso de Python {1}."
curso = "Avanzado"
print(mensaje_bienvenida.format(nombre, curso))  # Salida: "Hola, Ana. Bienvenido al curso de Python Avanzado."
```

¡El formateo de cadenas es una herramienta muy útil para crear mensajes dinámicos y legibles en Python! Espero que estos ejemplos te sean útiles para entender y aplicar el formateo de cadenas en tus proyectos. Si tienes alguna pregunta o necesitas ayuda adicional, no dudes en preguntar. ¡Buena práctica!
