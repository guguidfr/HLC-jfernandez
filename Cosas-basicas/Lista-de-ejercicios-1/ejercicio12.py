# José Daniel Fernández López
# 27-09-2022
# Devolver el número máximo
def DevuelveMax(n1,n2):
        if n1 > n2:
            print(f"El número mayor es: {n1}")
        elif n2 > n1:
            print(f"El número mayor es: {n2}")
        else:
            print(f"Ambos números son iguales")

temp1=int(input("Introduce el primer número: "))
temp2=int(input("Introduce el segundo número: "))
DevuelveMax(temp1,temp2)