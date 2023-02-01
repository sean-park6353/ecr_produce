from fastapi import APIRouter, Depends
from async_database import get_session, AsyncSession
from sqlalchemy import select, insert
from models.model import Book, User
import logging

logger = logging.getLogger(__name__)

logging.basicConfig(filename="./server.log", level=logging.INFO)
router = APIRouter(prefix="/diary", tags=["일기라우터"])

@router.get("", description="전체 일기 페이지",)
async def get_diary(
    user_name: str,
    session: AsyncSession = Depends(get_session)
):
    try:
        query = (
            select(Book, User)
            .join(User)
            .where(User.name==user_name, User.id==Book.contributer_id)
        )
        coroutine_result = await session.execute(query)
        result = coroutine_result.fetchall()
        return result

    except Exception as e:
        print(1)
        print(e)
        print(1)
        logger.info(e)

