from fastapi import FastAPI
import objetos as obj
import pymysql
import pandas as pd
import uvicorn

app = FastAPI()

@app.get("/books")
def get_all(genre = None):
    if not genre:
        return obj.get_all_as_objects()
    else:
        return obj.get_by_genre(genre)

@app.get("/books/{pk}")
def get_by_pk(pk):
    return obj.get_by_pk(pk)

@app.get("/")
def message():
    return "UP"

if __name__=="__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)