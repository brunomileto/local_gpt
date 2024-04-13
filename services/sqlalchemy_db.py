from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy import create_engine
from models.base import Base
from models.user import User
from sqlalchemy.orm import sessionmaker
from services.interfaces.i_db import IDatabase
from utils.utils import Utils

# Define the database session
engine = create_engine('sqlite:///app.db')
Session = scoped_session(sessionmaker(bind=engine))

class SQLAlchemyDatabase(IDatabase):
    def __init__(self) -> None:
        Base.metadata.create_all(engine)
    
    def create_user(self, username, password) -> None:
        user = self.get_user(username=username)
        
        if user:
            return user
        
        with Session() as session:
            user = User(username=username, password=Utils.hash(password))
            session.add(user)
            session.commit()

    def authenticate_user(self, username, password) -> bool:
        with Session() as session:
            user = session.query(User).filter_by(username=username).first()
            if user and user.password == Utils.hash(password):
                return True
            return False

    def get_user(self, username) -> User:
        with Session() as session:
            user = session.query(User).filter_by(username=username).first()
            return user
