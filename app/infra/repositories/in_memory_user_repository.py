from typing import Dict
from app.domain.user.entities.user import User
from app.domain.user.repositories.user_repository import UserRepository

class InMemoryUserRepository(UserRepository):
  def insert(self, user: User) -> User:
    return user
