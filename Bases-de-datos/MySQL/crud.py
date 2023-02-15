"""
Necesitarás tener "pip" instalado para que compruebe
Este programa solamente funcionará para un servidor de base de datos MySQL
y con una tabla que sea la siguiente:

    create table juegos(
    ID int primary key,
    Nombre varchar(100),
    Desarrolladora varchar(100),
    Pegi enum(3,7,12,16,18),
    Fecha_salida date
    );

"""
import subprocess
import re
def modules():
    modulos_en_el_sistema = subprocess.check_output("pip freeze", shell=True).decode("utf-8")
    modulos_instalados = [module.strip() for module in modulos_en_el_sistema.split('\n')]
    modulos_necesarios = ["pymysql"]
    modulos_cumplidos = [ re.sub("==[0-9.]*", "", x) for x in modulos_instalados if any(i in x for i in modulos_necesarios) ]
    if len(modulos_cumplidos) == len(modulos_necesarios):
        print("Están instalados todos los módulos necesarios.")
    else:
        print("Faltan módulos.")
        for modulo in modulos_cumplidos:
            if modulo in modulos_necesarios:
                modulos_necesarios.remove(modulo)
        print(f"Se van a instalar los siguientes módulos: {modulos_necesarios}")
        try:
            for modulo in modulos_necesarios:
                subprocess.run(["pip", "install", modulo],shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        except:
            print("No se han podido instalar los módulos modulos_necesarios.")

try:
    modules()
except:
    print("Ha habido un error al intentar instalar los módulos necesarios")
    sys.exit(1)
# --------------------------------------------------------------------------------
import pymysql
import sys
import datetime

# hostname = 'localhost'
# username = 'usu_prueba'
# password = 'prueba'
# database = 'pruebas'

class DB:
    def __init__(self, host, user, database, password):
        self.host = host #input("Introduce el host: ")
        self.user = user #input("Introduce el nombre del usuario con el que quieres conectar: ")
        self.database = database #input("Introduce el nombre de la base de datos a la que conectarte: ")
        self.password = password #input("Introduce la contraseña: ")
        self.conn = None
    
    def mysql_db_conn(self):
        """
        Método para hacer la conexión a la base de datos
        """
        try:
            self.conn=pymysql.connect(
                user=self.user,
                password=self.password,
                host=self.host, 
                database=self.database
            )
        except pymysql.Error as db_e:
            print(f"Error al conectar a la base de datos: {db_e}")
            sys.exit(1)
        else:
            print("Conexión establecida.")
    
    def do_query(self, statement):
        """
        Método para ejecutar una query que se pasa al parámetro "statement"
        """
        cursor = self.conn.cursor() #type: ignore
        try:
            cursor.execute(statement)
        except pymysql.IntegrityError:
            print("Error al hacer INSERT: clave primaria duplicada.")
        else:
            self.conn.commit() #type: ignore

    def close_conn(self):
        """
        Cerrar la conexión a la base de datos
        """
        self.conn.close() #type: ignore

    '''
    def return_cursor(self):
        """
        Devolver el cursor
        """
        return self.conn.cursor() #type: ignore
    '''

class Actions(DB):

    columns = ("ID", "Nombre", "Desarrolladora", "Pegi", "Fecha de salida")

    def define_field_value(self, field):
        """
        El bucle while con todos los "if" es para comprobar que la entrada es correcta en cada uno de los campos definidos para tabla con la que va a funcionar el programa.
        Todo esto se puede incluir en los métodos del SELECT e INSERT.
        """
        correct = False
        while correct == False:
            if field == "ID":
                try:
                    value = int(input("Introduce el ID: "))
                except:
                    print("Debes de introducir un número.")
                else:
                    correct = True

            elif field == "Nombre":
                try:
                    value = str(input("Introduce el nombre: "))
                except:
                    print("Entrada no válida.")
                else:
                    correct = True

            elif field == "Desarrolladora":
                try:
                    value = str(input("Introduce el nombre de la desarrolladora: "))
                except:
                    print("Entrada no válida.")
                else:
                    correct = True
            
            elif field == "Pegi":
                try:
                    value = int(input("Introduce el PEGI: "))
                except:
                    print("Entrada no válida.")
                else:
                    if value not in (3,7,12,16,18):
                        print("PEGI no válido.")
                    else:
                        correct = True

            elif field == "Fecha de salida":
                try:
                    value = datetime.date.fromisoformat(input("Introduce la fecha: "))
                except ValueError:
                    print("Formato de fecha no válido. Debe de ser: YYYY-MM-DD")
                else:
                    correct = True
        return value #type: ignore

    def select_column(self):
        print("Estas son las columnas de la tabla: ")
        counter = 1
        for field in self.columns:
            print(f" {counter} - {field}")
            counter += 1
        exit = False
        while exit == False:
            try:
                option = int(input(f"Elige una de las opciones (1-{len(self.columns)}): "))-1
            except:
                print("Debes de introducir un número.")
            else:
                if 0>option or option>len(self.columns):
                    print(f"Debes de introducir un número entre 1 y {len(self.columns)}")
                else:
                    exit = True
        return option #type: ignore

    def insert(self):
        query = f"INSERT INTO juegos values({self.define_field_value("ID")},{self.define_field_value("Nombre")},{self.define_field_value("Desarrolladora")},{self.define_field_value("PEGI")},{self.define_field_value("Fecha de salida")})" #type: ignore
        self.do_query(query)

    def select(self):
        exit = False
        while exit == False:
            try:
                respuesta = int(input("¿Quieres hacer un select de la tabla entera (1) o quieres filtrar por alguno de los campos (2)?: "))
            except:
                print("Debes de introducir un número.")
            else:
                exit = True
        if respuesta == 1: #type: ignore
            query = "SELECT * FROM juegos"
            self.conn.cursor().execute(query) #type: ignore
            for id, nombre, dev, pegi, date in self.conn.cursor().fetchall(): #type: ignore
                print(f"ID: {id}, Nombre: {nombre}, Desarrolladora: {dev}, PEGI: {pegi}, Fecha de lanzamiento: {date}")
        elif respuesta == 2: #type: ignore
            # print("Estas son las columnas de la tabla: ")
            # counter = 1
            # for field in self.columns:
            #     print(f" {counter} - {field}")
            #     counter += 1
            # exit = False
            # while exit == False:
            #     try:
            #         option = int(input(f"Elige una de las opciones (1-{len(self.columns)}): "))-1
            #     except:
            #         print("Debes de introducir un número.")
            #     else:
            #         if 0>option or option>len(self.columns):
            #             print(f"Debes de introducir un número entre 1 y {len(self.columns)}")
            #         else:
            #             exit = True

            print("Elige una de las columnas:")
            selected_column = self.select_column() #type: ignore
            print("Define el valor de la columna por la que quieres filtrar:")
            filter_value = self.define_field_value(selected_column)
            query = f"SELECT * FROM juegos WHERE {selected_column}={filter_value}"
            self.conn.cursor().execute(query) #type: ignore
            for id, nombre, dev, pegi, date in self.conn.cursor().fetchall(): #type: ignore
                print(f"ID: {id}, Nombre: {nombre}, Desarrolladora: {dev}, PEGI: {pegi}, Fecha de lanzamiento: {date}")

    def delete(self):
        # print("Estas son las columnas de la tabla: ")
        # counter = 1
        # for field in self.columns:
        #     print(f" {counter} - {field}")
        #     counter += 1
        # exit = False
        # while exit == False:
        #     try:
        #         option = int(input(f"Elige una de las opciones (1-{len(self.columns)}): "))-1
        #     except:
        #         print("Debes de introducir un número.")
        #     else:
        #         if 0>option or option>len(self.columns):
        #             print(f"Debes de introducir un número entre 1 y {len(self.columns)}")
        #         else:
        #             exit = True
        
        print("Elige una de las columnas:")
        selected_column = self.select_column() #type: ignore
        print("Define el valor de la columna por la que quieres filtrar:")
        filter_value = self.define_field_value(selected_column)
        query = f"DELETE FROM juegos WHERE {selected_column}={filter_value}"
        self.do_query(query)

    def update(self):
        print("Elige una de las columnas para filtrar:")
        filter_column = self.select_column() #type: ignore
        print("Define el valor de la columna por la que quieres filtrar:")
        filter_value = self.define_field_value(filter_column)
        print("Elige la columna de la que quieres cambiar el valor:")
        selected_column = self.select_column()
        print("Elige el nuevo valor para la columna seleccionada:")
        new_value = self.define_field_value(selected_column)
        query = f"UPDATE TABLE juegos SET {selected_column}={new_value} WHERE {filter_column}={filter_value}"
        self.do_query(query)

# --------------------------------------------------------------------------------
# hostname = 'localhost'
# username = 'usu_prueba'
# password = 'prueba'
# database = 'pruebas'
db_server = Actions("localhost","usu_prueba","pruebas","prueba")
db_server.mysql_db_conn()
print("Te doy la bienvenida al menú CRUD para MySQL.")
input("Pulsa ENTER para continuar... ")
while True:
    try:
        opcion= int(input("Elige una opción:\n 1-INSERT\n 2-SELECT\n 3-DELETE\n 4-UPDATE\n 5-Salir\n --> "))
    except:
        print("Tienes que introducir un número.")
    else:
        if opcion == 1:
            db_server.insert()
        elif opcion == 2:
            db_server.select()
        elif opcion == 3:
            db_server.delete()
        elif opcion == 4:
            db_server.update()
        elif opcion == 5:
            break
        else:
            print("Debes de elegir una de las opciones anteriores")