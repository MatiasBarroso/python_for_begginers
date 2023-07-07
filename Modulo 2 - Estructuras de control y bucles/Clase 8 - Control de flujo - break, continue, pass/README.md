# Clase 8: Control de flujo: break, continue, pass

En este módulo, aprenderemos sobre las herramientas de control de flujo adicionales en Python: `break`, `continue` y `pass`. Estas herramientas nos permiten tener un mayor control sobre cómo se ejecutan nuestros bucles y condicionales.

## `break`

La declaración `break` se utiliza para interrumpir la ejecución de un bucle de manera abrupta, sin completar todas las iteraciones. Cuando se encuentra la instrucción `break`, el bucle se detiene inmediatamente y el programa continúa con la siguiente línea de código fuera del bucle. Aquí tienes un ejemplo:

```python
for i in range(1, 6):
    if i == 4:
        break
    print(i)
```

En este caso, el bucle `for` imprimirá los números del 1 al 3, pero cuando `i` sea igual a 4, se encontrará la instrucción `break` y el bucle se detendrá.

## `continue`

La declaración `continue` se utiliza para saltar la iteración actual de un bucle y pasar a la siguiente iteración. Cuando se encuentra la instrucción `continue`, el programa salta el resto del bloque de código del bucle en esa iteración y continúa con la siguiente iteración. Aquí tienes un ejemplo:

```python
for i in range(1, 6):
    if i == 3:
        continue
    print(i)
```

En este caso, el bucle `for` imprimirá los números del 1 al 5, pero cuando `i` sea igual a 3, se encontrará la instrucción `continue` y esa iteración se saltará, omitiendo la impresión de ese número.

## `pass`

La declaración `pass` se utiliza como marcador de posición cuando no se desea realizar ninguna acción en un bloque de código, como en una función o un bucle. Es simplemente una instrucción nula que no hace nada. Aquí tienes un ejemplo:

```python
for i in range(1, 4):
    pass
```

En este caso, el bucle `for` no realizará ninguna acción dentro del bloque de código, ya que solo tiene la instrucción `pass`.

Estas herramientas de control de flujo (`break`, `continue` y `pass`) nos brindan flexibilidad adicional al trabajar con bucles y condicionales en Python. Nos permiten tener mayor control sobre la ejecución y tomar decisiones más precisas.

## Ejemplos de uso de `break`, `continue` y `pass`

Aquí tienes algunos ejemplos para ilustrar cómo utilizar estas herramientas:

```python
# Ejemplo de uso de break
for i in range(1, 6):
    if i == 3:
        break
    print(i)

# Ejemplo de uso de continue
for i in range(1, 6):
    if i == 3:
        continue
    print(i)

# Ejemplo de uso de pass
for i in range(1, 4):
    pass
```

En el primer ejemplo, el bucle `for` se detendrá cuando `i` sea igual a 3 debido a la instrucción `break`.

En el segundo ejemplo, el bucle `for` omitirá la iteración cuando `i` sea igual a 3 debido a la instrucción `continue`.

En el tercer ejemplo, el bucle `for` no realizará ninguna acción dentro del bloque de código debido a la instrucción `pass`.

Estas herramientas son útiles en diferentes situaciones y te permiten personalizar el comportamiento de tus bucles y condicionales según tus necesidades.

¡El uso adecuado de `break`, `continue` y `pass` puede ayudarte a tener un mayor control y eficiencia en tus programas en Python!

Recuerda completar el código en el archivo `ejercicios.py` para que los estudiantes puedan resolver los ejercicios.
