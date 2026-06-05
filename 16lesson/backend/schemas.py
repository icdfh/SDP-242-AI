from pydantic import BaseModel

class AnalyzeRequest(BaseModel):
    text: str

class AnalyzerResponse(BaseModel):
    id: int
    text: str
    sentiment: str
    confidence: float