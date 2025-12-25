🩺 Patient Readmission Risk Prediction System

An end-to-end Machine Learning–powered healthcare dashboard that predicts 30-day patient readmission risk using clinical, demographic, and lab data.
The system is deployed using Streamlit and runs on AWS SageMaker.

---

🚀 Project Overview

Hospital readmissions are costly and often preventable.
This project helps healthcare professionals:

Identify high-risk patients

Take preventive actions before discharge

Improve patient outcomes using data-driven insights

The solution uses a Random Forest classifier trained on synthetic patient data and provides real-time predictions through a clean Streamlit dashboard.

---

## 🏗️ System Architecture
flowchart TD
    A["Patient Data (CSV or User Input)"]
    B["Data Preprocessing (Scaling & Encoding)"]
    C["Machine Learning Model (Random Forest)"]
    D["Streamlit Dashboard"]
    E["AWS SageMaker Environment"]

    A --> B
    B --> C
    C --> D
    D --> E
Architecture Explanation

Patient Data: Synthetic dataset or manual user input

Preprocessing: Encoding categorical features and scaling numerical values (preprocessor.pkl)

ML Model: Random Forest classifier (model.pkl)

Dashboard: Streamlit app for real-time predictions

Cloud Platform: Hosted and executed on AWS SageMaker


**Cloud Platform:** AWS SageMaker  
**Monitoring Ready:** CloudWatch (future extension)

---

## 📌 Features

- 🔍 **Real-time patient risk prediction**
- 📊 **Probability-based readmission score**
- 🧪 Uses **lab results & vitals**
- 🖥️ Professional **Streamlit UI**
- ☁️ Runs on **AWS SageMaker**
- 📦 Trained model & preprocessor saved as `.pkl`

---

## 🗂️ Project Structure

healthcare/
├── app.py # Streamlit dashboard
├── data/
│ └── synthetic_patients.csv # Synthetic healthcare dataset
├── model.pkl # Trained ML model
├── preprocessor.pkl # Data preprocessing pipeline
├── healthcare.ipynb # Model training notebook
├── requirements.txt # Dependencies
└── README.md # Project documentation


---

## 🧾 Dataset

- **Type:** Synthetic patient healthcare dataset
- **Records:** 2,000 patients
- **Features:**
  - Age
  - Gender
  - Admission Type
  - Length of Stay
  - Previous Admissions
  - Lab Glucose
  - Hemoglobin
  - Cholesterol
  - Creatinine
  - Blood Pressure
  - Heart Rate
  - Temperature
- **Target:** `readmitted` (0 = No, 1 = Yes)

---

## 🧠 Machine Learning Model

- **Algorithm:** Random Forest Classifier
- **Preprocessing:**
  - Numeric scaling
  - Categorical encoding
- **Artifacts:**
  - `model.pkl`
  - `preprocessor.pkl`

---

## 🖥️ Running the Application

##
1️⃣ Install Dependencies

```bash
pip install -r requirements.txt

2️⃣ Start Streamlit App
streamlit run app.py

3️⃣ Open Browser
https://patient-risk-notebook-i0dz.notebook.eu-north-1.sagemaker.aws/proxy/8501/

📊 Dashboard Pages

🏠 Home: Project overview

📝 Predict Risk: Enter patient details & get risk score

📈 Model Info: Model and feature information

☁️ Deployment

Developed and tested in AWS SageMaker JupyterLab

Supports extension to:

SageMaker Endpoints

API Gateway

CloudWatch Monitoring

🔮 Future Enhancements

SHAP-based explainability

Doctor alert system

Real EHR data integration

Authentication & access control

Deployment as SageMaker Endpoint

👩‍💻 Author

Priya Phulpagar
🔗 GitHub: https://github.com/PRIYA-PHULPAGAR

