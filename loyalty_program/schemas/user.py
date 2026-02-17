from pydantic import BaseModel
from typing import Optional


class UserBase(BaseModel):
    phone: Optional[str] = None
    email: Optional[str] = None
    total_points: int = 0


class UserCreate(UserBase):
    phone: str  # phone is required for creation


class UserUpdate(BaseModel):
    phone: Optional[str] = None
    email: Optional[str] = None


class UserOut(UserBase):
    id: int
    is_deleted: bool
    deleted_at: Optional[str] = None
    
    class Config:
        from_attributes = True