# import streamlit as st
# import pickle

# st.title("SentimentSense - Simple Sentiment Analysis")

# # Load the saved model
# @st.cache_resource
# def load_model():
#     with open('sentiment_model.pkl', 'rb') as f:
#         return pickle.load(f)

# model = load_model()

# # User input text box
# user_input = st.text_area("Enter a sentence to analyze:")

# # Sentiment prediction
# if st.button("Analyze Sentiment"):
#     if user_input.strip():
#         prediction = model.predict([user_input])
#         sentiment = "Positive 😊" if prediction[0] == 1 else "Negative 😟"
#         st.write(f"Sentiment: **{sentiment}**")
#     else:
#         st.warning("Please enter some text to analyze.")
# Add this to your Streamlit app.py instead of your current ML pipeline
import streamlit as st
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import nltk

nltk.download('vader_lexicon')

st.title("SentimentSense - Simple Sentiment Analysis")
user_input = st.text_area("Enter a sentence to analyze:")

if st.button("Analyze Sentiment"):
    if user_input.strip():
        sid = SentimentIntensityAnalyzer()
        scores = sid.polarity_scores(user_input)
        sentiment = "Positive 😊" if scores['compound'] > 0 else "Negative 😟"
        st.write(f"Sentiment: **{sentiment}**")
    else:
        st.warning("Please enter some text to analyze.")
