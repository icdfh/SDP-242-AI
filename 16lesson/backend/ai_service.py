from transformers import pipeline

sentiment_pipeline = pipeline("sentiment-analysis",
                            model="cointegrated/rubert-tiny-sentiment-balanced")

def analyze_sentiment(text:str):
    result = sentiment_pipeline(text)[0]

    label = result["label"]
    score = float(result["score"])

    return{
        "sentiment": label,
        "confidence": score
    }