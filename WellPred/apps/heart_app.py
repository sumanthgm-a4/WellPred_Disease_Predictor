from flask import Flask, request, render_template
import numpy as np
from joblib import load

scaler, model = load("/home/sum/Desktop/WellPred/models/heart_model.pkl")

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('heart_main.html')

@app.route('/predict_heart', methods=['POST'])
def predict_heart():
        if request.method=='POST':
             age = int(request.form['age'])
             sex = request.form.get('sex')
             cp = request.form.get('cp')
             trestbps = int(request.form['trestbps'])
             chol = int(request.form['chol'])
             fbs = request.form.get('fbs')
             restecg = int(request.form['restecg'])
             thalach = int(request.form['thalach'])
             exang = request.form.get('exang')
             oldpeak = float(request.form['oldpeak'])
             slope = request.form.get('slope')
             ca = int(request.form['ca'])
             thal = request.form.get('thal')

             data = np.array(scaler.transform([[age,sex,cp,trestbps,chol,fbs,restecg,thalach,exang,oldpeak,slope,ca,thal]]))
             my_prediction = model.predict(data)
            
             return render_template('heart_res.html', prediction=my_prediction)
    
if __name__ == "__main__":
    app.run(debug = True)