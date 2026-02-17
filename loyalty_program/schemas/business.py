from pydantic import BaseModel
from typing import Optional


class BusinessBase(BaseModel):
    business_owner_id: int
    name: str
    category: str
    category_emoji: str
    address: Optional[str] = None
    city: Optional[str] = None
    description: Optional[str] = None
    image_url: Optional[str] = None
    phone: Optional[str] = None
    shop_param: str
    is_active: bool = True


class BusinessCreate(BusinessBase):
    pass


class BusinessUpdate(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    category_emoji: Optional[str] = None
    address: Optional[str] = None
    city: Optional[str] = None
    description: Optional[str] = None
    image_url: Optional[str] = None
    phone: Optional[str] = None
    is_active: Optional[bool] = None


class BusinessOut(BusinessBase):
    id: int
    is_deleted: bool
    deleted_at: Optional[str] = None
    
    class Config:
        from_attributes = True