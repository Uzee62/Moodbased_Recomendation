import streamlit as st
from models.mood_model import load_mood_model
from utils.load_data import load_data
from utils.mapping import map_mood
from modules.recommendation import recommend_items
from modules.display import display_recommendations

def main():
    st.title("Mood-Based Recommendation System")
    st.write("How are you feeling today?")

    # Load model and data
    mood_model = load_mood_model()
    data = load_data('data/mood_items.csv')

    # Get user input
    user_input = st.text_area("Describe your mood:", "")

    if st.button("Recommendations: "):
        if user_input:
            # Predict mood from user input
            mood_prediction = mood_model(user_input)
            detected_mood = mood_prediction[0]['label']
            mapped_mood = map_mood(detected_mood)

            if mapped_mood:
                # Get recommendations and display them
                recommendations = recommend_items(data, mapped_mood)
                display_recommendations(recommendations)
            else:
                st.write("Mood detected is not mapped to recommendations.")
        else:
            st.warning("Please describe your mood.")

if __name__ == "__main__":
    main()
