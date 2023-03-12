from pokemon_service.entity import PokemonRepository, MemPokemonRepository

db = MemPokemonRepository()

def get_db()-> PokemonRepository:
    return db
