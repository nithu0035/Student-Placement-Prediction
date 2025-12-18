
import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier
import pickle

df = pd.read_csv("placement_data.csv")

le = LabelEncoder()
for col in ["gender", "workex", "status"]:
    df[col] = le.fit_transform(df[col])

X = df.drop("status", axis=1)
y = df["status"]

model = RandomForestClassifier(n_estimators=200, random_state=42)
model.fit(X, y)

pickle.dump(model, open("model.pkl", "wb"))
