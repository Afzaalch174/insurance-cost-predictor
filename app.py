import streamlit as st
import numpy as np
import pandas as pd
import pickle

# Load the trained model
with open('insurance_model.pkl', 'rb') as file:
    model = pickle.load(file)

# App title
st.title("💰 Medical Insurance Cost Prediction App")
st.write("Enter the patient's details to estimate the insurance charges.")

# Input form
age = st.number_input("Age", min_value=1, max_value=100, value=30)
sex = st.selectbox("Sex", ("Male", "Female"))
bmi = st.number_input("BMI (Body Mass Index)", min_value=10.0, max_value=50.0, value=25.0)
children = st.number_input("Number of Children", min_value=0, max_value=10, value=1)
smoker = st.selectbox("Smoker", ("Yes", "No"))
region = st.selectbox("Region", ("Southeast", "Southwest", "Northeast", "Northwest"))

# Preprocess input
sex_val = 0 if sex == "Male" else 1
smoker_val = 0 if smoker == "Yes" else 1
region_map = {"Southeast": 0, "Southwest": 1, "Northeast": 2, "Northwest": 3}
region_val = region_map[region]

# Predict
if st.button("Predict Insurance Cost"):
    input_data = np.array([[age, sex_val, bmi, children, smoker_val, region_val]])
    prediction = model.predict(input_data)
    st.success(f"Estimated Insurance Charges: ${prediction[0]:,.2f}")
