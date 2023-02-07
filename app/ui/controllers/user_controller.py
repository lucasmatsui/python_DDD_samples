from fastapi import FastAPI, Request
from app.application.user.create_user.create_user import CreateUser
from app.application.user.create_user.create_user_input import CreateUserInput
from app.application.user.create_user.create_user_output import CreateUserOutput
from app.domain.model.user.invalid_email_error import InvalidEmailError
from app.infra.repositories.mysql_user_repository import MysqlUserRepository
from app.infra.utils.response_error import response_error

def user_controller(app: FastAPI):
  @app.post("/users",  response_model=None)
  async def create(request: Request) -> CreateUserOutput:
    try:
      body = await request.json()

      create_user = CreateUser(
        MysqlUserRepository()
      )

      return create_user.execute(
        CreateUserInput(body.get("email"))
      )
    except InvalidEmailError as aee:
      return response_error(aee.message, aee.status_code)
    except Exception as e:
      return response_error("Unexpected error, try again later.", 500)
