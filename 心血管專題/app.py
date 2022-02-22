#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from flask import Flask, render_template, request, jsonify, json
from flask_cors import CORS
import pandas as pd
import numpy as np
from sklearn import preprocessing
import tensorflow as tf
from tensorflow import keras 
from keras.layers import Dense
from keras.models import load_model
app = Flask(__name__)
CORS(app)

@app.route('/')
def webapi():
    return render_template('data.html')

model = tf.keras.models.load_model('static/model.h5', custom_objects={'Functional':tf.keras.models.Model})
heart = pd.read_csv("static/heart.csv", encoding="utf-8")
heart = heart.drop("target", axis=1)


@app.route('/process', methods=['POST'])
def predict():
    global model, heart
    # user = request.form.get('user')
    data = [request.form.get('age', type=float), request.form.get('sex', type=float),
            request.form.get('cp', type=float), request.form.get('trestbps', type=float),
            request.form.get('chol', type=float), request.form.get('fbs', type=float),
            request.form.get('restecg', type=float), request.form.get('thalach', type=float),
            request.form.get('exang', type=float), request.form.get('oldpeak', type=float),
            request.form.get('slope', type=float), request.form.get('ca', type=float),
            request.form.get('thal', type=float)]
    columns=["age", "sex", "cp", "trestbps", "chol", "fbs", "restecg", "thalach", "exang", "oldpeak", "slope", "ca", "thal"]
    data = dict(zip(columns, data))
    df = heart.append(data,ignore_index=True)
    MinMaxScaler = preprocessing.MinMaxScaler(feature_range=(0,1)) #使用Min-Max Normalization將data標準化至0-1間
    MinMax_data = MinMaxScaler.fit_transform(df)
    standard = pd.DataFrame(MinMax_data, columns=["age", "sex", "cp", "trestbps", "chol", "fbs", "restecg", "thalach", "exang", "oldpeak", "slope", "ca", "thal"])
    result = model.predict(standard.iloc[-1:,:])
    # result = model.predict(data)
    possibility = str(result[0][1])
    return possibility
    # passwd = request.form.get('password')
    # result = 'user:{}, pass:{}'.format(user, passwd)
    # result = 'user：{}'.format(user)
    # return result


if __name__ == '__main__':
    app.debug = True
    app.run('0.0.0.0')

