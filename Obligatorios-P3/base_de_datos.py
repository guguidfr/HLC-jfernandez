# José Daniel Fernández López
import csv
import time
import os
# --------------------------------------------------------------
class Database:
    def __init__(self, source, content=[]): # Inicializamos los atributos del objeto
        self.source = source # Arhivo desde el que importaremos la base de datos
        self.content = content # Es la lista que contiene la base de datos. Se inicializará vacía

    def load_db(self): # Método para cargar la base de datos en una lista       
        with open(self.source, 'r', newline="") as File:
            reader = csv.DictReader(File,)
            for line in reader: # Leemos cada línea, y la añadimos a la lista
                self.content.append(line)

    def show_db(self):
        for register in self.content:
            for key in register: # Para cada campo del registro, lo mostraremos junto con su valor
                print(f"{key} = {register[key]}")
            print("--------------------------------------")

    def get_register(self, ref_key, search):
        local_list = [] # Inicializamos una lista vacía que existirá solamente dentro de este método
        for register in self.content:
            if register[ref_key].lower()==search.lower():
                local_list.append(register) # Añadimos a la lista los registros que coincidan con los criterios de búsqueda
        if len(local_list) == 0: # Si la lista tiene 0 elementos, no hemos encontrado nada.
            print("No hay registros para la búsqueda realizada.")
        elif len(local_list) == 1: # Si la lista con
            return local_list[0]
        else:
            valid_option = False
            while valid_option == False:
                print("Hay varias coincidencias para la búsqueda. Los resultado son: ")
                option = 1
                for coincidence in local_list:
                    print(f"{option} => {coincidence}")
                    option += 1
                try:    
                    selection = int(input(f"¿Cuál de los registros quieres elegir? [1-{len(local_list)}]: "))
                except ValueError:
                    print(f"Debe de elegir un número entero entre 1 y {len(local_list)}.\n")
                except:
                    print("Error inesperado.")
                else:
                    if selection > len(local_list):
                        print("Elige una de las opciones posibles.\n")
                    else:
                        valid_option = True
                        return local_list[selection-1]
    
    def delete_register(self, ref_key, search):
        register = self.get_register(ref_key, search)
        if register != None:
            self.content.remove(register)

    def edit_register(self, ref_key, search):
        # user_option = ""
        register = self.get_register(ref_key, search)
        if register != None:
            register_copy = register
            finish = False
            while finish == False:
                valid_option = False      
                while valid_option == False:
                    # Obtener las keys y los valores del diccionario por separado
                    fields_keys_list = ["ID","Titulo","Responsable","DNI-Responsable","N-Horas"] # type: ignore  -> Hace que pylance ignore los errores posibles en esta línea
                    fields_values_list = list(register.values()) # type: ignore
                    field = 1
                    # Mostrar la información actual del registro seleccionado
                    print("Los datos actuales del registro son: ")
                    for (i,j) in zip(fields_keys_list, fields_values_list): 
                        print(f"{field}.{i} = {j}")
                        field += 1  
                    print("0. Salir.\n")
                    # Recibir una opción válida del campo a modifcar por el usuario
                    try:
                        user_option = int(input(f"Introduce el número del campo que quieras cambiar [0-{field-1}]: "))
                    except ValueError:
                        print("Debes de introducir el número del campo que quieras editar.\n+--------------------------------------+")
                    except:
                        print("Error inesperado.\n+--------------------------------------+")
                    else:
                        if user_option in range(0,field):
                            valid_option = True
                        else:
                            print(f"Las opciones disponibles van de 0 a {field-1}.\n+--------------------------------------+")
                # Hacer los cambios
                if user_option == 0: # type: ignore
                    finish = True
                else:
                    # Si el campo es numérico, se modificará sumando o restando
                    if (fields_values_list[user_option-1]).isdigit() or type(fields_values_list[user_option-1]) == int : # type: ignore
                        value = int(fields_values_list[user_option-1]) # type: ignore
                        valid_input = False
                        while valid_input == False:
                            try:
                                addition = int(input(f"¿En cuánto quieres aumentar (ej: 5) o reducir (ej: -2) el número? Valor actual: {value} --> "))
                            except ValueError:
                                print("Debes de introducir un número entero positivo o negativo")
                            else:
                                if value+addition <= 0:
                                    print("El valor del campo no puede acabar siendo 0 o negativo.")
                                else:
                                    valid_input = True
                                    register[fields_keys_list[user_option-1]] = str(value+addition) # type: ignore
                                    # Buscamos en la base de datos el registro original y lo modificamos con el valor nuevo
                                    for db_register in self.content:
                                        if db_register == register_copy:
                                            db_register = register
                    # Si el campo no es numérico, simplemente se sobreescribirá
                    else: 
                        # Editamos el registro con el que estamos trabajando localmente en este método       
                        register[fields_keys_list[user_option-1]] = input(f"Introduce el nuevo valor para el campo \"{fields_keys_list[user_option-1]}\" - valor actual = {fields_values_list[user_option-1]}: ").strip() # type: ignore
                        # Buscamos en la base de datos el registro original y lo modificamos con el valor nuevo
                        for db_register in self.content:
                                        if db_register == register_copy:
                                            db_register = register
    
    def new_entry(self):
        # Declaramos los campos que debe de rellenar el usuario
        fields_keys_list = ["ID","Titulo","Responsable","DNI-Responsable","N-Horas"]
        new_entry = {}
        for key in fields_keys_list:
            # Si es alguno de estos dos campos, que son numéricos, el usuario deberá de introducir un número
            if key == "ID" or key == "N-Horas":
                valid = False
                while valid == False:
                    # try:
                    #     new_entry[key] = int(input(f"Introduce el valor para \"{key}\": "))
                    # except ValueError:
                    #     print("El valor introducido debe de ser un número entero.")
                    # except:
                    #     print("Error inesperado.")
                    # else:
                    #     valid = True
                    temp = input(f"Introduce el valor para \"{key}\": ").strip()
                    if temp.isdigit():
                        valid = True
                        new_entry[key] = temp
                    else:
                        print("El valor introducide no es válido. Debes de introducir un número.")
            elif key == "DNI-Responsable": # Cuando se vaya a rellenar el DNI, se pasrá a mayúscula para que coincida con el resto de registros
                new_entry[key] = input(f"Introduce el valor para \"{key}\": ").upper().strip()
            else: # Para el resto de campos, pasaremos siempre la primera letra a mayúsculas
                new_entry[key] = input(f"Introduce el valor para \"{key}\": ").capitalize().strip()
        
        # Añadimos la nueva entrada a nuestra base de datos cargada en memoria
        self.content.append(new_entry)
