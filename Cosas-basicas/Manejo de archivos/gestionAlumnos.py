# José Daniel Fernández López
# 03/011/2022
with open("./Manejo de archivos/alumnos.txt","r") as file:
    alumnos = []
    for line in file:
        alumnos.append(line.strip())
print(alumnos)