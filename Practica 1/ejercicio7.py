# Escribe un programa que solicite al usuario una lista de palabras.
# Luego, construí una oración uniendo únicamente las palabras que 
# tengan más de 3 letras, separadas por espacios. Las palabras cortas
# deben ser excluidas del resultado final.

word_list = []

while True:
    word = input("Escribe palabras (escribe 'FIN' para finalizar): ")

    if (word == 'FIN'):
        break
    elif (len(word) > 3):
        word_list.append(word)
print(" ".join(word_list))