# Clase 8: Creación y uso de módulos personalizados

En Python, un módulo es un archivo que contiene definiciones de funciones, clases y variables que pueden ser reutilizadas en diferentes programas. Los módulos permiten organizar el código y facilitan la reutilización y mantenimiento del mismo.

## Creación de un módulo personalizado

Para crear un módulo personalizado, simplemente creamos un archivo con extensión `.py` que contenga nuestras definiciones de funciones, clases o variables. Por ejemplo, vamos a crear un módulo llamado `operaciones` con algunas funciones matemáticas básicas:

**operaciones.py**

```python
def suma(a, b):
    return a + b

def resta(a, b):
    return a - b

def multiplicacion(a, b):
    return a * b

def division(a, b):
    if b != 0:
        return a / b
    else:
        raise ValueError("No se puede dividir por cero")
```

## Uso de un módulo personalizado

Una vez que hemos creado nuestro módulo personalizado, podemos utilizarlo en cualquier otro programa importando sus funciones o clases. Para ello, asegúrate de que el archivo del módulo (`operaciones.py`) se encuentre en el mismo directorio o en un directorio incluido en la variable de entorno `PYTHONPATH`.

**main.py**

```python
import operaciones

print(operaciones.suma(5, 3))  # Salida: 8
print(operaciones.resta(10, 4))  # Salida: 6
print(operaciones.multiplicacion(3, 7))  # Salida: 21

try:
    print(operaciones.division(10, 2))  # Salida: 5.0
    print(operaciones.division(10, 0))  # Generará un ValueError
except ValueError as error:
    print(error)
```

En este ejemplo, importamos el módulo `operaciones` y utilizamos sus funciones `suma`, `resta`, `multiplicacion` y `division` para realizar diferentes operaciones matemáticas.

## Ventajas de los módulos personalizados

- **Reutilización de código**: Podemos crear funciones y clases que resuelvan tareas específicas y utilizarlas en múltiples programas, evitando duplicación de código.

- **Organización del código**: Los módulos nos permiten organizar el código en diferentes archivos, lo que facilita la comprensión y mantenimiento de los programas.

- **Abstracción**: Al crear módulos, podemos encapsular funcionalidades complejas en funciones o clases con nombres significativos, lo que mejora la legibilidad y abstracción del código.

- **Facilita el trabajo en equipo**: Cuando trabajamos en equipo, los módulos nos permiten dividir el trabajo en tareas más pequeñas y separadas, lo que facilita la colaboración y el desarrollo en paralelo.

En resumen, los módulos personalizados son una herramienta poderosa en Python que nos permite crear, organizar y reutilizar código de manera eficiente. Su uso es fundamental para mantener programas ordenados y fáciles de mantener y extender.
