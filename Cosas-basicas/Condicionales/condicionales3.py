# José Daniel Fernández López
# 05/10/2022
# Comparar la entrada por teclado con un dato guardado previamente
passwd="MyPaSsWoRd01"
passwd_check=input("Introduce la contraseña: ")
print("Contraseña correcta." if passwd.casefold() == passwd_check.casefold() else "Contraseña incorrecta.")