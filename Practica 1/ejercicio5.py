# Escribe un programa que simule una caja registradora: el usuario
# ingresa precios de productos de a uno. Cuando ingresa 0, el programa
# se detiene y muestra el total acumulado.
# Nota: utilizá la sentencia break cuando haga falta.

sum = 0
while True:
    num = int(input('Ingrese los precios de los productos: '))

    if(num == 0):
        break
    else:
        sum += num

print(f'La suma de los precios de los productos es {sum}')