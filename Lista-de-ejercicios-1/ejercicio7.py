# José Daniel Fernández López
# 27-09-2022
# Calcula el índice de masa corporal
peso = int(input("Introduzca su peso en Kg: "))
altura = float(input("Introduzca su altura en metros: "))
imc = peso/(altura**2)
dec2 = round(imc, 2)
print(f"Tu índice de masa corporal es {imc} donde {dec2} es el índice de masa corporal calculado redondeado con dos decimales.")