import mariadb
import sys

class DbConn:
    def __init__(self):
        self.host = "172.26.0.15"
        self.port = 3306
        self.user = "py_user"
        self.database = "pruebas_py"
        self.password = "python"
        self.conn = None
    
    def conectar(self):
        try:
            self.conn=mariadb.connect(
                user=self.user,
                password=self.password,
                host=self.host,
                port=self.port, 
                database=self.database
            )
        except mariadb.Error as db_e:
            print(f"Error al conectar a la base de datos: {db_e}")
            sys.exit(1)
        else:
            print("Conexión establecida.")
    
    def terminar_conn(self):
        self.conn.close() #type: ignore
    
    def query(self)