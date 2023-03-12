# José Daniel Fernández López
# 03/011/2022
def create_table():
    entrada_correcta = False
    while entrada_correcta == False:
        try:
            tabla_ref = int(input("Introduce un número [1,10]: "))
        except:
            print("La entrada debe de ser un número entero.")
        else:
            if tabla_ref < 1 or tabla_ref > 10:
                print("El número debe de estar en el intervalo [1,10].")
            else:
                entrada_correcta = True
    file = open(f"./Manejo de archivos/tabla_multiplicar_{tabla_ref}.txt","w")
    for i in range(1,11):
        file.write(f"{tabla_ref} x {i} = {tabla_ref * i}\n")
    file.close()
create_table()