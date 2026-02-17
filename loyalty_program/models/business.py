from sqlalchemy import Column, Integer, String, Text, Boolean, DateTime
from sqlalchemy.sql import func
from sqlalchemy import ForeignKey
from database.base import Base


class Business(Base):
    __tablename__ = "businesses"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    business_owner_id = Column(Integer, ForeignKey("business_owners.id"), nullable=False)
    name = Column(String(255), nullable=False)
    category = Column(String(100), nullable=False)
    category_emoji = Column(String(10), nullable=False)
    address = Column(Text, nullable=True)
    city = Column(String(100), nullable=True)
    description = Column(Text, nullable=True)
    image_url = Column(String(500), nullable=True)
    phone = Column(String(255), nullable=True)
    shop_param = Column(String(100), unique=True, nullable=False)
    is_active = Column(Boolean, default=True)
    is_deleted = Column(Boolean, default=False)
    deleted_at = Column(DateTime(timezone=True), nullable=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())