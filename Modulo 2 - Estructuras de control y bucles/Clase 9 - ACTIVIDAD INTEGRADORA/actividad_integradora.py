# Definir las funciones de operaciones matemáticas

# Función para suma
def suma(a, b):
    # Completar el codigo
    
# Función para resta
def resta(a, b):
    # Completar el codigo
    
# Función para multiplicación
def multiplicacion(a, b):
    # Completar el codigo
    
# Función para división
def division(a, b):
    # Completar el codigo

# Función principal para la calculadora
def calculadora():
    
    # Variable para controlar si se desea continuar o salir del programa
    continuar = True

    while continuar:
        # Mostrar el menú de opciones
        print("Calculadora")
        print("1. Suma")
        print("")
        print("")
        print("")
        print("")

        # Solicitar al usuario que elija una opción
        opcion = input("Elige una opción: ")

        if opcion == "1":
            # Opción de suma
            # Ejemplo:
            num1 = float(input("Ingresa el primer número: "))
            num2 = float(input("Ingresa el segundo número: "))
            resultado = suma(num1, num2)
            print("El resultado de la suma es:", resultado)

        elif opcion == "2":
            # Opción de resta

        elif opcion == "3":
            # Opción de multiplicación

        elif opcion == "4":
            # Opción de división

        elif opcion == "5":
            # Opción de salir

        else:
            print("Opción inválida. Por favor, elige una opción válida.")

        if continuar:
            # Preguntar si desea realizar otra operación
            respuesta = input("¿Deseas realizar otra operación? (s/n): ")
            # Si la respuesta es "S", la pasamos a minuscula con la funcion .lower() y hacemos la verificacion correspondiente
            if respuesta.lower() != "s":
                print("¡Hasta luego!")
                continuar = False

# Llamar a la función principal de la calculadora
calculadora()
