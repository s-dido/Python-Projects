# Juego del Ahorcado

## Descripción

Este es un **juego del ahorcado** simple implementado en Python. El juego elige una palabra secreta al azar de una lista y el jugador debe adivinarla letra por letra. El jugador tiene un número limitado de intentos para acertar todas las letras de la palabra antes de que se quede sin intentos y pierda el juego.

## Características

- El jugador tiene 8 intentos para adivinar la palabra secreta.
- El juego muestra el progreso de las letras adivinadas y las letras que aún faltan por adivinar.
- El jugador puede ingresar letras y el juego verifica si la letra está en la palabra secreta.
- El juego termina cuando el jugador adivina la palabra completa o se queda sin intentos.

## Requisitos

Este proyecto está escrito en Python 3, por lo que necesitas tener Python 3 instalado en tu máquina para ejecutar el juego.

### Cómo ejecutar el juego:

1. Clona este repositorio a tu máquina local o descarga el archivo del script de Python.
2. Abre una terminal o línea de comandos.
3. Navega hasta el directorio donde guardaste el archivo.
4. Ejecuta el archivo Python con el siguiente comando:
   ```bash
   python juego_del_ahorcado.py

### Cómo Jugar:

- El juego te mostrará el número de letras de la palabra secreta, representadas como guiones bajos (_).
- Debes ingresar una letra por vez y el juego te indicará si la letra está o no en la palabra secreta.
- Cada vez que ingreses una letra incorrecta, perderás un intento.
- Si adivinas todas las letras antes de quedarte sin intentos, ¡ganas el juego! De lo contrario, si te quedas sin intentos, pierdes.
# Estructura del Código

El código está dividido en las siguientes funciones:

1. obtener_palabra_secreta(): Esta función selecciona una palabra al azar de una lista predefinida de palabras.
2. progreso_palabra_secreta(palabra_secreta, letras_intentadas): Esta función muestra el progreso del juego, mostrando las letras adivinadas correctamente y dejando guiones bajos donde aún falta adivinar.
3. juego_ahorcado(): Esta es la función principal que maneja la lógica del juego, solicitando las letras al jugador y controlando los intentos y el estado del juego.

# Mejoras Futuras
- Agregar la posibilidad de jugar con diferentes categorías de palabras.
- Añadir una interfaz gráfica de usuario (GUI) para hacer el juego más interactivo.
- Permitir que el jugador juegue varias rondas sin tener que reiniciar el juego.

# Licencia
Este proyecto está bajo la Licencia MIT 