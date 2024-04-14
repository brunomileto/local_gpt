from enums.chat_roles import EnumChatRoles
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.ext.hybrid import hybrid_property
from sqlalchemy.orm import relationship
from models.base import Base

class GPT(Base):  
  __tablename__ = 'gpts'
  id = Column(Integer, primary_key=True)
  user_id = Column(Integer, ForeignKey('users.id'))
  _name = Column(String, nullable=False, name="name")
  _prompt = Column(String, nullable=False, name="prompt")  
  
  conversations = relationship("Conversation", back_populates="gpt", cascade="all, delete-orphan")
  user = relationship("User", back_populates="gpts")
  
  def __init__(self, name:str, prompt:str) -> None:
    self.name = name
    self.prompt = prompt
  
  @property
  def name(self) -> str:
    return self._name
  
  @name.setter
  def name(self, value:str) -> None:
    if not isinstance(value, str):
      raise ValueError("GPT name must be a string")
    self._name = value
  
  @property
  def prompt(self) -> str:
    return self._prompt
  
  @prompt.setter
  def prompt(self, value:str) -> None:
    if not isinstance(value, str):
      raise ValueError("GPT prompt must be a string")
    self._prompt = value
      