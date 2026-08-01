import logging

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app import crud
from app.core.config import get_embedding_provider
from app.core.db import get_db
from app.models import TrainingLog
from app.schemas.training import TrainingLogCreate, TrainingLogResponse

logger = logging.getLogger(__name__)
router = APIRouter()


@router.post("/training-logs", response_model=TrainingLogResponse, status_code=201)
async def create_training_log(
    payload: TrainingLogCreate,
    db: AsyncSession = Depends(get_db),
) -> TrainingLog:
    log = await crud.create_training_log(db, payload)

    # 埋め込みを非同期で生成・保存（失敗してもログ保存は成功扱い）
    try:
        text = f"{log.exercise} {log.sets}セット {log.reps}回 {log.weight_kg}kg"
        if log.memo:
            text += f" {log.memo}"
        provider = get_embedding_provider()
        embedding = await provider.embed(text)
        await crud.save_embedding(db, log.id, embedding)
    except Exception:
        logger.exception("埋め込み生成に失敗しました (training_log_id=%d)", log.id)

    return log


@router.get("/training-logs/{profile_id}", response_model=list[TrainingLogResponse])
async def get_training_logs(
    profile_id: int,
    db: AsyncSession = Depends(get_db),
) -> list[TrainingLog]:
    return await crud.get_training_logs(db, profile_id)
