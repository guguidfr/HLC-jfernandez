# José Daniel Fernández López
# 13/10/2022
# Comparar tres números
valores=[]
for i in range(3):
        salir=False
        while salir==False:
            try:
                user_input=float(input("Introduce un número: "))
            except:
                print("El valor introducido debe ser un número.")
            else:
                #print(type(user_input))
                valores.append(user_input)
                salir=True

# Las líneas comentadas a continuación las he usado para comprobar el funcionamiento del código

#print(valores)
#print(type(valores))
orden=sorted(valores)
#print(orden)
#print(orden[2])
#print(orden[0])
if orden[0] == orden[1] == orden[2]:
    print("Los tres números son iguales.")
else:
    print(f"El mayor número de la lista es: {print(orden[2])}")
    print(f"El menos número de la lista es: {print(orden[0])}")
