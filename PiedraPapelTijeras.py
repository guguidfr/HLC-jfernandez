# José Daniel Fernández López
# 10/10/2022
import random
def user_input():
    print("Introduce un número del 1 al 3, siendo: \n1- Piedra\n2- Papel\n3- Tijeras")
    salir=False
    while salir == False:
        user_option=input("Eliges: ")
        if user_option !="1" and user_option !="2" and user_option !="3":
            print("El número que has introducido no es válido. Vuelve a intentarlo.")
        else:
            salir=True
    return user_option
def game():
    opciones = ("1", "2", "3")
    machine_option=random.choice(opciones)
    user_option = user_input()
    print(f"Tú has elegido: {user_option}; la máquina ha elegido: {machine_option}.")
    if machine_option == user_option:
        print("¡La máquina y tú habéis elegido lo mismo!¡Empate!")
    elif user_option == "1":
        if machine_option == "2":
            print("¡Papel gana a piedra!¡Pierdes!")
        else:
            print("¡Piedra gana a tijeras!¡Ganas!")
    elif user_option == "2":
        if machine_option == "1":
            print("¡Papel gana a piedra!¡Ganas!")
        else:
            print("¡Tijeras gana a papel!¡Pierdes!")
    elif user_option == "3":
        if machine_option == "1":
            print("¡Piedra gana a tijeras!¡Pierdes!")
        else:
            print("¡Tijeras gana a papel!¡Ganas!")

fin=False
while fin == False:
    game()
    option=input("Gracias por jugar. Introduce [n/N] para salir o cualquier tecla para volver a jugar: ")
    if option == "n" or option == "N":
        fin = True