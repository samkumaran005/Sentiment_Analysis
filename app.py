import streamlit as st
import pickle
import joblib
import random

# --- Load model and vectorizer ---
vectorizer = pickle.load(open('BoW_Sentiment_Model.pkl', 'rb'))
model = joblib.load('Classifier_Sentiment_Model')

# --- Page Setup ---
st.set_page_config(page_title="Smart Restaurant Review Assistant 🍔", page_icon="🍔", layout="centered")

# --- Custom CSS for styling ---
st.markdown("""
    <style>
    /* Center title and make it one line */
    .main-title {
        text-align: center;
        font-size: 2.2em;
        font-weight: 600;
        color: #333;
        margin-bottom: 0.2em;
    }

    /* Fix footer at bottom */
    .footer {
        position: fixed;
        left: 0;
        bottom: 0;
        width: 100%;
        background-color: #f9f9f9;
        text-align: center;
        padding: 8px 0;
        color: #555;
        font-size: 0.9em;
        border-top: 1px solid #ddd;
    }
    </style>
""", unsafe_allow_html=True)

# --- Title ---
st.markdown("<h1 class='main-title'>🍽️ Smart Restaurant Review Assistant</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center;'>Analyze customer reviews and get improvement suggestions instantly!</p>", unsafe_allow_html=True)

# --- Reply templates ---
positive_replies = [
    "That’s wonderful! We’ll make sure the team hears about this! 🎉",
    "We’re thrilled you enjoyed your experience! Thank you for the kind words. 😊",
    "Awesome! Your feedback motivates us to keep serving our best. 💪",
    "Great to hear that! We’re so glad you loved it. ❤️",
    "Fantastic! Hope to see you again soon for another great meal! 🍽️"
]

negative_replies = [
    "Sorry for your experience 😔 — we’ll work hard to fix it next time!",
    "We sincerely apologize for the inconvenience. Your feedback will help us improve.",
    "That’s disappointing to hear 😞, but we appreciate your honesty — we’ll make it right.",
    "We’re sorry this didn’t meet your expectations. Our team is working to improve.",
    "Thanks for letting us know. We’ll make sure your next visit is much better! 🙏"
]

# --- Dynamic Suggestion Generator ---
def generate_suggestion(review, sentiment):
    review = review.lower()
    if "service" in review or "waiter" in review or "staff" in review:
        suggestion = "Improve service speed and train staff for better customer interaction."
    elif "food" in review or "taste" in review or "dish" in review:
        suggestion = "Focus on maintaining consistent food quality and taste."
    elif "price" in review or "expensive" in review or "cost" in review:
        suggestion = "Consider adjusting prices or adding more value combos."
    elif "clean" in review or "hygiene" in review:
        suggestion = "Ensure cleanliness and hygiene are top priority."
    elif "ambience" in review or "music" in review or "lighting" in review:
        suggestion = "Enhance ambience with better lighting and pleasant background music."
    else:
        suggestion = "Keep improving customer experience based on feedback."

    if sentiment == "Positive 😊":
        suggestion = "Keep it up! " + suggestion
    else:
        suggestion = "Needs improvement: " + suggestion

    return suggestion

# --- Text Input ---
review = st.text_area("✍️ Enter a restaurant review:", placeholder="Example: The food was tasty but the service was slow.")

if st.button("🔍 Analyze Review"):
    if review.strip() == "":
        st.warning("Please enter a review first!")
    else:
        input_data = vectorizer.transform([review]).toarray()
        prediction = model.predict(input_data)[0]

        if prediction == 1:
            sentiment = "Positive 😊"
            color = "green"
            reply = random.choice(positive_replies)
        else:
            sentiment = "Negative 😞"
            color = "red"
            reply = random.choice(negative_replies)

        suggestion = generate_suggestion(review, sentiment)

        st.markdown(f"### Sentiment: <span style='color:{color}'>{sentiment}</span>", unsafe_allow_html=True)
        st.info(f"💡 Suggestion: {suggestion}")

        st.markdown("#### 🤖 Assistant says:")
        st.write(reply)

# --- Footer ---
st.markdown("<div class='footer'>AI-powered Review Assistant 🍔</div>", unsafe_allow_html=True)
