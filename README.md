# 🎓 Student Academic Risk Prediction Using Machine Learning

## 📘 Overview
This project leverages **Machine Learning (ML)** to predict **student academic risk levels** — *Low, Medium, or High* — based on academic, demographic, and lifestyle data.  
The system helps educators identify at-risk students early, enabling timely interventions to improve academic outcomes.

It features an **end-to-end ML pipeline** including **data preprocessing**, **model training**, **deployment** via **FastAPI** and **Streamlit**, and an **ethical AI analysis** focused on fairness and bias.

---

## 🧠 Key Features
- **End-to-End ML Pipeline:** From data cleaning to deployment.  
- **Feature Engineering:** Created new metrics such as attendance ratio, average grades, and support index.  
- **Model Comparison:** Tested Logistic Regression, Decision Tree, Random Forest, SVM, and Neural Network.  
- **Best Model:** Random Forest achieved **84% accuracy**.  
- **Deployment:** FastAPI backend with Streamlit frontend for real-time predictions.  
- **Ethical AI:** Addresses bias, fairness, and responsible AI use in education.  

---

## 🗂️ Dataset
- **Source:** [UCI Student Performance Dataset](https://archive.ics.uci.edu/ml/datasets/student+performance)  
- **Samples:** ~650 students  
- **Features:** 33 academic, demographic, and lifestyle attributes  
- **Target:** Risk Category (*Low, Medium, High*) — engineered from final grade (G3)

### 🧩 Feature Categories
- **Demographics:** Age, gender, parental education, family size  
- **Academics:** Grades (G1, G2), study time, failures, absences  
- **Lifestyle:** Free time, going out, health, alcohol use  
- **Support:** Family and school support indicators  

---

## ⚙️ Methodology

### 🔧 Data Preprocessing
- Handled missing values and encoded categorical variables.  
- Scaled numerical features using **MinMaxScaler**.  
- Engineered new features:
  - `average_grade = (G1 + G2) / 2`  
  - `parent_edu_avg = (Medu + Fedu) / 2`  
  - `support_index = famsup + schoolsup`  
  - `attendance_ratio = absences / 100`  

### 🤖 Models Trained

| Model | Accuracy |
|--------|-----------|
| Logistic Regression | 65% |
| Decision Tree | 73% |
| **Random Forest** | **84%** |
| SVM | 70% |
| Neural Network | 59% |

---

## 🧩 NLP Component
- Performed **sentiment analysis** on synthetic student feedback using **TF-IDF** and **VADER**.  
- Found that **negative sentiment correlated** with higher academic risk.  
- Demonstrated the potential of combining **textual sentiment** with quantitative features for better prediction.  

---

## 🚀 Deployment

### 🖥️ Backend (FastAPI)
- REST API endpoint: `/predict`  
- **Input:** student features  
- **Output:** predicted risk level (*Low, Medium, High*)  

### 🌐 Frontend (Streamlit)
- Interactive web interface for user input and real-time predictions.  
- Clean UI with sidebar navigation and styled result cards.  

---

## 📊 Visualization Highlights
- Correlation heatmap between grades *(G1, G2, G3)*  
- Distribution of students by gender and risk level  
- Feature importance (Random Forest)  
- Risk vs. parental education and absences  

---

## 🧭 Monitoring & Maintenance
- Model drift detection using periodic accuracy checks.  
- Retraining strategy with new student data.  
- Continuous tracking of prediction distributions.  

---

## 🧩 Ethical Considerations
- **Privacy:** All data anonymized.  
- **Bias:** Acknowledged potential gender and socioeconomic bias.  
- **Fairness:** Future improvements include fairness metrics (e.g., Equal Opportunity).  
- **Responsible Use:** Designed to support students, not penalize them.  

---

## 🛠️ Technologies Used
- **Programming:** Python  
- **Libraries:** Pandas, NumPy, Scikit-learn, TensorFlow, NLTK, Matplotlib, Seaborn  
- **Deployment:** FastAPI, Streamlit  
- **Version Control:** Git, GitHub  

---

## 🧩 Future Work
- Expand dataset for improved generalization.  
- Integrate real student feedback for NLP analysis.  
- Add explainable AI tools (*SHAP, LIME*).  
- Implement real-time model monitoring dashboard.  

---

## 📁 Project Structure

📁 Project Structure
Student_Risk_Prediction/
├── data/                     # Dataset (CSV)
├── notebooks/                # EDA & modeling notebooks
├── models/                   # Saved ML models (pkl files)
├── api/                      # FastAPI backend
├── app/                      # Streamlit frontend
├── requirements.txt
├── README.md
└── student_model.pkl

📈 Results

🎯 Best Model: Random Forest
✅ Accuracy: 84%
📊 Metrics: High F1-score and balanced recall across all classes

👥 Contributors

Ziad M. Elgharby – Data Scientist
Team Members: Collaborated in model development, deployment, and reporting.
