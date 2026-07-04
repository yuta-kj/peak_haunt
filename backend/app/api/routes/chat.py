from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.config import get_llm_provider
from app.db.database import get_db
from app.db.models import TrainingLog
from app.providers.base import LLMProvider

router = APIRouter()


class RecommendRequest(BaseModel):
    profile_id: int


class RecommendResponse(BaseModel):
    recommendation: str


@router.post("/recommend", response_model=RecommendResponse)
async def recommend(
    payload: RecommendRequest,
    db: AsyncSession = Depends(get_db),
) -> RecommendResponse:
    result = await db.execute(
        select(TrainingLog)
        .where(TrainingLog.profile_id == payload.profile_id)
        .order_by(TrainingLog.logged_at.desc())
        .limit(5)
    )
    logs = list(result.scalars().all())

    if not logs:
        raise HTTPException(status_code=404, detail="トレーニング記録が見つかりません")

    log_text = "\n".join(
        f"- {log.exercise}: {log.sets}セット×{log.reps}回 {log.weight_kg}kg"
        + (f"（{log.memo}）" if log.memo else "")
        for log in logs
    )

    prompt = (
        "あなたは経験豊富な筋トレコーチです。\n"
        "以下は直近のトレーニング記録です：\n"
        f"{log_text}\n\n"
        "この記録をもとに、次回のトレーニングに向けた具体的なアドバイスを日本語で200字以内で提案してください。"
    )

    provider: LLMProvider = get_llm_provider()
    try:
        recommendation = await provider.generate(prompt)
    except Exception as exc:
        raise HTTPException(status_code=503, detail=f"LLM接続エラー: {exc}") from exc

    return RecommendResponse(recommendation=recommendation)
