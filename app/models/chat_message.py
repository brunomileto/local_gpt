from enums.chat_roles import EnumChatRoles
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.ext.hybrid import hybrid_property
from sqlalchemy.orm import relationship
from models.base import Base

class ChatMessage(Base):
    __tablename__ = 'chat_messages'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    conversation_id = Column(Integer, ForeignKey('conversations.id'))  # New foreign key

    _content = Column(String, nullable=False, name="content")
    _role = Column(String, nullable=False, name="role")  # Store the role as a string

    # Relationship to User
    user = relationship("User", back_populates="messages")
    conversation = relationship("Conversation", back_populates="messages")  # Link to Conversation

    def __init__(self, role: EnumChatRoles, content: str, user_id:int) -> None:
        self.role = role
        self.content = content
        self.user_id = user_id
    
    @hybrid_property
    def role(self) -> EnumChatRoles:
        """Getter for the role property, returning Enum."""
        return EnumChatRoles[self._role]

    @role.setter
    def role(self, value: EnumChatRoles) -> None:
        """Setter for the role property with validation."""
        if not isinstance(value, EnumChatRoles):
            raise ValueError("Role must be a EnumChatRoles instance.")
        self._role = value.name  # Store the enum name as a string

    @hybrid_property
    def content(self) -> str:
        """Getter for the content property."""
        return self._content

    @content.setter
    def content(self, value: str) -> None:
        """Setter for the content property with basic validation."""
        if not isinstance(value, str):
            raise ValueError("Content must be a string.")
        self._content = value

    def __repr__(self) -> str:
        """String representation of the Message object for debugging."""
        return f"Message(role='{self._role.value}', content='{self._content}')"
    
    def to_dict(self) -> dict:
        return {'role': self.role.value.lower(), 'content': self.content}
