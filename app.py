
import streamlit as st
import pickle
import numpy as np

# Load trained model
model = pickle.load(open('heart_model.pkl', 'rb'))

# Title
st.title("Heart Disease Risk Predictor")

st.write("Enter patient clinical details below:")

# User Inputs
age = st.slider("Age", 20, 100, 50)

sex = st.selectbox(
    "Sex",
    [0, 1]
)

cp = st.slider("Chest Pain Type (cp)", 0, 3, 1)

trestbps = st.slider(
    "Resting Blood Pressure",
    80,
    200,
    120
)

chol = st.slider(
    "Cholesterol",
    100,
    600,
    200
)

fbs = st.selectbox(
    "Fasting Blood Sugar",
    [0, 1]
)

restecg = st.slider(
    "Resting ECG",
    0,
    2,
    1
)

thalach = st.slider(
    "Maximum Heart Rate",
    60,
    220,
    150
)

exang = st.selectbox(
    "Exercise Induced Angina",
    [0, 1]
)

oldpeak = st.slider(
    "Oldpeak",
    0.0,
    6.0,
    1.0
)

slope = st.slider(
    "Slope",
    0,
    2,
    1
)

ca = st.slider(
    "Number of Major Vessels",
    0,
    4,
    0
)

thal = st.slider(
    "Thal",
    0,
    3,
    1
)

# Create input array
input_data = np.array([
    age,
    sex,
    cp,
    trestbps,
    chol,
    fbs,
    restecg,
    thalach,
    exang,
    oldpeak,
    slope,
    ca,
    thal
]).reshape(1, -1)

# Prediction Button
if st.button("Predict Heart Disease Risk"):

    prediction = model.predict(input_data)

    if prediction[0] == 1:
        st.error("High Risk of Heart Disease Detected")
    else:
        st.success("Low Risk of Heart Disease")
