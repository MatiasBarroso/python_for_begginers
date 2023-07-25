# Clase 28: Trabajo con archivos CSV y JSON

En esta clase, aprenderemos a trabajar con archivos CSV y JSON en Python. Estos formatos son ampliamente utilizados para el intercambio de datos estructurados y son muy importantes en el mundo de la programación.

## Archivos CSV (Comma Separated Values)

### ¿Qué es un archivo CSV?

CSV es un formato de archivo que se utiliza para representar datos tabulares. Los valores están separados por comas, lo que permite almacenar datos en filas y columnas. Es ampliamente utilizado para compartir datos entre diferentes aplicaciones.

### Módulo `csv`

El módulo `csv` de Python proporciona varias funciones y clases para trabajar con archivos CSV (Comma Separated Values). A continuación, se presentan algunas de las funciones más importantes y útiles que ofrece este módulo:

1. `csv.reader(file, dialect='excel', **kwargs)`: Esta función crea un objeto lector para leer datos desde un archivo CSV. Toma un objeto de archivo abierto y devuelve un iterador que produce listas con los datos de cada fila.

2. `csv.DictReader(file, fieldnames=None, restkey=None, restval=None, dialect='excel', **kwargs)`: Es similar a `csv.reader`, pero devuelve un iterador que produce diccionarios en lugar de listas. Cada fila del archivo CSV se convierte en un diccionario, donde las claves son los nombres de las columnas y los valores son los datos de esa fila.

3. `csv.writer(file, dialect='excel', **kwargs)`: Esta función crea un objeto escritor para escribir datos en un archivo CSV. Toma un objeto de archivo abierto y devuelve un escritor que puede ser utilizado para escribir listas de datos en el archivo.

4. `csv.DictWriter(file, fieldnames, restval='', extrasaction='raise', dialect='excel', **kwargs)`: Es similar a `csv.writer`, pero está diseñado para escribir diccionarios en lugar de listas. Permite especificar los nombres de las columnas y utiliza estos nombres como claves para escribir los datos del diccionario en el archivo CSV.

5. `csv.register_dialect(name, dialect, **fmtparams)`: Esta función registra un dialecto CSV personalizado para su posterior uso con las funciones `csv.reader` y `csv.writer`. Un dialecto define cómo se interpretarán los datos, incluyendo el delimitador, el carácter de cita, el carácter de escape y otros parámetros.

6. `csv.unregister_dialect(name)`: Elimina un dialecto CSV previamente registrado con `csv.register_dialect`.

7. `csv.get_dialect(name)`: Obtiene un objeto que representa un dialecto CSV registrado.

8. `csv.list_dialects()`: Devuelve una lista de los nombres de todos los dialectos CSV registrados.

Estas son algunas de las funciones principales que ofrece el módulo `csv` de Python. Además, también proporciona excepciones como `csv.Error`, que se utiliza para manejar errores relacionados con operaciones CSV. Te recomendamos consultar la documentación oficial de Python para obtener información más detallada sobre las funciones y clases del módulo `csv`: https://docs.python.org/3/library/csv.html

### Ejemplo:

Supongamos que tenemos un archivo CSV llamado "datos.csv" con el siguiente contenido:

```csv
Nombre,Edad,Email
Juan,25,juan@example.com
María,30,maria@example.com
Carlos,22,carlos@example.com
```

### Lectura de archivos CSV:

Para leer datos desde un archivo CSV, podemos utilizar el módulo `csv` de Python. Aquí hay un ejemplo:

```python
import csv
```

En esta línea, estamos importando el módulo `csv`, que es una biblioteca estándar de Python para trabajar con archivos CSV (Comma Separated Values).

```python
with open('datos.csv', newline='') as archivo_csv:
```

Aquí, abrimos el archivo CSV llamado "datos.csv" en modo de lectura. El parámetro `'newline=''` se utiliza para asegurarse de que no se interpreten saltos de línea adicionales durante la lectura del archivo. La declaración `with` se encarga de cerrar automáticamente el archivo después de que se ejecute el bloque de código que está indentado debajo.

```python
lector = csv.reader(archivo_csv)
```

Creamos un objeto lector utilizando la función `csv.reader()`. Este objeto nos permitirá leer los datos del archivo CSV. Le pasamos el archivo abierto `archivo_csv` como argumento.

