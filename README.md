# Diabetes Prediction API
This project provides an API to predict diabetes using Naive Bayes, Random Forest, and Logistic Regression models.
## Overview

The Diabetes Prediction System is a machine learning-based application that predicts the likelihood of diabetes based on user-input health parameters such as glucose level, BMI, insulin, and age. The system utilizes a trained model to classify individuals as diabetic or non-diabetic, helping in early diagnosis and preventive healthcare.

## Features
- User Input Form – Allows users to enter medical parameters.

- Machine Learning Model – Predicts diabetes risk based on health data.

- Flask API Backend – Handles input processing and prediction requests.

- Web Interface – Displays predictions and results.

## Technology Stack
- Frontend: HTML, CSS, JavaScript

- Backend: Python (Flask)

- Machine Learning Model: Scikit-learn (Logistic Regression, Random Forest, etc.)

- Database (Optional): SQLite / Firebase

- Deployment: Heroku / AWS / Google Cloud

## Installation
1. Clone the repository:
```
git clone https://github.com/yourusername/diabetes-prediction-system.git
cd diabetes-prediction-system
```
2. Install dependencies:
```
pip install -r requirements.txt
```
3. Run the Flask server:
```
python app.py
```
4. Open [http://127.0.0.1:5000/](http://127.0.0.1:5000/) in your browser.

## Usage
- Enter health parameters in the web form.

- Click Predict to get the result.

- The model will classify the user as Diabetic or Non-Diabetic.