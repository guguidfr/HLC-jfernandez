# José Daniel Fernández López
# 10/10/2022
# Adivinar el número
import random

# Definir las funciones para obtener cada uno de los dígitos, teniendo en cuenta que
# son solamente números de 4 dítigos, y que nos vamos a referir a ellos de la forma: ABCD

# Haciendo divisiones y truncando los resultados, podemos obtener las unidades de millar, centenas y decenas
# con facilidad.
# lpaneque: Quizás los nombres de estas funciones no son los más adecuados.
def get_A(num):
    resultado=num//1000
    return resultado
def get_B(num, param):
    resultado=(num-param)//100
    return resultado
def get_C(num, param):
    resultado=(num-param)//10
    return resultado

# En esta función nos encargamos de que el usuario introduzca un número válido, ya que
# si introduce una cadena de texto o un número con más o menos de 4 cifras, no funcionará
def get_user_input():
        valid_input=False
        # Salimos del while cambiando el valor de la variable booleana
        while valid_input==False:
            user_input=(input("Introduce tu intento (número entero): "))
            if user_input.isdigit(): # Nos aseguramos de que el usuario solamente introduce dígitos
                user_input=int(user_input)
                if user_input<1000 or user_input>9999: # Comprobamos que el número que ha introducido el usuario tiene 4 cifras
                    print("El valor introducido no es válido. Prueba otra vez.")
                else:
                    valid_input=True
            else:
                print("Debes de introducir un número entero.")
        return user_input

# Generamos el número a adivinar
numero=random.randint(1000,9999)

guessed=False
num_intentos=0
# Seguiremos pidiendo números al usuario hasta que adivine todos los dígitos a la vez
while guessed==False: # lpaneque: Mejor while not guessed
    got_A=False
    got_B=False
    got_C=False
    got_D=False

    user_try=get_user_input()
    num_intentos+=1 # Contamos los intentos del jugador
    # Tenemos que separar los dígitos tanto del número a adivinar como del que ha introducido el usuario
    A=get_A(numero)
    A2=get_A(user_try)
    # Las 'a' las necesitaremos para calcular 'B', y haremos algo parecido obteniendo 'b' para obtener 'C'
    a=A*1000
    a2=A2*1000
    # Calculamos la diferencia entre el dígito del número y el intento del usuario
    if (A-A2)==0:
        print("\nEl primer dígito es correcto.")
        got_A=True
    elif (A-A2)<0:
        # Si el resultado de la diferencia es negativo, lo multiplicamos por (-1) para mostrarlo como uno positivo
        print(f"\nHas fallado en el primer dígito por: +/-{(A-A2)*(-1)}.")
    elif (A-A2)>0:
        print(f"\nHas fallado en el primer dígito por: +/-{(A-A2)}.")

    # Para 'B' y 'C', necesitaremos pasar un parámetro
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
   
    # lpaneque: No sería más sencillo extraer cada dígito de la cifra y compararlo? También podrías convertirlo a integer para ver la diferencia entre ambos.
    # Tu solución es perfectamente válida, pero puede resultar algo compleja de entender y lleva algo de repetición de código, ya que todos estos bloques son iguales, quitando el peso del dígito, decenas, centenas, etc.
    # Lo podrías meter en un bucle.
    # Según la filosofía ZEN de python: "Simple is better than complex."
  
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
    
    # Siendo 'c' la suma de 'A', 'B' y 'C', podemos obtener el último dígito fácilmente
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
        # Si el usuario ha introducido el número correcto, termina el juego y muestra el número de intentos.
        print(f"¡Has acertado! El número es: {numero}")
        print(f"Has necesitado: {num_intentos} intentos.")
        guessed=True
        
 # lpaneque
