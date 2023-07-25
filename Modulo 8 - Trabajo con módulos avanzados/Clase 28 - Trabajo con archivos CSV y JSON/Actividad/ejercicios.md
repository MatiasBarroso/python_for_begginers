¡Claro! Aquí tienes algunos ejercicios para aplicar los conceptos trabajados en el módulo "Trabajo con archivos CSV y JSON" de la Clase 8:

Ejercicio 1: Leer datos desde un archivo CSV

- En el archivo CSV llamado "empleados.csv", escribe la siguiente estructura:

```
Nombre,Edad,Cargo
Juan,30,Ingeniero
María,25,Analista
Carlos,35,Gerente
```

- En el archivo, `ejercicios.py`, escribe una función llamada `leer_empleados_csv(archivo)` que reciba el nombre del archivo CSV y devuelva una lista de diccionarios, donde cada diccionario representa un empleado con las claves "Nombre", "Edad" y "Cargo".

Ejercicio 2: Escribir datos en un archivo CSV

- Define una lista de diccionarios que represente información sobre empleados, similar a la estructura del Ejercicio 1.
- Escribe una función llamada `escribir_empleados_csv(empleados, archivo)` que reciba la lista de diccionarios de empleados y el nombre del archivo CSV, y escriba los datos en el archivo CSV en el formato adecuado.

Ejercicio 3: Leer datos desde un archivo JSON

- En el archivo `productos.json` escribe la siguiente estructura:

```json
[
  {
    "nombre": "Camiseta",
    "precio": 20.99,
    "stock": 50
  },
  {
    "nombre": "Pantalón",
    "precio": 35.5,
    "stock": 30
  },
  {
    "nombre": "Zapatos",
    "precio": 50.0,
    "stock": 25
  }
]
```

- En el archivo `ejercicios.py`, esribe una función llamada `leer_productos_json(archivo)` que reciba el nombre del archivo JSON y devuelva una lista de diccionarios, donde cada diccionario representa un producto con las claves "nombre", "precio" y "stock".

Ejercicio 4: Escribir datos en un archivo JSON

- Define una lista de diccionarios que represente información sobre productos, similar a la estructura del Ejercicio 3.
- Escribe una función llamada `escribir_productos_json(productos, archivo)` que reciba la lista de diccionarios de productos y el nombre del archivo JSON, y escriba los datos en el archivo JSON en el formato adecuado.

Ejercicio 5: Generar un informe desde datos en un archivo CSV

- En el archivo llamado `ventas.csv`, escribe la siguiente estructura:

```
Producto,Cantidad,PrecioUnitario
Camiseta,15,20.99
Pantalón,8,35.50
Zapatos,5,50.00
```

- En el archivo `ejercicios.py` escribe una función llamada `generar_informe(archivo)` que lea los datos del archivo CSV y genere un informe en forma de diccionario, donde cada clave sea el nombre del producto y el valor sea el total de ventas (cantidad \* precio unitario) para ese producto.

Ejercicio 6: Obtener el producto más vendido desde un archivo JSON

- En el archivo llamado `ventas.json`, escribe la siguiente estructura:

```json
{
  "ventas": [
    { "producto": "Camiseta", "cantidad": 15, "precio_unitario": 20.99 },
    { "producto": "Pantalón", "cantidad": 8, "precio_unitario": 35.5 },
    { "producto": "Zapatos", "cantidad": 5, "precio_unitario": 50.0 }
  ]
}
```

- Escribe una función llamada `producto_mas_vendido(archivo)` que lea los datos del archivo JSON y devuelva el nombre del producto que ha sido más vendido.

Estos ejercicios te permitirán practicar la lectura y escritura de archivos CSV y JSON, así como el procesamiento de datos en estos formatos. Puedes utilizar el módulo `unittest` para crear pruebas automatizadas que verifiquen el correcto funcionamiento de tus funciones.
