import numpy as np
import pandas as pd
from flask import Flask, request, jsonify, render_template
import pickle
from flask_cors import CORS
app = Flask(__name__)
CORS(app)
model = pickle.load(open("model/asteroid_model.pkl", "rb"))
output = 0
@app.route("/")
def Home():
    return "<h1>Server is live</h1>"


@app.route("/predict", methods=['POST'])
def prediciton():
    print('hello')
    try:
        request_data = request.get_json()
    except Exception as er:
        print(er)
    print(request_data)
    magnitude = int(request_data['magnitude'])
    velocity = int(request_data['velocity'])

    predict = model.predict([[magnitude, velocity]])
    print(predict)
    return {"predict": predict[0]}


if __name__ == "__main__":
    app.run(debug = True)