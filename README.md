❤️ Heart Stroke Risk Prediction
An interactive web application built with Streamlit that predicts the risk of heart disease based on user-provided health parameters. The machine learning backend is powered by a logistic regression model trained on a labeled dataset of heart health records.

🚀 Features
Predicts high or low risk of heart disease in real-time.

User-friendly web interface built with Streamlit.

Model uses important clinical features such as age, chest pain type, cholesterol, blood pressure, and more.

Real-time feedback and visually appealing UI.

🛠 How It Works
The app collects user information such as Age, Gender, Chest Pain Type, Resting Blood Pressure, Cholesterol, and other heart health indicators. These inputs are processed, scaled, and passed to a trained logistic regression model, which outputs the probability of heart disease risk.

🖼️ Demo Screenshots
Low Risk Example
![Low Risk Result](Screenshot-2025-10-01-223 Risk Example
![High Risk Result](Screenshot-2025-10-01-224️ Setup and Usage

Clone the repository:

bash
git clone https://github.com/your-username/heart-stroke-risk-prediction.git
cd heart-stroke-risk-prediction
Install dependencies:

bash
conda install joblib streamlit pandas scikit-learn
# or
pip install joblib streamlit pandas scikit-learn
Run the app:

bash
streamlit run app.py
Open the provided local URL in your browser to interact with the app.

📁 Files
app.py : Streamlit web application.

Pretrained .pkl machine learning model, scaler, and column files.

Example screenshots.

📊 Model Information
Logistic Regression trained on a processed and one-hot encoded dataset.

Features include: Age, Sex, Chest Pain Type, RestingBP, Cholesterol, FastingBS, RestingECG, MaxHR, ExerciseAngina, Oldpeak, and ST_Slope.

Preprocessing pipeline matches training-time feature engineering for robust predictions.

🤝 Contributing
Feel free to submit issues or pull requests for improvements.
