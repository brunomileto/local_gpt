from sqlalchemy import create_engine, Column, Integer, String

from models.base import Base

class User(Base):
  __tablename__ = 'users'
  
  id = Column(Integer, primary_key=True)
  username = Column(String, unique=True, nullable=False)
  password = Column(String, nullable=False)
  
