# emotions.py – simple sentiment analysis with TextBlob

from textblob import TextBlob

def analyze_emotion(text):
    """
    Analyze the sentiment polarity of `text`:
      - Returns a tuple (emotion_label, polarity_score)
      - Polarity > 0.1   → "positive"
      - Polarity < -0.1  → "negative"
      - Otherwise        → "neutral"
    """
    blob = TextBlob(text)                   # Create a TextBlob object
    polarity = blob.sentiment.polarity      # Float in [-1.0, 1.0]
    
    # Classify into three buckets
    if polarity > 0.1:
        emotion = "positive"
    elif polarity < -0.1:
        emotion = "negative"
    else:
        emotion = "neutral"
    
    return emotion, polarity
