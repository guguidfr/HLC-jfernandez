# José Daniel Fernández López
# 06/10/2022
palabras=[]
while True:
    entrada=input("Introduce una palabra. Introduce 'Salir' para terminar: ")
    if entrada=="Salir":
        break
    else:
        palabras.append(entrada)
print("Las palabras introducidas han sido: ")
for i in palabras:
    print(i)