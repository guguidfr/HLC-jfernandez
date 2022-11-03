import io
f = open("./Manejo de archivos/file.txt", "w") # Abrir en modo escritura
f.write("Hola Mundo")
f.write("\nHasta luego")
f.close()

f2 = open("./Manejo de archivos/file.txt", "a") # Abrir en modo añadir
f2.write("-Una línea nueva")
f2.write("\nOtra línea más")
f2.close()

f3 = open("./Manejo de archivos/file.txt", "r") # Abrir en modo lectura
texto = f3.read()
print(texto)
f3.close()
print("---------------")
"""
f4 = open("./Manejo de archivos/none.txt", "r")
temp = f4.read()
print(temp)
f4.close()
"""

try:
    f4 = open("./Manejo de archivos/none.txt", "r")
    temp = f4.read()
except FileNotFoundError:
    print("El archivo que buscas no existe")
else: # El 'else' se ejecuta siempre, haya habido o no error
    f4.close()