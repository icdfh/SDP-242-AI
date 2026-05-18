from transformers import pipeline

classfier = pipeline("sentiment-analysis")

def analyze_review(text):
  result = classfier(text)[0]

  return{
      "text": text,
      "label": result["label"],
      "score": round(result["score"],2)
  }

reviews = [
    "I love this product"
]

predictions = analyze_review(reviews)
print(predictions)