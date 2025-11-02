🍽️ Smart Restaurant Review Assistant

🧠 Overview
Smart Restaurant Review Assistant is an AI-powered web app built with Streamlit that analyzes customer reviews to determine their sentiment (Positive or Negative) and provides personalized suggestions for improvement.

It combines:
Machine Learning (sentiment classification using TF-IDF & Naive Bayes)
Natural Language Processing (NLP) (keyword detection for contextual feedback)
This assistant helps restaurants instantly understand customer opinions and make data-driven improvements.

🚀 Features
✅ Classifies reviews as Positive 😊 or Negative 😞
✅ Provides contextual suggestions based on keywords in feedback
✅ Displays randomized conversational replies for a human-like experience
✅ Clean, modern Streamlit interface with centered layout and footer
✅ Runs fully offline or on Google Colab / local machine
✅ Easy to retrain with new restaurant review data

🧩 Tech Stack

Component	      Technology Used

Language	      Python 3.10+
Frontend	      Streamlit
ML Library	    scikit-learn
Vectorization	  TF-IDF (Term Frequency–Inverse Document Frequency)
Serialization	  pickle / joblib
NLP Layer	      Keyword-based contextual improvement engine

🧠 How It Works
Input Review – User enters a restaurant review (e.g., “The food was best but the service was slow.”)
Text Processing – Review is transformed into numerical features using TF-IDF Vectorizer.
Prediction – The trained model predicts the sentiment as Positive or Negative.
Keyword Engine – Detects specific keywords (e.g., food, service, price, ambience) and tailors suggestions.

Dynamic Reply – A random friendly AI-style response is shown to make the app more engaging.
