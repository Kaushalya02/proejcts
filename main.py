from langdetect import detect
from textblob import TextBlob
def detect_language_and_sentiment(text):
    language = detect(text)
    sentiment = TextBlob(text).sentiment.polarity
    return language, sentiment
text = input("Enter some text: ")
language, sentiment = detect_language_and_sentiment(text)
print(f"Detected language: {language}")
print(f"Sentiment polarity: {sentiment}")
