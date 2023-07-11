# Clase 22: Conceptos básicos de POO: clases, objetos, atributos, métodos

En este módulo, exploraremos los conceptos fundamentales de la Programación Orientada a Objetos (POO). La POO es un paradigma de programación que nos permite organizar y estructurar nuestro código de manera más eficiente y modular. A través de la POO, creamos objetos que contienen tanto datos como funciones relacionadas, lo que nos permite modelar entidades del mundo real de una manera más fiel.

## Contenido

1. Introducción a la POO
2. Clases
3. Objetos
4. Atributos
5. Métodos
6. Ejemplos

# 1. Introducción a la POO

La Programación Orientada a Objetos es un paradigma de programación que se basa en la idea de organizar el código alrededor de objetos, que son entidades con propiedades y comportamientos asociados. En lugar de enfocarnos en la secuencia de instrucciones, nos centramos en la interacción entre los objetos.

# 2. Clases

En Python, una clase es una estructura que permite definir un nuevo tipo de objeto. Las clases son la base de la Programación Orientada a Objetos (POO) y nos permiten crear objetos que contienen tanto datos (atributos) como comportamientos (métodos) relacionados.

### Definición de una clase

La sintaxis básica para definir una clase en Python es la siguiente:

```python
class NombreClase:
    # Definición de atributos y métodos
    pass
```

La palabra clave `class` se utiliza para indicar que estamos creando una nueva clase, seguida por el nombre de la clase, que por convención se escribe en CamelCase con la primera letra en mayúscula. Dentro de la clase, podemos definir los atributos y métodos que queremos que los objetos de esa clase tengan.

### Atributos de clase y atributos de instancia

En una clase, podemos definir atributos que almacenan información asociada a los objetos. Hay dos tipos de atributos en Python: atributos de clase y atributos de instancia.

Los atributos de clase son compartidos por todos los objetos de la clase y se definen fuera de cualquier método dentro de la clase. Estos atributos se pueden acceder a través de la clase misma o cualquier objeto de la clase. Se definen utilizando la sintaxis `nombre_atributo = valor`.

```python
class Persona:
    nacionalidad = "Española"
```

En este ejemplo, `nacionalidad` es un atributo de clase que tiene el valor "Española". Todos los objetos de la clase `Persona` compartirán este mismo valor para `nacionalidad`.

Los atributos de instancia son específicos de cada objeto y se definen dentro del método especial `__init__()` de la clase. Estos atributos se asignan a través del objeto utilizando la notación de punto (`self.nombre_atributo = valor`) dentro de `__init__()`.

```python
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
```

En este ejemplo, `nombre` y `edad` son atributos de instancia que se asignan a cada objeto `Persona` creado. Cada objeto tendrá su propio valor para estos atributos.

### Métodos de clase y métodos de instancia

Los métodos son funciones definidas dentro de una clase que definen el comportamiento de los objetos. Hay dos tipos de métodos en Python: métodos de clase y métodos de instancia.

Los métodos de clase son métodos que se aplican a toda la clase en lugar de a instancias individuales. Se definen utilizando el decorador `@classmethod` encima del método y toman la clase como primer argumento en lugar del objeto (`cls` en lugar de `self`).

```python
class Persona:
    @classmethod
    def saludar(cls):
        print("Hola, soy una persona.")
```

En este ejemplo, `saludar()` es un método de clase que se puede llamar directamente desde la clase `Persona`. No está relacionado con ningún objeto en particular.

Los métodos de instancia son métodos que operan en objetos individuales creados a partir de la clase. Se definen sin el decorador `@classmethod` y toman el objeto actual como primer argumento (`self`).

```python
class Persona:
    def __init__(self, nombre):
        self.nombre = nombre

    def presentarse(self):
        print(f"Hola, soy {self.nombre}.")
```

En este ejemplo, `presentarse()` es un método de instancia que se aplica a objetos individuales de la clase `Persona`. Cada objeto puede llamar a este método y acceder a sus propios atributos.

### Uso de la clase

