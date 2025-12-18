import streamlit as st
import pickle
import numpy as np
import pandas as pd
from datetime import datetime

# ======================================================
# PAGE CONFIG
# ======================================================
st.set_page_config(
    page_title="Placement Intelligence Platform",
    page_icon="🎯",
    layout="wide"
)

# ======================================================
# STYLES
# ======================================================
st.markdown("""
<style>
body {
    background: radial-gradient(circle at top, #0f2027, #000000 65%);
}
.glass {
    background: rgba(22, 27, 34, 0.92);
    backdrop-filter: blur(14px);
    border-radius: 18px;
    border: 1px solid rgba(255,255,255,0.08);
    padding: 22px;
    margin-bottom: 20px;
}
.header-box {
    background: linear-gradient(90deg, #1f6feb, #58a6ff);
    padding: 26px;
    border-radius: 20px;
    color: white;
}
.chip {
    padding: 6px 16px;
    border-radius: 30px;
    font-size: 13px;
    font-weight: 600;
    color: white;
}
.good { background: #238636; }
.mid { background: #9e6a03; }
.low { background: #8b1d1d; }
.footer {
    text-align: center;
    color: #8b949e;
    font-size: 14px;
    padding: 16px;
}
[data-testid="stMetricValue"] {
    font-size: 28px;
    color: #58a6ff;
}
</style>
""", unsafe_allow_html=True)

# ======================================================
# LOAD MODEL
# ======================================================
@st.cache_resource(show_spinner=False)
def load_model():
    return pickle.load(open("model.pkl", "rb"))

try:
    model = load_model()
except:
    st.error("❌ model.pkl not found. Please train the model.")
    st.stop()

# ======================================================
# HEADER
# ======================================================
st.markdown("""
<div class="header-box">
<h2>🎯 Placement Intelligence & Talent Analytics</h2>
<p>ML Prediction • Career Fit • Skill Gap • ATS Readiness (Simulated)</p>
</div>
""", unsafe_allow_html=True)

st.caption(f"Prototype Evaluation • {datetime.now().strftime('%d %b %Y')}")
st.divider()

# ======================================================
# SIDEBAR — UPDATED PROFILE SECTION
# ======================================================
with st.sidebar:
    st.header("👤 Candidate Profile")

    with st.expander("📚 Academic Details", True):
        ssc = st.slider("SSC (10th %)", 0, 100, 75)
        hsc = st.slider("HSC (12th %)", 0, 100, 70)
        deg = st.slider("Degree %", 0, 100, 68)
        branch = st.selectbox(
            "Branch / Domain",
            ["CSE", "AI & ML", "Data Science", "IT", "ECE", "EEE", "Mechanical", "Other"]
        )

    with st.expander("💼 Experience Profile", True):
        internships = st.slider("Internships Completed", 0, 5, 1)
        projects = st.slider("Academic / Personal Projects", 0, 5, 2)
        workex = st.radio("Work Experience", ["Yes", "No"], horizontal=True)

    with st.expander("🎯 Career Intent", True):
        target_role = st.selectbox(
            "Target Role",
            ["Software Engineer", "Data Analyst", "ML Engineer",
             "Full Stack Developer", "Intern / Trainee"]
        )
        confidence_level = st.slider("Self-Assessed Confidence Level", 1, 5, 3)

    gender = st.selectbox("Gender", ["Male", "Female"])

    st.divider()
    st.subheader("🧠 Technical Skills")
    skills = st.multiselect(
        "Select Skills You Possess",
        ["Python", "Machine Learning", "Data Analysis", "SQL",
         "Deep Learning", "React", "Java", "Cloud Basics"]
    )

    analyze = st.button("🚀 Run Career Evaluation")

