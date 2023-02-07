import abc

from app.domain.model.user.user import User

class UserRepository:
  @abc.abstractmethod
  def insert(self, user: User) -> User:
    pass
