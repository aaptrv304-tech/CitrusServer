from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import declarative_base
from .settings import settings

# Синхронный движок для Alembic
sync_engine = create_engine(
    settings.database_url.replace("+asyncpg", ""),
    pool_pre_ping=True,
)

SyncSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=sync_engine)

# Асинхронный движок для приложения
async_engine = create_async_engine(
    settings.database_url,
    pool_pre_ping=True,
    echo=True
)

AsyncSessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    expire_on_commit=False,
    class_=AsyncSession,
    bind=async_engine
)

Base = declarative_base()

def get_sync_db():
    db = SyncSessionLocal()
    try:
        yield db
    finally:
        db.close()

async def get_async_db():
    async with AsyncSessionLocal() as db:
        try:
            yield db
        finally:
            await db.close()