from services.db.interfaces.i_db import IDatabase
from typing import List
from models.gpt import GPT

class GPTDbService:
    def __init__(self, db_session: IDatabase[GPT]) -> None:
        self.db = db_session

    def create_gpt(self, name: str, prompt: str, user_id: int) -> GPT:
        """Create a new GPT instance and add it to the database."""
        new_gpt = GPT(name=name, prompt=prompt, user_id=user_id)
        self.db.add(new_gpt)
        self.db.commit()
        return new_gpt

    def get_gpt_by_id(self, gpt_id: int) -> GPT | None:
        """Retrieve a GPT instance by its ID."""
        return self.db.get_by_id(GPT, gpt_id)

    def get_all_gpts(self) -> list[GPT]:
        """Retrieve all GPT instances."""
        return self.db.query_all(GPT)

    def update_gpt(self, gpt_id: int, **kwargs) -> GPT:
        """Update a GPT instance's attributes given by keyword arguments."""
        gpt = self.get_gpt_by_id(gpt_id)
        if gpt:
            for key, value in kwargs.items():
                if hasattr(gpt, key):
                    setattr(gpt, key, value)
            self.db.commit()
        return gpt

    def delete_gpt(self, gpt_id: int) -> None:
        """Delete a GPT instance from the database."""
        gpt = self.get_gpt_by_id(gpt_id)
        if gpt:
            self.db.delete(gpt)
