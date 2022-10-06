# José Daniel Fernández López
# 06/10/2022
lineas=(1,2,3,4,5,6,7,8,9,10)
n=int(input("Introduce un número del 1 al 10 del cual obtener la tabla: "))
if n < 1 or n > 10:
    print("El número introducido no es válido.")
else:
    print(f"La tabla del {n} es:")
    for i in lineas:
        print(f"{n}*{i}={n*i}")