from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from models.base import Base

class User(Base):
  __tablename__ = 'users'
  
  id = Column(Integer, primary_key=True)
  username = Column(String, unique=True, nullable=False)
  password = Column(String, nullable=False)
  conversations = relationship("Conversation", back_populates="user")  # Link to Conversations
  messages = relationship("ChatMessage", back_populates="user")  # Existing link to Messages

  
