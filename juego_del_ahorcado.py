import random

# Obtenemos la palabra a adivinar 
def obtener_palabra_secreta():
    palabras = ["python", "java", "kotlin", "php", "javascript", "ruby", "verdura", "fruta", "swift"]
    return random.choice(palabras)

# Mostramos el progreso del juego palabra secreta 
def progreso_palabra_secreta(palabra_secreta, letras_intentada):
    letras_adivinadas = ''
    
    for letra in palabra_secreta:
        if letra in letras_intentada:
            letras_adivinadas += letra
        else:
            letras_adivinadas += '_'
    return letras_adivinadas

def juego_ahorcado():
    palabra_secreta = obtener_palabra_secreta()
    letras_intentadas = []
    intentos = 8
    juego_terminado = False
    
    print ("Bienvenido al juego del ahorcado")
    print(f"Tenes {intentos} intentos para adivinar la palabra secreta")
    print(progreso_palabra_secreta(palabra_secreta, letras_intentadas), "\n" , "La cantidad de letras de la palabra es: ", len(palabra_secreta))
    
    
    while not juego_terminado and intentos > 0:
        intento_letra = input("Ingrese una Letra por favor: ").lower()
        
        if len(intento_letra) != 1 or not intento_letra.isalpha():
            print("Por favor, ingresa una letra.")
            continue
        elif intento_letra in letras_intentadas:
            print("Esa letra ya esta adivinada. Intenta otra.")
            continue
        else:
            letras_intentadas.append(intento_letra)
            if intento_letra in palabra_secreta:
                print(f"La letra {intento_letra} esta en la palabra secreta.")
            else:
                intentos -= 1
                print(f"La letra {intento_letra} no esta en la palabra secreta. Te quedan {intentos} intentos.")
        
        progreso_actual = progreso_palabra_secreta(palabra_secreta, letras_intentadas)
        print(progreso_actual)
        
        if "_" not in progreso_actual:
            juego_terminado = True
            palabra_secreta.capitalize()
            print("¡Felicidades, Has Ganado! La palabra secreta era {palabra_secreta}.")        
    
    if intentos == 0:
        palabra_secreta.capitalize()
        print(f"¡Has perdido! La palabra secreta era {palabra_secreta}.")
        
        
juego_ahorcado()