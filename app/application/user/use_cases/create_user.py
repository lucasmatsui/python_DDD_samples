from app.domain.user.entities.user import User
from app.domain.user.email import Email
from app.application.user.dtos.input.create_user_input import CreateUserInput
from app.application.user.dtos.output.create_user_output import CreateUserOutput
from app.domain.user.repositories.user_repository import UserRepository

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
