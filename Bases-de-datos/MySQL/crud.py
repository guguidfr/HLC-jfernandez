import pymysql
# import mariadb
import sys

# hostname = 'localhost'
# username = 'usu_prueba'
# password = 'prueba'
# database = 'pruebas'

class DbConn:
    def __init__(self, host, user, database, password):
        self.host = input("Introduce el host: ") #"localhost"
        self.user = input("Introduce el nombre del usuario con el que quieres conectar: ")#"usu_prueba"
        self.database = input("Introduce el nombre de la base de datos a la que conectarte: ")#"pruebas"
        self.password = input("Introduce la contraseña: ") #"prueba"
        self.conn = None
    
    def conectar(self):
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
    
    def terminar_conn(self):
        self.conn.close() #type: ignore
    
    # def query(self, query):
    #     self.conn.cursor().execute(query) #type: ignore
    
    # def return_cursor(self):
    #     return self.conn.cursor() #type: ignore

class ActionsInDB(DbConn):

    def insert(self):
        pass

    def delete(self):
        pass

    def update(self):
        pass

    def alter(self):
        pass