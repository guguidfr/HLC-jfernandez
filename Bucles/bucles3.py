# José Daniel Fernández López
# 06/10/2022
nombre_apellidos=input("Introduce tu nombre y apellidos: ")
total_letras=0
for letra in nombre_apellidos:
    total_letras+=1
print(f"El total de letras introducido es: {total_letras} -- {len(nombre_apellidos)}")