import streamlit as st
import pandas as pd
import joblib

# Load model
math_model = joblib.load("math_model.pkl")
port_model = joblib.load("port_model.pkl")
preprocessor = joblib.load("math_preprocessor.pkl")

# Set page config
st.set_page_config(page_title="Student Grade Predictor 🎓", page_icon="📘", layout="centered")

# Sidebar Info
with st.sidebar:
    st.title("📚 About")
    st.markdown("""
    This app predicts a student's final grade (**G3**) based on academic progress and behavior.

    - Select the **subject**
    - Enter details for the **7 features**
    - Get a personalized **grade estimate**

   
    """)

# Title
st.markdown("<h1 style='text-align: center; color: #4f8bf9;'>✨ Final Grade Predictor ✨</h1>", unsafe_allow_html=True)
st.markdown("### 🎓 Predict student Exam performance")

# Subject dropdown
subject = st.selectbox("📘 Choose Subject", ["Math", "Portuguese"])

# Input form
st.markdown("#### 📝 Student Details")

col1, col2 = st.columns(2)

with col1:
    G1 = st.slider("🧮 G1 - First Period Grade", 0, 20, 10)
    G2 = st.slider("📐 G2 - Second Period Grade", 0, 20, 10)
    failures = st.selectbox("❌ Past Class Failures", [0, 1, 2, 3])
    health = st.selectbox("🧍 Health (1 = Poor, 5 = Excellent)", [1, 2, 3, 4, 5])

with col2:
    studytime = st.selectbox("📚 Study Time (1 = <2 hrs, 4 = 10+ hrs)", [1, 2, 3, 4])
    absences = st.number_input("🚪 Total Absences", min_value=0, max_value=100, value=2)
    internet = st.selectbox("🌐 Internet Access at Home", ["yes", "no"])

# Predict
if st.button("🎯 Predict Final Grade"):
    input_df = pd.DataFrame([{
        "G2": G2,
        "G1": G1,
        "failures": failures,
        "studytime": studytime,
        "absences": absences,
        "health": health,
        "internet": internet
    }])

    processed = preprocessor.transform(input_df)

    model = math_model if subject == "Math" else port_model
    prediction = round(min(max(model.predict(processed)[0], 0), 20), 2)


    st.markdown(
        f"""
        <div style="background-color:#eaf4ff;padding:20px;border-radius:15px;margin-top:20px;text-align:center;">
            <h2 style="color:#1f77b4;">📊 Predicted Final Grade (G3): <span style="color:#111;">{round(prediction, 2)} / 20</span></h2>
        </div>
        """, unsafe_allow_html=True
    )
