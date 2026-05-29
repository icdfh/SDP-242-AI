from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

from backend.app.ai_service import analyze_text


app = FastAPI(
    title="AI Feedback Analyzer API",
    description="FastAPI backend with real AI model",
    version="1.0.0"
)


class TextRequest(BaseModel):
    text: str


@app.get("/")
def home():
    return {
        "message": "AI Feedback Analyzer API is running"
    }


@app.post("/analyze")
def analyze(request: TextRequest):
    try:
        result = analyze_text(request.text)
        return result

    except Exception as error:
        raise HTTPException(
            status_code=500,
            detail=f"AI model error: {str(error)}"
        )