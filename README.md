# 🎓 Student Grade Predictor

A machine learning-powered web application that predicts a student's final grade (G3) based on academic and behavioral features. Built with Streamlit, it provides a simple and interactive interface for predicting performance in Math and Portuguese using real-world educational data.

---

## 📊 About the Dataset

This project uses the Student Performance Dataset from the UCI Machine Learning Repository. The dataset contains student records collected from two Portuguese schools and includes attributes related to:

- Demographics (age, sex, family background)
- School support (internet access, guardian, school support)
- Academic records (past grades, failures, study time, absences)

Two separate datasets are provided:
- student-mat.csv → Math course students
- student-por.csv → Portuguese course students

Each record includes:
- G1: First period grade
- G2: Second period grade
- G3: Final grade (target variable)

📂 Dataset link: https://archive.ics.uci.edu/ml/datasets/student+performance

---

## 🧠 Models Used

Two different models were trained for optimal performance:

| Subject      | Model               | R² Score |
|--------------|---------------------|----------|
| Math         | Random Forest        | 0.83     |
| Portuguese   | Linear Regression    | 0.85     |

Each model was trained using 7 selected features chosen based on feature importance and interpretability.

---

## 🛠 Features

- Predicts final student grade (G3) on a scale of 0–20
- Subject selection: Math or Portuguese
- Uses a trained model based on 7 academic + behavioral inputs
- Instant result with clear UI
- Deployed on Streamlit Cloud

---

## 📥 Inputs Required

| Feature      | Description                                      |
|--------------|--------------------------------------------------|
| G1           | Grade in the 1st period (0–20)                   |
| G2           | Grade in the 2nd period (0–20)                   |
| failures     | Past class failures (0–3)                        |
| studytime    | Weekly study time (1 = <2h, 4 = 10+ hrs)         |
| absences     | Number of school absences                        |
| health       | Health status (1 = very bad, 5 = very good)      |
| internet     | Internet access at home (yes or no)             |

These features were selected for being both accessible to users and highly influential in grade prediction.

---

## 🌐 Live Demo

Try the app live on Streamlit Cloud:  
👉 https://student-grade-predictor.streamlit.app

---

## 🧾 Project Structure

student_perfomance_prediction/  
├── app.py                    # Main Streamlit app  
├── math_model_rf.pkl         # Trained Random Forest model (Math)  
├── port_model.pkl            # Trained Linear Regression model (Portuguese)  
├── math_preprocessor.pkl     # Shared preprocessor for both datasets  
├── requirements.txt          # Python dependencies  
└── README.md
