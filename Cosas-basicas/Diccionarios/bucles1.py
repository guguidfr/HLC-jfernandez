# José Daniel Fernández López
# 20/10/2022
informacion_usuario={"nombre":"", "edad":"", "telefono":"", "direccion":""}
for campo in informacion_usuario:
        entrada=input(f"Introduce tu {campo}: ")
        informacion_usuario[campo]=entrada
print(informacion_usuario)
print(f"{informacion_usuario['nombre']} tiene {informacion_usuario['edad']}, vive en {informacion_usuario['direccion']} y su teléfono es {informacion_usuario['telefono']}")