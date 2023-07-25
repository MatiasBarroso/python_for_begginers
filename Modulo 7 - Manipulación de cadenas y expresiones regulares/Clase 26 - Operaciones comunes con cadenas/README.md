# Clase 26: Manipulación de Cadenas y Expresiones Regulares

En este módulo, aprenderemos sobre la manipulación de cadenas y el uso de expresiones regulares en Python. Las cadenas son secuencias de caracteres y son una parte fundamental de la programación para manipular y procesar texto. Las expresiones regulares nos permiten buscar patrones específicos dentro de cadenas y realizar operaciones avanzadas de búsqueda y reemplazo.

### 1. Introducción a las cadenas

Las cadenas son secuencias de caracteres que se utilizan para representar texto en Python. Se pueden definir utilizando comillas simples ('') o comillas dobles ("").

Ejemplo:

```python
cadena1 = 'Hola, mundo!'
cadena2 = "¡Bienvenidos a Python!"
```

### 2. Operaciones comunes con cadenas

Python proporciona diversas operaciones y métodos para trabajar con cadenas. Algunas de las operaciones más comunes son la concatenación, la repetición y la indexación.

Ejemplo:

```python
cadena1 = "Hola"
cadena2 = "mundo"

# Concatenación
resultado_concatenacion = cadena1 + " " + cadena2
print(resultado_concatenacion)  # Salida: "Hola mundo"

# Repetición
resultado_repeticion = cadena1 * 3
print(resultado_repeticion)  # Salida: "HolaHolaHola"

# Indexación
primer_caracter = cadena1[0]
ultimo_caracter = cadena2[-1]
print(primer_caracter)  # Salida: "H"
print(ultimo_caracter)  # Salida: "o"
```

### 3. Métodos útiles de cadenas

Python proporciona una gran variedad de métodos incorporados para trabajar con cadenas. Algunos de los métodos más útiles incluyen `lower()`, `upper()`, `strip()`, `split()` y `replace()`.

Ejemplo:

```python
texto = "   Hola, mundo!   "

# Convertir a minúsculas
texto_en_minusculas = texto.lower()
print(texto_en_minusculas)  # Salida: "   hola, mundo!   "

# Convertir a mayúsculas
texto_en_mayusculas = texto.upper()
print(texto_en_mayusculas)  # Salida: "   HOLA, MUNDO!   "

# Eliminar espacios en blanco al inicio y al final
texto_limpio = texto.strip()
print(texto_limpio)  # Salida: "Hola, mundo!"

# Dividir la cadena en palabras utilizando espacios como separadores
palabras = texto.split()
print(palabras)  # Salida: ['Hola,', 'mundo!']

# Reemplazar una parte de la cadena
texto_modificado = texto.replace("mundo", "Python")
print(texto_modificado)  # Salida: "   Hola, Python!   "
```

### 4. Expresiones Regulares

Las expresiones regulares son patrones de búsqueda que nos permiten encontrar y manipular texto de manera eficiente. Se utilizan para buscar coincidencias en cadenas y realizar operaciones de búsqueda y reemplazo más complejas.

### 5. Uso de Expresiones Regulares en Python

En Python, podemos utilizar el módulo `re` para trabajar con expresiones regulares. El módulo `re` proporciona funciones para buscar patrones y realizar operaciones basadas en expresiones regulares.

```python
import re

# Ejemplo 1: Búsqueda de patrón en una cadena
cadena = "La programación en Python es genial y fácil de aprender."
patron = "Python"
resultado = re.search(patron, cadena)
if resultado:
    print("Se encontró el patrón.")
else:
    print("No se encontró el patrón.")

# Ejemplo 2: Búsqueda y reemplazo
cadena = "Hola, mi nombre es Juan. Hola a todos."
patron = "Hola"
reemplazo = "Hola de nuevo"
resultado = re.sub(patron, reemplazo, cadena)
print(resultado)  # Salida: "Hola de nuevo, mi nombre es Juan. Hola de nuevo a todos."

# Ejemplo 3: Validación de formato de correo electrónico
correo = "usuario@example.com"
patron = r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b"
if re.fullmatch(patron, correo):
    print("El correo electrónico es válido.")
else:
    print("El correo electrónico no es válido.")

# Ejemplo 4: Búsqueda de todas las coincidencias de un patrón
cadena = "Python es un lenguaje de programación muy popular y Python es fácil de aprender."
patron = "Python"
resultados = re.findall(patron, cadena)
print(resultados)  # Salida: ['Python', 'Python']
```

¡Bienvenidos a la manipulación de cadenas y expresiones regulares! En este módulo, aprendimos cómo trabajar con texto en Python y cómo utilizar expresiones regulares para realizar operaciones más complejas con cadenas. Estos conceptos son esenciales para cualquier programador que desee manipular y procesar texto de manera eficiente y efectiva.
