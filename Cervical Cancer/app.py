# Importing essential libraries
from flask import Flask, render_template, request
import joblib
import numpy as np

data, scaler, xgb_model, X, y = joblib.load("cerv_canc_models.pkl")

app = Flask(__name__)

@app.route('/')
def cerv_canc():
    return render_template("main.html")


@app.route('/predict', methods=['GET','POST'])
def predict():
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

        prediction = xgb_model.predict(scaler.transform([[a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, u, v, w, x, y, z, aa, ab, ac, ad, ae, af, ag]]))

        return render_template('result.html', prediction = prediction)

if __name__ == "__main__":
    app.run(debug = True)