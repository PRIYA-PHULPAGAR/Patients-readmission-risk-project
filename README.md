# 🩺 Patient Readmission Risk Prediction Dashboard

A professional **Streamlit-based healthcare dashboard** that predicts the **30-day hospital readmission risk** of patients using machine learning.  
Built, trained, and deployed using **Python, Scikit-learn, Streamlit, and AWS SageMaker**.

---

## 🚀 Project Overview

Hospital readmissions increase healthcare costs and impact patient outcomes.  
This project uses **machine learning** to predict whether a patient is at risk of readmission within **30 days** based on demographics, lab results, and vitals — allowing doctors to intervene early.

---

## 🏗️ System Architecture

## 🏗️ System Architecture

```mermaid
flowchart TD
    A[Patient Data<br/>(CSV / User Input)] --> B[Data Preprocessing<br/>(Scaling & Encoding)<br/>preprocessor.pkl]
    B --> C[ML Model<br/>Random Forest<br/>model.pkl]
    C --> D[Streamlit Dashboard<br/>Risk % & Category]


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

### 1️⃣ Install Dependencies

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

