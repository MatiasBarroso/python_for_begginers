# Ejemplo de lectura y escritura de archivos

# Creamos un archivo de texto para escribir en él
with open('ejemplo.txt', 'w') as archivo:
    archivo.write('Hola, mundo!\n')
    archivo.write('Este es un ejemplo de escritura en un archivo.')

# Abrimos el archivo en modo de lectura y leemos su contenido
with open('ejemplo.txt', 'r') as archivo:
    contenido = archivo.read()

# Imprimimos el contenido del archivo
print(contenido)

# Resultado esperado:
# Hola, mundo!
# Este es un ejemplo de escritura en un archivo.
