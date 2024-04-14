from sqlalchemy.orm import Session
from typing import Type, List, Optional, Dict
from services.db.interfaces.i_db import IDatabase, Model


class SQLAlchemyDatabase(IDatabase):
  def __init__(self, session: Session):
    self._session = session

  def add(self, instance) -> None:
    self._session.add(instance)

  def commit(self) -> None:
    self._session.commit()

  def query_all(self, model: Type[Model]) -> List[Model]:
      return self._session.query(model).all()

  def get_by_id(self, model: Type[Model], id: int) -> Optional[Model]:
      return self._session.query(model).get(id)

  def delete(self, instance):
    self._session.delete(instance)

    def find_by(self, model: Type[Model], conditions: Dict[str, any]) -> List[Model]:
        query = self._session.query(model)
        for attr, value in conditions.items():
            query = query.filter(getattr(model, attr) == value)
        return query.all()