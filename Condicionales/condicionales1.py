# José Daniel Fernández López
# 05/10/2022
# Comprobar resto
n1=int(input("Introduce el primer número: "))
n2=int(input("Introduce el segundo número: "))
print(f"El resultado de la división es: {n1//n2}" if n1%n2 == 0 else "Error: el resto de la división no es 0")