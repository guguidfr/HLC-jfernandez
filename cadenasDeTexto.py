# José Daniel Fernández López
# 29/09/2022
mensaje="Buenos días"
print(mensaje[2]) #Devuelve la letra 'e'
# print(menasje[45]) --> Da error 'out of range'
longitud=len(mensaje)
print(f"La longitud del mensaje es: {longitud}") #Muestra la longitud del mensaje
print(mensaje[len(mensaje)-1]) #Muestra el último carácter del mensaje
print(mensaje.lower()) #Muestra el mensaje con todo en minúscula
print(mensaje.upper()) #Muestra el mensaje con todo en mayúsucla
mensaje2="aló presidentes"
print(mensaje2.capitalize()) #Pone en mayúscula la primera letra, y las demás en minúscula
email="guguidfr@pm.me"
print(email.find("@pm.me")) #Devuelve la posición del primer caracter de la string dentro del 'find'

#Slicing = recorte de una cadena de texto
usuario=email[0:8]
print(f"El usuario es: {usuario}")
usuario=email[:8]
print(f"El usuario es: {usuario}")
dominio=email[9:14]
print(f"El dominio es: {dominio}")
dominio=email[9:]
print(f"El dominio es: {dominio}")