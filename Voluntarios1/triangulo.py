# José Daniel Fernández López
# 13/10/2022
valid_input=False
# Salimos del while cambiando el valor de la variable booleana
while valid_input==False:
    user_input=(input("Introduce la altura del triángulo: "))
    if user_input.isdigit(): # Nos aseguramos de que el usuario solamente introduce dígitos
        user_input=int(user_input)
        if user_input<0: 
            print("El valor introducido no es válido. Prueba otra vez.")
        else:
            valid_input=True
    else:
        print("Debes de introducir un número entero.")

