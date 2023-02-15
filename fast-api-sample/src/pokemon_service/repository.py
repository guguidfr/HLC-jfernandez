from abc import abstractmethod
from uuid import uuid4


class Entity:
    def __init__(self, entity_id = None):
        self.entity_id = entity_id or str(uuid4())


class Repository:
    @abstractmethod
    def get_all(self): ...

    @abstractmethod
    def get_by_id(self, id): ...

    @abstractmethod
    def save(self, entity): ...

    @abstractmethod
    def delete(self, id): ...


class MemRepository:
    _data = {}

    def __init__(self, init_data = None):
        if init_data:
            self._data.update(init_data)
    
    def get_all(self):
        return list(self._data.values())

    def get_by_id(self, id):
        return self._data.get(id)

    def save(self, entity):
        if entity.entity_id is None:
            entity.entity_id = str(uuid4)
        self._data[entity.entity_id] = entity
        return entity

    def delete(self, id):
        try:
            return self._data.pop(id) if id else None
        except KeyError:
            return None
