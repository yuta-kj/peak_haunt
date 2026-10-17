from pgvector.sqlalchemy import Vector
from sqlalchemy import select
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.ext.asyncio import AsyncSession

from app.models import Profile, TrainingLog, TrainingLogEmbedding
from app.schemas.profile import ProfileCreate
from app.schemas.training import TrainingLogCreate


async def create_profile(db: AsyncSession, data: ProfileCreate) -> Profile:
    profile = Profile(**data.model_dump())
    db.add(profile)
    try:
        await db.commit()
        await db.refresh(profile)
    except SQLAlchemyError:
        await db.rollback()
        raise
    return profile


async def create_training_log(
    db: AsyncSession, payload: TrainingLogCreate
) -> TrainingLog:
    log = TrainingLog(**payload.model_dump())
    db.add(log)
    await db.commit()
    await db.refresh(log)
    return log


async def get_training_logs(
    db: AsyncSession, profile_id: int
) -> list[TrainingLog]:
    result = await db.execute(
        select(TrainingLog)
        .where(TrainingLog.profile_id == profile_id)
        .order_by(TrainingLog.logged_at.desc())
        .limit(20)
    )
    return list(result.scalars().all())


async def get_recent_training_logs(
    db: AsyncSession, profile_id: int, limit: int = 5
) -> list[TrainingLog]:
    result = await db.execute(
        select(TrainingLog)
        .where(TrainingLog.profile_id == profile_id)
        .order_by(TrainingLog.logged_at.desc())
        .limit(limit)
    )
    return list(result.scalars().all())


async def save_embedding(
    db: AsyncSession, training_log_id: int, embedding: list[float]
) -> TrainingLogEmbedding:
    record = TrainingLogEmbedding(training_log_id=training_log_id, embedding=embedding)
    db.add(record)
    await db.commit()
    await db.refresh(record)
    return record


async def search_similar_logs(
    db: AsyncSession, profile_id: int, query_embedding: list[float], limit: int = 5
) -> list[TrainingLog]:
    result = await db.execute(
        select(TrainingLog)
        .join(TrainingLogEmbedding, TrainingLog.id == TrainingLogEmbedding.training_log_id)
        .where(TrainingLog.profile_id == profile_id)
        .order_by(TrainingLogEmbedding.embedding.cosine_distance(query_embedding))
        .limit(limit)
    )
    return list(result.scalars().all())
