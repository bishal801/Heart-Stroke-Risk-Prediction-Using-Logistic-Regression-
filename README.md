❤️ Heart Stroke Risk Prediction

An interactive web application built with Streamlit that predicts the risk of heart disease based on user-provided health parameters.
The machine learning backend is powered by a Logistic Regression model trained on a labeled dataset of heart health records.

🚀 Features

✔️ Real-time prediction of high or low risk of heart disease.
✔️ User-friendly web interface built with Streamlit.
✔️ Uses clinically important features like Age, Chest Pain Type, Cholesterol, Blood Pressure, and more.
✔️ Instant visual feedback with a clean and modern UI.


🖼️ Demo Screenshots
🔹 Low Risk Example
<img width="739" height="849" alt="Screenshot 2025-10-01 223936" src="https://github.com/user-attachments/assets/8830e3bb-89cd-4a32-932c-c316754d4977" />




🔹 High Risk Example
<img width="528" height="833" alt="Screenshot 2025-10-01 224116" src="https://github.com/user-attachments/assets/ea6b7299-534f-4847-951f-e736e8a62e63" />



⚙️ How It Works

The app collects user health information such as:

Age, Gender, Chest Pain Type

Resting Blood Pressure, Cholesterol, Fasting Blood Sugar

Resting ECG, Max Heart Rate, Exercise-Induced Angina

Oldpeak (ST Depression), ST Slope

Inputs are preprocessed and scaled before being passed into the trained Logistic Regression model.

The model outputs the probability of heart disease risk, which is classified into Low Risk or High Risk.

🛠️ Setup and Usage

Clone the repository:

git clone https://github.com/your-username/heart-stroke-risk-prediction.git
cd heart-stroke-risk-prediction


Install dependencies:

# Using conda
conda install joblib streamlit pandas scikit-learn

# Or using pip
pip install joblib streamlit pandas scikit-learn


Run the app:

streamlit run app.py


Open the provided local URL in your browser to interact with the app.

📁 Project Structure

app.py → Main Streamlit web application

model.pkl → Pretrained Logistic Regression model

scaler.pkl → Feature scaling object

columns.pkl → Saved feature list for input alignment

Screenshots/ → Example results for Low/High risk

📊 Model Information

Algorithm: Logistic Regression

Features:

Age, Sex, ChestPainType, RestingBP, Cholesterol, FastingBS,

RestingECG, MaxHR, ExerciseAngina, Oldpeak, ST_Slope

Dataset: Processed and one-hot encoded heart health dataset

Preprocessing: Matches training-time transformations for robust predictions

🤝 Contributing

💡 Feel free to open issues or submit pull requests for improvements.
🚑 Together, we can make AI-driven heart health prediction more accessible.