```python
for fila in lector:
    print(fila)
```

En esta parte, utilizamos un bucle `for` para recorrer el lector de CSV línea por línea. Cada línea del archivo se convierte en una lista, donde cada elemento de la lista representa un valor separado por comas de la fila. Cada línea se almacena temporalmente en la variable `fila`.

Finalmente, dentro del bucle, imprimimos cada línea (es decir, cada lista) utilizando `print(fila)`. Esto mostrará en la consola cada fila del archivo CSV en forma de lista.

Si asumimos que el archivo "datos.csv" tiene el siguiente contenido:

```
Nombre,Edad,Email
Juan,25,juan@example.com
María,30,maria@example.com
Carlos,22,carlos@example.com
```

La salida del código sería:

```
['Nombre', 'Edad', 'Email']
['Juan', '25', 'juan@example.com']
['María', '30', 'maria@example.com']
['Carlos', '22', 'carlos@example.com']
```

Cada línea del archivo CSV se muestra como una lista donde los elementos están separados por comas. Ten en cuenta que los elementos de la lista son cadenas, incluso si representan números. Si necesitas trabajar con valores numéricos, tendrías que realizar conversiones de cadenas a números según sea necesario.

### Salida:

```
['Nombre', 'Edad', 'Email']
['Juan', '25', 'juan@example.com']
['María', '30', 'maria@example.com']
['Carlos', '22', 'carlos@example.com']
```

### Escritura de archivos CSV:

Para escribir datos en un archivo CSV, tambien utilizaremos el modulo `csv`. Aquí hay un ejemplo:

```python
import csv

datos = [
    ['Nombre', 'Edad', 'Email'],
    ['Juan', '25', 'juan@example.com'],
    ['María', '30', 'maria@example.com'],
    ['Carlos', '22', 'carlos@example.com']
]

with open('datos_nuevos.csv', 'w', newline='') as archivo_csv:
    escritor = csv.writer(archivo_csv)
    escritor.writerows(datos)
```

El parámetro 'w' indica que el archivo se abrirá en modo de escritura y, si el archivo ya existe, su contenido se sobrescribirá.
Creamos un objeto escritor utilizando la función csv.writer(). Este objeto nos permitirá escribir datos en el archivo CSV que hemos abierto. Le pasamos el archivo abierto archivo_csv como argumento.
Finalmente, utilizamos el objeto escritor para escribir los datos en el archivo CSV. La función writerows() toma una lista de listas (datos en este caso) y escribe cada sublista como una fila en el archivo CSV. Cada elemento de las sublistas se separa automáticamente por comas para formar las columnas del archivo CSV.

El resultado final del archivo "datos_nuevos.csv" sería:

```
Nombre,Edad,Email
Juan,25,juan@example.com
María,30,maria@example.com
Carlos,22,carlos@example.com
```

Con esto, has creado con éxito un nuevo archivo CSV llamado "datos_nuevos.csv" y has escrito los datos contenidos en la lista datos en él. Los datos ahora están almacenados en formato CSV y pueden ser utilizados para su posterior procesamiento o análisis. ¡Excelente trabajo!

## Archivos JSON (JavaScript Object Notation)

### ¿Qué es un archivo JSON?

JSON es un formato de intercambio de datos ligero y fácil de leer. Se utiliza ampliamente para transmitir datos estructurados a través de una red o para almacenar datos de configuración.

### Módulo `json`

El módulo `json` de Python proporciona funciones para trabajar con datos en formato JSON (JavaScript Object Notation). JSON es un formato de intercambio de datos ampliamente utilizado debido a su facilidad de lectura y escritura tanto para humanos como para máquinas. A continuación, se presentan algunas de las funciones más importantes del módulo `json`:

1. `json.dumps(obj, *, skipkeys=False, ensure_ascii=True, check_circular=True, allow_nan=True, cls=None, indent=None, separators=None, default=None, sort_keys=False, **kw)`: Esta función toma un objeto de Python y lo convierte en una cadena de texto en formato JSON (serialización). Puedes ajustar el comportamiento de la serialización utilizando los argumentos opcionales.

