# train_model.py

import pandas as pd
from sklearn.naive_bayes import MultinomialNB
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
import joblib
import os

def read_data():
    df = pd.read_csv("Email Detector/data/spam.csv", encoding="latin-1")
    df = df[["Category", "Message"]]
    df["spam"] = df["Category"].apply(lambda x: 1 if x == "spam" else 0)
    return df

def train_model(data):
    X = data["Message"]
    y = data["spam"]
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=42)
    return X_train, X_test, y_train, y_test

def create_model(X_train, y_train):
    cv = CountVectorizer()
    X_train_count = cv.fit_transform(X_train)
    model = MultinomialNB()
    model.fit(X_train_count, y_train)
    return model, cv


if __name__ == "__main__":
    df = read_data()
    X_train, X_test, y_train, y_test = train_model(df)
    model, cv = create_model(X_train, y_train)

    # Ensure the 'model directory exists'
    os.makedirs('Email Detector/model',exist_ok=True)
    joblib.dump(model, 'Email Detector/model/spam_classifier.pkl')
    joblib.dump(cv, 'Email Detector/model/count_vectorizer.pkl')
