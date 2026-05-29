from datetime import datetime
from sqlmodel import SQLModel, Field


class Feedback(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    text: str = Field(index=True)
    ai_label: str
    confidence: float
    created_at: datetime = Field(default_factory=datetime.utcnow)