# José Daniel Fernández López
# 10/10/2022
# Adivinar el número
import random

def get_A(num):
    resultado=num//1000
    return resultado
def get_B(num, param):
    resultado=(num-param)//100
    return resultado
def get_C(num, param):
    resultado=(num-param)//10
    return resultado

def get_user_input():
        valid_input=False
        while valid_input==False:
            user_input=(input("Introduce tu intento: "))
            if user_input.isdigit():
                user_input=int(user_input)
                if user_input<1000 or user_input>9999:
                    print("El valor introducido no es válido. Prueba otra vez.")
                else:
                    valid_input=True
            else:
                print("Debes de introducir un número entero.")
        return user_input

numero=random.randint(1000,9999)

guessed=False
num_intentos=0
while guessed==False:
    got_A=False
    got_B=False
    got_C=False
    got_D=False

    user_try=get_user_input()
    num_intentos+=1
    A=get_A(numero)
    A2=get_A(user_try)
    a=A*1000
    a2=A2*1000
    if (A-A2)==0:
        print("\nEl primer dígito es correcto.")
        got_A=True
    elif (A-A2)<0:
        print(f"\nHas fallado en el primer dígito por: +/-{(A-A2)*(-1)}.")
    elif (A-A2)>0:
        print(f"\nHas fallado en el primer dígito por: +/-{(A-A2)}.")

    B=get_B(numero,a)
    B2=get_B(user_try, a2)
    b=a+B*100
    b2=a2+B2*100
    if (B-B2)==0:
        print("El segundo dígito es correcto.")
        got_B=True
    elif (B-B2)<0:
        print(f"Has fallado en el segundo dígito por: +/-{(B-B2)*(-1)}.")
    elif (B-B2)>0:
        print(f"Has fallado en el segundo dígito por: +/-{(B-B2)}.")
    
    C=get_C(numero,b)
    C2=get_C(user_try, b2)
    c=b+C*10
    c2=b2+C2*10
    if (C-C2)==0:
        print("El tercer dígito es correcto.")
        got_C=True
    elif (C-C2)<0:
        print(f"Has fallado en el tercer dígito por: +/-{(C-C2)*(-1)}.")
    elif (C-C2)>0:
        print(f"Has fallado en el tercer dígito por: +/-{(C-C2)}.")
    
    D=numero-c
    D2=user_try-c2
    if (D-D2)==0:
        print("El cuarto dígito es correcto.\n")
        got_D=True
    elif (D-D2)<0:
        print(f"Has fallado en el cuarto dígito por: +/-{(D-D2)*(-1)}.\n")
    elif (D-D2)>0:
        print(f"Has fallado en el cuarto dígito por: +/-{(D-D2)}.\n")
    
    if got_A==True and got_B==True and got_C==True and got_D==True:
        print(f"¡Has acertado! El número es: {numero}")
        print(f"Has necesitado: {num_intentos} intentos.")
        guessed=True