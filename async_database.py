from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession

import os


MYSQL_URL = os.getenv("MYSQL_URL")
async_engine = create_async_engine(MYSQL_URL)

async def get_session():
    session = AsyncSession(bind=async_engine)
    try:
        yield session
    finally:
        await session.close()

