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
    
    def fill_none_values(self, other_book):
        if self.isbn is None:
            self.isbn = other_book.isbn
        if self.title is None:
            self.title = other_book.title
        if self.author is None:
            self.author = other_book.author
        if self.genre is None:
            self.genre = other_book.genre
        if self.date is None:
            self.date = other_book.date

conn = pymysql.connect(host="localhost",user="usu_prueba",password="prueba",database="pruebas_python")

def js_to_book(js):
    # book = Book(isbn=js["isbn"],titulo=js["title"],autor=js["author"],genero=js["genre"],fecha_salida=js["date"])
    book = Book(
        isbn=None if "isbn" not in js else js["isbn"],
        titulo=None if "title" not in js else js["title"],
        autor=None if "author" not in js else js["author"],
        genero=None if "genre" not in js else js["genre"],
        fecha_salida=None if "date" not in js else js["date"]
    )
    return book

def get_all_as_objects():
    books_tuple = []
    query = "SELECT * FROM LIBROS"
    frame = pd.read_sql_query(query,conn) #type: ignore
    js=frame.to_dict('records')
    for book in js:

        obj_book = Book(
            id=book["id"],
            isbn=book["ISBN"],
            titulo=book["Titulo"],
            autor=book["Autor"],
            genero=book["Genero"],
            fecha_salida=book["Fecha_salida"])
        
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
    # bookshelf = get_all_as_objects()
    
    # for book in bookshelf:
    #     if book.id == int(pk):
    #         target = book
    
    # return target
    return [book for book in get_all_as_objects() if book.id == int(pk)]

def add_book(book):
    query=f"INSERT INTO LIBROS (ISBN,Titulo,Autor,Genero,Fecha_salida) VALUES (\"{book.isbn}\", \"{book.title}\", \"{book.author}\", \"{book.genre}\", \"{book.date}\")"
    cursor = conn.cursor()
    cursor.execute(query)
    conn.commit()

def update_book(pk, new_data):
    new_book = js_to_book(new_data)
    old_book = get_by_pk(pk)[0]
    new_book.fill_none_values(old_book)
    query = f'UPDATE LIBROS SET  ISBN = "{new_book.isbn}", Titulo = "{new_book.title}", Autor = "{new_book.author}", Genero = "{new_book.genre}", Fecha_salida = "{new_book.date}" WHERE id = {int(pk)}'
    cursor = conn.cursor()
    cursor.execute(query)
    conn.commit()
