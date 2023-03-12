# José Daniel Fernández López
import csv
import random
'''
# Ejercicio 1:
mis_numeros = [] # Creamos vacía la lista contenedora de los números ganadores .
for i in range(6):
    nuevo_numero = random.randint(1,49) # Generamos un número aleatorio...
    mis_numeros.append(nuevo_numero) # ... y lo añadimos a la lista anteriormente creada.

# numeros_ganadores = (15,36,8,44,21,29) # En caso de que no queramos generar números aleatorios, podemos crear ya una tupla que contenga los números. Bastaría con comentar las líneas de la 5 a la 8.
numeros_ganadores = tuple(mis_numeros) # Transformamos la lista a tupla para que no sea modificable.
print("Se muestran aquí los números ganadores simplemente para comprobar el funcionamiento.")
print(numeros_ganadores)
# Creamos las listas necesarias y las declaramos vacías
numeros_usuario = []
numeros_acertados = []
numeros_errados = []
for i in range(6): # Le pediremos 6 números al usuario, uno a uno
    entrada_correcta = False
    while entrada_correcta == False: # Hasta que el número del usuario no sea válido, no ejecutaremos otra iteración
        try:
            intento_usuario = int(input("Introduce uno de tus números elegidos: "))
        except ValueError: # Si el usuario introduce algo que no sea un número entero, no avanzará.
            print("Debes de introducir un número entero.")
        else:
            if intento_usuario not in range(1,50): # Si el usuario introduce un número fuera del intervalo, no avanzará.
                print("Los números válidos son los pertenecientes al intervalo: [1,49]")
            elif intento_usuario in numeros_usuario: # Si el usuario introduce algún número repetido, no avanzará.
                print("Ya has introducido ese número.")
            else: # Finalmente, si la entrada del usuario es correcta, añadiremos el número y continuaremos con la siguiente iteración.
                numeros_usuario.append(intento_usuario)
                entrada_correcta = True

# El contador de aciertos a 0
aciertos = 0
# Si queremos, podemos añadir uno para el número de fallos.
# errores = 0
for i in range(6):
    if numeros_usuario[i] in numeros_ganadores: # Si el número que estamos comprobando está entre los ganadores, se añade a la lista de los acertados.
        aciertos+=1
        numeros_acertados.append(numeros_usuario[i])
for j in range(6): 
    """
    Recorreremos los números ganadores y comprobaremos que no están entre los que ha acertado el usuario.
    De esta manera podremos añadirlos a los números que ha fallado el usuario.
    """
    if numeros_ganadores[j] not in numeros_acertados:
        numeros_errados.append(numeros_ganadores[j])

# Al final, mostraremos en pantalla los resultados.
print("#############RESULTADOS#############")
print(f"Has acertado {aciertos} de 6 números.")
print(f"Has acertado los números: {numeros_acertados}")
print(f"Has fallado los números: {numeros_errados}")
print("####################################") 
'''

# Ejercicio 2
mi_csv = "./Examen1/peliculas.csv" # Guardamos la ubicación del csv en una variable
cabeceras = ["titulo","anyo","genero","director"] # Declaramos las cabeceras del csv para usarlas más adelante
peliculas = [] # Declaramos vacía la lista en la que guardaremos las líneas del csv
try: 
    with open(mi_csv,'r',newline="") as file: # Abrimos el csv y lo vamos guardando línea a lína
        reader = csv.DictReader(file)
        for linea in reader:
            peliculas.append(linea)
except FileNotFoundError:
    print("No se ha podido encontrar el archivo deseado.")
else: 
    for elemento in peliculas: # Mostramos las películas y la información de cada una accediendo a cada clave del diccionario
        print("Título:",elemento["titulo"],"- Director:",elemento["director"],"- Año:",elemento["anyo"],"- Género:",elemento["genero"])

# Ejercicio 3
def nueva_pelicula(lista_de_peliculas):
    # Declaramos en un diccionario la nueva película que vamos a añadir
    nueva_peli={
        "titulo":"La Vida es Bella",
        "director":"Roberto Benigni",
        "genero":"Drama",
        "anyo":"1997"
    }
    lista_de_peliculas.append(nueva_peli) # Añadimos al final de la lista el diccionario de la nueva película
nueva_pelicula(peliculas)

# Ejercicio 4
def eliminar_pelicula(lista_de_peliculas2):
    for peli in lista_de_peliculas2:
        if peli["titulo"] == "Origen": # Recorremos nuestra lista de películas buscando la coincidencia de que el título sea "Origen"
            lista_de_peliculas2.remove(peli) # Cuando encontremos la coincidencia, borramos el diccionario
eliminar_pelicula(peliculas)

# Ejercicio 5
with open(mi_csv,'w',newline="") as file: # Abrimos el csv...
    writer = csv.DictWriter(file, cabeceras) # ... le decimos a DictWriter qué archivo tiene que leer y cuáles son las cabeceras...
    writer.writeheader() # ... escribimos las cabeceras...
    writer.writerows(peliculas) # ... y finalmente las películas.
