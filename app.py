import streamlit as st
import pandas as pd
import numpy as np
import pickle

# Load the model and cleaned dataset
model = pickle.load(open('C:\\Users\\91933\\OneDrive\\Desktop\\Car\\LinearRegressionModel.pkl', 'rb'))
car = pd.read_csv('Cleaned_Car_data.csv')

# Set up UI
st.set_page_config(page_title="Used Car Price Predictor", layout="centered")
st.title("🚗 Used Car Price Predictor")

# Dropdown values
companies = sorted(car['company'].unique())
car_models = sorted(car['name'].unique())
years = sorted(car['year'].unique(), reverse=True)
fuel_types = car['fuel_type'].unique()

# Sidebar Inputs
st.sidebar.header("Enter Car Details")
selected_company = st.sidebar.selectbox("Select Car Company", companies)
selected_model = st.sidebar.selectbox("Select Car Model", car_models)
selected_year = st.sidebar.selectbox("Select Year of Purchase", years)
selected_fuel = st.sidebar.selectbox("Select Fuel Type", fuel_types)
kms_driven = st.sidebar.number_input("Enter KMs Driven", min_value=0, step=100)

# Prediction trigger
if st.sidebar.button("Predict Selling Price"):

    # Create single row input DataFrame
    input_df = pd.DataFrame([[selected_model, selected_company, selected_year, kms_driven, selected_fuel]],
                            columns=['name', 'company', 'year', 'kms_driven', 'fuel_type'])

    # Combine with original dataset to get all dummy columns
    final_input = pd.concat([input_df, car[['name', 'company', 'year', 'kms_driven', 'fuel_type']]], axis=0)

    # One-hot encode
    final_input = pd.get_dummies(final_input, drop_first=True)

    # Select only the first row (user input)
    input_final = final_input.iloc[0:1]

    # Predict
    prediction = model.predict(input_final)[0]
    st.success(f"💰 Estimated Selling Price: ₹ {int(prediction):,}")
  
