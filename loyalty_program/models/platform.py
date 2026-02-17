from sqlalchemy import Column, Integer, String
from sqlalchemy.sql import func
from ..config.database import Base


class Platform(Base):
    __tablename__ = "platforms"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String(50), unique=True, nullable=False)