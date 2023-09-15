{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "2023-09-15 12:21:25.452 \n",
      "  \u001b[33m\u001b[1mWarning:\u001b[0m to view this Streamlit app on a browser, run it with the following\n",
      "  command:\n",
      "\n",
      "    streamlit run C:\\Users\\KAUSHALYA YADAV\\AppData\\Roaming\\Python\\Python310\\site-packages\\ipykernel_launcher.py [ARGUMENTS]\n"
     ]
    },
    {
     "ename": "LangDetectException",
     "evalue": "No features in text.",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mLangDetectException\u001b[0m                       Traceback (most recent call last)",
      "\u001b[1;32mc:\\Users\\KAUSHALYA YADAV\\Desktop\\multi language sentiment analyisis\\main.ipynb Cell 1\u001b[0m line \u001b[0;36m1\n\u001b[0;32m      <a href='vscode-notebook-cell:/c%3A/Users/KAUSHALYA%20YADAV/Desktop/multi%20language%20sentiment%20analyisis/main.ipynb#W0sZmlsZQ%3D%3D?line=7'>8</a>\u001b[0m st\u001b[39m.\u001b[39mtitle(\u001b[39m\"\u001b[39m\u001b[39mLanguage Detection and Sentiment Analysis\u001b[39m\u001b[39m\"\u001b[39m)\n\u001b[0;32m      <a href='vscode-notebook-cell:/c%3A/Users/KAUSHALYA%20YADAV/Desktop/multi%20language%20sentiment%20analyisis/main.ipynb#W0sZmlsZQ%3D%3D?line=8'>9</a>\u001b[0m text \u001b[39m=\u001b[39m st\u001b[39m.\u001b[39mtext_input(\u001b[39m\"\u001b[39m\u001b[39mEnter some text:\u001b[39m\u001b[39m\"\u001b[39m)\n\u001b[1;32m---> <a href='vscode-notebook-cell:/c%3A/Users/KAUSHALYA%20YADAV/Desktop/multi%20language%20sentiment%20analyisis/main.ipynb#W0sZmlsZQ%3D%3D?line=9'>10</a>\u001b[0m language, sentiment \u001b[39m=\u001b[39m detect_language_and_sentiment(text)\n\u001b[0;32m     <a href='vscode-notebook-cell:/c%3A/Users/KAUSHALYA%20YADAV/Desktop/multi%20language%20sentiment%20analyisis/main.ipynb#W0sZmlsZQ%3D%3D?line=10'>11</a>\u001b[0m st\u001b[39m.\u001b[39mwrite(\u001b[39mf\u001b[39m\u001b[39m\"\u001b[39m\u001b[39mDetected language: \u001b[39m\u001b[39m{\u001b[39;00mlanguage\u001b[39m}\u001b[39;00m\u001b[39m\"\u001b[39m)\n\u001b[0;32m     <a href='vscode-notebook-cell:/c%3A/Users/KAUSHALYA%20YADAV/Desktop/multi%20language%20sentiment%20analyisis/main.ipynb#W0sZmlsZQ%3D%3D?line=11'>12</a>\u001b[0m st\u001b[39m.\u001b[39mwrite(\u001b[39mf\u001b[39m\u001b[39m\"\u001b[39m\u001b[39mSentiment polarity: \u001b[39m\u001b[39m{\u001b[39;00msentiment\u001b[39m}\u001b[39;00m\u001b[39m\"\u001b[39m)\n",
      "\u001b[1;32mc:\\Users\\KAUSHALYA YADAV\\Desktop\\multi language sentiment analyisis\\main.ipynb Cell 1\u001b[0m line \u001b[0;36m5\n\u001b[0;32m      <a href='vscode-notebook-cell:/c%3A/Users/KAUSHALYA%20YADAV/Desktop/multi%20language%20sentiment%20analyisis/main.ipynb#W0sZmlsZQ%3D%3D?line=3'>4</a>\u001b[0m \u001b[39mdef\u001b[39;00m \u001b[39mdetect_language_and_sentiment\u001b[39m(text):\n\u001b[1;32m----> <a href='vscode-notebook-cell:/c%3A/Users/KAUSHALYA%20YADAV/Desktop/multi%20language%20sentiment%20analyisis/main.ipynb#W0sZmlsZQ%3D%3D?line=4'>5</a>\u001b[0m     language \u001b[39m=\u001b[39m detect(text)\n\u001b[0;32m      <a href='vscode-notebook-cell:/c%3A/Users/KAUSHALYA%20YADAV/Desktop/multi%20language%20sentiment%20analyisis/main.ipynb#W0sZmlsZQ%3D%3D?line=5'>6</a>\u001b[0m     sentiment \u001b[39m=\u001b[39m TextBlob(text)\u001b[39m.\u001b[39msentiment\u001b[39m.\u001b[39mpolarity\n\u001b[0;32m      <a href='vscode-notebook-cell:/c%3A/Users/KAUSHALYA%20YADAV/Desktop/multi%20language%20sentiment%20analyisis/main.ipynb#W0sZmlsZQ%3D%3D?line=6'>7</a>\u001b[0m     \u001b[39mreturn\u001b[39;00m language, sentiment\n",
      "File \u001b[1;32m~\\AppData\\Roaming\\Python\\Python310\\site-packages\\langdetect\\detector_factory.py:130\u001b[0m, in \u001b[0;36mdetect\u001b[1;34m(text)\u001b[0m\n\u001b[0;32m    128\u001b[0m detector \u001b[39m=\u001b[39m _factory\u001b[39m.\u001b[39mcreate()\n\u001b[0;32m    129\u001b[0m detector\u001b[39m.\u001b[39mappend(text)\n\u001b[1;32m--> 130\u001b[0m \u001b[39mreturn\u001b[39;00m detector\u001b[39m.\u001b[39;49mdetect()\n",
      "File \u001b[1;32m~\\AppData\\Roaming\\Python\\Python310\\site-packages\\langdetect\\detector.py:136\u001b[0m, in \u001b[0;36mDetector.detect\u001b[1;34m(self)\u001b[0m\n\u001b[0;32m    132\u001b[0m \u001b[39mdef\u001b[39;00m \u001b[39mdetect\u001b[39m(\u001b[39mself\u001b[39m):\n\u001b[0;32m    133\u001b[0m \u001b[39m    \u001b[39m\u001b[39m'''Detect language of the target text and return the language name\u001b[39;00m\n\u001b[0;32m    134\u001b[0m \u001b[39m    which has the highest probability.\u001b[39;00m\n\u001b[0;32m    135\u001b[0m \u001b[39m    '''\u001b[39;00m\n\u001b[1;32m--> 136\u001b[0m     probabilities \u001b[39m=\u001b[39m \u001b[39mself\u001b[39;49m\u001b[39m.\u001b[39;49mget_probabilities()\n\u001b[0;32m    137\u001b[0m     \u001b[39mif\u001b[39;00m probabilities:\n\u001b[0;32m    138\u001b[0m         \u001b[39mreturn\u001b[39;00m probabilities[\u001b[39m0\u001b[39m]\u001b[39m.\u001b[39mlang\n",
      "File \u001b[1;32m~\\AppData\\Roaming\\Python\\Python310\\site-packages\\langdetect\\detector.py:143\u001b[0m, in \u001b[0;36mDetector.get_probabilities\u001b[1;34m(self)\u001b[0m\n\u001b[0;32m    141\u001b[0m \u001b[39mdef\u001b[39;00m \u001b[39mget_probabilities\u001b[39m(\u001b[39mself\u001b[39m):\n\u001b[0;32m    142\u001b[0m     \u001b[39mif\u001b[39;00m \u001b[39mself\u001b[39m\u001b[39m.\u001b[39mlangprob \u001b[39mis\u001b[39;00m \u001b[39mNone\u001b[39;00m:\n\u001b[1;32m--> 143\u001b[0m         \u001b[39mself\u001b[39;49m\u001b[39m.\u001b[39;49m_detect_block()\n\u001b[0;32m    144\u001b[0m     \u001b[39mreturn\u001b[39;00m \u001b[39mself\u001b[39m\u001b[39m.\u001b[39m_sort_probability(\u001b[39mself\u001b[39m\u001b[39m.\u001b[39mlangprob)\n",
      "File \u001b[1;32m~\\AppData\\Roaming\\Python\\Python310\\site-packages\\langdetect\\detector.py:150\u001b[0m, in \u001b[0;36mDetector._detect_block\u001b[1;34m(self)\u001b[0m\n\u001b[0;32m    148\u001b[0m ngrams \u001b[39m=\u001b[39m \u001b[39mself\u001b[39m\u001b[39m.\u001b[39m_extract_ngrams()\n\u001b[0;32m    149\u001b[0m \u001b[39mif\u001b[39;00m \u001b[39mnot\u001b[39;00m ngrams:\n\u001b[1;32m--> 150\u001b[0m     \u001b[39mraise\u001b[39;00m LangDetectException(ErrorCode\u001b[39m.\u001b[39mCantDetectError, \u001b[39m'\u001b[39m\u001b[39mNo features in text.\u001b[39m\u001b[39m'\u001b[39m)\n\u001b[0;32m    152\u001b[0m \u001b[39mself\u001b[39m\u001b[39m.\u001b[39mlangprob \u001b[39m=\u001b[39m [\u001b[39m0.0\u001b[39m] \u001b[39m*\u001b[39m \u001b[39mlen\u001b[39m(\u001b[39mself\u001b[39m\u001b[39m.\u001b[39mlanglist)\n\u001b[0;32m    154\u001b[0m \u001b[39mself\u001b[39m\u001b[39m.\u001b[39mrandom\u001b[39m.\u001b[39mseed(\u001b[39mself\u001b[39m\u001b[39m.\u001b[39mseed)\n",
      "\u001b[1;31mLangDetectException\u001b[0m: No features in text."
     ]
    }
   ],
   "source": [
    "import streamlit as st\n",
    "from langdetect import detect\n",
    "from textblob import TextBlob\n",
    "def detect_language_and_sentiment(text):\n",
    "    language = detect(text)\n",
    "    sentiment = TextBlob(text).sentiment.polarity\n",
    "    return language, sentiment\n",
    "st.title(\"Language Detection and Sentiment Analysis\")\n",
    "text = st.text_input(\"Enter some text:\")\n",
    "language, sentiment = detect_language_and_sentiment(text)\n",
    "st.write(f\"Detected language: {language}\")\n",
    "st.write(f\"Sentiment polarity: {sentiment}\") "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.10.5"
  },
  "orig_nbformat": 4
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
