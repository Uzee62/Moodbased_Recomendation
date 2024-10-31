import streamlit as st

def display_recommendations(recommendations):
    if not recommendations.empty:
        st.subheader("These are the Recommendations based on your Mood :")
        for _, row in recommendations.iterrows():
            st.write(f"- {row['item']} ({row['type']})")
    else:
        st.write("No recommendations found for this mood.")








