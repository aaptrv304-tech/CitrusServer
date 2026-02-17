from fastapi import APIRouter, Depends, HTTPException
from ....schemas.user import UserOut
from ....repositories.user import UserRepository
from ....repositories.visit import VisitRepository
from ....repositories.shift_token import ShiftTokenRepository
from ....database.session import get_db
from sqlalchemy.orm import Session

router = APIRouter()

@router.post("/read-card/{card_uid}")
def read_nfc_card(card_uid: str, shift_token: str, db: Session = Depends(get_db)):
    """
    Чтение NFC карты и регистрация визита
    """
    # Находим токен смены
    shift_token_repo = ShiftTokenRepository(db)
    shift_token_obj = shift_token_repo.get_shift_token_by_token(shift_token)
    
    if not shift_token_obj:
        raise HTTPException(status_code=404, detail="Invalid shift token")
    
    # Находим пользователя по UID карты (предполагаем, что UID хранится в каком-то виде)
    user_repo = UserRepository(db)
    user = user_repo.get_user_by_card_uid(card_uid)
    
    if not user:
        raise HTTPException(status_code=404, detail="User with this card not found")
    
    # Регистрируем визит
    visit_repo = VisitRepository(db)
    visit = visit_repo.create_visit(
        user_id=user.id,
        shift_token_id=shift_token_obj.id,
        visit_type="in_person"
    )
    
    return {
        "message": "Card read successfully",
        "user": user,
        "visit_registered": True,
        "visit_id": visit.id
    }

@router.post("/link-card")
def link_nfc_card_to_user(card_uid: str, user_id: int, db: Session = Depends(get_db)):
    """
    Привязка NFC карты к пользователю
    """
    user_repo = UserRepository(db)
    user = user_repo.get_user_by_id(user_id)
    
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    
    # В реальной реализации здесь будет логика привязки карты к пользователю
    # Пока просто возвращаем успешный результат
    return {
        "message": f"NFC card {card_uid} linked to user {user_id}",
        "user_id": user_id,
        "card_uid": card_uid
    }