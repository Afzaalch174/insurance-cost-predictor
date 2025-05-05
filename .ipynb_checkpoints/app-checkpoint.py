{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "44c23cb2-7d3f-4f36-bc86-8ec18280e9d6",
   "metadata": {},
   "outputs": [],
   "source": [
    "import streamlit as st\n",
    "import numpy as np\n",
    "import pandas as pd\n",
    "import pickle\n",
    "\n",
    "# Load the trained model\n",
    "with open('insurance_model.pkl', 'rb') as file:\n",
    "    model = pickle.load(file)\n",
    "\n",
    "# App title\n",
    "st.title(\"💰 Medical Insurance Cost Prediction App\")\n",
    "st.write(\"Enter the patient's details to estimate the insurance charges.\")\n",
    "\n",
    "# Input form\n",
    "age = st.number_input(\"Age\", min_value=1, max_value=100, value=30)\n",
    "sex = st.selectbox(\"Sex\", (\"Male\", \"Female\"))\n",
    "bmi = st.number_input(\"BMI (Body Mass Index)\", min_value=10.0, max_value=50.0, value=25.0)\n",
    "children = st.number_input(\"Number of Children\", min_value=0, max_value=10, value=1)\n",
    "smoker = st.selectbox(\"Smoker\", (\"Yes\", \"No\"))\n",
    "region = st.selectbox(\"Region\", (\"Southeast\", \"Southwest\", \"Northeast\", \"Northwest\"))\n",
    "\n",
    "# Preprocess input\n",
    "sex_val = 0 if sex == \"Male\" else 1\n",
    "smoker_val = 0 if smoker == \"Yes\" else 1\n",
    "region_map = {\"Southeast\": 0, \"Southwest\": 1, \"Northeast\": 2, \"Northwest\": 3}\n",
    "region_val = region_map[region]\n",
    "\n",
    "# Prediction\n",
    "if st.button(\"Predict Insurance Cost\"):\n",
    "    input_data = np.array([[age, sex_val, bmi, children, smoker_val, region_val]])\n",
    "    prediction = model.predict(input_data)\n",
    "    st.success(f\"Estimated Insurance Charges: ${prediction[0]:,.2f}\")\n"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.13.1"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
