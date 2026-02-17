from sqlalchemy import Column, Integer, String, Boolean, DateTime
from sqlalchemy.sql import func
from database.base import Base


class BusinessOwner(Base):
    __tablename__ = "business_owners"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    email = Column(String(255), unique=True, nullable=False)
    password_hash = Column(String(255), nullable=False)
    full_name = Column(String(255), nullable=True)
    is_active = Column(Boolean, default=True)
    is_deleted = Column(Boolean, default=False)
    deleted_at = Column(DateTime(timezone=True), nullable=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())