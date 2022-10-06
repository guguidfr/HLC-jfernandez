# José Daniel Fernández López
# 06/10/2022
cadena=input("Introduce el texto que quieras: ")
letra=input("Introduce la letra que quieres contar: ")
total=0
for caracter in cadena:
    if caracter==letra:
        total+=1
print(f"La letra '{letra}' ha aparecido {total} veces.")