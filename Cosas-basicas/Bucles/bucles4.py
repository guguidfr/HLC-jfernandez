# José Daniel Fernández López
# 06/10/2022
n=int(input("Introduce un número entero del que hacer el factorial (>1): "))
fact=n
if n<=0:
    print("El valor introducido debe de ser positivo.")
else:
    for i in range(n-1, 1, -1):
        fact*=i
    print(f"El factorial de {n} es: {fact}.")