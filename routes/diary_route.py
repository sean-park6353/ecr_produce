from fastapi import APIRouter

router = APIRouter(prefix="/diary", tags=["일기라우터"])

@router.get("", description="일기장 기본 페이지",)
async def get_diary():
    return "2322"