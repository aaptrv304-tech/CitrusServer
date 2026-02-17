from fastapi import APIRouter, Depends, HTTPException
from typing import List
from schemas.business import BusinessCreate, BusinessUpdate, BusinessOut
from repositories.business import BusinessRepository
from database.session import get_db
from sqlalchemy.orm import Session

router = APIRouter()

@router.get("/", response_model=List[BusinessOut])
def get_businesses(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    """
    Получение списка бизнесов
    """
    business_repo = BusinessRepository(db)
    businesses = business_repo.get_businesses(skip=skip, limit=limit)
    return businesses

@router.get("/{business_id}", response_model=BusinessOut)
def get_business(business_id: int, db: Session = Depends(get_db)):
    """
    Получение бизнеса по ID
    """
    business_repo = BusinessRepository(db)
    business = business_repo.get_business_by_id(business_id)
    if not business:
        raise HTTPException(status_code=404, detail="Business not found")
    return business

@router.post("/", response_model=BusinessOut)
def create_business(business: BusinessCreate, db: Session = Depends(get_db)):
    """
    Создание нового бизнеса
    """
    business_repo = BusinessRepository(db)
    db_business = business_repo.create_business(business)
    return db_business

@router.put("/{business_id}", response_model=BusinessOut)
def update_business(business_id: int, business_update: BusinessUpdate, db: Session = Depends(get_db)):
    """
    Обновление бизнеса
    """
    business_repo = BusinessRepository(db)
    updated_business = business_repo.update_business(business_id, business_update)
    if not updated_business:
        raise HTTPException(status_code=404, detail="Business not found")
    return updated_business

@router.delete("/{business_id}")
def delete_business(business_id: int, db: Session = Depends(get_db)):
    """
    Удаление бизнеса (soft delete)
    """
    business_repo = BusinessRepository(db)
    success = business_repo.delete_business(business_id)
    if not success:
        raise HTTPException(status_code=404, detail="Business not found")
    return {"message": "Business deleted successfully"}