from fastapi import FastAPI, HTTPException, status, Body
import objetos as obj
from uvicorn import run

app = FastAPI()

@app.get("/books")
def get_all(genre = None, author = None):
    if not genre and not author:
        return obj.get_all_as_objects()
    elif genre or author:
        return obj.get_by_genre_or_author(genre, author)
    else:
        raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, 
                detail="ERROR: No matches")

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

@app.post("/books", status_code=status.HTTP_201_CREATED)
def new_book(js = Body()):
    try:
        book = obj.js_to_book(js)
        book.add_book()
        return "New entry added successfully"
    except Exception:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="Error when trying to save the new book") 
    
@app.put("/books/{pk}")
def update_book(pk, js = Body()):
    try:
        book = obj.js_to_book(js)
        book.update_book(pk)
        return "Record updated"
    except Exception:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, 
            detail=f"Could not update book with id '{pk}' with '{js}'")

@app.delete("/books/{pk}", status_code=status.HTTP_204_NO_CONTENT)
def delte_book(pk):
    code = obj.delete_book(pk)
    if code == 0:
        return "Book deleted successfully"
    else:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"There is no book with id={pk}")

run(app, host="0.0.0.0", port=8000)