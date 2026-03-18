# Escribe un programa que solicite al usuario una cantidad de segundos
# y muestre cuántas horas, minutos y segundos equivalen.
# Por ejemplo, 3661 segundos son 1 hora, 1 minuto y 1 segundo.

seconds = int(input('Ingrese una cantidad de segundos: '))

hours = seconds // 3600
rest = seconds % 3600
minutes = rest // 60
secs = rest % 60 

print(f'{seconds} segundos equivale a {hours} horas, {minutes} minutos y {secs} segundos')