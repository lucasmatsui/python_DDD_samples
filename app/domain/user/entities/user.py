from uuid import UUID, uuid4
from app.domain.user.email import Email

class User:
  __id: UUID
  __email: Email

  def create_user(self, email: Email):
    self.__id = uuid4()
    self.__email = email

    return self

  def fill_user(self, id: UUID, email: Email):
    self.__id = id
    self.__email = email

    return self

  def get_id(self):
    return self.__id

  def get_email(self):
    return self.__email.value
