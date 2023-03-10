from fastapi import FastAPI
from abc import abstractmethod
from modules import checking
import uvicorn
import pymysql
import pandas as pd
# import sys
# checking()

class DataBaseConn:
    def __init__(self):
        # self.credentials
        try:
            self.conn = pymysql.connect(host="localhost",user="usu_prueba",password="prueba",database="pruebas_python")
        except:
            self.error_code = 1
        else:
            self.error_code = 0
    
    @abstractmethod
    def get_all(): ...

    @abstractmethod
    def get_by_pk(): ...

    @abstractmethod
    def get_by_unique(): ...

    @abstractmethod
    def new_entry(): ...

    @abstractmethod
    def delete_entry(): ...

class DoQueryInDB(DataBaseConn):

    def get_all(self):
        get_all_query="SELECT * FROM LIBROS"
        df=pd.read_sql_query(get_all_query,self.conn) #type: ignore
        print(df)

    def get_by_pk(self):
        pass

    def get_by_unique(self):
        pass

    def new_entry(self):
        pass

    def delete_entry(self):
        pass

app = FastAPI()
@app.get("/")
def message():
    return "UP"

@app.on_event('startup')
def at_boot():
    db=DoQueryInDB()

@app.get("/all")
def output():
    return db.get_all

if __name__=="__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
    # try:
    #     conn = pymysql.connect(host="localhost",user="usu_prueba",password="prueba",database="api_python")
    # except:
    #     error_code = 1
    # else:
    #     error_code = 0

    # if error_code == 0:
    #     cursor = conn.cursor() #type: ignore
    #     try:
    #         cursor.execute("SELECT * FROM api_python.LIBROS")
    #     except:
    #         pass

