import streamlit as st
import requests

# FastAPI backend URL
API_URL = "http://127.0.0.1:8000/predict"

st.set_page_config(page_title="Student Risk Predictor", page_icon="🎓", layout="wide")

# --- Custom CSS ---
st.markdown("""
    <style>
        .main {
            background-color: #f9f9f9;
            padding: 2rem;
        }
        h1 {
            color: #2c3e50;
            text-align: center;
        }
        .risk-card {
            padding: 1.5rem;
            border-radius: 12px;
            text-align: center;
            font-size: 1.5rem;
            font-weight: bold;
        }
        .low { background-color: #d4edda; color: #155724; }
        .medium { background-color: #fff3cd; color: #856404; }
        .high { background-color: #f8d7da; color: #721c24; }
    </style>
""", unsafe_allow_html=True)

st.title("🎓 Student Risk Prediction")
st.write("Provide student details to predict **risk category** (Low, Medium, High).")

# --- Tabs for inputs ---
tabs = st.tabs(["📊 Demographics", "📚 Academics", "🏠 Family & Support", "🎯 Lifestyle"])

with tabs[0]:
    col1, col2 = st.columns(2)
    with col1:
        age = st.number_input("Age", 10, 30, 16)
        sex = st.selectbox("Sex", ["F","M"])
        address = st.selectbox("Address", ["U","R"])
        famsize = st.selectbox("Family Size", ["LE3","GT3"])
        Pstatus = st.selectbox("Parent Status", ["T","A"])
        school = st.selectbox("School", ["GP","MS"])
    with col2:
        Medu = st.selectbox("Mother Education (0-4)", [0,1,2,3,4])
        Fedu = st.selectbox("Father Education (0-4)", [0,1,2,3,4])
        Mjob = st.selectbox("Mother Job", ["teacher","health","services","at_home","other"])
        Fjob = st.selectbox("Father Job", ["teacher","health","services","at_home","other"])
        reason = st.selectbox("Reason for School", ["home","reputation","course","other"])
        guardian = st.selectbox("Guardian", ["mother","father","other"])

with tabs[1]:
    col1, col2 = st.columns(2)
    with col1:
        G1 = st.number_input("Grade 1 (0-20)", 0, 20, 10)
        G2 = st.number_input("Grade 2 (0-20)", 0, 20, 12)
        studytime = st.selectbox("Study Time (1-4)", [1,2,3,4])
        traveltime = st.selectbox("Travel Time (1-4)", [1,2,3,4])
    with col2:
        failures = st.number_input("Failures", 0, 5, 0)
        absences = st.number_input("Absences", 0, 100, 2)

with tabs[2]:
    col1, col2 = st.columns(2)
    with col1:
        schoolsup = st.selectbox("School Support", ["yes","no"])
        famsup = st.selectbox("Family Support", ["yes","no"])
        paid = st.selectbox("Extra Paid Classes", ["yes","no"])
        higher = st.selectbox("Wants Higher Education", ["yes","no"])
    with col2:
        nursery = st.selectbox("Nursery Attended", ["yes","no"])
        activities = st.selectbox("Activities", ["yes","no"])
        internet = st.selectbox("Internet Access", ["yes","no"])
        romantic = st.selectbox("Romantic Relationship", ["yes","no"])

with tabs[3]:
    col1, col2 = st.columns(2)
    with col1:
        famrel = st.slider("Family Relationship (1-5)", 1, 5, 4)
        freetime = st.slider("Free Time (1-5)", 1, 5, 3)
        goout = st.slider("Go Out (1-5)", 1, 5, 3)
    with col2:
        Dalc = st.slider("Workday Alcohol (1-5)", 1, 5, 1)
        Walc = st.slider("Weekend Alcohol (1-5)", 1, 5, 2)
        health = st.slider("Health (1-5)", 1, 5, 3)

# --- Submit Button ---
if st.button(" Predict Risk", use_container_width=True):
    student_data = {
        "age": age, "Medu": Medu, "Fedu": Fedu, "traveltime": traveltime,
        "studytime": studytime, "failures": failures, "famrel": famrel,
        "freetime": freetime, "goout": goout, "Dalc": Dalc, "Walc": Walc,
        "health": health, "absences": absences, "G1": G1, "G2": G2,
        "school": school, "sex": sex, "address": address, "famsize": famsize,
        "Pstatus": Pstatus, "Mjob": Mjob, "Fjob": Fjob, "reason": reason,
        "guardian": guardian, "schoolsup": schoolsup, "famsup": famsup,
        "paid": paid, "activities": activities, "nursery": nursery,
        "higher": higher, "internet": internet, "romantic": romantic
    }

    response = requests.post(API_URL, json=student_data)

    if response.status_code == 200:
        risk = response.json()['risk_category']

        # Show result as styled card
        if risk == "Low Risk":
            st.markdown(f"<div class='risk-card low'>🟢 Predicted Risk: {risk}</div>", unsafe_allow_html=True)
        elif risk == "Medium Risk":
            st.markdown(f"<div class='risk-card medium'>🟠 Predicted Risk: {risk}</div>", unsafe_allow_html=True)
        else:
            st.markdown(f"<div class='risk-card high'>🔴 Predicted Risk: {risk}</div>", unsafe_allow_html=True)
    else:
        st.error("❌ Error: Could not get prediction")

# Footer
st.markdown("<br><hr><center>Developed by Ziad Mohamed | Student Risk ML Model </center>", unsafe_allow_html=True)
