# Función para calcular el precio total de una compra
def calcular_precio_total(precios, cantidades):
    total = 0
    for libro in precios:
        if libro in cantidades:
            total += precios[libro] * cantidades[libro]
    return total

# Función para verificar si un libro está disponible
def verificar_disponibilidad(libros_disponibles, libro):
    return libro in libros_disponibles

# Función para mostrar el listado de libros disponibles
def mostrar_libros_disponibles(libros_disponibles):
    print("Libros disponibles:")
    for libro in libros_disponibles:
        print(libro)

# Prueba de las funciones
precios = {'Harry Potter': 25, 'El señor de los anillos': 30, 'Cien años de soledad': 20}
cantidades = {'Harry Potter': 2, 'Cien años de soledad': 1}

precio_total = calcular_precio_total(precios, cantidades)
print("Precio total:", precio_total)

libro1 = 'Harry Potter'
libro2 = 'El principito'
disponible1 = verificar_disponibilidad(precios, libro1)
disponible2 = verificar_disponibilidad(precios, libro2)
print("Disponibilidad de", libro1 + ":", disponible1)
print("Disponibilidad de", libro2 + ":", disponible2)

libros_disponibles = ['Harry Potter', 'El señor de los anillos', 'Cien años de soledad']
mostrar_libros_disponibles(libros_disponibles)
