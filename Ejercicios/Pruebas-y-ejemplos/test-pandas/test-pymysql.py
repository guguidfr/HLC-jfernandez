import pandas as pd
import pymysql

conn = pymysql.connect(host="localhost",user="usu_prueba",password="prueba",database="pruebas_python")
df = pd.read_sql_query("SELECT * FROM LIBROS", conn) #type: ignore
print(df)