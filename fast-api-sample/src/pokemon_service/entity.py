from abc import abstractmethod
from pokemon_service.repository import Entity, Repository, MemRepository


class Pokemon(Entity):
    def __init__(self, name, pkmn_type, id = None):
        super().__init__(id)
        self.name = name
        self.pkmn_type = pkmn_type

class PokemonRepository(Repository):
    @abstractmethod
    def find_by_type(self, pkmn_type):
        # La línea sigueinte equivale a pass, o return None
        ...

class MemPokemonRepository(MemRepository):
    def __init__(self):
        super().__init__()
    
    def find_by_type(self, pkmn_type):
        return [pkmn for pkmn in self.get_all() if pkmn.pkmn_type == pkmn_type]
