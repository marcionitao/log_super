from pydantic import BaseModel, ConfigDict, EmailStr


class Message(BaseModel):
    message: str


# requição
class UserSchema(BaseModel):
    username: str
    email: EmailStr
    password: str


# response
class UserPublic(BaseModel):
    id: int
    username: str
    email: EmailStr
    model_config = ConfigDict(from_attributes=True)


# ConfigDict(from_attributes=True) - habilita a conversão automática de atributos de objetos (como instâncias de modelos de banco de dados) para campos do modelo Pydantic.˚


# response List -> retorna uma lista de objetos sem password
class UserList(BaseModel):
    users: list[UserPublic]
