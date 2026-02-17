from fastapi import APIRouter, Depends, HTTPException
from typing import List
from ....schemas.shift import ShiftCreate, ShiftUpdate, ShiftOut
from ....repositories.shift import ShiftRepository
from ....repositories.shift_token import ShiftTokenRepository
from ....database.session import get_db
from sqlalchemy.orm import Session
import secrets

router = APIRouter()

@router.get("/", response_model=List[ShiftOut])
def get_shifts(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    """
    Получение списка смен
    """
    shift_repo = ShiftRepository(db)
    shifts = shift_repo.get_shifts(skip=skip, limit=limit)
    return shifts

@router.get("/{shift_id}", response_model=ShiftOut)
def get_shift(shift_id: int, db: Session = Depends(get_db)):
    """
    Получение информации о смене
    """
    shift_repo = ShiftRepository(db)
    shift = shift_repo.get_shift_by_id(shift_id)
    if not shift:
        raise HTTPException(status_code=404, detail="Shift not found")
    return shift

@router.post("/", response_model=ShiftOut)
def create_shift(shift_data: ShiftCreate, db: Session = Depends(get_db)):
    """
    Начало новой смены
    """
    shift_repo = ShiftRepository(db)
    new_shift = shift_repo.create_shift(shift_data)
    
    # Создаем токен для смены
    shift_token_repo = ShiftTokenRepository(db)
    token = secrets.token_urlsafe(32)  # Генерируем уникальный токен
    
    shift_token = shift_token_repo.create_shift_token(
        shift_id=new_shift.id,
        platform_id=shift_data.platform_id,  # Предполагаем, что платформа передается в данных
        token=token
    )
    
    return new_shift

@router.put("/{shift_id}/close", response_model=ShiftOut)
def close_shift(shift_id: int, db: Session = Depends(get_db)):
    """
    Завершение смены
    """
    shift_repo = ShiftRepository(db)
    updated_shift = shift_repo.close_shift(shift_id)
    if not updated_shift:
        raise HTTPException(status_code=404, detail="Shift not found")
    return updated_shift

@router.delete("/{shift_id}")
def delete_shift(shift_id: int, db: Session = Depends(get_db)):
    """
    Удаление смены (soft delete)
    """
    shift_repo = ShiftRepository(db)
    success = shift_repo.delete_shift(shift_id)
    if not success:
        raise HTTPException(status_code=404, detail="Shift not found")
    return {"message": "Shift deleted successfully"}