import os

from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine
from sqlalchemy.orm import DeclarativeBase

_DATABASE_URL = os.environ.get(
    "DATABASE_URL",
    "postgresql+asyncpg://postgres:postgres@db:5432/peak_haunt",
)
# psycopg 形式で指定されている場合は asyncpg 形式に変換
DATABASE_URL = _DATABASE_URL.replace(
    "postgresql+psycopg://", "postgresql+asyncpg://"
)

engine = create_async_engine(DATABASE_URL, echo=False)
SessionLocal = async_sessionmaker(engine, expire_on_commit=False)


class Base(DeclarativeBase):
    pass


async def get_db() -> AsyncSession:  # type: ignore[return]
    async with SessionLocal() as session:
        yield session  # type: ignore[misc]
