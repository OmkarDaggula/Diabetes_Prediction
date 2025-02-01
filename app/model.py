import joblib
import numpy as np

# Load the logistic regression model
model = joblib.load("lr_model.joblib")
def predict(dict):
# Example input features (replace with your actual feature values)
    val =[float(dict["pregnancies"]),float(dict["glucose"]),float(dict["bloodPressure"]),float(dict["skinThickness"]),float(dict["insulin"]),
         float(dict["bmi"]),float(dict["diabetesPedigreeFunction"]),float(dict["age"])]
    outcome = np.array (val).reshape(1, -1)


# Make a prediction
    prediction = model.predict(outcome)

# Print the prediction
    print("Prediction:", prediction)
    return bool(prediction[0])