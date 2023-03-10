import pandas as pd
import sqlalchemy

# Definir la conexión a la base de datos
url="mysql+mysqlconnector://usu_prueba:prueba@localhost:3306/pruebas_python"
# Pasarle a sqlalchemy la conexión
engine=sqlalchemy.create_engine(url)

sql = "SELECT * FROM LIBROS"
with engine.connect() as conn:
    query=conn.execute(sql)
df = pd.DataFrame(query.fetchall())

# conn = pymysql.connect(host="localhost",user="usu_prueba",password="prueba",database="pruebas_python")
# df = pd.read_sql_query("SELECT * FROM LIBROS", conn) #type: ignore
# print(df)