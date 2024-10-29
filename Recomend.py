import streamlit as st
import pandas as pd
from transformers import pipeline

# Load the mood classification model
mood_model = pipeline("text-classification", model="bhadresh-savani/bert-base-uncased-emotion")

# Load the recommendation dataset
data = pd.read_csv('mood_items.csv')

def recommend_items(mood):
    # Filter the dataset based on the mood
    recommendations = data[data['mood'] == mood]
    return recommendations

def main():
    st.title("Mood-Based Recommendation System")
    st.write("How are you feeling today?")

    # Input box for user mood description
    user_input = st.text_area("Describe your mood:", "")

    if st.button("Get Recommendations"):
        if user_input:
        # Analyze the mood from the user input
            mood_prediction = mood_model(user_input)

        # Print the full prediction for debugging
            # st.write("Full Mood Prediction Output:", mood_prediction)  # Display the full prediction output

            detected_mood = mood_prediction[0]['label'].lower()  # Get the mood label
            # st.write(f"Detected Mood: {detected_mood}")  # Print detected mood

        # Map detected mood to recommendation categories
            mood_mapping = {
                "joy": "happy",
                "happy": "happy",
                "low": "sadness",     
                "sadness": "sad",      
                "bored": "bored",   
                "anger": "angry",
                "fear": "sad",
                "surprise": "surprise",
                "neutral": "relaxed",
                "bore": "bored" ,
                "love" : "nostalgic",
                "Calm" : "joy"
            }

        # Check the mapped mood
        mapped_mood = mood_mapping.get(detected_mood, None)


        if mapped_mood:
                # st.subheader(f"Detected Mood: {mapped_mood}")

                # Get recommendations based on the detected mood
                recommendations = recommend_items(mapped_mood)
                if not recommendations.empty:
                    st.subheader("Recommendations:")
                    for _, row in recommendations.iterrows():
                        st.write(f"- {row['item']} ({row['type']})")
                else:
                    st.write("No recommendations found for this mood.")
        else:
                st.write("Mood detected is not mapped to recommendations.")
    else:
            st.warning("Please describe your mood.")

if __name__ == "__main__":
    main()
