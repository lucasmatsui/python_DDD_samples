from uuid import UUID, uuid4

from app.domain.model.user.email import Email

class User:
  __id: UUID
  __email: Email

  def __init__(self, id: UUID, email: Email) -> None:
    self.__id = id
    self.__email = email
    
  @staticmethod
  def create_user(email: Email):
    id = uuid4()

    return User(id, email)

  def change_email(self, email: Email):
    self.__email = email

  def get_id(self):
    return self.__id

  def get_email(self):
    return self.__email.value
