# José Daniel Fernández López
# 27-09-2022
# Es una calculadora
def Suma(n1,n2):
    print(f"El resultado de la suma de {n1}+{n2} es: {n1+n2}")

def Resta(n1,n2):
    print(f"El resultado de la resta de {n1}-{n2} es: {n1-n2}")

def Multp(n1,n2):
    print(f"El resultado de la multiplicación de {n1}*{n2} es: {n1*n2}")

def Div(n1,n2):
    print(f"El resultado de la división de {n1}/{n2} es: {n1/n2}")

print("1. Sumar\n2. Restar\n3. Multiplicar\n4. Dividir")
ref=input("Introduce una opción [1-4] → ")
o1=int(input("Introduce el primer operando → "))
o2=int(input("Introduce el segundo operando → "))

if ref == 1:
    Suma(o1,o2)
elif ref == 2:
    Resta(o1,o2)
elif ref == 3:
    Multp(o1,o2)
elif ref == 4:
    Div(o1,o2)
else:
    print("Ha habido un error")