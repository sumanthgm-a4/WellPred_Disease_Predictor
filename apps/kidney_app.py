from flask import Flask, request, render_template, redirect, url_for
import numpy as np
import joblib  # or any other model loading library

app = Flask(__name__)

# Load your pre-trained model
data, scaler, model = joblib.load('/home/sum/Desktop/WellPred/models/kidney_models.pkl')

@app.route('/')
def index():
    return render_template('kidney_main.html')

@app.route('/predict_kidney', methods=['POST'])
def predict_kidney():
    features = [float(request.form.get(f)) for f in request.form]
    features_array = np.array([features])
    features_array = scaler.transform(features_array)
    
    prediction = model.predict(features_array)[0]
    prediction_proba = model.predict_proba(features_array)[0].tolist()
    
    return render_template('kidney_res.html', prediction=prediction)


if __name__ == '__main__':
    app.run(debug=True)
