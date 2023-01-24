from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession

import os


MYSQL_URL = os.getenv("MYSQL_URL")
async_engine = create_async_engine("mysql+aiomysql://admin:o815o511@database-2.cwwalfzheezp.ap-northeast-2.rds.amazonaws.com:3306/jiseong2?charset=UTF8MB4")

async def get_session():
    session = AsyncSession(bind=async_engine)
    try:
        yield session
    finally:
        await session.close()

