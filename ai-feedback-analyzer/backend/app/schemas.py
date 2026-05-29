from datetime import datetime
from sqlmodel import SQLModel


class FeedbackCreate(SQLModel):
    text: str


class FeedbackRead(SQLModel):
    id: int
    text: str
    ai_label: str
    confidence: float
    created_at: datetime


class StatsRead(SQLModel):
    total: int
    positive: int
    negative: int
    neutral: int