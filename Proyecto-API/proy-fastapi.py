from fastapi import FastAPI
from abc import abstractmethod
from modules import checking
import uvicorn
import pymysql
# import sys
checking()

class DataBaseConn:
    def __init__(self):
        try:
            self.conn = pymysql.connect(host="localhost",user="usu_prueba",password="prueba",database="api_python")
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

    def get_all():
        pass

    def get_by_pk():
        pass

    def get_by_unique():
        pass

    def new_entry():
        pass

    def delete_entry():
        pass

app = FastAPI()
@app.get("/")
def message():
    return "UP"


if __name__=="__proy-fastapy__":
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
