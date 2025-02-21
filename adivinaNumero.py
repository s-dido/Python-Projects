import random


def adivinaNumero():
    # Generar un numero aleatorio entre 1 y 100
    numero_secreto = random.randint(1, 20)
    intentos = 0
    adivinado = False

    print("¡Bienvenido al juego de adivina el número!")
    print("Debes adivinar un numero entre el 1 y el 20")
    print("Es tu turno, Intentalo!")
    while not adivinado:
        intentos += 1
        numero_ingresado = input("Ingresa tu numero: ")

        if numero_ingresado.isdigit():
            numero_ingresado = int(numero_ingresado)
            if numero_ingresado == numero_secreto:
                adivinado = True
                print(f"¡Felicidades! Adivinaste el número en {intentos} intentos.")
                print(f"El Numero Secreto es: {numero_secreto}")
            elif numero_ingresado < numero_secreto:
                print("El numero secreto es mayor!")
            elif numero_ingresado > numero_secreto:
                print("El Numero Secreto es menor!")


adivinaNumero()
