from pydantic import BaseModel, EmailStr
from uuid import UUID


class UserCreate(BaseModel):
    name: str
    email: EmailStr
    age: int


class UserResponse(UserCreate):
    id: UUID