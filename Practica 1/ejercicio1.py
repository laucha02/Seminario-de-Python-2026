# Escribe un programa que solicite al usuario su año de nacimiento
# y muestre en qué año cumplirá 18, 21 y 100 años.

YEAR = 2026
OBJ_AGE = [18, 21, 100]
user_birth = int(input('Ingrese su fecha de nacimiento: '))
user_age = YEAR - user_birth

for edad in OBJ_AGE:
    if (user_age > edad):
        print(f'Ya cumpliste {edad} en {YEAR - (user_age - edad)}')
    else:
        print(f'Cumpliras {edad} en {(edad - user_age) + YEAR}')