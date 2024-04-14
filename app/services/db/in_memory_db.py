from typing import Type, Generic, TypeVar, List, Optional, Dict

from services.db.interfaces.i_db import IDatabase, Model

class InMemoryDatabase(IDatabase[Model]):
    def __init__(self):
        self._data = {}
        self._committed = []

    def add(self, instance: Model) -> None:
        # Assuming all instances have a unique 'id' attribute
        self._data[instance.id] = instance

    def commit(self) -> None:
        # Simulate a database commit by snapshotting the current state
        self._committed.append(self._data.copy())

    def query_all(self, model: Type[Model]) -> List[Model]:
        # Return all instances of the model
        return [instance for instance in self._data.values() if isinstance(instance, model)]

    def get_by_id(self, model: Type[Model], id: int) -> Optional[Model]:
        # Retrieve a single instance by its ID
        return self._data.get(id, None) if any(isinstance(instance, model) for instance in self._data.values()) else None

    def delete(self, instance: Model) -> None:
        # Delete an instance based on its ID
        if instance.id in self._data:
            del self._data[instance.id]
            
    def find_by(self, model: Type[Model], conditions: Dict[str, any]) -> List[Model]:
        matched_instances: List[Model] = []    
        for instance in self._data.values():
            if not isinstance(instance, model):
                continue         
            matches = True
            for key, value in conditions.items():
                instance_value = getattr(instance, key, None)
                
                if instance_value != value:
                    matches = False
                    break    
            if matches:
                matched_instances.append(instance)
        
        return matched_instances