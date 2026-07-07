from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.models import Profile, TrainingLog
from app.schemas.profile import ProfileCreate
from app.schemas.training import TrainingLogCreate


async def create_profile(db: AsyncSession, data: ProfileCreate) -> Profile:
    profile = Profile(**data.model_dump())
    db.add(profile)
    await db.commit()
    await db.refresh(profile)
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
