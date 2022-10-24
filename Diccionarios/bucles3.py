# José Daniel Fernández López
# 20/10/2022
precios={"Cebolla":1.30, "Patata":0.9, "Tomate":1.59, "Berenjena":1.25}
print("Tenemos disponibles los siguientes productos: ")
for producto in precios:
    print(producto)
verdura=False
while verdura==False:
    verdura_usuario=input("Introduce la verdura que quieres comprar: ")
    if verdura_usuario.title() not in precios:
        print("La verdura que has elegido no está diponible.")
    else:
        verdura=True
kilos=False
while kilos==False:
    try:
        kilos_usuario=float(input("Introduce los kilos que quieres comprar: "))
    except:
        print("Debes introducir un número.")
    else:
        kilos=True

print(f"El coste total de {kilos_usuario} kilos de {verdura_usuario} es: {kilos_usuario*precios.get(verdura_usuario.title())}")