from pydantic import BaseModel, EmailStr


class Message(BaseModel):
    message: str


# requição
class UserSchema(BaseModel):
    username: str
    email: EmailStr
    password: str


# response
class UserPublic(BaseModel):
    username: str
    email: EmailStr
