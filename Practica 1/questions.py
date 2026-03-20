import random
dic = {
    'Informatica': ['python', 'programa', 'variable', 'funcion', 'bucle', 'cadena', 'entero', 'lista'],
    'Paises': ['argentina', 'bolivia', 'surinam', 'belice', 'china', 'francia'],
    'Colores': ['rojo', 'verde', 'violeta', 'amarillo', 'rosa', 'celeste'],
    'Marcas': ['sony', 'guillete', 'chevrolet', 'logitech'],
}
category_names = [
                'Informatica',
                'Paises',
                'Colores',
                'Marcas'
                ]
guessed = []
attempts = 6
total_points = 0
print("¡Bienvenido al Ahorcado!")
print('*' * 35)
print("""      CATEGORÍAS
    1. Informatica
    2. Paises
    3. Colores
    4. Marcas""")
print('*' * 35)
while True:
    try:
        category = int(input("Por favor, elija el número de la categoría que desea utilizar: "))
        if (1 <= category <= len(category_names)):
            category_choosed = category_names[category-1]
            print(f'Elegiste la categoría {category_choosed}')
            word = random.choice(dic[category_choosed])
            break
        else:
            print('ERROR: número no valido.')
    except ValueError:
        print('ERROR: no ingresaste un número. ')
while attempts > 0:
    # Mostrar progreso: letras adivinadas y guiones para las que faltan
    progress = ""
    for letter in word:
        if letter in guessed:
            progress += letter + " "
        else:
            progress += "_ "
    print(progress)
    # Verificar si el jugador ya adivinó la palabra completa
    if "_" not in progress:
        total_points += 6
        print("¡Ganaste!")
        break
    print(f"Intentos restantes: {attempts}")
    print(f"Letras usadas: {', '.join(guessed)}")
    letter = input("Ingresá una letra: ").lower()
    if not ((letter.isalpha() and not letter in 'áéíóú') and (len(letter) == 1)):
        print('Entrada no válida.')
        continue
    elif letter in guessed:
        print("Ya usaste esa letra.")
    elif letter in word:
        guessed.append(letter)
        print("¡Bien! Esa letra está en la palabra.")
    else:
        guessed.append(letter)
        attempts -= 1
        total_points -= 1
        print("Esa letra no está en la palabra.")
    print()
else:
    total_points = 0
    print(f"¡Perdiste! La palabra era: {word}")

dic = {
    'Informatica': ['python', 'programa', 'variable', 'funcion', 'bucle', 'cadena', 'entero', 'lista'],
    'Paises': ['argentina', 'bolivia', 'surinam', 'belice', 'china', 'francia'],
    'Colores': ['rojo', 'verde', 'violeta', 'amarillo', 'rosa', 'celeste'],
    'Marcas': ['sony', 'guillete', 'chevrolet', 'logitech'],
}

category_names = ['Informatica', 'Paises', 'Colores', 'Marcas']
category_played = []
total_points = 0

print("¡Bienvenido al Ahorcado!")

while True:
    try:

        print('*' * 35)
        print("""      CATEGORÍAS
    1. Informatica
    2. Paises
    3. Colores
    4. Marcas
    0. Salir""")
        print('*' * 35)
        category = int(input("Por favor, elija el número de la categoría que desea utilizar: "))
        
        if (category == 0):
            break
        elif (1 <= category <= len(category_names)):
            category_choosed = category_names[category-1]

            if (category_choosed in category_played):
                print('Ya elegiste esta categoria.')
                continue

            print(f'Elegiste la categoría {category_choosed}')
            list_choosed = dic[category_choosed].copy()
            category_played.append(category_choosed)

            while (len(list_choosed) > 0):

                guessed = []
                attempts = 6

                word = random.sample(list_choosed, 1)[0]        # random.sample() devuelve una lista de 1 elem.
                list_choosed.remove(word)       

                while attempts > 0:
                    # Mostrar progreso: letras adivinadas y guiones para las que faltan
                    progress = ""
                    for letter in word:
                        if letter in guessed:
                            progress += letter + " "
                        else:
                            progress += "_ "
                    print(progress)
                    # Verificar si el jugador ya adivinó la palabra completa

                    if "_" not in progress:
                        total_points += 6
                        print("¡Ganaste!")
                        break

                    print(f"Intentos restantes: {attempts}")
                    print(f"Letras usadas: {', '.join(guessed)}")
                    letter = input("Ingresá una letra: ").lower()

                    if not ((letter.isalpha() and not letter in 'áéíóú') and (len(letter) == 1)):
                        print('Entrada no válida.')
                        continue
                    elif letter in guessed:
                        print("Ya usaste esa letra.")
                    elif letter in word:
                        guessed.append(letter)
                        print("¡Bien! Esa letra está en la palabra.")
                    else:
                        guessed.append(letter)
                        attempts -= 1
                        total_points -= 1
                        print("Esa letra no está en la palabra.")
                    print()
                else:
                    total_points = 0
                    print(f"¡Perdiste! La palabra era: {word}")

                print(f'Puntos conseguidos totales: {total_points}')
            else:
                print('No hay mas palabras para elegir')
        else:
            print('ERROR: número no valido.')
    except ValueError:
        print('ERROR: no ingresaste un número. ')
