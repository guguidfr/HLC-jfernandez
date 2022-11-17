# José Daniel Fernández López
import csv
class Database:
    def __init__(self, source, content=[]):
        self.source = source
        self.content = content

    def load_db(self):       
        with open(self.source, 'r', newline="") as File:
            reader = csv.DictReader(File,)
            for line in reader:
                self.content.append(line)

    def get_register(self, ref_key, search):
        local_list = []
        for register in self.content:
            if register[ref_key]==search:
                local_list.append(register)
        if len(local_list) == 0:
            print("No hay registros para la búsqueda realizada.")
        elif len(local_list) == 1:
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
        self.content.remove(register)

    def edit_register(self, ref_key, search):
        # user_option = ""
        register = self.get_register(ref_key, search)
        register_copy = register
        finish = False
        while finish == False:
            valid_option = False      
            while valid_option == False:
                # Obtener las keys y los valores del diccionario por separado
                fields_keys_list = list(register.keys()) # type: ignore  -> Hace que pylance ignore los errores posibles en esta línea
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
                if (fields_values_list[user_option-1]).isdigit(): # type: ignore
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
                                register[fields_keys_list[user_option-1]] = value+addition # type: ignore
                                # Buscamos en la base de datos el registro original y lo modificamos con el valor nuevo
                                for db_register in self.content:
                                    if db_register == register_copy:
                                        db_register = register
                # Si el campo no es numérico, simplemente se sobreescribirá
                else: 
                    # Editamos el registro con el que estamos trabajando localmente en este método       
                    register[fields_keys_list[user_option-1]] = input(f"Introduce el nuevo valor para el campo \"{fields_keys_list[user_option-1]}\" - valor actual = {fields_values_list[user_option-1]}: ") # type: ignore
                    # Buscamos en la base de datos el registro original y lo modificamos con el valor nuevo
                    for db_register in self.content:
                                    if db_register == register_copy:
                                        db_register = register
    def new_entry(self):
        print("Próximamente")
        

main_db = Database(source="./Obligatorios-P3/db.csv")
main_db.load_db()
# output = main_db.get_register("Responsable","Miguel")
# print(output)
# main_db.delete_register("ID", "5")
# main_db.edit_register("Responsable","Miguel")
# for element in main_db.content:
#     print(element)