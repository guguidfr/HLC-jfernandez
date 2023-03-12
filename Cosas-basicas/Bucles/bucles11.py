# José Daniel Fernández López
# 06/10/2022
total=int(input("¿Cuántos números vas a introducir? "))
suma=0
for i in range(total):
    n=float(input(f"Introduce el número {i+1}: "))
    suma+=n
print(f"La suma total de los números introducidos es: {suma}")