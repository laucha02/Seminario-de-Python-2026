# Seminario de Python 2026

## Temario

**Entregable 1**

- [Funcionalidad 1](#funcionalidad-1)
- [Funcionalidad 2](#funcionalidad-2)
- [Funcionalidad 3](#funcionalidad-3)
- [Funcionalidad 4](#funcionalidad-4)

## Entregable Práctica 1

### Funcionalidad 1

#### Consigna

El juego tiene un bug. Si el usuario ingresa más de una letra, un número o
cualquier otro carácter inválido, el programa se comporta de manera inesperada. Modificalo para que en ese caso muestre el mensaje "Entrada no válida" y continúe el juego en la siguiente iteración.

####  Resultado

El resultado se encuentra en el commit [f445ab8](https://github.com/laucha02/Seminario-de-Python-2026/commit/f445ab8) "Agrego funcionalidad 1.".

Primero, modifiqué la linea 32 para que todas las letras ingresadas sean convertidas a minúsculas.
Luego, desde la linea 33 hasta la linea 35, creé una condición de que el carácter ingresado sea un carácter alfabético (y que no tenga acento, ya que estos tambien se encuentra dentro de los caracteres mencionados) y que ese string solo tenga un elemento. Si esta condición es falsa, entonces que vaya a la siguiente iteración y pregunta de vuelta por una letra.

### Funcionalidad 2
#### Consigna

Modificá el juego para que al final de la partida se muestre el puntaje del jugador. El puntaje se calcula de la siguiente forma: cada letra incorrecta resta 1 punto, adivinar la palabra completa suma 6 puntos, y perder deja el puntaje en 0.

#### Resultado

El resultado se encuentra en el commit [63b9571](https://github.com/laucha02/Seminario-de-Python-2026/commit/63b9571) "Agrego funcionalidad 2".

Creé la variable ```total_points``` de tipo int (linea 15) para que cuando es una letra incorrecta reste un punto (linea 46), cuando gane el ahorcado sume 6 puntos (linea 29), cuando pierda, el resultado de los puntos es 0 (linea 50) y al final de la partida, se visualice los puntos obtenidos (linea 53)

### Funcionalidad 3
#### Consigna

Modificá el juego para que las palabras estén agrupadas por categoría. Al inicio de cada partida, mostrar las categorías disponibles y permitir que el usuario elija una. Ayuda: utilizá un diccionario donde las claves sean los nombres de las categorías y los valores sean listas de palabras.

#### Resultado

El resultado se encuentra en el commit [cf00ae0](https://github.com/laucha02/Seminario-de-Python-2026/commit/cf00ae0) "Agrego funcionalidad 3".

Creé un diccionario ```dic``` desde la linea 2 hasta la linea 7, reemplazando a la lista ```words```, donde la clave es un string que es la categoría a elegir, y los valores son la lista de strings que son las palabras relacionadas a esa categoría.

Creé una lista de strings ```category_played``` que son las categorías a elegir, desde la linea 8 hasta la 13.

Ahora en la consola se visualizará un menú donde el usuario debe elegir el número de categoría (desde la linea 18 hasta la linea 24). Para controlar que efectivamente se haya ingresado un número correcto, se crea un ```while``` (linea 25) con bucle infinito. Dentro, con ```try``` y ```except```, se regula si el usuario ingresó un numero o si tira error ValueError, ya que la variable ```category``` convierte el string a un int, y ese error aparece cuando se quiere convertir un caracter que no es un número. Para salir del bucle infinito, se debe ingresar un numero que esté en el rango de 1 a 4, que sale de la cantidad de elementos en la lista ```category_names```. Cuando ingresa, para que linea 31 no sea muy extensa, lo dividí primero creando ```category_choosed``` que es un string y se calcula a partir del valor que está en la lista ```category_played``` en la posición ```category```, y como va de 0 a N, se debe restar 1. Ya obtenida la clave del diccionario, en la linea 31, se modifica la variable ```word``` para que busque correctamente en ella.

### Funcionalidad 4
#### Consigna

Modificá el juego para que, al jugar varias rondas seguidas, no se repita la misma palabra. Investigá la función random.sample() .

#### Resultado

El resultado se encuentra en el commit [1637856](https://github.com/laucha02/Seminario-de-Python-2026/commit/1637856) "Agrego funcionalidad 4 (final)".

Tuve problemas con el merge de questions.py debido a que hice esta práctica en dos compus distintas, y no hice ```git pull``` para traerme la ultima version del repositorio remoto, lo actualicé pasandome el archivo en un pendrive.

Añadí nuevas variables: una lista ```category_played``` (linea 11) que en principio viene vacía, y agrega las categorías que se jugaron y una lista ```list_choosed``` (linea 39) que se actualiza cada vez que se elige una nueva categoría, y toma una copia por valor de la lista del diccionario con valor de la categoría elegida.
Modifiqué la estructura. Como ahora se puede jugar varias rondas, el ```while attempts > 0``` ahora es ```while (len(list_choosed) > 0)```, es decir, mientras haya elementos dentro de ```list_choosed``` que siga jugando (caso contrario, que eliga otra categoría), y ahora se encuentra dentro del bucle infinito.

Modifiqué el menú con una nueva opción (0. Salir), y ahora se encuentra dentro del bucle infinito, que solo sale si escribe 0.

Añadí una condición (linea 34) luego de elegir la categoría para saber si ya se eligió anteriormente. Si se había elegido, entonces que vaya al menú y eliga de vuelta. Si no se había elegido, entonces se agrega esa categoría en ```category_choosed```. 

Se mueve las variables ```guessed``` y ```attempts``` (linea 44 y 45) ya que se van a modificar cuando empieza una ronda nueva.

Se modifica la variable ```word``` (linea 47)para que funcione correctamente con random.sample(poblacion es la lista que eligió el usuario, y k sería 1, porque solo quiero que me traiga un elemento) y como devuelve una lista de un único elemento, me posiciono en la primera posición que contiene la palabra elegida. Luego se elimina ese elemento (linea 48) de ```list_choosed```

