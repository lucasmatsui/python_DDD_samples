import abc
from app.domain.user.entities.user import User

class UserRepository:
  @abc.abstractmethod
  def insert(self, user: User) -> User:
    pass
