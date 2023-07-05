# Clase 1: Primer programa en Python: ¡Hola, mundo!

En este módulo, vamos a escribir nuestro primer programa en Python: ¡Hola, mundo! Este programa es un clásico en el mundo de la programación y es utilizado como una introducción para familiarizarse con el lenguaje.

## Paso 1

Abre el archivo llamado `hola_mundo.py`.

## Paso 2

Escribe el siguiente código:

```python
name = input("Ingresa tu nombre: ")
print("¡Hola, " + name + "!")
```

En este código, utilizamos la función `input()` para solicitar al usuario que ingrese su nombre. Luego, utilizamos la función `print()` para mostrar el mensaje "¡Hola, [tu nombre]!".

## Paso 3

Guarda el archivo `hola_mundo.py`.

## Paso 4

Abre una terminal o línea de comandos en la ubicación donde se encuentra el archivo `hola_mundo.py`.

### ¿Como abrir el terminal en Visual Studio Code?

- **Atajo de teclado:** Utiliza el atajo de teclado `Ctrl`+`Ñ` (tecla de acento grave) para abrir y cerrar la terminal integrada en Visual Studio Code. Este atajo funciona en la mayoría de los sistemas operativos.

- **Menú de Visual Studio Code:** En la barra de menú de Visual Studio Code, selecciona "View" (Vista) y luego elige "Terminal". Aparecerá la terminal integrada en la parte inferior de la ventana.

- **Barra de tareas:** En la barra de tareas inferior de Visual Studio Code, busca el icono de la terminal (generalmente tiene el símbolo ">\_") y haz clic en él. Esto abrirá la terminal integrada.

- **Comando de la paleta de comandos:** Utiliza el comando de la paleta de comandos de Visual Studio Code para abrir la terminal. Presiona `Ctrl+Shift+P` (o `Cmd+Shift+P` en macOS) para abrir la paleta de comandos, luego escribe "Terminal" y selecciona la opción "View: Toggle Terminal" (Ver: Alternar Terminal).

Estas son algunas formas comunes de abrir la terminal en Visual Studio Code. Puedes elegir la que más te convenga según tus preferencias y flujo de trabajo.

Recuerda que una vez que hayas abierto la terminal, asegúrate de navegar a la ubicación correcta donde se encuentra tu archivo `hola_mundo.py` antes de ejecutar el programa.

## Paso 5

Ejecuta el programa escribiendo el siguiente comando y presionando Enter:

```shell
python hola_mundo.py
```

Se mostrará el mensaje "Ingresa tu nombre: " en la consola. Ingresa tu nombre y presiona Enter.

Ejemplo:

```
Ingresa tu nombre: Ana
¡Hola, Ana!
```

Observa que el programa muestra el mensaje personalizado con tu nombre.

## Paso 6

Ahora, vamos a modificar el programa para que también pregunte la edad del usuario y muestre un mensaje apropiado de acuerdo a su edad.

```python
name = input("Ingresa tu nombre: ")
age = int(input("Ingresa tu edad: "))

if age >= 18:
    print("¡Hola, " + name + "! Eres mayor de edad.")
else:
    print("¡Hola, " + name + "! Eres menor de edad.")
```

Hemos agregado una nueva línea para solicitar al usuario que ingrese su edad utilizando la función `input()`. Luego, utilizamos una estructura condicional (`if-else`) para determinar si el usuario es mayor o menor de edad y mostramos un mensaje apropiado en función de su edad.

## Paso 7

Guarda los cambios en el archivo `hola_mundo.py`.

## Paso 8

Ejecuta nuevamente el programa escribiendo el siguiente comando y presionando Enter:

```shell
python hola_mundo.py
```

Se mostrarán los mensajes "Ingresa tu nombre: " y "Ingresa tu edad: " en la consola. Ingresa tu nombre y tu edad, y presiona Enter.

Ejemplo:

```
Ingresa tu nombre: Ana
Ingresa tu edad: 25
¡Hola, Ana! Eres mayor de edad.
```

Observa que el programa ahora muestra el mensaje apropiado según la edad ingresada.

Has completado el ejercicio de modificar el programa "Hola, mundo". En este ejercicio, has practicado la manipulación de cadenas de texto, la entrada de datos del usuario y el uso de estructuras condicionales en Python.

¡Sigue practicando y divirtiéndote programando en Python!
