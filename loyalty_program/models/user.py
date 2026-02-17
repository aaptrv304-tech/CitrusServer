from sqlalchemy import Column, Integer, String, Boolean, DateTime, BigInteger
from sqlalchemy.sql import func
from ..config.database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    phone = Column(String(20), unique=True, nullable=True)
    email = Column(String(255), unique=True, nullable=True)
    total_points = Column(Integer, default=0)
    is_deleted = Column(Boolean, default=False)
    deleted_at = Column(DateTime(timezone=True), nullable=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now())

    # Relationship attributes (not actual columns)
    # user_platforms: List[UserPlatform] = relationship("UserPlatform", back_populates="user")
    # visits: List[Visit] = relationship("Visit", back_populates="user")
    # reward_redemptions: List[RewardRedemption] = relationship("RewardRedemption", back_populates="user")
    # user_businesses: List[UserBusiness] = relationship("UserBusiness", back_populates="user")
    # phone_number_history: List[PhoneNumberHistory] = relationship("PhoneNumberHistory", back_populates="user")