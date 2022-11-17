# José Daniel Fernández López
# 02/11/2022

import random
import time

# Introducción al juego
print("Acabas de iniciar el juego del Ahorcado.")
nombre=(input("Introduce tu nombre: "))
time.sleep(1)
print(f"\n¡Buena suerte {nombre}!")
print("La partida va a empezar en breves...")
time.sleep(3)
print("\n")

# Función para preguntar al usuario si quiere volver a jugar
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
    # En la array están las fases del muñeco del ahorcado
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
     /|\\  |
          |
          |
    =========''', '''
      +---+
      |   |
      O   |
     /|\\  |
     /    |
          |
    =========''', '''
      +---+
      |   |
      O   |
     /|\\  |
     / \\  |
          |
    =========''']
    # Se declaran las variables necesarias para que funcione
    global salida # Es la variable en la que se guarda el progreso del usuario en la palabra a adivinar (es la misma que en la función 'main')
    global palabra_a_adivinar # (es la misma que en la función 'main')
    global word_size # Es el tamaño de la palabra elegida (es la misma que en la función 'main')
    global letras_usadas # Es una array con las letras que ha ido introduciendo el usuario (es la misma que en la función 'main')
    global palabra_sin_modificar # Una copia sin modificar de la palabra elegida (es la misma que en la función 'main')
    contador = 0 # Contador que se va a usar, junto con 'max_intentos', para imprimir el muñeco del ahorcado
    max_intentos = 7 # Número de intentos que tiene el usuario
    palabra_adivinada = False # Condición de victoria
    game_over = False # Condición de derrota
    intento_usuario = ""
    while palabra_adivinada == False and game_over == False: # Aquí empieza la partida de ahorcado, que termina cuando el jugador adivina la palabra, o se queda sin intentos
        letra_acertada = False # Condición que cambiará si el usuario introduce una letra que está en la palabra
        entrada_correcta = False # Cambiará si la entrada del usuario es válida
        while entrada_correcta == False:
            intento_usuario = input(f"Tu progreso con la palabra: {salida}\nLetras que has usado: {letras_usadas}\nIntroduce una letra: ")
            intento_usuario = intento_usuario.strip().lower() # Pasamos la letra a minúscula para que no haya problemas
            if len(intento_usuario) != 1:
                print("La entrada no es válida. Debes de introducir solamente un carácter. Prueba otra vez.\n")
            elif intento_usuario.isdigit():
                print("Solamente se admiten letras. Prueba otra vez.\n")
            elif intento_usuario in letras_usadas:
                print("Ya has usado esa letra. Prueba con otra.\n")
            else:
                entrada_correcta = True
        """
        Aquí está lo más importante del juego:
            Por cada carácter que tenga la palabra a adivinar, la comprobaremos con la letra que ha introducido el usuario.
            Si se encuentra una coincidencia:
                - Se añade a la lista de letras usadas.
                - Se cambia 'letra_acertada' a 'True'.
                - Se obtiene la posición de la coincidencia con la letra.
                - En esta posición obtenida, se cambia la letra por un guión bajo ("_") y lo demás se deja igual en 'palabra_a_adivinar'.
                - En 'salida' se hace lo mismo que en 'palabra_a_adivinar', pero cambiando el guión de la posición correspondiente por la letra acertada.
              
            Si no se ha encontrado una conicidencia:
                - Se suma 1 al contador.
                - Se resta un intento.
                - Se imprime el estado del muñeco.
                - Se le dice al usuario que la letra no es correcta y se le muestra el número de intentos restantes.
                * Si tras restar el número de intentos, el total es 0, se muestra el último estado, la palabra que había que adivinar, y se le pregunta al usuario si quiere jugar de nuevo tras establecer a 'True' la varibale 'game_over'.
            
            Al final de cada iteración, se comprueba si la 'palabra_a_adivinar' ya se ha transformado entera en guiones. Si este ese el caso, se cambia la variable 'palabra_adivinada' y se termina el juego para luego pregintar al usuario si quiere jugar de nuevo.
        """
        for caracter in palabra_a_adivinar:
            if intento_usuario == caracter:
                if intento_usuario not in letras_usadas:
                    letras_usadas.extend(intento_usuario)
                letra_acertada = True
                posicion = palabra_a_adivinar.find(intento_usuario) # Aquí se obtiene la posición de la primera conicidencia de la letra
                palabra_a_adivinar = palabra_a_adivinar[:posicion] + "_" + palabra_a_adivinar[posicion+1:] # Aquí se cambia por el guión en la 'palabra_a_adivinar'
                salida = salida[:posicion] + intento_usuario + salida[posicion+1:] # Aquí se cambia por la letra en 'salida'
            else:
                if intento_usuario not in letras_usadas: # Si no se ha acertado la letra, no hacemos nignún cambio y añadimos la letra a la lista de las ya usadas.
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
    word_size = len(palabra_a_adivinar) # Se define el tamaño de la palabra
    letras_usadas = []
    salida = "_" * word_size  # Se crea la variable que se le muestra al usuario como progreso
    partida()
    play_again()

main()