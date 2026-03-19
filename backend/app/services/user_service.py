from uuid import uuid4
from typing import Dict
from fastapi import HTTPException
from app.schemas.user_schema import UserCreate


# In-memory database
users_db: Dict[str, dict] = {}


def create_user(user: UserCreate):
    # Check for duplicate email
    for existing_user in users_db.values():
        if existing_user["email"] == user.email:
            raise HTTPException(
                status_code=400,
                detail="Email already registered"
            )

    user_id = str(uuid4())
    users_db[user_id] = user.dict()
    return {"id": user_id, **user.dict()}


def get_all_users():
    return [{"id": uid, **data} for uid, data in users_db.items()]


def get_user(user_id: str):
    user = users_db.get(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return {"id": user_id, **user}


def update_user(user_id: str, user: UserCreate):
    if user_id not in users_db:
        raise HTTPException(status_code=404, detail="User not found")

    # Check for duplicate email (excluding current user)
    for uid, existing_user in users_db.items():
        if existing_user["email"] == user.email and uid != user_id:
            raise HTTPException(
                status_code=400,
                detail="Email already registered"
            )

    users_db[user_id] = user.dict()
    return {"id": user_id, **user.dict()}


def delete_user(user_id: str):
    if user_id not in users_db:
        raise HTTPException(status_code=404, detail="User not found")

    users_db.pop(user_id)
    return {"message": "User deleted successfully"}