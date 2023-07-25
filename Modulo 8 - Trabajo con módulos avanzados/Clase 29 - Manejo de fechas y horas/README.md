# Clase 29: Manejo de fechas y horas

En el desarrollo de aplicaciones, el manejo de fechas y horas es una tarea común y esencial. Python cuenta con un módulo incorporado llamado `datetime` que proporciona clases y funciones para trabajar con fechas y horas de manera eficiente.

## Clase `datetime`

La clase `datetime` es una de las clases fundamentales del módulo `datetime`. Representa una combinación de fecha y hora en Python. Se utiliza para almacenar y operar con información de fechas y horas específicas.

```python
from datetime import datetime

# Crear una instancia de datetime con una fecha y hora específicas
fecha_hora = datetime(2023, 7, 25, 12, 30, 0)
print(fecha_hora)  # Salida: 2023-07-25 12:30:00

# Obtener la fecha y la hora por separado
fecha = fecha_hora.date()
hora = fecha_hora.time()

print(fecha)  # Salida: 2023-07-25
print(hora)   # Salida: 12:30:00
```

### Módulo `time`

El módulo `time` proporciona funciones para trabajar con horas, minutos, segundos y microsegundos independientes de fechas específicas. Es útil cuando solo necesitas trabajar con la hora del día.

```python
import time

# Obtener la hora actual en segundos desde la época (1 de enero de 1970)
segundos_desde_epoca = time.time()
print(segundos_desde_epoca)  # Salida: 1692142200.1364298

# Obtener la hora local actual como una estructura de tiempo
hora_actual = time.localtime(segundos_desde_epoca)
print(hora_actual)  # Salida: time.struct_time(tm_year=2023, tm_mon=7, tm_mday=15, tm_hour=16, tm_min=23, tm_sec=20, tm_wday=5, tm_yday=196, tm_isdst=0)

# Formatear la hora actual como una cadena legible
hora_formateada = time.strftime("%Y-%m-%d %H:%M:%S", hora_actual)
print(hora_formateada)  # Salida: 2023-07-15 16:23:20
```

## Ejemplos de uso

### Ejemplo 1: Cálculo de diferencia de fechas

Supongamos que queremos calcular la diferencia en días entre dos fechas específicas:

```python
from datetime import datetime

# Fechas de ejemplo
fecha1 = datetime(2023, 7, 25)
fecha2 = datetime(2023, 8, 15)

# Calcular la diferencia en días
diferencia = fecha2 - fecha1
print(diferencia.days)  # Salida: 21
```

### Ejemplo 2: Obtener el día de la semana

Si deseamos saber el día de la semana de una fecha en particular:

```python
from datetime import datetime

# Fecha de ejemplo
fecha = datetime(2023, 7, 25)

# Obtener el día de la semana (0 = Lunes, 1 = Martes, ..., 6 = Domingo)
dia_semana = fecha.weekday()
print(dia_semana)  # Salida: 0 (Lunes)
```

### Ejemplo 3: Uso del módulo `time` para medir el rendimiento de un programa

Supongamos que queremos medir el tiempo que tarda una función en ejecutarse:

```python
import time

def funcion_lenta():
    # Simulamos una función que tarda 3 segundos en ejecutarse
    time.sleep(3)

inicio = time.time()
funcion_lenta()
fin = time.time()

tiempo_transcurrido = fin - inicio
print(f"Tiempo transcurrido: {tiempo_transcurrido:.2f} segundos")
```

En este ejemplo, utilizamos `time.sleep(3)` para simular una función que tarda 3 segundos en ejecutarse. Al medir el tiempo entre el inicio y el final de la ejecución, podemos determinar cuánto tiempo tardó realmente la función en ejecutarse.

Con el uso del módulo `datetime` y `time`, podemos trabajar de manera eficiente con fechas y horas en Python y realizar tareas como cálculos de diferencia de fechas, obtención de días de la semana o medición de rendimiento de programas. Estas herramientas son fundamentales en el desarrollo de aplicaciones que requieran manipulación y análisis de datos temporales.
