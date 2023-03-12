# José Daniel Fernández López
# 10/10/2022
# Adivinar el número
import random
def entrada_usuario():
    lista_usuario=[]
    salir=False
    contador=0
    while salir==False:
        try:
            numero_usuario=int(input("Introduce un numero del 0 al 9: "))
        except:
            print("Solamente se admiten números enteros del 0 al 9.")
        else:
            if numero_usuario<0 or numero_usuario>9:
                print("El número no puede ser negativo, o 0 o mayor que 9.")
            else:
                if contador==0:
                    if numero_usuario==0:
                        print("El primer dígito no puede ser 0.")
                    else:
                        lista_usuario.append(numero_usuario)
                        contador+=1
                        #contador=contador+1
                else:
                    lista_usuario.append(numero_usuario)
                    contador+=1
                    #contador=contador+1
                    if contador==4:
                        salir=True
    return lista_usuario
        
'''
def entrada_usuario():
    lista_usuario=[]
    salir=False
    contador=0
    while salir==False:
        numero_usuario=int(input("Introduce un numero del 0 al 9: "))
        if numero_usuario<0 or numero_usuario>9:
            print("El número no puede ser negativo, o 0 o mayor que 10.")
        else:
            if contador==0:
                if numero_usuario==0:
                    print("El primer dígito no puede ser 0.")
                else:
                    lista_usuario.append(numero_usuario)
                    contador+=1
                    #contador=contador+1
            else:
                lista_usuario.append(numero_usuario)
                contador+=1
                #contador=contador+1
                if contador==4:
                    salir=True
    return lista_usuario
'''
def numeros_maquina():
    numeros_maquina=[]
    for i in range(4):
        if i==0:
            numero=random.randint(1,9)
            numeros_maquina.append(numero)
        else:
            numero=random.randint(0,9)
            numeros_maquina.append(numero)
    return numeros_maquina

def comprobar_digito(digito_usuario,digito_maquina,posicion):
    if digito_usuario-digito_maquina==0:
        print(f"El dígito de la posición {posicion+1} es correcto.")
        return True
    else:
        print(f"El dígito de la posición {posicion+1} es incorrecto.")
        return False


numero_de_la_maquina=numeros_maquina()
acertado=False
numero_intentos=0
while acertado==False:
    correcto_primero=False
    correcto_segundo=False
    correcto_tercero=False
    correcto_cuarto=False

    numero_del_usuario=entrada_usuario()
    print(f"El número que has introducido es: {numero_del_usuario[0]}{numero_del_usuario[1]}{numero_del_usuario[2]}{numero_del_usuario[3]}")
    numero_intentos+=1
    print(f"El número del usuario en formato lista es: {numero_del_usuario}")
    #print(f"E número de la máquina en formato lista es: {numero_de_la_maquina}")
    for i in range(4):
        if comprobar_digito(numero_del_usuario[i],numero_de_la_maquina[i],i)==True:
            if i==0:
                correcto_primero=True
            elif i==1:
                correcto_segundo=True
            elif i==2:
                correcto_tercero=True
            elif i==3:
                correcto_cuarto=True
    
    if correcto_primero==True and correcto_segundo==True and correcto_tercero==True and correcto_cuarto==True:
        print("¡Has acertado!")
        print(f"Has necesitado {numero_intentos} intentos.\n")
        acertado=True