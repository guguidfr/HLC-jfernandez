# José Daniel Fernández López  
# 2022-12-13
clave = {"M":"0","U":"1","R":"2","C":"3","I":"4","E":"5","L":"6","A":"7","G":"8","O":"9",
         "0":"M","1":"U","2":"R","3":"C","4":"I","5":"E","6":"L","7":"A","8":"G","9":"O",
         " ":" "}
# Creamos un diccionario con los valores de cada letra y número
coincidencias = [] # Creamos una lista vacía en la que añadiremos más adelante las letras o números que estén en el diccinario
entrada_usuario = str(input("Introduce lo que quieres codificar o decodificar: ")).upper()

for caracter in entrada_usuario:
    if caracter in clave and caracter not in coincidencias: # Añadimos a la lista los caracteres que coincidan y que no estén ya en ella
            coincidencias.append(caracter)

for elemento in coincidencias: # Y por cada coincidencia, lo reemplazaremos por su valor corresponiente
    entrada_usuario = entrada_usuario.replace(elemento,clave[elemento])

print(entrada_usuario)