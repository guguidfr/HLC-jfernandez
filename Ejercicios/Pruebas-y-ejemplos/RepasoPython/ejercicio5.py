# José Daniel Fernández López
# 2022-12-13
entrada_valida = False
while entrada_valida == False:
    try:
        year = int(input("Introduce un año para comprobar si es bisiesto: "))
    except ValueError:
        print("Debes de introducir un número.")
    else:
        entrada_valida = True
if year%400==0: # type: ignore
    print(f"El año {year} es bisiesto") # type: ignore
elif year%4==0 and year%100!=0: # type: ignore
    print(f"El año {year} es bisiesto.") # type: ignore
else:
    print(f"El año {year} no es bisiesto.") # type: ignore