# Clase 5: Encapsulamiento y Modularidad

En este módulo, exploraremos los conceptos de encapsulamiento y modularidad en la programación orientada a objetos (POO). Estos conceptos nos permiten crear programas más organizados, flexibles y seguros al ocultar la implementación interna de las clases y promover la reutilización del código.

## Contenido

1. Introducción al encapsulamiento
2. Visibilidad de atributos y métodos
3. Métodos de acceso (getters y setters)
4. Modularidad y reutilización del código
5. Ejemplos

## 1. Introducción al encapsulamiento

El encapsulamiento es un principio clave de la POO que consiste en agrupar datos y comportamiento relacionado dentro de una clase, ocultando los detalles internos y exponiendo solo una interfaz pública para interactuar con la clase. Esto protege los datos de acceso no autorizado y evita que otros componentes del programa dependan de la implementación interna de la clase.

## 2. Visibilidad de atributos y métodos

En la programación orientada a objetos, la visibilidad de los atributos y métodos se refiere a qué partes del programa pueden acceder y utilizarlos. En Python, la visibilidad se controla mediante convenciones de nomenclatura y mediante el uso de modificadores de acceso. Aunque Python no tiene modificadores de acceso estrictos como otros lenguajes (como `public`, `protected` y `private`), existen convenciones que indican el nivel de visibilidad de los atributos y métodos.

Aquí están los tres niveles de visibilidad comunes en Python:

### Atributos y métodos públicos

Los atributos y métodos públicos son aquellos que se pueden acceder desde cualquier parte del programa que tenga una referencia al objeto de la clase. En Python, los atributos y métodos públicos se nombran con letras minúsculas y palabras separadas por guiones bajos. Por convención, se consideran accesibles y seguros de utilizar desde cualquier contexto.

```python
class Persona:
    def __init__(self, nombre):
        self.nombre = nombre

    def saludar(self):
        print(f"Hola, mi nombre es {self.nombre}.")
```

En este ejemplo, `nombre` es un atributo público y `saludar()` es un método público. Pueden ser accedidos y utilizados directamente desde fuera de la clase.

### Atributos y métodos protegidos

Los atributos y métodos protegidos son aquellos que se consideran como una convención interna de la clase, y aunque se pueden acceder desde fuera de la clase, se indica que no deben ser utilizados directamente. En Python, los atributos y métodos protegidos se nombran con un guion bajo al comienzo del nombre del atributo o método.

```python
class Persona:
    def __init__(self, nombre):
        self._nombre = nombre

    def _saludar(self):
        print(f"Hola, mi nombre es {self._nombre}.")
```

En este ejemplo, `_nombre` es un atributo protegido y `_saludar()` es un método protegido. Aunque se pueden acceder desde fuera de la clase, su uso directo se desaconseja y se considera una convención interna de la clase.

### Atributos y métodos privados

Los atributos y métodos privados son aquellos que se consideran estrictamente internos de la clase y no deben ser accedidos desde fuera de la clase. En Python, los atributos y métodos privados se nombran con dos guiones bajos al comienzo del nombre del atributo o método.

```python
class Persona:
    def __init__(self, nombre):
        self.__nombre = nombre

    def __saludar(self):
        print(f"Hola, mi nombre es {self.__nombre}.")
```

En este ejemplo, `__nombre` es un atributo privado y `__saludar()` es un método privado. Son inaccesibles desde fuera de la clase. Si intentamos acceder a ellos, Python generará un error.

Es importante destacar que la visibilidad en Python se basa en convenciones y no en restricciones estrictas. Si bien se pueden acceder y utilizar atributos y métodos protegidos y privados desde fuera de la clase, se espera que los desarrolladores respeten las convenciones y eviten su uso directo. Esto ayuda a mantener una interfaz pública clara y a evitar dependencias en la implementación interna de la clase.

## 3. Métodos de acceso (getters y setters)

Los métodos de acceso, también conocidos como getters y setters, se utilizan para acceder y modificar los atributos de una clase de forma controlada. Los getters se utilizan para obtener el valor de un atributo y los setters se utilizan para asignar un valor al atributo. Estos métodos proporcionan una interfaz para interactuar con los atributos de la clase y permiten la validación y modificación de datos.

```python
class Persona:
    def __init__(self, nombre, edad):
        self._nombre = nombre
        self._edad = edad

    def get_nombre(self):
        return self._nombre

    def set_nombre(self, nombre):
        self._nombre = nombre

    def get_edad(self):
        return self._edad

    def set_edad(self, edad):
        if edad >= 0:
            self._edad = edad
        else:
            raise ValueError("La edad debe ser mayor o igual a cero.")
```

En este ejemplo, se definen métodos getters y setters para los atributos `_nombre` y `_edad` de la clase `Persona`. Los métodos de acceso permiten obtener y modificar los valores de los atributos, y en el caso del setter de `edad`, se realiza una validación para asegurarse de que la edad sea mayor o igual a cero.

## 4. Modularidad y reutilización del código

La modularidad es un principio importante en la programación que consiste en dividir un programa en módulos más pequeños y cohesivos. En la POO, esto se logra mediante la creación de clases y módulos que encapsulan datos y comportamiento relacionado. Esto nos permite reutilizar el código, ya que los módulos y clases pueden ser utilizados en diferentes partes del programa sin necesidad de volver a escribir el mismo código.

## 5. Ejemplos

En este módulo, se proporcionarán ejemplos prácticos para ilustrar los conceptos de encapsulamiento y modularidad. Algunos ejemplos pueden incluir la creación de una clase `Banco` que encapsula información sobre cuentas bancarias y proporciona métodos para realizar operaciones, o la creación de un módulo `Utilidades` que contiene funciones y clases genéricas que pueden ser utilizadas en diferentes partes del programa.

¡Bienvenido al mundo del encapsulamiento y la modularidad! En este módulo, aprenderás cómo utilizar el encapsulamiento para ocultar la implementación interna de las clases y promover la reutilización del código mediante la modularidad. Estos conceptos son fundamentales para construir programas más organizados, flexibles y seguros en la programación orientada a objetos.
