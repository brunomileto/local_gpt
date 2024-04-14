from abc import ABC, abstractmethod
from typing import Type, Generic, TypeVar, List, Optional, Dict

from models.base import Base

Model = TypeVar('Model', bound=Base)

class IDatabase(ABC, Generic[Model]):
    @abstractmethod
    def add(self, instance: Model) -> None:
        """Add an instance to the database."""
        pass

    @abstractmethod
    def commit(self) -> None:
        """Commit the current transaction."""
        pass
    
    @abstractmethod
    def query_all(self, model: Type[Model]) -> List[Model]:
        """Retrieve all instances of a model."""
        pass
    
    @abstractmethod
    def get_by_id(self, model: Type[Model], id: int) -> Optional[Model]:
        """Retrieve a single instance by its ID."""
        pass
    
    @abstractmethod
    def delete(self, instance: Model) -> None:
        """Delete an instance from the database."""
        pass

    @abstractmethod
    def find_by(self, model: Type[Model], conditions: Dict[str, any]) -> List[Model]:
        """Retrieve instances based on arbitrary conditions."""
        pass