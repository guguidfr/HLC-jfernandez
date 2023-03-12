# José Daniel Fernández López
# 05/10/2022
# Comprobar tipo de archivo
file_path=input("Introduce el nombre completo de un archivo o su ruta: ")
extnsn=file_path[file_path.find("."):]
if extnsn == ".pdf":
    print("El archivo introducido es un PDF.")

elif extnsn == ".py":
    print("El archivo introducido es un script de Python.")

elif extnsn == ".docx":
    print("El archivo introducido es un archivo de Word.")

elif extnsn == ".sh":
    print("El archivo introducido es un script de Bash.")

elif extnsn == ".exe":
    print("El archivo introducido es un ejecutable de Windows.")

elif extnsn == ".jpg" | extnsn == ".png":
    print("El archivo introducido es una imagen.")

elif extnsn == ".mp4" | extnsn == ".avi" | extnsn == ".mkv":
    print("El archivo introducido es un vídeo.")

elif extnsn == ".deb":
    print("El archivo introducido es un paquete de Debian.")

elif extnsn == ".txt":
    print("El archivo introducido es un archivo de texto.")
    
else:
    print("Tipo de archivo desconocido.")