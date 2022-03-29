'''

EJERCICIO: 

1) Pedir nombre al usuario
2) Crear un número aleatorio entre 1 y 100
3) 8 intentos para adivinarlo
4) Pedir números hasta agotar los 8 intentos

En cada intento, el programa debe responder 4 cosas distinas:

    - Menos de 1 o más de 100 -> Fuera de rango
    - Número menor al n° secreto
    - Número mayor al n° secreto
    - si el usuario acertó:
        - se le informa que ha ganado
        - cuántos intentos le ha tomado
        
'''

from random import *

random = randint(1, 101)

attempts = 0

number = int(input('Ingresa un número entre 1 y 100 (8 intentos): '))

while number > 100 or number < 1:
    number = int(input('Fuera de rango. Ingresa otro número: '))        
else:
    print('Número dentro de rango.')

while number != random:
    if number > random:
        print('Número mayor al N° secreto.')
    elif number < random:
        print('Número menor al N° secreto.')

    attempts = attempts + 1
    attempts_rev = 8 - attempts
    if attempts_rev == 0:
        print('Te has quedado sin intentos.')
        break
    number = int(input(f'No has acertado. Te quedan {attempts_rev} intentos: '))
else:
    print('Has acertado el número.')
    print(f'Lo lograste en {attempts} intentos.')




