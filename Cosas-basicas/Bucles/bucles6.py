# José Daniel Fernández López
# 06/10/2022
modulos=["ASO", "HLC", "SRI", "SAD", "IAW", "SGBD"]
notas=[]

for i in modulos:
    num=int(input(f"Introduce tu nota para {i}: "))
    notas.append(num)
    
for j in range(len(modulos)):
    print(f"En {modulos[j]} has sacado un {notas[j]}.")