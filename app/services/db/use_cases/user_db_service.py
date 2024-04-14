from services.db.interfaces.i_db import IDatabase
from models.user import User

class UserDbService:
    def __init__(self, db_session: IDatabase[User]) -> None:
        self.db = db_session
  
    def create_user(self, username: str, password: str) -> User:
        """Create a new user and add to the database."""
        new_user = User(username=username, password=password)
        self.db.add(new_user)
        self.db.commit()
        return new_user

    def get_user_by_id(self, user_id: int) -> User | None:
        """Retrieve a user by their ID."""
        return self.db.get_by_id(User, user_id)

    def get_user_by_username(self, username: str) -> User | None:
        """Retrieve a user by their username."""
        # Implementing this requires a custom method in the IDatabase interface or using a query method that supports filtering by non-ID fields.
        return self.db.get_by_username(User, username)

    def update_user(self, user_id: int, **kwargs) -> User:
        """Update a user's attributes given by keyword arguments."""
        user = self.get_user_by_id(user_id)
        if user:
            for key, value in kwargs.items():
                setattr(user, key, value)
            self.db.commit()
        return user

    def delete_user(self, user_id: int) -> None:
        """Delete a user from the database."""
        user = self.get_user_by_id(user_id)
        if user:
            self.db.delete(user)
            self.db.commit()
