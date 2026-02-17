import nltk
nltk.download('stopwords')
nltk.download('wordnet')
import streamlit as st
import pickle
import re
import string
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

# ---------------- LOAD MODELS ----------------
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

with open(os.path.join(BASE_DIR, "tfidf.pkl"), "rb") as f:
    tfidf = pickle.load(f)

with open(os.path.join(BASE_DIR, "spam_model.pkl"), "rb") as f:
    model = pickle.load(f)


# ---------------- NLP SETUP ----------------
lemmatizer = WordNetLemmatizer()
stop_words = set(stopwords.words("english"))

def preprocess_text(text):
    text = text.lower()
    text = re.sub(r"\s+", " ", text)
    text = "".join(ch for ch in text if ch not in string.punctuation)
    words = text.split()
    words = [lemmatizer.lemmatize(w) for w in words if w not in stop_words]
    return " ".join(words)

# ---------------- RULES ----------------
phrase_keywords = [
    "click here", "verify", "urgent", "claim",
    "account suspended", "limited time", "free"
]

word_keywords = ["win", "lottery", "prize"]

def predict_spam(email_text):
    text_lower = email_text.lower()

    # rule-based
    for phrase in phrase_keywords:
        if phrase in text_lower:
            return "SPAM ❌ (rule-based)"

    for word in word_keywords:
        if re.search(rf"\b{word}\b", text_lower):
            return "SPAM ❌ (rule-based)"

    # ML-based
    clean_text = preprocess_text(email_text)
    vector = tfidf.transform([clean_text])
    pred = model.predict(vector)

    return "SPAM ❌" if pred[0] == 1 else "NOT SPAM ✅"

# ---------------- STREAMLIT UI ----------------
st.set_page_config(page_title="Spam Email Detection", layout="centered")

st.title("📧 Spam Email Detection System")
st.write("Enter an email message below to check whether it is Spam or Not Spam.")

user_input = st.text_area("✉️ Enter Email Text", height=200)

if st.button("🔍 Check"):
    if user_input.strip() == "":
        st.warning("Please enter some text.")
    else:
        result = predict_spam(user_input)
        if "SPAM" in result:
            st.error(result)
        else:
            st.success(result)
