import pymysql
import pandas as pd

class Book:

    def __init__(self,isbn,titulo,autor,genero,fecha_salida,id=None):
        self.id = id
        self.isbn = isbn
        self.title = titulo
        self.author = autor
        self.genre = genero
        self.date = fecha_salida

conn = pymysql.connect(host="localhost",user="usu_prueba",password="prueba",database="pruebas_python")

def get_all_as_objects():
    books_tuple = []
    query = "SELECT * FROM LIBROS"
    frame = pd.read_sql_query(query,conn) #type: ignore
    js=frame.to_dict('records')
    for book in js:
        obj_book = Book(book["id"],book["ISBN"],book["Titulo"],book["Autor"],book["Genero"],book["Fecha_salida"])
        books_tuple.append(obj_book)
    return books_tuple

def get_by_genre_or_author(genre = None, author = None):
    books = get_all_as_objects()
    if genre:
        books = [book for book in books if book.genre == genre]
    if author:
        books = [book for book in books if book.author == author]
    return books

def get_by_pk(pk):
    return [book for book in get_all_as_objects() if book.id == pk]

def add_book(book):
    query=f"INSERT INTO LIBROS (ISBN,Titulo,Autor,Genero,Fecha_salida) VALUES (\"{book.isbn}\", \"{book.title}\", \"{book.author}\", \"{book.genre}\", \"{book.date}\")"
    cursor = conn.cursor()
    cursor.execute(query)
    conn.commit()

def update_book(pk, book):
    new_values = pd.DataFrame(book,index=[0])
    table_old_data = pd.read_sql_query(f"SELECT * FROM LIBROS WHERE id = {pk}",conn) #type: ignore
    # new_values = new_values.drop(columns="id")
    new_values.update(table_old_data)
    new_values.to_sql('LIBROS',conn,if_exists="replace",index=True) #type: ignore
    '''
    new_values = pd.DataFrame.from_dict(book)
    table_old_data = pd.read_sql_query(f"SELECT * FROM LIBROS WHERE id = {pk}",conn) #type: ignore
    new_values = new_values.set_index("id")
    table_old_data = table_old_data.set_index("id")
    updated_data = new_values.combine_first(table_old_data)
    # new_values.to_sql('LIBROS',conn,if_exists="replace",index=False) #type: ignore
    updated_data.reset_index().to_sql('LIBROS',conn,if_exists="replace",index=False) #type: ignore
    '''
    """
    Posible solución:
        - Obtener el registro antes de cambiarlo
        - Comparar el antes y el después
        - Cambiar los registros del antes que son diferentes y cambiarlo a los valores nuevos
        - Hacer un update al completo, así el usuario puede cambiar todos los campos que quiera del registro (menos el id, que es autoincremental)
    """

datos = {"isbn":"2222222222222","title":"Prueba 2","author":"Tú"}
update_book(32,datos)