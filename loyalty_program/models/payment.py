from sqlalchemy import Column, Integer, String, DateTime, Boolean, Numeric, Text
from sqlalchemy.sql import func
from sqlalchemy import ForeignKey
from sqlalchemy.dialects.postgresql import JSONB
from database.base import Base


class Payment(Base):
    __tablename__ = "payments"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    subscription_id = Column(Integer, ForeignKey("subscriptions.id"), nullable=False)
    yookassa_payment_id = Column(String(100), unique=True)
    yookassa_status = Column(String(50))
    amount = Column(Numeric(10, 2), nullable=False)
    currency = Column(String(3), default='RUB')
    payment_method = Column(String(50))
    status = Column(String(20), nullable=False)  # pending, succeeded, failed
    paid_at = Column(DateTime(timezone=True), nullable=True)
    description = Column(Text, nullable=True)
    metadata = Column(JSONB)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now())