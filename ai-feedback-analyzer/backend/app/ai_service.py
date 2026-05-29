import torch
from transformers import AutoTokenizer, AutoModelForSequenceClassification


MODEL_NAME = "cointegrated/rubert-tiny-sentiment-balanced"

tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)

model = AutoModelForSequenceClassification.from_pretrained(MODEL_NAME)

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

model.to(device)

model.eval()


def analyze_text(text: str) -> dict:
    inputs = tokenizer(
        text,
        return_tensors="pt",
        truncation=True,
        padding=True,
        max_length=512
    )

    inputs = {
        key: value.to(device)
        for key, value in inputs.items()
    }

    with torch.no_grad():
        outputs = model(**inputs)

        logits = outputs.logits

        probabilities = torch.softmax(logits, dim=1)

        predicted_class_id = torch.argmax(probabilities, dim=1).item()

        confidence = probabilities[0][predicted_class_id].item()

        label = model.config.id2label[predicted_class_id]

    return {
        "label": label,
        "confidence": round(confidence, 4)
    }