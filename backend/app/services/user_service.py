from sqlalchemy.orm import Session
from fastapi import HTTPException
from uuid import uuid4

from app.models.user_model import User
from app.schemas.user_schema import UserCreate


def create_user(db: Session, user: UserCreate):
    # Check duplicate email
    existing_user = db.query(User).filter(User.email == user.email).first()
    if existing_user:
        raise HTTPException(
            status_code=400,
            detail="Email already registered"
        )

    new_user = User(
        id=str(uuid4()),
        name=user.name,
        email=user.email,
        age=user.age,
        password=user.password,   # FIXED
        role=user.role            # FIXED
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user


def get_all_users(db: Session):
    return db.query(User).all()


def get_user(db: Session, user_id: str):
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user


def update_user(db: Session, user_id: str, user: UserCreate):
    existing_user = db.query(User).filter(User.id == user_id).first()
    if not existing_user:
        raise HTTPException(status_code=404, detail="User not found")

    # Check duplicate email (excluding current user)
    email_check = db.query(User).filter(User.email == user.email).first()
    if email_check and email_check.id != user_id:
        raise HTTPException(
            status_code=400,
            detail="Email already registered"
        )

    existing_user.name = user.name
    existing_user.email = user.email
    existing_user.age = user.age
    existing_user.password = user.password   # FIXED
    existing_user.role = user.role           # FIXED

    db.commit()
    db.refresh(existing_user)

    return existing_user


def delete_user(db: Session, user_id: str):
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    db.delete(user)
    db.commit()

    return {"message": "User deleted successfully"}