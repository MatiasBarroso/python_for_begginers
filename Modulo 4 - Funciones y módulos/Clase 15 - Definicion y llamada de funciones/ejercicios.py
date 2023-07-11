
# Ejercicio 1: Cálculo del promedio de calificaciones
# Completa la función 'calcular_promedio' para que reciba una lista de calificaciones como parámetro y devuelva el promedio de las mismas.
def calcular_promedio(calificaciones):
    # Completa el código
    total = sum(calificaciones)
    promedio = total / len(calificaciones)
    return round(promedio, 2)

# Ejercicio 2: Generación de nombres de usuario
# Completa la función 'generar_usuario' para que reciba el nombre y apellido de una persona como parámetros y devuelva un nombre de usuario en formato 'nombre.apellido'.
def generar_usuario(nombre, apellido):
    # Completa el código
    usuario = nombre.lower() + "." + apellido.lower()
    return usuario

# Ejercicio 3: Análisis de tweets
# Completa la función 'analizar_tweets' para que reciba una lista de tweets como parámetro y devuelva el porcentaje de tweets que contienen una palabra clave específica.
def analizar_tweets(tweets, palabra_clave):
    # Completa el código
    total_tweets = len(tweets)
    tweets_con_palabra_clave = sum(palabra_clave in tweet.lower() for tweet in tweets)
    porcentaje = (tweets_con_palabra_clave / total_tweets) * 100
    return round(porcentaje, 2)

# Ejercicio 4: Conversión de unidades de temperatura
# Completa la función 'convertir_temperatura' para que reciba una temperatura en grados Celsius y la convierta a grados Fahrenheit.
def convertir_temperatura(celsius):
    # Completa el código
    fahrenheit = (celsius * 9/5) + 32
    return round(fahrenheit, 2)