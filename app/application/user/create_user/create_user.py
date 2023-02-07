from app.domain.model.user.user import User
from app.domain.model.user.email import Email
from app.domain.model.user.user_repository import UserRepository
from app.application.user.create_user.create_user_input import CreateUserInput
from app.application.user.create_user.create_user_output import CreateUserOutput

class CreateUser:
  user_repository: UserRepository

  def __init__(self, user_repository: UserRepository) -> None:
    self.user_repository = user_repository

  def execute(self, input: CreateUserInput) -> CreateUserOutput:
    user = User().create_user(
      Email(input.email)
    )

    inserted_user: User = self.user_repository.insert(user)

    return CreateUserOutput(
      inserted_user.get_id(),
      inserted_user.get_email()
    )
