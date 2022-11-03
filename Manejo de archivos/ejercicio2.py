import io
def obtener_tabla(tabla_elegida):
    try:
        file = open(f"./Manejo de archivos/tabla_multiplicar_{tabla_elegida}.txt","r")
    except FileNotFoundError:
        print(f"No existe el fichero \"tabla_multiplicar_{tabla_elegida}.txt\".")
    else:
        tabla = file.read()
        print(tabla)
        file.close()

entrada_correcta = False
while entrada_correcta == False:
    try:
        tabla_ref = int(input("Introduce la tabla de la que quieres mostrar la tabla de multiplicar [1,10]: "))
    except:
        print("La entrada debe de ser un número entero.")
    else:
        if tabla_ref < 1 or tabla_ref > 10:
            print("El número debe de estar en el intervalo [1,10].")
        else:
            entrada_correcta = True
obtener_tabla(tabla_ref)