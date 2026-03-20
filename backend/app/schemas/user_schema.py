from pydantic import BaseModel, EmailStr
from uuid import UUID


class UserCreate(BaseModel):
    name: str
    email: EmailStr
    age: int
    password: str
    role: str = "customer"


class UserResponse(BaseModel):
    id: UUID
    name: str
    email: EmailStr
    age: int
    role: str