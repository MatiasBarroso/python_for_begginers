# Clase 19: Manipulación de archivos: lectura, escritura, cierre

En este módulo, aprenderemos cómo manipular archivos en Python, lo cual es una tarea fundamental en el desarrollo de aplicaciones y el procesamiento de datos. Exploraremos cómo realizar operaciones de lectura, escritura y cierre de archivos, además de abordar el manejo de excepciones en caso de errores durante estas operaciones.

**1. Lectura de archivos:**

- Para abrir un archivo en modo de lectura, utilizamos la función incorporada `open()` y especificamos la ruta del archivo y el modo de apertura como "r". Por ejemplo:

```python
archivo = open('ruta/archivo.txt', 'r')
```

- Podemos utilizar el método `read()` para leer todo el contenido del archivo como una cadena, o el método `readline()` para leer una línea a la vez.
- Es importante cerrar el archivo después de leerlo mediante el método `close()` para liberar los recursos del sistema operativo. Por ejemplo:

```python
archivo.close()
```

**2. Escritura de archivos:**

- Para abrir un archivo en modo de escritura, utilizamos la función `open()` y especificamos el modo de apertura como "w". Si el archivo no existe, se crea automáticamente. Si ya existe, se sobrescribe su contenido.
- Podemos utilizar el método `write()` para escribir datos en el archivo. Por ejemplo:

```python
archivo = open('ruta/archivo.txt', 'w')
archivo.write('Este es un ejemplo de texto.')
archivo.close()
```

**3. Cierre seguro de archivos con la cláusula "with":**

- La cláusula "with" nos permite abrir y cerrar automáticamente un archivo de manera segura, incluso si ocurren excepciones durante el proceso.
- En lugar de utilizar `archivo.close()` explícitamente, podemos usar la cláusula "with" de la siguiente manera:

```python
with open('ruta/archivo.txt', 'r') as archivo:
    contenido = archivo.read()
```

En este ejemplo, el archivo se cierra automáticamente al salir del bloque "with".

**4. Manejo de excepciones al trabajar con archivos:**

- Durante la manipulación de archivos, pueden ocurrir errores, como archivos no encontrados, permisos insuficientes o problemas de lectura/escritura. Para manejar estos errores, utilizamos bloques `try` y `except`.
- Por ejemplo, si queremos abrir un archivo para lectura y manejar el caso en el que no se encuentre, podemos hacer lo siguiente:

```python
try:
    archivo = open('ruta/archivo.txt', 'r')
    contenido = archivo.read()
    archivo.close()
except FileNotFoundError:
    print('El archivo no se encuentra.')
```

En este módulo, hemos aprendido cómo manipular archivos en Python. Desde la lectura de archivos y escritura de datos en ellos, hasta el cierre seguro y el manejo de excepciones. Estos conceptos nos proporcionan las herramientas necesarias para trabajar con archivos y procesar datos de manera efectiva en nuestros programas.
