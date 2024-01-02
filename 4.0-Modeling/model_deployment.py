import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle
from markupsafe import Markup

# Create flask app
flask_app = Flask(__name__)
model = pickle.load(open("model.pkl", "rb"))

@flask_app.route("/")
def Home():
    return render_template("index.html")

@flask_app.route("/predict", methods = ["POST"])
def predict():
    int_features = [int(x) for x in request.form.values()]
    features = np.array(int_features).reshape(-1, 4)
    prediction = model.predict(features)[0]
    if prediction == 'LOW':
        warn = " .The possibility of theft is LOW. You can rest assured about asset protection."
    else:
        warn = ' .The possibility of theft is HIGH. You must be careful and vigilant in protecting your assets.'
    return render_template("index.html", prediction_text = "The chance is {}".format(prediction + warn))

if __name__ == "__main__":
    flask_app.run(debug=True)