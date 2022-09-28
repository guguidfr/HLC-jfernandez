# José Daniel Fernández López
# 27-09-2022
# Da la nota correspondiente al número introducido por el usuario
nota=int(input("Introduce tu nota: "))
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