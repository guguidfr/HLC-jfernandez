import mariadb
import sys

# Connect to MariaDB Platform
try:
   conn = mariadb.connect(
       user="root",
       password="mi_contraseña",
       host="172.26.0.15",
       port=3306,
       database="pruebas_py"


   )
except mariadb.Error as e:
   print(f"Error al conectar: {e}")
   sys.exit(1)


# Get Cursor
cur = conn.cursor() # type: ignore
cur.execute("select * from alumnos")
for id, nombre, apellidos, email in cur:
   print(f"Id: {id}, Nombre: {nombre}, Apellidos: {apellidos}, Email: {email}")


try:
   cur.execute("insert into alumnos(nombre, apellidos, email) values('Misco', 'Jones33', 'micorreo@yo.com')")
except mariadb.Error as e:
   print(f"Error: {e}")
conn.commit() # type: ignore
conn.close() # type: ignore