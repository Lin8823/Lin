#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from keras.models import load_model
def Calculate(data):
    model = load_model('NN_model')
    result = model.predict(data)
    possibility = print('患有心血管疾病之機率：',result[0])
    return possibility
if __name__ == '__main__':
    Calculate()

