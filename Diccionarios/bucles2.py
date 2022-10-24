# José Daniel Fernández López
# 20/10/2022
monedas={"Euro":"€", "Dolar":"$", "Libra":"£", "Yen":"¥"}
entrada_usuario=input("Introduce la divisa de la que quieras consultar el símbolo: ")
if entrada_usuario.title() in monedas:
    print(monedas[entrada_usuario.title()])
else:
    print("La divisa no se ha encontrado.")
print("--------------")
print(monedas[entrada_usuario.title()]) if entrada_usuario.title() in monedas else print("La divisa no se ha encontrado.")