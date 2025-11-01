🍽️ Smart Restaurant Review Assistant

🧠 Overview

Smart Restaurant Review Assistant is an AI-powered web app built using Streamlit that analyzes customer reviews to determine their sentiment (Positive or Negative) and provides dynamic improvement suggestions based on the content of the feedback.

It combines Machine Learning (sentiment classification) with Natural Language Processing (keyword analysis) to help restaurants gain insights from customer feedback in real-time.

🚀 Features

✅ Classifies restaurant reviews as Positive 😊 or Negative 😞
✅ Provides dynamic suggestions (e.g., improve service, taste, hygiene, etc.)
✅ Displays randomized conversational replies for more natural interaction
✅ Clean Streamlit UI with one-line title and bottom-fixed footer
✅ Lightweight — runs entirely on local machine or Google Colab

🧩 Tech Stack

Python 3.10+

Streamlit – Frontend web framework

scikit-learn – Model training & prediction

pickle / joblib – Model & vectorizer serialization

NLP – Keyword-based improvement suggestion logic

📁 Project Structure
📦 Smart_Restaurant_Review_Assistant
├── app.py                         # Streamlit main application
├── BoW_Sentiment_Model.pkl        # Saved CountVectorizer (Bag of Words)
├── Classifier_Sentiment_Model     # Trained classifier (e.g., Naive Bayes)
├── requirements.txt               # Dependencies
└── README.md                      # Project documentation

🧠 How It Works

The trained sentiment analysis model classifies reviews as Positive (1) or Negative (0).

The app’s keyword engine identifies review topics like food, service, price, ambience, etc.

It generates a context-aware suggestion (e.g., “Improve service speed” or “Maintain food quality”).

A random AI-style reply is displayed for human-like interaction.
