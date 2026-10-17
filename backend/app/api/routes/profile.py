from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.ext.asyncio import AsyncSession

from app import crud
from app.core.db import get_db
from app.schemas.profile import ProfileCreate, ProfileResponse

router = APIRouter()


@router.post("/profiles", response_model=ProfileResponse, status_code=201)
async def create_profile(
    data: ProfileCreate,
    db: AsyncSession = Depends(get_db),
) -> ProfileResponse:
    try:
        return await crud.create_profile(db, data)
    except SQLAlchemyError:
        raise HTTPException(status_code=500, detail="プロフィールの保存に失敗しました")
