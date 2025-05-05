import numpy as np
from tensorflow.keras.preprocessing.sequence import pad_sequences
from utils import get_word_index
from tensorflow.keras.models import load_model


model = load_model("sentiment_model.h5")
word_index = get_word_index()
word_to_index = word_index

def encode_text(text, vocab_size=10000):
    words = text.lower().split()
    encoded = [1]
    for word in words:
        index = word_to_index.get(word, 2)
        if index < vocab_size:
            encoded.append(index)
    return encoded

def predict_sentiment(text, maxlen=500):
    encoded = encode_text(text)
    padded = pad_sequences([encoded], maxlen=maxlen, padding='pre', truncating='pre', value=0)
    prediction = model.predict(padded)[0][0]
    label = "Positive" if prediction >= 0.5 else "Negative"
    print(f"\nReview: {text}")
    print(f"Predicted Sentiment: {label} ({prediction:.2f})")

if __name__ == "__main__":
    review = input("Enter a movie review:\n> ")
    predict_sentiment(review)
