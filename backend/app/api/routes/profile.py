from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.db.database import get_db
from app.db.models import Profile
from app.schemas.profile import ProfileCreate, ProfileResponse

router = APIRouter()


@router.post("/profiles", response_model=ProfileResponse, status_code=201)
async def create_profile(
    data: ProfileCreate,
    db: AsyncSession = Depends(get_db),
) -> ProfileResponse:
    profile = Profile(**data.model_dump())
    db.add(profile)
    await db.commit()
    await db.refresh(profile)
    return profile
