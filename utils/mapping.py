from config.mood_mapping import mood_mapping

def map_mood(detected_mood):
    return mood_mapping.get(detected_mood.lower())
