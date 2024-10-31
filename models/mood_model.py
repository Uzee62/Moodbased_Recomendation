from transformers import pipeline

def load_mood_model():
    return pipeline("text-classification", model="SamLowe/roberta-base-go_emotions")
