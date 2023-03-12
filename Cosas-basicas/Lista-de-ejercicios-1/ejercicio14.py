# José Daniel Fernández López
# 27-09-2022
# Da la nota correspondiente al número introducido por el usuario

nota=float(input("Introduce tu nota: "))
if nota < 5 and nota >= 0:
    print("La nota es INSUFICIENTE")
elif nota >= 5 and nota < 7:
    print("La nota es SUFICIENTE")
elif nota >=7 and nota < 9:
    print("La nota es NOTABLE")
elif nota >=9 and nota < 10:
    print("La nota es SOBRESALIENTE")
elif nota == 10:
    print("La nota es MATRÍCULA DE HONOR")
else:
    print("La nota introducida no es válida")

# Versión con las condiciones más simplificadas
'''
nota=float(input("Introduce tu nota: "))
if 0 <= nota < 5:
    print("La nota es INSUFICIENTE")
elif 5 <= nota < 7:
    print("La nota es SUFICIENTE")
elif 7 <= nota < 9:
    print("La nota es NOTABLE")
elif 9 <= nota < 10:
    print("La nota es SOBRESALIENTE")
elif nota == 10:
    print("La nota es MATRÍCULA DE HONOR")
else:
    print("La nota introducida no es válida")
'''