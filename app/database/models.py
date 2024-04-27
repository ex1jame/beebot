from sqlalchemy import BigInteger
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncAttrs
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

engine = create_async_engine(url='sqlite+aiosqlite:///db.sqlite3')

async_session = async_sessionmaker(engine)


class Base(AsyncAttrs, DeclarativeBase):
    pass


class User(Base):
    __tablename__ = 'users'

    id:Mapped[int] = mapped_column(primary_key=True)
    tg_id = mapped_column(BigInteger)


async def async_main() -> object:
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
