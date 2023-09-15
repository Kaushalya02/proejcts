from langdetect import detect
from textblob import TextBlob
# Get the user input.
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
text = input("Enter a text: ")
# Detect the language of the text.
lang = detect(text)
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
# Return the language code and full name.
print(f"Language code: {lang}")
print(f"Language name: {lang_names[lang]}")
print(f"Sentiment category: {sentiment_category}")
