from services.db.interfaces.i_db import IDatabase
from models.chat_message import ChatMessage
from enums.chat_roles import EnumChatRoles
from typing import List

class ChatMessageDbService:
    def __init__(self, db_session: IDatabase[ChatMessage]) -> None:
        self.db = db_session

    def create_message(self, role: EnumChatRoles, content: str, user_id: int, conversation_id: int) -> ChatMessage:
        """Create a new ChatMessage and add it to the database."""
        new_message = ChatMessage(role=role, content=content, user_id=user_id, conversation_id=conversation_id)
        self.db.add(new_message)
        self.db.commit()
        return new_message

    def get_message_by_id(self, message_id: int) -> ChatMessage | None:
        """Retrieve a ChatMessage by its ID."""
        return self.db.get_by_id(ChatMessage, message_id)

    def get_messages_by_conversation_id(self, conversation_id: int) -> List[ChatMessage]:
        """Retrieve all messages for a specific conversation."""
        return self.db.find_by(ChatMessage, {'conversation_id': conversation_id})

    def update_message(self, message_id: int, **kwargs) -> ChatMessage:
        """Update a ChatMessage's attributes given by keyword arguments."""
        message = self.get_message_by_id(message_id)
        if message:
            for key, value in kwargs.items():
                if hasattr(message, key):
                    setattr(message, key, value)
            self.db.commit()
        return message

    def delete_message(self, message_id: int) -> None:
        """Delete a ChatMessage from the database."""
        message = self.get_message_by_id(message_id)
        if message:
            self.db.delete(message)
            self.db.commit()