2. `json.dump(obj, fp, *, skipkeys=False, ensure_ascii=True, check_circular=True, allow_nan=True, cls=None, indent=None, separators=None, default=None, sort_keys=False, **kw)`: Similar a `json.dumps`, pero en lugar de retornar la cadena JSON, escribe el resultado en un archivo (objeto de archivo) dado por `fp`.

3. `json.loads(s, *, cls=None, object_hook=None, parse_float=None, parse_int=None, parse_constant=None, object_pairs_hook=None, **kw)`: Esta función toma una cadena JSON y la convierte en un objeto de Python (deserialización). Puedes utilizar argumentos opcionales para personalizar la deserialización.

4. `json.load(fp, *, cls=None, object_hook=None, parse_float=None, parse_int=None, parse_constant=None, object_pairs_hook=None, **kw)`: Similar a `json.loads`, pero en lugar de tomar una cadena, lee la cadena JSON desde un objeto de archivo (fp).

Estas son las funciones principales del módulo `json`, y te permiten convertir datos entre Python y JSON de manera sencilla y eficiente. También hay otros parámetros y opciones que puedes utilizar para controlar el proceso de serialización y deserialización según tus necesidades.

Estas son algunas de las funciones principales que ofrece el módulo json de Python. Te recomendamos consultar la documentación oficial de Python para obtener información más detallada sobre las funciones y clases del módulo csv: https://docs.python.org/3/library/json.html

### Ejemplo:

Supongamos que tenemos un archivo JSON llamado `"datos.json"` con el siguiente contenido:

```json
{
  "nombre": "Juan",
  "edad": 25,
  "email": "juan@example.com"
}
```

### Lectura de archivos JSON:

Para leer datos desde un archivo JSON, podemos utilizar el módulo `json` de Python. Aquí hay un ejemplo:

```python
import json

with open('datos.json') as archivo_json:
    datos = json.load(archivo_json)

print(datos)
```

La función `json.load()` es utilizada para cargar los datos del archivo JSON abierto en el paso anterior. Esta función deserializa el contenido JSON y lo convierte en un objeto de Python. En este caso, los datos se almacenan en la variable `datos`. Finalmente, se imprime en la consola el contenido de la variable `datos`.

En resumen, este código carga el contenido del archivo JSON 'datos.json' y lo almacena en la variable datos, para luego imprimirlo en la consola.

### Salida:

```
{'nombre': 'Juan', 'edad': 25, 'email': 'juan@example.com'}
```

### Escritura de archivos JSON:

Para escribir datos en un archivo JSON, lo hacemos de la siguiente manera:

```python
import json

datos = {
    "nombre": "Juan",
    "edad": 25,
    "email": "juan@example.com"
}

with open('datos_nuevos.json', 'w') as archivo_json:
    json.dump(datos, archivo_json)
```

La función `json.dump(objeto, archivo)` es parte del módulo `json` de Python y se utiliza para escribir datos en formato JSON en un archivo.

- `objeto`: Es el objeto que se desea convertir a formato JSON y escribir en el archivo. Puede ser un diccionario, una lista, una cadena, un número u otro objeto válido que pueda ser representado en JSON.

- `archivo`: Es el objeto archivo abierto en modo de escritura (`'w'`) donde se escribirá el contenido en formato JSON.

La función `json.dump(objeto, archivo)` toma el objeto y lo serializa en formato JSON, escribiéndolo en el archivo proporcionado. La serialización es el proceso de convertir un objeto de Python en una representación en cadena en formato JSON, que puede ser almacenada en un archivo o transmitida a través de una red.

En el ejemplo, se utiliza `json.dump(datos, archivo_json)` para escribir el diccionario `datos` en el archivo "datos_nuevos.json" en formato JSON. El resultado sera el siguiente:

```json
{
  "nombre": "Juan",
  "edad": 25,
  "email": "juan@example.com"
}
```

Ahora, tienes un archivo JSON llamado "datos_nuevos.json" que contiene los datos del diccionario `datos`. ¡Excelente trabajo!

Con estos ejemplos, ahora deberías tener una comprensión básica de cómo trabajar con archivos CSV y JSON en Python. Estos formatos son muy útiles para almacenar y compartir datos estructurados en tus proyectos. ¡Continúa practicando y explorando para mejorar tus habilidades en Python!
