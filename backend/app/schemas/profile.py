from datetime import datetime
from typing import Literal

from pydantic import BaseModel, Field


GenderType = Literal["male", "female", "other"]


class ProfileCreate(BaseModel):
    name: str = Field(..., min_length=1, max_length=100)
    gender: GenderType
    age: int = Field(..., ge=0, le=150)


class ProfileResponse(ProfileCreate):
    id: int
    created_at: datetime

    model_config = {"from_attributes": True}
