import pymysql
import json
import pandas as pd
conn = pymysql.connect(host="localhost",user="usu_prueba",password="prueba",database="pruebas_python")
query = "SELECT * FROM LIBROS"
# cur = conn.cursor()
# cur.execute(query)
# salida = cur.fetchall()
# for i in salida:
#     print(i)
frame = pd.read_sql_query(query,conn) #type: ignore
# print(frame)
# for i in frame:
#     print(i)
js=frame.to_dict('records')
print(js) # -> Tipo 'lista'
# for i in js:
#     print(type(i)) # -> Tipo 'diccionario'