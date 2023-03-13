from fastapi import FastAPI, HTTPException, status, Body
import objetos as obj
from uvicorn import run

app = FastAPI()

'''
Obtener todos los libros, o busca si se ha recibido algún parámetros mediante '?[campo]=[valor]'
'''
@app.get("/books")
def get_all(genre = None, author = None):
    if not genre and not author: # Si no se recibe ninguno, se muestran todos
        return obj.get_all_as_objects()
    elif genre or author: # Si se recibe alguno, se filtra
        return obj.get_by_genre_or_author(genre, author)
    else:
        raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, 
                detail="No matches") # Si no hay coincidencias, se devuelve el error 404

'''
Se pasa un valor mediante la url. Si tiene exactamente 13 caracteres, se busca por ISBN.
En cualquier otro caso se busca por id.
Si no hay coincidencias se devuelve el error 404
'''
@app.get("/books/{value}")
def get_by_pk_or_isbn(value):
    if len(value) == 13:
        if book := obj.get_by_isbn(value):
            print(book)
            return book
        else:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, 
                detail=f"Book with isbn={value} does not exists")
    else:
        if book := obj.get_by_pk(value):
            return book
        else:
            raise HTTPException(
                    status_code=status.HTTP_404_NOT_FOUND, 
                    detail=f"Book with id={value} does not exists")

'''
Se recibe información en formato json, se transforma a objeto y se hace el insert con sus datos.
En caso de que falte alguno de los campos necesarios, se devolverá un error.
'''
@app.post("/books", status_code=status.HTTP_201_CREATED)
def new_book(js = Body()):
    try:
        book = obj.js_to_book(js)
        book.add_book()
        return "New entry added successfully"
    except Exception:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="Error when trying to save the new book") 

'''
Lo mismo que al hacer el post, pero se debe de elegir un libro mediante la url.
Si no se pasan algunos de los campos del libro, no se modificarán.
'''    
@app.put("/books/{pk}")
def update_book(pk, js = Body()):
    try:
        book = obj.js_to_book(js)
        book.update_book(pk)
        # return "Record updated"
        return book
    except Exception:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, 
            detail=f"Could not update book with id '{pk}' with '{js}'")
'''
Se elige un libro mediante url.
Se hace un delete a esa id; si se ha borrado correctamente, se muestra un mensaje; en el caso de no haber borrado nada (porque no existe ese libro), se devuelve el error 404
'''
@app.delete("/books/{pk}")
def delte_book(pk):
    code = obj.delete_book(pk)
    if code == 0:
        return "Book deleted successfully"
    else:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"There is no book with id={pk}")

run(app, host="0.0.0.0", port=8000)