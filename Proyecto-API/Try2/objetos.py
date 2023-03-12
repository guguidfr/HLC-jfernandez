import pymysql
import pandas as pd
import sys

try:
    conn = pymysql.connect(host="localhost",user="usu_prueba",password="prueba",database="pruebas_python")
except:
    sys.exit(1)


"""
Función que permite pasar de un json (o diccionario) a un objeto de la clase 'Book'.
Se usa sobre todo para añadir un libro nuevo.
"""
def js_to_book(js):
    book = Book(
        id=0 if "id" not in js else js["id"],
        isbn=None if "isbn" not in js else js["isbn"],
        titulo=None if "title" not in js else js["title"],
        autor=None if "author" not in js else js["author"],
        genero=None if "genre" not in js else js["genre"],
        fecha_salida=None if "date" not in js else js["date"]
    )
    return book

class Book:

    """
    __init__ de la clase 'Book': tiene los mismos atributos que columnas tiene la tabla
    El "id" por defecto es 'None' porque es autoincremental en la tabla
    """
    def __init__(self,isbn,titulo,autor,genero,fecha_salida,id=None):
        self.id = id
        self.isbn = isbn
        self.title = titulo
        self.author = autor
        self.genre = genero
        self.date = fecha_salida
    
    """
    Método que se usará para modificar el objeto nuevo que se crea para hacer el 'UPDATE' en la tabla.
    Se pasan 2 libros: el nuevo con los datos que ha pasado el usuario, y el que está ya en la tabla.
    Si alguno de los valores del 'libro nuevo' es 'None' (lo que significa que el usuario no quiere cambiar ese valor), tomará el valor que ya hay en la tabla.
    """
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

    """
    Recibe un libro y lo inserta en la base de datos
    """
    def add_book(self):
        query=f'INSERT INTO LIBROS VALUES ("{self.id}","{self.isbn}", "{self.title}", "{self.author}", "{self.genre}", "{self.date}")'
        cursor = conn.cursor()
        cursor.execute(query)
        conn.commit()
    
    """
    Recibe un diccionario con la información que pasa el usuario; obtiene el objeto de la tabla correspondiente al id que ha elegido el usuario
    Compara ambos objetos: si alguno de los campos del libro que se ha creado con la información del usuario está vacío, se completa con los valores que ya había en el objeto antes de actualizarlo
    """
    def update_book(self,pk):
        old_book = get_by_pk(pk)[0]
        self.fill_none_values(old_book)
        query = f'UPDATE LIBROS SET ISBN = "{self.isbn}", Titulo = "{self.title}", Autor = "{self.author}", Genero = "{self.genre}", Fecha_salida = "{self.date}" WHERE id = {int(pk)}'
        cursor = conn.cursor()
        cursor.execute(query)
        conn.commit()


"""
Obtiene toda la información de los libros de la tabla, los transforma de json a objeto y los añade a una lista, y devuelve ésta
"""
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

"""
Usa la lista de todos los libros y filtra por género y/o autor
"""
def get_by_genre_or_author(genre = None, author = None):
    books = get_all_as_objects()
    if genre:
        books = [book for book in books if book.genre == genre]
    if author:
        books = [book for book in books if book.author == author]
    return books

"""
Lo mismo que filtrar por género o autor, pero lo hace por id
"""
def get_by_pk(pk):
    return [book for book in get_all_as_objects() if book.id == int(pk)]

"""
Lo mismo que buscar por id, pero con el isbn
"""
def get_by_isbn(isbn):
    return [book for book in get_all_as_objects() if book.isbn == isbn]

"""
Recibe el id de un libro y lo borra
Si se borra una fila se devuelve 0, y si no se ha borrado nada devuelve 1
"""
def delete_book(pk):
    query=f"DELETE FROM LIBROS WHERE id = {int(pk)}"
    cursor = conn.cursor()
    cursor.execute(query)
    conn.commit()

    if cursor.rowcount == 0:
        return 1
        # No se ha borrado ninguna fila -> No se ha encontrado
    else:
        return 0
        # Se ha borrado la fila correcamente

