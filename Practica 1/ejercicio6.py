# Modifica el ejercicio 4 para que, en lugar de imprimir los números,
# genere dos listas: una con los múltiplos de 5 y otra con el resto
# de los números. Imprimí ambas listas al finalizar.

list_multiples = []
list_rest = []

num = int(input('Ingrese un numero: '))
for i in range(1,num+1):
    if (i%5 == 0):
        list_multiples.append(i)
    else:
        list_rest.append(i)
if (len(list_multiples) > 0):
    print(f'Lista de multiplos de 5: {list_multiples}')
else:
    print('La lista de multiplos no tiene elementos.')

print(f'Lista del resto: {list_rest}')
