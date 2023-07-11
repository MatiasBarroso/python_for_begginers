import unittest

# Ejercicio 1: Creación de un diccionario vacío
def crear_diccionario():
    # Completa el código para crear un diccionario vacío
    diccionario = {}
    return diccionario


# Ejercicio 2: Acceso a elementos de un diccionario
def obtener_valor(diccionario, clave):
    # Completa el código para obtener el valor asociado a la clave en el diccionario
    if clave in diccionario:
        valor = diccionario[clave]
    else:
        valor = None
    return valor


# Ejercicio 3: Modificación de valores en un diccionario
def modificar_valor(diccionario, clave, nuevo_valor):
    # Completa el código para modificar el valor asociado a la clave en el diccionario
    if clave in diccionario:
        diccionario[clave] = nuevo_valor


# Ejercicio 4: Agregar elementos a un diccionario
def agregar_elemento(diccionario, clave, valor):
    # Completa el código para agregar un nuevo par clave-valor al diccionario
    diccionario[clave] = valor


# Ejercicio 5: Eliminar elementos de un diccionario
def eliminar_elemento(diccionario, clave):
    # Completa el código para eliminar el par clave-valor del diccionario
    if clave in diccionario:
        del diccionario[clave]


