from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.db.database import get_db
from app.db.models import TrainingLog
from app.schemas.training import TrainingLogCreate, TrainingLogResponse

router = APIRouter()


@router.post("/training-logs", response_model=TrainingLogResponse, status_code=201)
async def create_training_log(
    payload: TrainingLogCreate,
    db: AsyncSession = Depends(get_db),
) -> TrainingLog:
    log = TrainingLog(**payload.model_dump())
    db.add(log)
    await db.commit()
    await db.refresh(log)
    return log


@router.get("/training-logs/{profile_id}", response_model=list[TrainingLogResponse])
async def get_training_logs(
    profile_id: int,
    db: AsyncSession = Depends(get_db),
) -> list[TrainingLog]:
    result = await db.execute(
        select(TrainingLog)
        .where(TrainingLog.profile_id == profile_id)
        .order_by(TrainingLog.logged_at.desc())
        .limit(20)
    )
    return list(result.scalars().all())
