from abc import ABC, abstractmethod

class IDatabase(ABC):
    @abstractmethod
    def create_user(self, username, password):
        pass

    @abstractmethod
    def authenticate_user(self, username, password):
        pass

    @abstractmethod
    def get_user(self, username):
        pass
