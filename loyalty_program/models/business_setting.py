from sqlalchemy import Column, Integer, Numeric, DateTime
from sqlalchemy.sql import func
from sqlalchemy import ForeignKey
from database.base import Base


class BusinessSetting(Base):
    __tablename__ = "business_settings"

    business_id = Column(Integer, ForeignKey("businesses.id"), primary_key=True)
    points_rate = Column(Numeric(5, 2), default=10.00)  # За 100₽ = 10 очков
    bonus_points_first_visit = Column(Integer, default=100)  # Бонус за первый визит в бизнес
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now())