# Crea un programa que solicite al usuario un número y muestre
# su tabla de multiplicar del 1 al 10 utilizando un bucle for.

number = int(input('Ingrese un numero: '))
for i in range(1, 11):    # Del 1 al 10 (N-1)
    print(f'{i} x {number} = {i*number}')