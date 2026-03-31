# Escribe un programa que solicite al usuario una cantidad de segundos
# y muestre cuántas horas, minutos y segundos equivalen.
# Por ejemplo, 3661 segundos son 1 hora, 1 minuto y 1 segundo.

seconds = int(input('Ingrese una cantidad de segundos: '))

hours = seconds // 3600
rest = seconds % 3600
minutes = rest // 60
secs = rest % 60 

if (seconds == 1):
    word_seconds = "segundo"
else:
    word_seconds = "segundos"

if (hours == 1):
    word_h = "hora"
else:
    word_h = "horas"

if (minutes == 1):
    word_m = "minuto"
else:
    word_m = "minutos"

if (secs == 1):
    word_s = "segundo"
else:
    word_s = "segundos"
print(f'{seconds} {word_seconds} equivale a {hours} {word_h}, {minutes} {word_m} y {secs} {word_s}.')