Una vez que hemos definido una clase, podemos crear objetos a partir de ella utilizando la sintaxis `nombre_objeto = NombreClase()`. Los objetos creados a partir de una clase se conocen como instancias de la clase.

```python
class Persona:
    def __init__(self, nombre):
        self.nombre = nombre

persona1 = Persona("Juan")
persona2 = Persona("María")
```

En este ejemplo, `persona1` y `persona2` son dos instancias de la clase `Persona`. Cada una tiene su propio atributo `nombre` con el valor especificado al crear el objeto.

Podemos acceder a los atributos y métodos de un objeto utilizando la notación de punto (`nombre_objeto.atributo` o `nombre_objeto.metodo()`).

```python
print(persona1.nombre)  # Salida: Juan
persona2.presentarse()  # Salida: Hola, soy María.
```

En resumen, las clases en Python nos permiten definir nuevas estructuras de datos que contienen atributos y métodos relacionados. Los objetos creados a partir de una clase son instancias específicas de esa clase y nos permiten trabajar con datos y comportamientos encapsulados en la clase.

# 3. Objetos

En Python, los objetos son instancias específicas de una clase. Cada objeto creado a partir de una clase es una entidad única con su propio estado (atributos) y comportamiento (métodos). Los objetos nos permiten interactuar con los datos y comportamientos definidos en una clase.

### Creación de objetos

Para crear un objeto, utilizamos la sintaxis de invocación de la clase seguida de paréntesis vacíos o con argumentos si la clase tiene un constructor definido. La invocación de la clase devuelve una nueva instancia de la clase, es decir, un nuevo objeto.

```python
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

# Creación de objetos
persona1 = Persona("Juan", 25)
persona2 = Persona("María", 30)
```

En el ejemplo anterior, la clase `Persona` tiene un constructor `__init__()` que se llama automáticamente al crear un objeto. Los argumentos `nombre` y `edad` se pasan al constructor para inicializar los atributos `nombre` y `edad` de cada objeto.

Cada objeto creado a partir de una clase tiene su propia área de memoria y almacena sus propios valores para los atributos definidos en la clase. Esto significa que cada objeto puede tener diferentes valores para los atributos, lo que les permite representar entidades únicas con características individuales.

### Acceso a los atributos y métodos

Para acceder a los atributos y métodos de un objeto, utilizamos la notación de punto (`objeto.atributo` o `objeto.metodo()`). El operador de punto nos permite interactuar con los datos y comportamientos definidos en la clase a través de un objeto específico.

```python
print(persona1.nombre)  # Salida: Juan
persona2.edad = 31  # Modificación del valor del atributo
```

En el ejemplo anterior, `persona1.nombre` accede al atributo `nombre` del objeto `persona1` y devuelve su valor "Juan". También podemos modificar el valor de un atributo utilizando la notación de punto, como se muestra con `persona2.edad = 31`, donde se actualiza el valor del atributo `edad` del objeto `persona2`.

Para llamar a un método de un objeto, utilizamos la misma notación de punto seguida de paréntesis. Los métodos pueden realizar acciones o cálculos basados en los datos del objeto.

```python
persona1.saludar()  # Llamada al método saludar()
```

En este ejemplo, `saludar()` es un método definido en la clase `Persona` y se llama en el objeto `persona1` utilizando la notación de punto. El método `saludar()` puede acceder a los atributos del objeto y realizar alguna acción, como imprimir un saludo con el nombre de la persona.

### Comportamiento individual de los objetos

Cada objeto tiene su propio conjunto de valores para los atributos definidos en la clase. Esto significa que los objetos pueden tener características y comportamientos individuales, lo que los distingue unos de otros.

```python
class Perro:
    def __init__(self, nombre, raza):
        self.nombre = nombre
        self.raza = raza

    def ladrar(self):
        print(f"{self.nombre} está ladrando.")

perro1 = Perro("Bobby", "Labrador")
perro2 = Perro("Rex", "Pastor Alemán")

perro1.ladrar()  # Salida: Bobby está ladrando.
perro2.ladrar()  # Salida: Rex está ladrando.
```

