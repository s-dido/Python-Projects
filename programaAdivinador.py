print(" Bienvenido al programa de adivinador de números 👋😃")
print("1- Selecciona un rango de numeros 😊")

while True:
    try:
        limite_inferior = int(input("¿Cuál es el límite inferior? : "))
        limite_superior = int(input("¿Cuál es el límite superior? : "))

        if limite_inferior >= limite_superior:
            print(
                "⚠️ El límite inferior debe ser menor que el límite superior. Inténtalo de nuevo."
            )
        else:
            break
    except ValueError:
        print("⚠️ Ingresa solo números enteros.")

print("\n2- Ahora piensa en un número y mantenlo en secreto 🔒")


adivinado = False
intentos = 0

while not adivinado and limite_inferior <= limite_superior:

    numero = (limite_inferior + limite_superior) // 2
    intentos += 1
    print(f"\n🤔 ¿Es el {numero}?")

    print(
        "📌 Si es mayor, escribe 'mayor'. Si es menor, escribe 'menor'. Si lo adiviné, escribe 'si': "
    )

    respuesta = input("Respuesta: ").lower()

    if respuesta == "si":
        adivinado = True
        print(f"\n🎉Lo adivine! El numero es {numero} en {intentos} intentos.")

    elif respuesta == "mayor":
        limite_inferior = numero + 1

    elif respuesta == "menor":
        limite_superior = numero - 1

    else:
        print(
            " ⚠️ Respuesta no reconocida. Por favor, responde con 'mayor', 'menor' o 'si'."
        )


if limite_inferior > limite_superior:
    print(" \n❌ Parece que hubo un error. ¿Seguro que respondiste correctamente?")
