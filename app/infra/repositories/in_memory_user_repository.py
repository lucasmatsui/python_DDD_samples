from app.domain.model.user.user import User
from app.domain.model.user.user_repository import UserRepository


class InMemoryUserRepository(UserRepository):
  def insert(self, user: User) -> User:
    return user
