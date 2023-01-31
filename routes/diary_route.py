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
        query = select(Diary).where(User.name==user_name, Diary.user_id==User.id)
        coroutine_result = await session.execute(query)
        result = coroutine_result.scalars().all()
        return result

    except Exception as e:
        logger.info("!"*30)
        logger.info(e)
        logger.info("!"*30)

# @router.get("/create", description="일기 쓰기")
# async def add_diary(
#     session: AsyncSession = Depends(get_session)    
# )
#     try:
#         query = insert()