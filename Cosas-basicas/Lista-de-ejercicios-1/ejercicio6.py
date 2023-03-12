# José Daniel Fernández López
# 27-09-2022
# Pide al usuario 3 valores para luego hacer la media aritmética de los 3
'''
Forma compleja

n1, n2, n3 = [int(x) for x in input("Introduce 3 valores: ").split()]
print(f"La media aritmética de {n1}+{n2}+{n3} es {(n1+n2+n3)/3}")

'''
# Forma simple
n1 = int(input("Introduce el primer valor: "))
n2 = int(input("Introduce el segundo valor: "))
n3 = int(input("Introduce el tercer valor: "))
print(f"La media aritmética de {n1}+{n2}+{n3} es {(n1+n2+n3)/3}")