# José Daniel Fernández López
# 05/10/2022
# Ordenar los números de la primitiva
primitiva=list(map(int,input("Números: ").strip().split())) # Transforma en enteros los caracteres introducidos por el usuario y guárdalos como una lista usando map()
primitiva.sort()
print(f"Los números de la primitiva ordenados de menor a mayor son: ", end="")
print(primitiva)
primitiva.reverse()
print(f"Los números de la primitiva ordenados de mayor a menor son: ", end="")
print(primitiva)