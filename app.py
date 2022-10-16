#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
from flask import Flask, render_template, request
import pickle

app = Flask(__name__)
model = pickle.load(open('model.pkl', 'rb'))

@app.route('/', methods=['POST', 'GET'])
def home():
    return render_template('index.html')

@app.route('/churn', methods=['POST', 'GET'])
def rchurn():
    return render_template('resultp.html')

@app.route('/resultp.html', methods=['POST', 'GET'])
def churn():
    float_features = [float(x) for x in request.form.values()]
    final_features = [np.array(float_features)]
    prediction = model.predict(final_features)
    if prediction == 1:
        pred = "will Churn"
    elif prediction == 0:
        pred = "will not Churn"
    output = pred
    return render_template('resultp.html', prediction_text='Person {}'.format(output))

if __name__ == "__main__":
    app.run(debug=True)

