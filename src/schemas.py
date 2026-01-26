from pydantic import BaseModel, EmailStr


class Message(BaseModel):
    message: str


# requição
class UserSchema(BaseModel):
    username: str
    email: EmailStr
    password: str


class UserDB(UserSchema):
    id: int


# response
class UserPublic(BaseModel):
    id: int
    username: str
    email: EmailStr
