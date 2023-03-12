import uvicorn
from fastapi import FastAPI
from pokemon_service.endpoints import router, get_db, Pokemon
from pokemon_service.utils import load_from_file


app = FastAPI()

app.include_router(router)

@app.get("/")
def get_root():
    return "Hello World"

@app.get("/health")
def health_check():
    return "OK"

@app.get("/greeting")
def get_greeting():
    return "Aló presidente"

@app.on_event("startup")
def startup_event():
    for pkmn_dict in load_from_file():
        get_db().save(Pokemon(
            name=pkmn_dict.get("name"), 
            pkmn_type=pkmn_dict.get("type_1"),
            id=pkmn_dict.get("number")))


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=5000)
