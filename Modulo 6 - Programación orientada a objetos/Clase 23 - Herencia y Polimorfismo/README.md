# Clase 6: Herencia y Polimorfismo

En este módulo, exploraremos los conceptos de herencia y polimorfismo en el contexto de la programación orientada a objetos (POO). Estos conceptos nos permiten crear jerarquías de clases y aprovechar la flexibilidad y reutilización del código.

## Contenido

1. Introducción a la herencia
2. Clases base y clases derivadas
3. Herencia múltiple
4. Polimorfismo
5. Ejemplos

## 1. Introducción a la herencia

La herencia es un concepto fundamental en POO que nos permite crear nuevas clases basadas en clases existentes. Con la herencia, una clase nueva (denominada clase derivada o subclase) puede heredar atributos y métodos de una clase existente (denominada clase base o superclase). Esto nos permite compartir y reutilizar código, así como extender o especializar la funcionalidad de la clase base.

## 2. Clases base y clases derivadas

En la herencia, la clase base es la clase existente de la cual se heredan atributos y métodos. La clase derivada es la nueva clase que se crea utilizando la herencia y que hereda los atributos y métodos de la clase base. Para indicar la herencia, utilizamos la sintaxis de la declaración de clase, seguida del nombre de la clase base entre paréntesis.

```python
class ClaseBase:
    # Atributos y métodos de la clase base

class ClaseDerivada(ClaseBase):
    # Atributos y métodos adicionales de la clase derivada
```

En este ejemplo, `ClaseDerivada` se crea utilizando la herencia de `ClaseBase`. La clase derivada puede tener sus propios atributos y métodos adicionales, además de los que hereda de la clase base.

## 3. Herencia múltiple

La herencia múltiple es un concepto en el que una clase puede heredar atributos y métodos de múltiples clases base. En Python, se permite la herencia múltiple, lo que nos brinda una gran flexibilidad al diseñar jerarquías de clases.

```python
class ClaseBase1:
    # Atributos y métodos de la clase base 1

class ClaseBase2:
    # Atributos y métodos de la clase base 2

class ClaseDerivada(ClaseBase1, ClaseBase2):
    # Atributos y métodos adicionales de la clase derivada
```

En este ejemplo, `ClaseDerivada` hereda atributos y métodos tanto de `ClaseBase1` como de `ClaseBase2`. Esto permite que la clase derivada tenga acceso a los atributos y métodos de ambas clases base.

## 4. Polimorfismo

El polimorfismo es un concepto que permite que un objeto pueda tomar muchas formas o comportarse de diferentes maneras según el contexto. En POO, el polimorfismo nos permite utilizar una interfaz común para objetos de diferentes clases, lo que nos brinda flexibilidad y reutilización del código.

El polimorfismo se logra mediante el uso de herencia y métodos con el mismo nombre pero diferentes implementaciones en las clases derivadas. Esto nos permite tratar objetos de diferentes clases como si fueran del mismo tipo y llamar a los mismos métodos en ellos, aunque tengan comportamientos diferentes.

## 5. Ejemplos

En este módulo, se proporcionarán ejemplos prácticos para ilustrar los conceptos de herencia y polimorfismo. Algunos ejemplos pueden incluir la creación de una jerarquía de clases para representar animales, donde la clase base `Animal` tiene atributos y métodos comunes, y las clases derivadas, como `Perro` y `Gato`, heredan de la clase base y tienen comportamientos específicos.

Por supuesto, aquí tienes algunos ejemplos para ilustrar los conceptos de herencia y polimorfismo en el contexto de la programación orientada a objetos.

```python
# Ejemplo 1: Jerarquía de clases Animal

class Animal:
    def __init__(self, nombre):
        self.nombre = nombre

    def sonido(self):
        pass

class Perro(Animal):
    def sonido(self):
        return "Woof!"

class Gato(Animal):
    def sonido(self):
        return "Meow!"

# Crear objetos de las clases derivadas
perro1 = Perro("Bobby")
gato1 = Gato("Felix")

# Llamar al método sonido en diferentes objetos
print(perro1.sonido())  # Salida: Woof!
print(gato1.sonido())  # Salida: Meow!


# Ejemplo 2: Polimorfismo

class Figura:
    def calcular_area(self):
        pass

class Rectangulo(Figura):
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def calcular_area(self):
        return self.base * self.altura

class Circulo(Figura):
    def __init__(self, radio):
        self.radio = radio

    def calcular_area(self):
        return 3.14 * self.radio**2

# Crear objetos de las clases derivadas
rectangulo1 = Rectangulo(4, 5)
circulo1 = Circulo(3)

# Llamar al método calcular_area en diferentes objetos
print(rectangulo1.calcular_area())  # Salida: 20
print(circulo1.calcular_area())  # Salida: 28.26
```

En el ejemplo 1, se crea una jerarquía de clases para representar animales. La clase base `Animal` define un método `sonido()` que no tiene una implementación específica. Las clases derivadas `Perro` y `Gato` heredan de la clase base y proporcionan sus propias implementaciones para el método `sonido()`. Al crear objetos de las clases derivadas, podemos llamar al método `sonido()` en cada objeto y obtener el sonido correspondiente del animal.

En el ejemplo 2, se muestra el polimorfismo en acción. La clase base `Figura` define un método `calcular_area()` que no tiene una implementación específica. Las clases derivadas `Rectangulo` y `Circulo` heredan de la clase base y proporcionan sus propias implementaciones para el método `calcular_area()`. Al crear objetos de las clases derivadas, podemos llamar al método `calcular_area()` en cada objeto, y a pesar de que tienen implementaciones diferentes, podemos tratarlos de manera polimórfica y llamar al mismo método en todos ellos.

¡Bienvenido al mundo de la herencia y el polimorfismo! En este módulo, aprenderás cómo crear jerarquías de clases, compartir y reutilizar código, y cómo utilizar objetos de diferentes clases de manera flexible y eficiente. La herencia y el polimorfismo son conceptos poderosos que te permitirán crear programas más estructurados y extensibles en la programación orientada a objetos.