# --------------------------------------------------------------
def loading():
    for i in range(3):
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Cargando base de datos.")
        time.sleep(0.5)
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Cargando base de datos..")
        time.sleep(0.5)
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Cargando base de datos...")
        time.sleep(0.5)
        os.system('cls' if os.name == 'nt' else 'clear')

def get_user_input():
    print("Los campos por lo que puedes filtrar son los siguientes:")
    global fields_keys_list 
    fields_keys_list = ["ID","Titulo","Responsable","DNI-Responsable","N-Horas"]
    counter = 1
    for i in fields_keys_list:
        print(f"{counter} - {i}")
        counter += 1
    valid_field = False
    while valid_field == False:
        try:
            field = int(input("¿Por cuál de los campos quieres filtrar?: "))
        except ValueError:
            print("Debes de introducir un número.")
        else:
            if field not in range(1,counter):
                print("La opción que has elegido no existe")
            else:
                key = fields_keys_list[field-1]
                # print(f"La key es: {key}")
                search = input("Introduce tu búsqueda: ").strip()
                # print(f"La búsqueda es: {search}")
                return key, search
# --------------------------------------------------------------
main_db = Database(source="./Obligatorios-P3/db.csv")
main_db.load_db()
# --------------------------------------------------------------
loading()

user_choice = ""
save_db = False
exit_no_saving = False
while save_db == False and exit_no_saving == False:
    valid_entry = False
    print("--------------------------------------")
    while valid_entry == False:
        print("¿Qué es lo que quieres hacer?")
        try:
            user_choice = int(input("1. Imprimir la base de datos\n2. Obtener un registro\n3. Eliminar un registro\n4. Editar un registro\n5. Añadir un nuevo registro \n6. Guardar y salir \n7. Salir sin guardar \n====> "))
        except ValueError:
            print("Debes de introducir un número.\n")
        else:
            if user_choice<0 or user_choice>7:
                print("Debes de elegir el número de una de las opciones.\n")
            else:
                valid_entry = True
    if user_choice == 1:
        os.system('cls' if os.name == 'nt' else 'clear')
        main_db.show_db()
        input("Pulsa enter para contiuar... ")
        os.system('cls' if os.name == 'nt' else 'clear')

    elif user_choice == 2:
        ref, search = get_user_input() # type: ignore
        selected_register = main_db.get_register(ref, search)
        if selected_register != None:
            r_id = selected_register.get("ID") # type: ignore
            r_title = selected_register.get("Titulo") # type: ignore
            r_responsible = selected_register.get("Responsable") # type: ignore
            r_dni_responsible = selected_register.get("DNI-Responsable") # type: ignore
            r_n_horas = selected_register.get("N-Horas") # type: ignore
            print(f"El ID es \"{r_id}\", el título es \"{r_title}\" y el responsable es \"{r_responsible}\". Su DNI es \"{r_dni_responsible}\" y el número de horas totales es \"{r_n_horas}\"")
            input("Pulsa enter para contiuar... ")
            os.system('cls' if os.name == 'nt' else 'clear')
        else:
            input("Pulsa enter para contiuar... ")
            os.system('cls' if os.name == 'nt' else 'clear')

    elif user_choice == 3:
        ref, search = get_user_input() # type: ignore
        main_db.delete_register(ref, search)
        input("Pulsa enter para contiuar... ")
        os.system('cls' if os.name == 'nt' else 'clear')

    elif user_choice == 4:
        ref, search = get_user_input() # type: ignore
        main_db.edit_register(ref, search)
        input("Pulsa enter para contiuar... ")
        os.system('cls' if os.name == 'nt' else 'clear')

    elif user_choice == 5:
        main_db.new_entry()
        input("Pulsa enter para contiuar... ")
        os.system('cls' if os.name == 'nt' else 'clear')

    elif user_choice == 6:
        with open("./Obligatorios-P3/db.csv", 'w', newline="") as File:
            writer = csv.DictWriter(File, fields_keys_list)
            writer.writeheader()
            writer.writerows(main_db.content)
        for i in range(3):
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Guardando base de datos.")
            time.sleep(0.5)
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Guardando base de datos..")
            time.sleep(0.5)
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Guardando base de datos...")
            time.sleep(0.5)
            os.system('cls' if os.name == 'nt' else 'clear')
        print("Base de datos guardada.")
        time.sleep(0.8)
        save_db = True

    elif user_choice == 7:
        for i in range(3):
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Limpiando.")
            time.sleep(0.5)
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Limpiando..")
            time.sleep(0.5)
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Limpiando...")
            time.sleep(0.5)
            os.system('cls' if os.name == 'nt' else 'clear')
        print("Se han descartados los cambios.")
        time.sleep(0.8)
        exit_no_saving = True
                