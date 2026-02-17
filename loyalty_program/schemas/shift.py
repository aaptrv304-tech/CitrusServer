from pydantic import BaseModel
from typing import Optional


class ShiftBase(BaseModel):
    cashier_id: int
    business_id: int
    platform_id: int  # Adding platform_id since it's needed for shift tokens


class ShiftCreate(ShiftBase):
    pass


class ShiftUpdate(BaseModel):
    closed_at: Optional[str] = None
    is_active: Optional[bool] = None


class ShiftOut(ShiftBase):
    id: int
    started_at: Optional[str] = None
    closed_at: Optional[str] = None
    is_active: bool
    is_deleted: bool
    deleted_at: Optional[str] = None
    
    class Config:
        from_attributes = True