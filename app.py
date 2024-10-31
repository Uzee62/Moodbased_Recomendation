import streamlit as st
from models.mood_model import load_mood_model
from utils.load_data import load_data
from utils.mapping import map_mood
from modules.recommendation import recommend_items
from modules.display import display_recommendations

def main():
    st.subheader("Mood-Based Recommendation System")
    st.write("How are you feeling today?")

    # Model And Data Loading
    mood_model = load_mood_model()
    data = load_data('data/mood_items.csv')

    # Geting input from the  user
    user_input = st.text_area("Describe your mood : ", "")

    if st.button("Get Recommendations"):
        if user_input:
            # Using Model to detect the Users Mood from the input
            mood_prediction = mood_model(user_input)
            detected_mood = mood_prediction[0]['label']
            mapped_mood = map_mood(detected_mood)
            # st.subheader(f"Detected mood is :  {detected_mood}")
            if mapped_mood:
                # Geting recommendations from the dataset based on Users Mood and displaying them
                recommendations = recommend_items(data, mapped_mood)
                display_recommendations(recommendations)
            else:
                st.write("Mood detected is not mapped to recommendations.")
        else:
            st.warning("Please describe your mood.")

if __name__ == "__main__":
    main()