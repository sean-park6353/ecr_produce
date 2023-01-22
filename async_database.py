from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.ext.declarative import declarative_base
import os 
Base = declarative_base()
MYSQL_URL = os.getenv("MYSQL_URL")
print("*"*30)
print(MYSQL_URL)
print("*"*30)
async_engine = create_async_engine(MYSQL_URL)

async def get_session():
    session = AsyncSession(bind=async_engine)
    try:
        yield session
    finally:
        await session.close()

