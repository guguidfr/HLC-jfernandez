import pymysql
import pandas as pd
class Book:

    def __init__(self,id,isbn,titulo,autor,genero,fecha_salida):
        self.id = id
        self.ISBN = isbn
        self.title = titulo
        self.author = autor
        self.genre = genero
        self.date = fecha_salida
    
    def __str__(self):
        return f"{self.id}, {self.title}"

def get_all_as_objects():
    books_tuple = []
    conn = pymysql.connect(host="localhost",user="usu_prueba",password="prueba",database="pruebas_python")
    query = "SELECT * FROM LIBROS"
    frame = pd.read_sql_query(query,conn) #type: ignore
    js=frame.to_dict('records')
    for book in js:
        obj_book = Book(book["id"],book["ISBN"],book["Titulo"],book["Autor"],book["Genero"],book["Fecha_salida"])
        books_tuple.append(obj_book)
    return books_tuple

def get_by_genre(genre):
    return [book for book in get_all_as_objects() if book.genre == genre]

def get_by_pk(pk):
    for book in get_all_as_objects():
        if book.id == pk:
            return book
        
libro = get_by_pk(1)
print(libro)