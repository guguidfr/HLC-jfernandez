# José Daniel Fernández López
# 2022-12-13
vetados = ("00000000T","00000001R","99999999R")
entrada_valida = False
while entrada_valida == False:
    dni = str(input("Introduce un DNI: ")).upper().strip()
    if dni in vetados:
        print("Ese DNI está declarado como no válido.")
    elif len(dni) != 9:
        print("Longitud incorrecta. Deben de ser 9 caracteres")
    elif not dni[0:8].isnumeric():
        print("Los 8 primeros caracteres deben de ser numéricos.")
    elif dni[-1::].isnumeric():
        print("El último carácter debe de ser una letra.")
    else:
        entrada_valida = True

ref_dni = {0:"T",1:"R",2:"W",3:"A",4:"G",5:"M",6:"Y",7:"F",8:"P",9:"D",10:"X",11:"B",12:"N",13:"J",14:"Z",15:"S",16:"Q",17:"V",18:"H",19:"L",20:"C",21:"K",22:"E"
}
if ref_dni[(int(dni[0:8]))%23] != dni[-1::]: # type: ignore
    print("El DNI no es válido.")
else:
    print("El DNI es correcto.")