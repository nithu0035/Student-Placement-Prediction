
import streamlit as st
import pickle
import numpy as np

# Load trained model
model = pickle.load(open("model.pkl", "rb"))

st.set_page_config(page_title="Placement Readiness System", layout="centered")
st.title("🎓 Intelligent Student Placement Prediction & Readiness System")

st.markdown("Predict placement probability and understand **why** the prediction was made.")

# ---------------- User Inputs ----------------
gender = st.selectbox("Gender", ["Male", "Female"])
ssc_p = st.slider("SSC Percentage", 40, 100, 70)
hsc_p = st.slider("HSC Percentage", 40, 100, 70)
degree_p = st.slider("Degree Percentage", 40, 100, 65)
workex = st.selectbox("Work Experience", ["Yes", "No"])

gender_val = 1 if gender == "Male" else 0
workex_val = 1 if workex == "Yes" else 0

features = np.array([[gender_val, ssc_p, hsc_p, degree_p, workex_val]])

# ---------------- Prediction ----------------
if st.button("Predict Placement Probability"):
    prob = model.predict_proba(features)[0][1] * 100
    result = "Placed" if prob >= 60 else "Not Placed"

    st.subheader("📊 Prediction Result")
    st.success(f"Placement Probability: {prob:.2f}%")
    st.info(f"Prediction Outcome: {result}")

    # ---------------- Skill Gap Analysis ----------------
    if prob < 60:
        st.warning("🔧 Skill Gap Analysis")
        suggestions = []
        if degree_p < 65:
            suggestions.append("Improve core subject understanding and academic scores")
        if workex == "No":
            suggestions.append("Gain internship or project-based experience")
        if ssc_p < 60 or hsc_p < 60:
            suggestions.append("Strengthen fundamentals and aptitude skills")

        for s in suggestions:
            st.write("- ", s)

    # ---------------- Explainability (Placeholder) ----------------
    st.markdown("### 🔍 Model Explainability (SHAP)")
    st.info(
        """This project supports SHAP-based explainability.
        In production, SHAP plots can be generated to explain how
        features like academics and work experience influenced
        the prediction."""
    )
