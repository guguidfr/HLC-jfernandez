from csv import DictReader

men = "./Apuntes-introduccion/NombresComunesHombre.csv"
women = "./Apuntes-introduccion/NombresComunesMujer.csv"

def create_list(archivo):
    lista=[]
    with open(archivo, 'r') as file:
        reader = DictReader(file)
        for linea in reader:
            lista.append(linea)
    return lista

def buscar(nombre_clave,genero):
    check = False
    if genero == men:
        lista_elegida = "hombres"
    elif genero == women:
        lista_elegida = "mujeres"
    
    lista_nombres = create_list(genero)
    for registro in lista_nombres:
        if registro['Nombre'] == nombre_clave:
            print(f"El nombre '{nombre_clave}' está en la posición {registro['Numero']} de la lista de {lista_elegida}.\nHay {registro['Frecuencia']} personas que se llaman '{nombre_clave}' y hay {registro['DeCadaMil']} personas de cada mil que se llaman así.")
            check = True
    return check

key_name = input("Introduce el nombre que quieres buscar: ")
key_name = key_name.upper().strip()

encontrado_m = buscar(key_name,men)
if encontrado_m == False:
    encontrado_w = buscar(key_name,women)
    if encontrado_w == False:
        print(f"No se han encontrado registros de: {key_name}")