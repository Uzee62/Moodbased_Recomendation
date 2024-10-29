from transformers import pipeline

def load_mood_model():
    return pipeline("text-classification", model="bhadresh-savani/bert-base-uncased-emotion")
