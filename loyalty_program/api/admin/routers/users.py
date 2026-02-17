from fastapi import APIRouter, Depends, HTTPException
from typing import List
from schemas.user import UserCreate, UserUpdate, UserOut
from repositories.user import UserRepository
from database.session import get_db
from sqlalchemy.orm import Session

router = APIRouter()

@router.get("/", response_model=List[UserOut])
def get_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    """
    Получение списка пользователей
    """
    user_repo = UserRepository(db)
    users = user_repo.get_users(skip=skip, limit=limit)
    return users

@router.get("/{user_id}", response_model=UserOut)
def get_user(user_id: int, db: Session = Depends(get_db)):
    """
    Получение пользователя по ID
    """
    user_repo = UserRepository(db)
    user = user_repo.get_user_by_id(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@router.post("/", response_model=UserOut)
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    """
    Создание нового пользователя
    """
    user_repo = UserRepository(db)
    db_user = user_repo.create_user(user)
    return db_user

@router.put("/{user_id}", response_model=UserOut)
def update_user(user_id: int, user_update: UserUpdate, db: Session = Depends(get_db)):
    """
    Обновление пользователя
    """
    user_repo = UserRepository(db)
    updated_user = user_repo.update_user(user_id, user_update)
    if not updated_user:
        raise HTTPException(status_code=404, detail="User not found")
    return updated_user

@router.delete("/{user_id}")
def delete_user(user_id: int, db: Session = Depends(get_db)):
    """
    Удаление пользователя (soft delete)
    """
    user_repo = UserRepository(db)
    success = user_repo.delete_user(user_id)
    if not success:
        raise HTTPException(status_code=404, detail="User not found")
    return {"message": "User deleted successfully"}