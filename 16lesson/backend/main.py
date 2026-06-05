from fastapi import FastAPI, HTTPException, Depends
from fastapi.middleware.cors import CORSMiddleware
from sqlmodel import Session,select
import os


from ai_service import analyze_sentiment
from schemas import AnalyzeRequest
from database import create_db_and_tables, get_session
from models import Feedback

app = FastAPI()

FRONTEND_URL = os.getenv("FRONTEND_URL", "http://localhost:5173")
app.add_middleware(
    CORSMiddleware,
     allow_origins=[FRONTEND_URL],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

@app.on_event("startup")
def on_startup():
    create_db_and_tables()


@app.get("/")
def home():
    return {"message": "AI Feedback Analyzer API is running"}

@app.post("/analyze")
def analyze_feedback(
    data: AnalyzeRequest,
    session: Session = Depends(get_session)):

    text = data.text.strip()

    if len(text) == 0:
        raise HTTPException(status_code=400, detail="Text cannot be empty")

    ai_result = analyze_sentiment(text)
    feedback = Feedback(text=text, sentiment=ai_result["sentiment"], confidence=ai_result["confidence"])
    session.add(feedback)
    session.commit()
    session.refresh(feedback)

    return feedback

@app.get("/feedbacks")
def get_feedbacks(session: Session = Depends(get_session)):
    statement = select(Feedback).order_by(Feedback.id.desc())
    feedbacks = session.exec(statement).all()
    return feedbacks

@app.get("/stats")
def get_stats(session: Session = Depends(get_session)):
    feedbacks = session.exec(select(Feedback)).all()

    stats = {
        "positive": 0,
        "neutral": 0,
        "negative": 0,
        "total": len(feedbacks)
    }

    for feedback in feedbacks:
        if feedback.sentiment in stats:
            stats[feedback.sentiment] += 1
    return stats


@app.delete("/feedbacks/{feedback_id}")
def delete_feedback(
    feedback_id: int,
    session: Session = Depends(get_session)
):
    feedback = session.get(Feedback, feedback_id)

    if feedback is None:
        raise HTTPException(status_code=404, detail="Feedback not found")

    session.delete(feedback)
    session.commit()

    return {"message": "Feedback was deleted"}




