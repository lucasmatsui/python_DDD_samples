from app.domain.model.user.invalid_email_error import InvalidEmailError

class Email:
  value: str

  def __init__(self, value: str) -> None:
    if type(value) != str:
      raise InvalidEmailError("The field email must be a string")

    if not "@" in value:
      raise InvalidEmailError("Invalid email address: %s" % value)

    self.value = value
