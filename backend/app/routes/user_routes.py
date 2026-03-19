from fastapi import APIRouter, HTTPException
from app.schemas.user_schema import UserCreate, UserResponse
from app.services.user_service import (
    create_user,
    get_all_users,
    get_user,
    update_user,
    delete_user
)

router = APIRouter()


@router.post("/users", response_model=UserResponse)
def create(user: UserCreate):
    return create_user(user)


@router.get("/users")
def get_all():
    return get_all_users()


@router.get("/users/{user_id}", response_model=UserResponse)
def get_single(user_id: str):
    user = get_user(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return {"id": user_id, **user}


@router.put("/users/{user_id}", response_model=UserResponse)
def update(user_id: str, user: UserCreate):
    updated = update_user(user_id, user)
    if not updated:
        raise HTTPException(status_code=404, detail="User not found")
    return updated


@router.delete("/users/{user_id}")
def delete(user_id: str):
    deleted = delete_user(user_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="User not found")
    return {"message": "User deleted successfully"}