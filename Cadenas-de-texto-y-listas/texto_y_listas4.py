# José Daniel Fernández López
# 29/09/2022
# Dividir correo electrónico
correo=input("Introduce tu correo electrónico: ")
half=correo.find("@")
usuario=correo[:half]
dominio=correo[half+1:]
print(f"El usuario es: {usuario}")
print(f"El dominio es: {dominio}")