import streamlit as st
import requests

API_URL = "http://localhost:8000/predict"

st.title("Insurance Premium Prediction")

st.markdown("Enter your details below to predict your insurance premium.")

age = st.number_input("Age", min_value=1, max_value=120, step=1)
weight = st.number_input("Weight (in kg)", min_value=1.0, step=0.1)
height = st.number_input("Height (in meters)", min_value=0.1, step=0.01)
income_lpa = st.number_input("Income (in LPA)", min_value=0, step=1)
smoker = st.selectbox("Are you a smoker?", options=[True, False])
city = st.text_input("City",value="faridabad")
occupation = st.selectbox("Occupation", options=['teacher', 'doctor', 'army', 'police'])

if st.button("Predict Premium"):
    user_data = {
        "age": age,
        "weight": weight,
        "height": height,
        "income_lpa": income_lpa,
        "smoker": smoker,
        "city": city,
        "occupation": occupation
    }

    response = requests.post(API_URL, json=user_data)

    try:
        response=requests.post(API_URL, json=user_data)
        if response.status_code == 200:
            result = response.json()
            st.success(f"Predicted Insurance Premium: {result['prediction']}")
        else:
            st.error(f"Error: {response.status_code} - {response.text}")
    except requests.exceptions.RequestException as e:
        st.error(f"Request failed: {e}")