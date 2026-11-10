from collections.abc import AsyncGenerator

from sqlalchemy.ext.asyncio import (AsyncEngine,AsyncSession, create_async_engine, async_sessionmaker)
from app.core.config import settings
from typing import Annotated
from fastapi import Depends

engine: AsyncEngine = create_async_engine(
    settings.DATABASE_URL,
    pool_size= settings.DB_POOL_SIZE,
    max_overflow = settings.DB_MAX_OVERFLOW,
    pool_pre_ping = True,
    echo = False
)

AsyncSessionLocal = async_sessionmaker(
    bind=engine,
    expire_on_commit=False,
    autoflush=False,
)

async def get_db_session()-> AsyncGenerator[AsyncSession, None]:
    async with AsyncSessionLocal() as session:
        yield session

DbSession = Annotated[AsyncSession, Depends(get_db_session)]