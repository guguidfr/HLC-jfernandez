# José Daniel Fernández López
# 29/09/2022
# Separar en euros y céntimos
precio=input(f"Introduce el precio: ")
get_dot=precio.find(".")
euros=precio[:get_dot]
centimos=precio[get_dot+1:]
print(f"El importe total es de {euros} euros y {centimos} céntimos.")