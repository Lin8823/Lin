#!/usr/bin/env python
# coding: utf-8

# In[ ]:

import string
from flask import Flask, render_template, request, jsonify, json
from json import dumps
from flask_cors import CORS
import pandas as pd
import numpy as np
app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False
CORS(app)



@app.route('/')
def webapi():
    return render_template('API.html')


def transform(uchars_chinese):
    chinese_dict ={'零':0, '一':1, '二':2, '兩':2, '三':3, '四':4, '五':5, '六':6, '七':7, '八':8, '九':9, '十':10, 
                           '百':100, '千':1000, '萬':10000, '億':100000000}
    total = 0
    r = 1              #表示單位：個十百千...
    try:
        for i in range(len(uchars_chinese) - 2, -1, -1):
            val = chinese_dict.get(uchars_chinese[i])
            if val >= 10 and i == 0:  #應對 十三 十四 十*之類
                if val > r:
                    r = val
                    total = total + val
                else:
                    r = r * val
            elif val >= 10:
                if val > r:
                    r = val
                else:
                    r = r * val
            else:
                total = total + r * val
    except TypeError:
        pass

    return total
path = ['static/A_lvr_land_A.csv', 'static/B_lvr_land_A.csv', 'static/E_lvr_land_A.csv', 'static/F_lvr_land_A.csv', 'static/H_lvr_land_A.csv']
df = pd.concat((pd.read_csv(i,  encoding="utf-8") for i in path)).reset_index(drop = True)
df['總樓層數'][1:] = df['總樓層數'][1:].apply(lambda x:transform(x))


@app.route('/process', methods=['POST'])
def predict():
    global df
    data = [request.form.get('district', type=str), request.form.get('floor', type=int),
            request.form.get('state', type=str)]
    if data[1]=='':
        df_filter = df.filter[df['鄉鎮市區']==data[0] & df['建物型態']==data[2]]
    else:
        df_filter = df[(df['鄉鎮市區']==data[0]) & (df['總樓層數']==data[1]) & df['建物型態'].str.contains(data[2], regex= True, na=False)]

    df_filter = df_filter.to_json()

    # return df_filter
    return json.dumps(df_filter,ensure_ascii=False)

if __name__ == '__main__':
    # app.debug = True
    app.run('0.0.0.0')

