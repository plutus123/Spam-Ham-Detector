import joblib
import pandas as pd
import numpy as np
import streamlit as st
model = joblib.load(open("xgb.pkl", "rb"))

vect = joblib.load(open("vectorizer.pkl", "rb"))



def predict_spam_or_ham(msg):
    test_vector = vect.transform([msg])
    prediction = model.predict(test_vector)
    return prediction[0]


# Streamlit app
st.title("Spam/Ham Detector")

# User input for message
user_input = st.text_area("Enter a message:")

# Make prediction when user clicks the button
if st.button("Predict"):
    if user_input:
        prediction = predict_spam_or_ham(user_input)
        st.write(f"Prediction: {'Spam' if prediction == 1 else 'Ham'}")
    else:
        st.warning("Please enter a message.")