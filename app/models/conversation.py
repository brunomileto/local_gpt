from enums.chat_roles import EnumChatRoles
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.ext.hybrid import hybrid_property
from sqlalchemy.orm import relationship
from models.base import Base

class Conversation(Base):
  __tablename__ = 'conversations'

  id = Column(Integer, primary_key=True)
  user_id = Column(Integer, ForeignKey('users.id'))  # Reference to the user
  gpt_id = Column(Integer, ForeignKey('gpts.id'), nullable=True)
  
  # Relationships
  user = relationship("User", back_populates="conversations")  # Link to User
  messages = relationship("ChatMessage", back_populates="conversation", cascade="all, delete-orphan")
  gpt = relationship("GPT", back_populates="conversations")
