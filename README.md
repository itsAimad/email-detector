# Email Detector with Streamlit and Machine Learning 

## Overview 🔎

This project is a **email spam detector** built using Python, Streamlit, and machine learning. It uses the Naive Bayes Algorithm to classify emails as spam or not spam(ham).

## Features 

- **Spam Detection** :  DEtects whether an email is spam based on its content.
- **User-Friendly Interface**: Provides an intuitive interface using Streamlit for easy interaction.
- **Model Training**: Includes scripts to train the model on

## Project Structure 
``` 
 Email Detector/
├── data/ 
│ └── spam.csv   # Dataset for training the model 
├── model/ 
│    ├── spam_classifier.pkl # Trained model 
│    └── count_vectorizer.pkl # Count vectorizer for transforming text data 
├── app.py # Streamlit app script 
├── train_model.py # Script to train the model 
└── README.md # Project documentation
```