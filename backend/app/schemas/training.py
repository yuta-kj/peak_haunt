from datetime import datetime

from pydantic import BaseModel, Field


class TrainingLogCreate(BaseModel):
    profile_id: int
    exercise: str = Field(min_length=1, max_length=100)
    sets: int = Field(ge=1)
    reps: int = Field(ge=1)
    weight_kg: float = Field(ge=0)
    memo: str | None = None


class TrainingLogResponse(TrainingLogCreate):
    id: int
    logged_at: datetime

    model_config = {"from_attributes": True}
