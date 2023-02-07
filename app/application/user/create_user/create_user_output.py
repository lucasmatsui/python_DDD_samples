from uuid import UUID

class CreateUserOutput:
  id: UUID
  email: str

  def __init__(self, id: UUID, email: str):
    self.id = id
    self.email = email
