# Leer línea a línea
with open("./Manejo de archivos/tabla_multiplicar_5.txt","r") as f:
    contador = 1
    for linea in f:
        print(f"{contador} - {linea.strip()}")
        contador+=1

# Método 'readlines'
with open("./Manejo de archivos/tabla_multiplicar_5.txt","r") as f:
    lista=f.readlines()
    # lista=[linea.strip() for linea in f] -> Esto le quita los saltos de línea automáticamente
print("-------------------")
print("Con 'readlines'")
print(lista[0])
print(lista[1])