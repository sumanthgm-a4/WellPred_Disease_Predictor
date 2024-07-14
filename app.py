from flask import Flask, render_template, redirect, url_for, request
import joblib
import numpy as np

app = Flask(__name__)

# Routes to different prediction applications
@app.route('/')
def index():
    return render_template('index.html')

heart_scaler, heart_model = joblib.load("/home/sum/Desktop/WellPred/models/heart_model.pkl")

@app.route('/heart')
def heart():
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

        data = np.array(heart_scaler.transform([[age,sex,cp,trestbps,chol,fbs,restecg,thalach,exang,oldpeak,slope,ca,thal]]))
        my_prediction = heart_model.predict(data)
            
        return render_template('heart_res.html', prediction=my_prediction)
        


cerv_data, cerv_scaler, cerv_model, X, y = joblib.load("/home/sum/Desktop/WellPred/models/cerv_canc_models.pkl")

@app.route('/cervical')
def cervical():
     return render_template('cerv_main.html')

@app.route('/predict_cerv', methods=['GET','POST'])
def predict_cerv():
    if request.method == 'POST':
        a = int(request.form["textbox1"])
        b = float(request.form["textbox2"])
        c = float(request.form["textbox3"])
        d = float(request.form["textbox4"])
        e = float(request.form["textbox5"])
        f = float(request.form["textbox6"])
        g = float(request.form["textbox7"])
        h = float(request.form["textbox8"])
        i = float(request.form["textbox9"])
        j = float(request.form["textbox10"])
        k = float(request.form["textbox11"])
        l = float(request.form["textbox12"])
        m = float(request.form["textbox13"])
        n = float(request.form["textbox14"])
        o = float(request.form["textbox15"])
        p = float(request.form["textbox16"])
        q = float(request.form["textbox17"])
        r = float(request.form["textbox18"])
        s = float(request.form["textbox19"])
        t = float(request.form["textbox20"])
        u = float(request.form["textbox21"])
        v = float(request.form["textbox22"])
        w = float(request.form["textbox23"])
        x = float(request.form["textbox24"])
        y = float(request.form["textbox25"])
        z = int(request.form["textbox26"])
        aa = int(request.form["textbox27"])
        ab = int(request.form["textbox28"])
        ac = int(request.form["textbox29"])
        ad = int(request.form["textbox30"])
        ae = int(request.form["textbox31"])
        af = int(request.form["textbox32"])
        ag = int(request.form["textbox33"])

        prediction = cerv_model.predict(cerv_scaler.transform([[a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, u, v, w, x, y, z, aa, ab, ac, ad, ae, af, ag]]))

        return render_template('cerv_res.html', prediction = prediction)



kidney_data, kidney_scaler, kidney_model = joblib.load('/home/sum/Desktop/WellPred/models/kidney_models.pkl')

@app.route('/kidney')
def kidney():
    return render_template('kidney_main.html')

@app.route('/predict_kidney', methods=['POST'])
def predict_kidney():
    features = [float(request.form.get(f)) for f in request.form]
    features_array = np.array([features])
    features_array = kidney_scaler.transform(features_array)
    
    prediction = kidney_model.predict(features_array)[0]
    prediction_proba = kidney_model.predict_proba(features_array)[0].tolist()
    
    return render_template('kidney_res.html', prediction=prediction)



if __name__ == '__main__':
    app.run(debug=True)
