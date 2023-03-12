# Este es el primer programa de Python

# Se usa la almohadilla para comentar una línea

'''
Se usan 3 comillas simples para comentar en bloque
'''

# Variables
usuario = "ASIR2"
numero = 254678
decimal = 2.56849874
booleana = True

print(usuario)
print("Hello World!")
print("Hello " + usuario) #Forma no recomendable
print(f"Hello {usuario}! Bienvenido") #Forma correcta

saludo = "Feliz jueves"
print(f"{saludo} {usuario}!")

tipo1 = type(usuario)
print(f"La variable usuario es de tipo: {tipo1}")
tipo2 = type(numero)
print(f"La variable numero es de tipo: {tipo2}")
tipo3 = type(decimal)
print(f"La variable decimal es de tipo: {tipo3}")

print(usuario, numero, decimal, booleana)