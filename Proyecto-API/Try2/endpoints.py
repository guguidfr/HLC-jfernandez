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
                detail=f"ERROR: No matches")

@app.get("/books/{pk}")
def get_by_pk(pk):
    if book := obj.get_by_pk(int(pk)):
        return book
    else:
        raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, 
                detail=f"Book with id {pk} does not exists")

def js_to_book(js):
    book = obj.Book(isbn=js["isbn"],titulo=js["title"],autor=js["author"],genero=js["genre"],fecha_salida=js["date"])
    return book

@app.post("/books", status_code=status.HTTP_201_CREATED)
def new_book(js = Body()):
    try:
        book = js_to_book(js)
        obj.add_book(book)
        return "New entry added successfully"
    except Exception:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=f"Error when trying to save the new entry") 
    
@app.put("/books/{pk}")
def update_book(pk, js = Body()):
    try:
        obj.update_book(pk,js)
        return "Record updated"
    except Exception:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, 
            detail=f"Couldn't update book with id '{pk}' with '{js}'")
    # except:
    #     return "F"

if __name__=="__main__":
    run(app, host="0.0.0.0", port=8000)