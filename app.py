from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import pandas as pd

# Load trained model
model = joblib.load("D:/maim_project/best_rf_model.pkl")
feature_order = joblib.load("D:/maim_project/feature_order.pkl")  # ensure this exists

app = FastAPI()

# Input schema
class StudentInput(BaseModel):
    age: int
    Medu: int
    Fedu: int
    traveltime: int
    studytime: int
    failures: int
    famrel: int
    freetime: int
    goout: int
    Dalc: int
    Walc: int
    health: int
    absences: int
    G1: int
    G2: int
    school: str
    sex: str
    address: str
    famsize: str
    Pstatus: str
    Mjob: str
    Fjob: str
    reason: str
    guardian: str
    schoolsup: str
    famsup: str
    paid: str
    activities: str
    nursery: str
    higher: str
    internet: str
    romantic: str

# Preprocessing
def preprocess(data: dict):
    df = pd.DataFrame([data])

    # Engineered features
    df["Average_grade"] = (df["G1"] + df["G2"]) / 2
    df["parent_edu_avg"] = (df["Medu"] + df["Fedu"]) / 2
    df["attendance_ratio"] = df["absences"] / 100
    df["support_index"] = (df["schoolsup"].str.lower().map({"yes":1,"no":0}) +
                           df["famsup"].str.lower().map({"yes":1,"no":0}))
    df["leisure_score"] = (df["freetime"] + df["goout"]) / 2
    df["study_commitment"] = df["studytime"] / 4  # normalized to max=4
    df["high_absentee"] = (df["absences"] > 10).astype(int)
    df["multiple_failures"] = (df["failures"] > 1).astype(int)

    # One-hot encoding
    df = pd.get_dummies(df, drop_first=False)

    # Align with training features
    df = df.reindex(columns=feature_order, fill_value=0)

    return df




# API endpoint
@app.post("/predict")
def predict(student: StudentInput):
    X = preprocess(student.dict())
    pred = model.predict(X)[0]  # This is already "Low Risk" / "Medium Risk" / "High Risk"
    return {"risk_category": pred}

