from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app import crud
from app.core.db import get_db
from app.models import TrainingLog
from app.schemas.training import TrainingLogCreate, TrainingLogResponse

router = APIRouter()


@router.post("/training-logs", response_model=TrainingLogResponse, status_code=201)
async def create_training_log(
    payload: TrainingLogCreate,
    db: AsyncSession = Depends(get_db),
) -> TrainingLog:
    return await crud.create_training_log(db, payload)


@router.get("/training-logs/{profile_id}", response_model=list[TrainingLogResponse])
async def get_training_logs(
    profile_id: int,
    db: AsyncSession = Depends(get_db),
) -> list[TrainingLog]:
    return await crud.get_training_logs(db, profile_id)
