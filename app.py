import streamlit as st
import pandas as pd
import joblib

# Load the saved model and related files
model = joblib.load('logictic_regression_heart.pkl')
scaler = joblib.load('scaler.pkl')
expected_columns = joblib.load('columns.pkl')

# Page config and title
st.set_page_config(page_title="Heart Stroke Risk Predictor", layout="centered")
st.title('❤️ Heart Stroke Risk Prediction')
st.markdown('### Please provide the following information:')

# All inputs in single vertical column
age = st.slider('Age', 18, 100, 40, help="Age of the patient in years")
gender = st.selectbox('Gender', ['M', 'F'], help="Select your gender (M/F)")
chest_pain = st.selectbox('Chest Pain Type', ['ATA', 'NAP', 'TA', 'ASY'], help="Atypical or typical chest pain type")
resting_blood_pressure = st.number_input('Resting Blood Pressure (mm Hg)', min_value=80, max_value=200, value=120)
cholesterol = st.number_input('Cholesterol (mg/dL)', min_value=100, max_value=600, value=200)
fasting_blood_sugar = st.selectbox('Fasting Blood Sugar > 120 mg/dl', [0, 1], format_func=lambda x: 'Yes' if x else 'No')
resting_ecg = st.selectbox('Resting ECG', ['Normal', 'ST', 'LVH'], help="Resting electrocardiographic results")
max_heart_rate = st.slider('Max Heart Rate', 60, 220, 150)
exercise_angina = st.selectbox('Exercise Induced Angina', ['Y', 'N'], help="Whether exercise induced angina is present")
oldpeak = st.slider('Oldpeak (ST Depression)', 0.0, 6.0, 1.0)
st_slope = st.selectbox('ST Slope', ['Up', 'Flat', 'Down'], help="Slope of the peak exercise ST segment")

if st.button('Predict Risk'):
    with st.spinner('Predicting...'):
        raw_input = {
            'Age': age,
            'Sex': gender,
            'ChestPainType': chest_pain,
            'RestingBP': resting_blood_pressure,
            'Cholesterol': cholesterol,
            'FastingBS': fasting_blood_sugar,
            'RestingECG': resting_ecg,
            'MaxHR': max_heart_rate,
            'ExerciseAngina': exercise_angina,
            'Oldpeak': oldpeak,
            'ST_Slope': st_slope
        }

        input_df = pd.DataFrame([raw_input])

        # One-hot encode categorical columns to match training
        categorical_cols = ['Sex', 'ChestPainType', 'ExerciseAngina', 'RestingECG', 'ST_Slope']
        input_df = pd.get_dummies(input_df, columns=categorical_cols)

        # Add missing expected columns with 0 values
        for col in expected_columns:
            if col not in input_df.columns:
                input_df[col] = 0

        # Reorder columns to expected order
        input_df = input_df[expected_columns]

        # Scale input features
        scaled_input = scaler.transform(input_df)

        prediction = model.predict(scaled_input)[0]

        if prediction == 0:
            st.success('✅ LOW Risk of Heart Disease')
        else:
            st.error('🚨 HIGH Risk of Heart Disease')

st.markdown("---")
st.markdown("Developed with ❤️ for Heart Disease prediction.")
