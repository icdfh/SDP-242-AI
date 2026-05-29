from datetime import datetime
from pydantic import BaseModel, Field

class FeedbackCreate(BaseModel):
    text:str = Field(min_length=2, max_length=1000)

class FeedbackRead(BaseModel):
    id:int
    text:str
    ai_labe:str
    confidence:float
    created_at: datetime

class StatsRad(BaseModel):
    positive: int
    neutral: int
    negative: int