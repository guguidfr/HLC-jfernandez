# José Daniel Fernández López
# 29/09/2022
# Mostrar el país correspondiente al prefijo de un número de teléfono
# +34670980990
def pais(prfx):
    if prfx == "+34":
        print("El país es: ESPAÑA")
    elif prfx == "+49":
        print("El país es: ALEMANIA")
    elif prfx == "+33":
        print("El país es: FRANCIA")
    else:
        print("País del prefijo desconocido")
# --------------------------------------------
def get_prefix(char_set):
    prfx=char_set[:3]
    num_tlfn=char_set[3:]
    print(f"Tu prefijo es: {prfx}")
    print(f"Tu número de teléfono es: {num_tlfn}")
    pais(prfx)
# ---------------------------------------------
tlfn=(input("Introduce tu número de teléfono completo (prefijo y signo '+' incluídos): "))
get_prefix(tlfn)