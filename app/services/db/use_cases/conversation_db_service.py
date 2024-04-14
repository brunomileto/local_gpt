from services.db.interfaces.i_db import IDatabase
from models.conversation import Conversation

class ConversationDbService:
    def __init__(self, db_session: IDatabase[Conversation]) -> None:
        self.db = db_session

    def create_conversation(self, user_id: int, gpt_id: int = None) -> Conversation:
        """Create a new conversation and add it to the database."""
        new_conversation = Conversation(user_id=user_id, gpt_id=gpt_id)
        self.db.add(new_conversation)
        self.db.commit()
        return new_conversation

    def get_conversation_by_id(self, conversation_id: int) -> Conversation | None:
        """Retrieve a conversation by its ID."""
        return self.db.get_by_id(Conversation, conversation_id)

    def update_conversation(self, conversation_id: int, **kwargs) -> Conversation:
        """Update a conversation's attributes given by keyword arguments."""
        conversation = self.get_conversation_by_id(conversation_id)
        if conversation:
            for key, value in kwargs.items():
                if hasattr(conversation, key):
                    setattr(conversation, key, value)
            self.db.commit()
        return conversation

    def delete_conversation(self, conversation_id: int) -> None:
        """Delete a conversation from the database."""
        conversation = self.get_conversation_by_id(conversation_id)
        if conversation:
            self.db.delete(conversation)
            self.db.commit()