# ======================================================
# RESULTS — UPDATED OUTPUT SECTION
# ======================================================
if analyze:
    with st.spinner("Analyzing candidate profile..."):
        gender_val = 1 if gender == "Male" else 0
        work_val = 1 if workex == "Yes" else 0

        X = np.array([[gender_val, ssc, hsc, deg, work_val]])
        placement_prob = model.predict_proba(X)[0][1] * 100

        readiness = min(
            0.45 * deg +
            0.30 * hsc +
            0.15 * ssc +
            internships * 2 +
            projects * 2 +
            (10 if work_val else 0),
            100
        )

        skill_score = min(len(skills) * 12, 100)
        ats_score = min((readiness * 0.5) + (skill_score * 0.3) + (internships * 4), 100)

        if ats_score >= 75:
            verdict, color = "Strong Hire", "good"
        elif ats_score >= 55:
            verdict, color = "Consider Candidate", "mid"
        else:
            verdict, color = "Upskilling Required", "low"

    # ================= DASHBOARD =================
    st.markdown("### 📊 Hiring Readiness Dashboard")
    st.markdown(f"<span class='chip {color}'>{verdict}</span>", unsafe_allow_html=True)

    c1, c2, c3, c4 = st.columns(4)
    c1.metric("Placement Probability", f"{placement_prob:.1f}%")
    c2.metric("Readiness Index", f"{readiness:.1f}/100")
    c3.metric("Skill Coverage", f"{skill_score}/100")
    c4.metric("ATS Readiness (Simulated)", f"{ats_score:.1f}%")

    st.progress(int(readiness))
    st.divider()

    # ================= CAREER FIT =================
    st.markdown("### 🧭 Career Fit Analysis")
    st.markdown("<div class='glass'>", unsafe_allow_html=True)

    suitable_roles = []
    if deg >= 70 and internships >= 2:
        suitable_roles.append("Software Engineer")
    if hsc >= 65:
        suitable_roles.append("Data Analyst")
    if skill_score >= 60:
        suitable_roles.append("ML Engineer")

    if target_role in suitable_roles:
        st.write(f"✅ Your profile aligns well with **{target_role}**.")
    else:
        st.write(
            f"⚠️ Your current profile is partially aligned with **{target_role}**. "
            "Focused preparation is recommended."
        )

    st.write(f"• Branch / Domain: **{branch}**")
    st.write(f"• Career Confidence Level: **{confidence_level}/5**")

    st.markdown("</div>", unsafe_allow_html=True)

    # ================= CONFIDENCE VS READINESS =================
    st.markdown("### 🧠 Confidence vs Readiness")
    st.markdown("<div class='glass'>", unsafe_allow_html=True)

    expected_readiness = confidence_level * 20

    if readiness >= expected_readiness:
        st.write("✅ Your confidence level matches your actual readiness.")
    else:
        st.write(
            "⚠️ Your confidence is higher than current readiness. "
            "Targeted preparation will help close this gap."
        )

    st.write(f"• Expected Readiness: **{expected_readiness}/100**")
    st.write(f"• Actual Readiness: **{readiness:.1f}/100**")

    st.markdown("</div>", unsafe_allow_html=True)

    # ================= ACTION PLAN =================
    st.markdown("### 📌 Personalized Action Plan")
    st.markdown("<div class='glass'>", unsafe_allow_html=True)

    if skill_score < 60:
        st.write("• Strengthen technical skills relevant to your target role.")
    if internships < 2:
        st.write("• Gain more internship or industry exposure.")
    if projects < 3:
        st.write("• Build additional hands-on projects.")
    if ats_score < 75:
        st.write("• Improve resume clarity with measurable outcomes.")

    st.write("• Continue consistent academic and interview preparation.")

    st.markdown("</div>", unsafe_allow_html=True)

# ======================================================
# FOOTER
# ======================================================
st.markdown("---")
st.markdown(
    "<div class='footer'>🚀 Developed by <b>Nitesh</b> · AI & ML Engineer · Academic Prototype</div>",
    unsafe_allow_html=True
)
