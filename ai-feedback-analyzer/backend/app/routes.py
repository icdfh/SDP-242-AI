from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session, select

from app.database import get_session
from app.models import Feedback
from app.schemas import FeedbackCreate, FeedbackRead, StatsRead
from app.ai_service import analyze_text


router = APIRouter()


@router.post("/feedbacks", response_model=FeedbackRead)
def create_feedback(
    feedback_data: FeedbackCreate,
    session: Session = Depends(get_session)
):
    try:
        ai_result = analyze_text(feedback_data.text)
    except Exception as error:
        raise HTTPException(
            status_code=500,
            detail=f"AI model error: {str(error)}"
        )

    feedback = Feedback(
        text=feedback_data.text,
        ai_label=ai_result["label"],
        confidence=ai_result["confidence"]
    )

    session.add(feedback)
    session.commit()
    session.refresh(feedback)

    return feedback


@router.get("/feedbacks", response_model=list[FeedbackRead])
def get_feedbacks(
    session: Session = Depends(get_session)
):
    statement = select(Feedback).order_by(Feedback.id.desc())

    feedbacks = session.exec(statement).all()

    return feedbacks


@router.delete("/feedbacks/{feedback_id}")
def delete_feedback(
    feedback_id: int,
    session: Session = Depends(get_session)
):
    feedback = session.get(Feedback, feedback_id)

    if feedback is None:
        raise HTTPException(
            status_code=404,
            detail="Feedback not found"
        )

    session.delete(feedback)
    session.commit()

    return {
        "message": "Feedback deleted successfully",
        "deleted_id": feedback_id
    }


@router.get("/stats", response_model=StatsRead)
def get_stats(
    session: Session = Depends(get_session)
):
    statement = select(Feedback)

    feedbacks = session.exec(statement).all()

    total = len(feedbacks)

    positive = 0
    negative = 0
    neutral = 0

    for feedback in feedbacks:
        if feedback.ai_label == "positive":
            positive += 1
        elif feedback.ai_label == "negative":
            negative += 1
        elif feedback.ai_label == "neutral":
            neutral += 1

    return {
        "total": total,
        "positive": positive,
        "negative": negative,
        "neutral": neutral
    }