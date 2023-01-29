from fastapi import APIRouter, Depends
from async_database import get_session, AsyncSession
from sqlalchemy import select, insert
from models.model import Diary, User
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
        query = select(User).where(User.name==user_name)
        coroutine_result = await session.execute(query)
        result = coroutine_result.scalars().all()
        logger.info("!"*30)
        logger.info(e)
        logger.info("!"*30)
        return result

    except Exception as e:
        logger.info("!"*30)
        logger.info(e)
        logger.info("!"*30)
        