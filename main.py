from langdetect import detect
from textblob import TextBlob
import streamlit as s
# Define the function to detect the language and perform sentiment analysis
def main():
    # Get the user input.
    text = s.text_input("Enter a text: ")
    # Detect the language of the text.
    lang = detect(text)
    # Perform sentiment analysis on the text.
    sentiment_category = sentiment_analysis(text)
    # Print the language code, full name, and sentiment category.
    s.write(f"Language code: {lang}")
    s.write(f"Language name: {lang_names[lang]}")
    s.write(f"Sentiment category: {sentiment_category}")
# Define the function to perform sentiment analysis
def sentiment_analysis(text):
    # Create a TextBlob object from the text.
    text_blob = TextBlob(text)
    # Get the sentiment polarity.
    sentiment = text_blob.sentiment.polarity
    # Convert the sentiment polarity to a sentiment category.
    if sentiment < 0:
        sentiment_category = "negative"
    elif sentiment == 0:
        sentiment_category = "neutral"
    else:
        sentiment_category = "positive"
    # Return the sentiment category.
    return sentiment_category
# Define the dictionary of language codes and full names
lang_names = {"en":"English",
              "hi":"Hindi",
              "ur":"Urdu",
              "af":"Afrikaans",
              "ar":"Arabic",
              "bn":"Bengali	",
              "zh":"Chinese	",
              "de":"German",
              "it":"Italian",
              "kn":"Kannada"}
# Call the main function
if __name__ == "__main__":
    main()
