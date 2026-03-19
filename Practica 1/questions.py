import random
words = [
    "python",
    "programa",
    "variable",
    "funcion",
    "bucle",
    "cadena",
    "entero",
    "lista",
]
word = random.choice(words)
guessed = []
attempts = 6
total_points = 0
print("¡Bienvenido al Ahorcado!")
print()
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

print(f'Puntos totales en la partida: {total_points}')