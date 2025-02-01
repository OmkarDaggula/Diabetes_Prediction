import joblib
import numpy as np
import model
from flask import Flask, render_template, request,jsonify

app = Flask(__name__)
 
@app.route('/')
def hello_world():
    return render_template('index.html')
@app.post('/predict')
def predict():
    data = request.get_json()  # Parses JSON data from request body
    print(data)
    outcome=model.predict(data)
    print(outcome)
    return jsonify({"message": "Data received", "data": outcome})

if __name__ == "__main__":
    app.run(debug=True)
