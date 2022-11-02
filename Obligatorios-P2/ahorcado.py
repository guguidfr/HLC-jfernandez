# José Daniel Fernández López
# 02/11/2022

import random
import time

print("Acabas de iniciar el juego del Ahorcado.")
nombre=(input("Introduce tu nombre: "))
time.sleep(1)
print(f"\n¡Buena suerte {nombre}!")
print("La partida va a empezar en breves...")
time.sleep(3)
print("\n")

def play_again():
    salir = False
    while salir == False:
        respuesta = input("¿Quieres jugar otra vez?[Y/N]: ")
        if respuesta == "y" or respuesta == "Y":
            salir = True
            time.sleep(2)
            main()
        elif respuesta == "n" or respuesta == "N":
            print(f"¡Gracias por jugar, {nombre}!")
            time.sleep(1)
            salir = True
        else:
            print("Lo que has introducido no es válido. Prueba otra vez.\n")

def partida():
    estado_ahorcado = ['''
      +---+
      |   |
          |
          |
          |
          |
    =========''', '''
      +---+
      |   |
      O   |
          |
          |
          |
    =========''', '''
      +---+
      |   |
      O   |
      |   |
          |
          |
    =========''', '''
      +---+
      |   |
      O   |
     /|   |
          |
          |
    =========''', '''
      +---+
      |   |
      O   |
     /|\  |
          |
          |
    =========''', '''
      +---+
      |   |
      O   |
     /|\  |
     /    |
          |
    =========''', '''
      +---+
      |   |
      O   |
     /|\  |
     / \  |
          |
    =========''']
    global salida
    global palabra_a_adivinar
    global word_size
    global letras_usadas
    global palabra_sin_modificar
    contador = 0
    max_intentos = 7
    palabra_adivinada = False
    game_over = False
    while palabra_adivinada == False and game_over == False:
        letra_acertada = False
        entrada_correcta = False
        while entrada_correcta == False:
            intento_usuario = input(f"Tu progreso con la palabra: {salida}\nLetras que has usado: {letras_usadas}\nIntroduce una letra: ")
            intento_usuario = intento_usuario.strip().lower()
            if len(intento_usuario) != 1:
                print("La entrada no es válida. Debes de introducir solamente un carácter. Prueba otra vez.\n")
            elif intento_usuario.isdigit():
                print("Solamente se admiten letras. Prueba otra vez.\n")
            elif intento_usuario in letras_usadas:
                print("Ya has usado esa letra. Prueba con otra.\n")
            else:
                entrada_correcta = True
        
        for caracter in palabra_a_adivinar:
            if intento_usuario == caracter:
                if intento_usuario not in letras_usadas:
                    letras_usadas.extend(intento_usuario)
                letra_acertada = True
                posicion = palabra_a_adivinar.find(intento_usuario)
                palabra_a_adivinar = palabra_a_adivinar[:posicion] + "_" + palabra_a_adivinar[posicion+1:]
                salida = salida[:posicion] + intento_usuario + salida[posicion+1:]      
            else:
                if intento_usuario not in letras_usadas:
                    letras_usadas.extend(intento_usuario)
        
        if letra_acertada == False:
            max_intentos-=1
            contador+=1
            if max_intentos == 0:
                print(estado_ahorcado[6])
                print(f"¡Has perdido, {nombre}!\nLa palabra era \"{palabra_sin_modificar}\".\nMejor suerte la próxima vez.")
                game_over = True
            else:
                print("Esa letra no está en la palabra.")
                print(estado_ahorcado[contador-1])
                print(f"Intentos restantes: {max_intentos}\n")
        else:
            print(f"¡Letra correcta!\n")
        
        if palabra_a_adivinar == "_" * word_size:
            print(f"¡Felicidades {nombre}!¡Has acertado la palabra: \"{palabra_sin_modificar}\"!")
            palabra_adivinada = True

def main():
    global salida
    global palabra_a_adivinar
    global word_size
    global letras_usadas
    global palabra_sin_modificar
    palabras_disponibles = ("punta","recital","gallo","lavadora","comer","maduro","cosechar","biplano","cosecha","luminoso","curva","retirar","principio","digital","planetas","broma","caracol","patata")
    palabra_a_adivinar = random.choice(palabras_disponibles)
    palabra_sin_modificar = palabra_a_adivinar
    word_size = len(palabra_a_adivinar)
    letras_usadas = []
    salida = "_" * word_size
    partida()
    play_again()

main()