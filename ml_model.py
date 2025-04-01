import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.ensemble import RandomForestClassifier
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import LabelEncoder

data = {
    "username": [],
    "type": [],
    "url": []
}

df = pd.DataFrame(data)

le = LabelEncoder()
df["url_encoded"] = le.fit_transform(df["url"])

X_train, X_test, y_train, y_test = train_test_split(df["type"], df["url_encoded"], test_size=0.2, random_state=42)

model = make_pipeline(CountVectorizer(), RandomForestClassifier(n_estimators=100, random_state=42))

model.fit(X_train, y_train)

def predict_url(username_type):
    pred = model.predict([username_type])
    return le.inverse_transform(pred)[0]

print(predict_url("funny"))
print(predict_url("professional"))