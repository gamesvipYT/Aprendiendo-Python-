# Este mini juego es un clásico: el programa genera un número aleatorio y el usuario tiene que adivinarlo. El programa le dará pistas al usuario indicando si su suposición es demasiado alta, demasiado baja o correcta.

import random

# Generar un número aleatorio entre 1 y 100
numero_secreto = random.randint(1, 100)
intentos = 0

# El juego comienza aquí
print("Adivina el numero secreto entre el 1 y el 100.")

# El bucle continuará hasta que el usuario adivine el número
while True:
    intento = int(input("Tu numero: "))
    intentos += 1

    if intento < numero_secreto:
        print("Mas alto")
    elif intento > numero_secreto:
        print("Mas bajo")
    else:
        print(f"Felicidades! Has adivinado el numero en {intentos} intentos.")
        break
