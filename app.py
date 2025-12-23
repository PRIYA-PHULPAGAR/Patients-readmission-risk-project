
import streamlit as st
import pandas as pd
import numpy as np
import joblib

# -----------------------------------------------------------------------
# LOAD MODEL + PREPROCESSOR
# -----------------------------------------------------------------------
@st.cache_resource
def load_model():
    try:
        model = joblib.load("model.pkl")
        preprocessor = joblib.load("preprocessor.pkl")
        return model, preprocessor
    except:
        st.error("⚠ Model files not found! Please upload model.pkl and preprocessor.pkl.")
        return None, None

model, preprocessor = load_model()

# -----------------------------------------------------------------------
# PAGE SETUP
# -----------------------------------------------------------------------
st.set_page_config(
    page_title="Patient Readmission Risk Dashboard",
    layout="wide",
    page_icon="🩺"
)

st.markdown("""
    <h1 style='text-align:center; color:#2C3E50;'>🩺 Patient Readmission Risk Prediction</h1>
    <p style='text-align:center; font-size:18px;'>AI-powered dashboard to estimate 30-day readmission risk.</p>
""", unsafe_allow_html=True)
st.write("---")

# -----------------------------------------------------------------------
# SIDEBAR
# -----------------------------------------------------------------------
st.sidebar.title("📊 Navigation")
page = st.sidebar.radio("Go to", ["🏠 Home", "📝 Predict Risk", "📈 Model Info"])

# -----------------------------------------------------------------------
# HOME PAGE
# ---------------------------------------------------------------------

if page == "🏠 Home":
    st.subheader("Overview")
    st.write("""
    This AI system predicts whether a patient is at risk of being readmitted
    within 30 days after discharge.
    """)

elif page == "📝 Predict Risk":
    st.header("📝 Enter Patient Information")

    col1, col2, col3 = st.columns(3)

    with col1:
        age = st.slider("Age", 18, 100, 45)
        gender = st.selectbox("Gender", ["Male", "Female"])
        admission_type = st.selectbox("Admission Type", ["Emergency", "Elective", "Urgent"])

    with col2:
        length_of_stay = st.number_input("Length of Stay (days)", 1, 30, 4)
        previous_admissions = st.number_input("Previous Admissions", 0, 10, 1)
        lab_glucose = st.number_input("Lab Glucose", 50.0, 300.0, 120.0)

    with col3:
        lab_hemoglobin = st.number_input("Hemoglobin Level", 5.0, 20.0, 13.5)
        cholesterol = st.number_input("Cholesterol", 100, 300, 180)
        creatinine = st.number_input("Creatinine", 0.2, 5.0, 1.0)
        blood_pressure = st.number_input("Blood Pressure", 80, 200, 120)
        heart_rate = st.number_input("Heart Rate", 40, 160, 75)
        temperature = st.number_input("Temperature", 95.0, 105.0, 98.6)

    # 🔴 BUTTON MUST ALSO BE HERE
    if st.button("🔍 Predict Risk"):
        if model is None:
            st.stop()

        FEATURE_COLUMNS = [
            'age','gender','admission_type','length_of_stay',
            'previous_admissions','lab_glucose','lab_hemoglobin',
            'cholesterol','creatinine','blood_pressure',
            'heart_rate','temperature'
        ]

        input_data = pd.DataFrame([[
            age, gender, admission_type, length_of_stay,
            previous_admissions, lab_glucose, lab_hemoglobin,
            cholesterol, creatinine, blood_pressure,
            heart_rate, temperature
        ]], columns=FEATURE_COLUMNS)

        prob = model.predict_proba(input_data)[0][1]
        risk = prob * 100

        st.success(f"Readmission Risk: {risk:.2f}%")


elif page == "📈 Model Info":
    st.header("📈 Model Details")
    st.write("""
    - Model: Random Forest Classifier
    - Features: Labs, vitals, demographics
    - Use case: Early readmission detection
    """)