En este ejemplo, se definen dos objetos `perro1` y `perro2` a partir de la clase `Perro`. Cada perro tiene su propio nombre y raza, y cuando se llama al método `ladrar()`, se imprime el nombre del perro seguido de "está ladrando". Cada objeto tiene un comportamiento individual basado en sus propios atributos.

### Relaciones entre objetos

Los objetos también pueden interactuar entre sí. Pueden comunicarse, intercambiar datos o incluso invocar métodos de otros objetos. Esto permite modelar relaciones y estructuras más complejas en nuestros programas.

```python
class Persona:
    def __init__(self, nombre):
        self.nombre = nombre

    def saludar(self):
        print(f"Hola, soy {self.nombre}. ¡Mucho gusto!")

class Amigo:
    def __init__(self, nombre):
        self.nombre = nombre

    def saludar_amigo(self, amigo):
        print(f"Hola {amigo.nombre}, soy {self.nombre}. ¡Qué bueno verte!")

juan = Persona("Juan")
maria = Persona("María")
amigo1 = Amigo("Carlos")

juan.saludar()  # Salida: Hola, soy Juan. ¡Mucho gusto!
maria.saludar()  # Salida: Hola, soy María. ¡Mucho gusto!
amigo1.saludar_amigo(juan)  # Salida: Hola Juan, soy Carlos. ¡Qué bueno verte!
```

En este ejemplo, se definen una clase `Persona` y una clase `Amigo`. La clase `Persona` tiene un método `saludar()`, mientras que la clase `Amigo` tiene un método `saludar_amigo()` que acepta un objeto `Persona` como argumento. Los objetos `juan`, `maria` y `amigo1` interactúan llamando a los métodos de otros objetos.

En resumen, los objetos en Python son instancias específicas de una clase. Cada objeto tiene su propio estado (atributos) y comportamiento (métodos). Los objetos nos permiten representar entidades únicas y trabajar con datos y comportamientos específicos de cada objeto. Además, los objetos pueden interactuar entre sí, lo que nos permite modelar relaciones y estructuras más complejas en nuestros programas.

## 4. Atributos

Los atributos son variables que almacenan información sobre el estado de un objeto. Los atributos pueden ser variables de instancia, que son específicas de cada objeto, o variables de clase, que son compartidas por todos los objetos de esa clase. Los atributos nos permiten representar las características de un objeto y definir cómo se ve y se comporta.

Ejemplo de una clase `Persona` con atributos de instancia:

```python
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

# Creación de objetos
persona1 = Persona("Juan", 25)
persona2 = Persona("María", 30)
```

En este ejemplo, la clase `Persona` tiene dos atributos de instancia: `nombre` y `edad`. Cada objeto `persona1` y `persona2` tiene su propio conjunto de valores para estos atributos.

## 5. Métodos

Los métodos son funciones definidas dentro de una clase que definen el comportamiento de los objetos. Los métodos nos permiten especificar qué puede hacer un objeto y cómo interactúa con otros objetos. Los métodos pueden acceder y modificar los atributos de un objeto, así como realizar cálculos y manipulaciones específicas.

Ejemplo de una clase `Círculo` con métodos para calcular el área y el perímetro:

```python
import math

class Circulo:
    def __init__(self, radio):
        self.radio = radio

    def calcular_area(self):
        return math.pi * self.radio ** 2

    def calcular_perimetro(self):
        return 2 * math.pi * self.radio

# Creación de objeto
circulo = Circulo(5)
area = circulo.calcular_area()
perimetro = circulo.calcular_perimetro()
```

En este ejemplo, la clase `Circulo` tiene dos métodos: `calcular_area()` y `calcular_perimetro()`. Estos métodos realizan cálculos basados en el atributo `radio` del objeto `circulo`.

¡Bienvenido al mundo de la Programación Orientada a Objetos! En este módulo, adquirirás los conocimientos básicos sobre clases, objetos, atributos y métodos. Estos conceptos te permitirán crear programas más estructurados, modulares y fáciles de mantener. A medida que avancemos, descubrirás cómo la POO te ofrece un enfoque poderoso para modelar y resolver problemas de programación de manera más intuitiva y eficiente.
