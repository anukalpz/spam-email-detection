# 🚀 Spam Email Detection System

🔗 **Live Demo:**  
👉 https://spam-email-detection-anukalpz.streamlit.app

🚀 A real-time **Spam Email Detection Web Application** built using **Machine Learning and NLP**, deployed with **Streamlit**.

This project classifies emails as **Spam ❌** or **Not Spam ✅** using a **hybrid approach** combining:
- Machine Learning models
- Rule-based spam detection
- Natural Language Processing techniques

---

## 🧠 Problem Statement
Spam emails are a major cybersecurity threat and are commonly used for:
- Phishing attacks  
- Fake lottery & reward scams  
- Account compromise attempts  

The goal of this project is to **automatically detect spam emails** with high accuracy using only the email text.

---

## ✨ Features
✔ Real-time spam detection  
✔ Hybrid **ML + rule-based** approach  
✔ Handles real-world & unseen messages  
✔ Fast and lightweight predictions  
✔ User-friendly web interface  

---

## 🛠 Tech Stack
- **Programming Language:** Python  
- **Web Framework:** Streamlit  
- **Machine Learning Models:**  
  - Logistic Regression  
  - Random Forest  
  - Linear SVM (Final Model)  
- **NLP Techniques:**  
  - TF-IDF Vectorization  
  - Lemmatization  
  - Stopword Removal  
- **Dataset:** SMS Spam Collection Dataset  

---

## 📊 Model Performance

| Model | Accuracy |
|------|----------|
| Logistic Regression | 96.5% |
| Random Forest | 97.7% |
| **Linear SVM (Final Model)** | **98.3%** |

📌 **Final Model Selected:** Balanced Linear SVM  
**Reason:** High accuracy and better spam recall on imbalanced data.

---

## ⚙️ How It Works
1. User enters an email message  
2. Text preprocessing (cleaning & lemmatization)  
3. TF-IDF feature extraction  
4. Hybrid checks:
   - Rule-based spam patterns  
   - ML-based classification  
5. Instant spam / not-spam prediction  

---

## 🌐 Web Application
The system is deployed using **Streamlit**, allowing users to:
- Paste any email text
- Instantly check whether it is **Spam ❌** or **Not Spam ✅**

---

## 📂 Project Structure

Spam_mail_detection/
│
├── app.py # Streamlit web app
├── spam_model.pkl # Trained ML model
├── tfidf.pkl # TF-IDF vectorizer
├── Spam_email_detection.ipynb # Model training notebook
├── dataset.csv # Dataset
├── requirements.txt # Dependencies
└── README.md # Project documentation
---

## 🧪 Example Predictions

| Email Text | Prediction |
|-----------|------------|
| "Congratulations! You won a free iPhone" | Spam ❌ |
| "Are we still meeting tomorrow at 10?" | Not Spam ✅ |
| "Claim your ₹1,00,000 lottery prize now" | Spam ❌ |

---

## 🚧 Limitations
- Uses only email text (no sender/domain metadata)
- Does not analyze attachments or deep URL reputation

> Real-world systems also use sender reputation, links, and user feedback.

---

## 🔮 Future Improvements
- URL and sender domain analysis  
- Email attachment inspection  
- Gmail / Outlook integration  
- Deep Learning models (LSTM / Transformers)  
- Continuous learning via user feedback  

---

## 👨‍💻 Author
**Anukalp Shukla**  
B.Tech – Computer Science  
NLP
---

## ⭐ Final Note
This project demonstrates **end-to-end ML deployment, from model training to a fully functional web application, making it suitable for academic projects, portfolios, and interviews.
