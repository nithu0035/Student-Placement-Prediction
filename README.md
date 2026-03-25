# 🎯 Student Placement Prediction & Career Intelligence Platform

An end-to-end Machine Learning web app that predicts student placement probability and delivers a full career readiness evaluation — including skill gap analysis, ATS readiness score, career fit, and a personalized action plan.

---

## ✨ Features

- 🤖 **Placement Prediction** — Random Forest model predicts placement probability from academic and experience data
- 📊 **Hiring Readiness Dashboard** — Real-time scores for Readiness Index, Skill Coverage, and ATS Readiness
- 🧭 **Career Fit Analysis** — Matches your profile against target roles like SWE, Data Analyst, ML Engineer
- 🧠 **Confidence vs Readiness Check** — Compares self-assessed confidence with actual profile readiness
- 📌 **Personalized Action Plan** — Targeted suggestions to close skill and experience gaps
- 🎨 **Modern Glass UI** — Dark-themed Streamlit dashboard with custom CSS styling

---

## 🛠️ Tech Stack

| Layer | Technology |
|---|---|
| Frontend / UI | Streamlit |
| ML Model | Scikit-learn (Random Forest Classifier) |
| Data Processing | Pandas, NumPy |
| Model Persistence | Pickle |
| Language | Python 3 |

---

## 📁 Project Structure
```
Student-Placement-Prediction/
├── app.py               # Streamlit web app (UI + prediction logic)
├── train_model.py       # Model training script
├── model.pkl            # Trained Random Forest model
├── placement_data.csv   # Training dataset
└── README.md
```

---

## 📊 Input Features

| Feature | Description |
|---|---|
| Gender | Male / Female |
| SSC % | 10th standard marks |
| HSC % | 12th standard marks |
| Degree % | Undergraduate percentage |
| Work Experience | Yes / No |
| Internships | Number of internships completed |
| Projects | Number of academic/personal projects |
| Skills | Python, ML, SQL, React, etc. |
| Target Role | Desired job role |
| Confidence Level | Self-assessed (1–5) |

---

## ⚙️ Setup & Installation

### 1. Clone the repository
```bash
git clone https://github.com/nithu0035/Student-Placement-Prediction.git
cd Student-Placement-Prediction
```

### 2. Install dependencies
```bash
pip install streamlit pandas scikit-learn numpy
```

### 3. Train the model (optional — `model.pkl` already included)
```bash
python train_model.py
```

### 4. Run the app
```bash
streamlit run app.py
```

Open your browser at `http://localhost:8501`

---

## 🧠 How It Works

1. User fills in academic scores, experience, skills, and target role in the sidebar
2. The trained Random Forest model predicts placement probability using: Gender, SSC %, HSC %, Degree %, and Work Experience
3. A Readiness Index is computed from grades + internships + projects
4. Skill Coverage and ATS Readiness scores are calculated
5. Career Fit and an Action Plan are generated based on the full profile

---

## 📄 License

[MIT](https://choosealicense.com/licenses/mit/)

## 👤 Author

**Gudipatoju Nitesh**  
GitHub: [@nithu0035](https://github.com/nithu0035)  
Role: AI & ML Engineer
