# José Daniel Fernández López
# 27-09-2022
# Mostrar un saludo a partir de 2 parámetros de entrada
def saludo(p1,p2):
        p1=input("Introduce el saludo: ")
        p2=input("Introduce tu nombre: ")
        #print(f"Prueba p1 → {p1}")
        #print(f"Prueba p2 → {p2}")
        #print(f"{p1} {p2}")
        if p1 == "" and p2 == "":
            print("Hello World!")
        else:
            print(f"{p1} {p2}")

temp1="texto"
temp2="texto"
saludo(temp1,temp2)