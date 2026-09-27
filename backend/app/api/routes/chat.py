from collections.abc import AsyncGenerator

from fastapi import APIRouter, Depends, HTTPException
from fastapi.responses import StreamingResponse
from pydantic import BaseModel
from sqlalchemy.ext.asyncio import AsyncSession

from app import crud
from app.core.config import get_embedding_provider, get_llm_provider
from app.core.db import get_db
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
    # クエリ用の直近ログを1件取得してベクトル化
    recent = await crud.get_recent_training_logs(db, payload.profile_id, limit=1)
    if not recent:
        raise HTTPException(status_code=404, detail="トレーニング記録が見つかりません")

    embedding_provider = get_embedding_provider()
    query_log = recent[0]
    query_text = f"{query_log.exercise} {query_log.sets}セット {query_log.reps}回 {query_log.weight_kg}kg"
    try:
        query_embedding = await embedding_provider.embed(query_text)
        logs = await crud.search_similar_logs(db, payload.profile_id, query_embedding, limit=5)
    except Exception:
        # 埋め込み失敗時は直近ログにフォールバック
        logs = await crud.get_recent_training_logs(db, payload.profile_id, limit=5)

    log_text = "\n".join(
        f"- {log.exercise}: {log.sets}セット×{log.reps}回 {log.weight_kg}kg"
        + (f"（{log.memo}）" if log.memo else "")
        for log in logs
    )

    prompt = (
        "あなたは経験豊富な筋トレコーチです。\n"
        "以下は関連するトレーニング記録です：\n"
        f"{log_text}\n\n"
        "この記録をもとに、次回のトレーニングに向けた具体的なアドバイスを日本語で200字以内で提案してください。"
    )

    provider: LLMProvider = get_llm_provider()
    try:
        recommendation = await provider.generate(prompt)
    except Exception as exc:
        raise HTTPException(status_code=503, detail=f"LLM接続エラー: {exc}") from exc

    return RecommendResponse(recommendation=recommendation)


@router.post("/recommend/stream")
async def recommend_stream(
    payload: RecommendRequest,
    db: AsyncSession = Depends(get_db),
) -> StreamingResponse:
    logs = await crud.get_recent_training_logs(db, payload.profile_id, limit=5)

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

    async def event_stream() -> AsyncGenerator[str, None]:
        try:
            async for token in await provider.generate_stream(prompt):
                yield f"data: {token}\n\n"
        except Exception as exc:
            yield f"data: [ERROR] {exc}\n\n"
        yield "data: [DONE]\n\n"

    return StreamingResponse(event_stream(), media_type="text/event-stream")
