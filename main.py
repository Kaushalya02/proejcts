from streamlit as st
from langdetect import detect
from textblob import TextBlob
# Get the user input.
lang_names = st.{"en":"English",
              "hi":"Hindi",
              "ur":"Urdu",
              "af":"Afrikaans",
              "ar":"Arabic",
              "bn":"Bengali	",
              "zh":"Chinese	",
              "de":"German",
              "it":"Italian",
              "kn":"Kannada"}
text = st.input("Enter a text: ")
# Detect the language of the text.
lang = st.detect(text)
text_blob = st.TextBlob(text)
    # Get the sentiment polarity.
sentiment = st.text_blob.sentiment.polarity
    # Convert the sentiment polarity to a sentiment category.
st.if sentiment < 0:
    sentiment_category = "negative"
st.elif sentiment == 0:
    sentiment_category = "neutral"
st.else:
    sentiment_category = "positive"
    # Return the sentiment category.
# Return the language code and full name.
st.print(f"Language code: {lang}")
st.print(f"Language name: {lang_names[lang]}")
st.print(f"Sentiment category: {sentiment_category}")
