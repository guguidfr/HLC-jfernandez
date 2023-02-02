"""
pip install pymysql --> Este parece que va bien
pip install mysqlclient
pip install mysql
"""
import pymysql

hostname = 'localhost'
username = 'root'
password = 'toor'
database = 'employees'
def query(conn):
    cur = conn.cursor()
    cur.execute("select emp_no, first_name from employees limit 20")

    for emp_no, first_name in cur.fetchall():
        print(emp_no, first_name)

py_conn = pymysql.connect(host=hostname, user=username, passwd=password, db=database)
query(py_conn)
py_conn.close()