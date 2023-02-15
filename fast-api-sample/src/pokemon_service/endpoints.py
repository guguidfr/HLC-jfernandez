from pokemon_service.db import get_db
from pokemon_service.entity import Pokemon
from fastapi import APIRouter, HTTPException, status, Body

router = APIRouter()


@router.get("/pokemon")
def get_pokemons(pokemon_type = None):
    if pokemon_type:
        return get_db().find_by_type(pokemon_type)
    else:
        return get_db().get_all()


@router.get("/pokemon/{pokemon_id}")
def get_a_pokemon(pokemon_id):
    if poke := get_db().get_by_id(pokemon_id):
        return poke
    else:
        raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, 
                detail=f"Pokemon with ID {pokemon_id} doesn't exists")


@router.post("/pokemon", status_code=status.HTTP_201_CREATED)
def create_pokemon(pokemon = Body()):
    try:
        return get_db().save(Pokemon(pokemon.get("name"), pokemon.get("pkmn_type")))
    except Exception:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=f"Couldn't save new pokemon {pokemon}")


@router.put("/pokemon/{pokemon_id}")
def update_pokemon(pokemon_id, pokemon = Body()):
    try:
        return get_db().save(Pokemon(pokemon_id, pokemon["name"], pokemon["pkmn_type"]))
    except Exception:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, 
            detail=f"Couldn't update pokemon ID {pokemon_id} with {pokemon}")


@router.delete("/pokemon/{pokemon_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_pokemon(pokemon_id):
    try:
        get_db().delete(pokemon_id)
    except Exception:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Couldn't delete pokemon ID {pokemon_id}")
