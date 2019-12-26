# -*- coding: utf-8 -*-
"""
Created on Thu Dec 26 08:52:13 2019

@author: berka
"""

from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

data = pd.read_csv('data.csv')
data.drop(['id','Unnamed: 32'], axis=1, inplace=True)
data.diagnosis = [1 if each == 'M' else 0 for each in data.diagnosis]
# %%
y = data.diagnosis.values
x_data = data.drop(['diagnosis'], axis=1)
x = (x_data - np.min(x_data)) / (np.max(x_data)-np.min(x_data)).values
print(data.info())
# %%
x_train, x_test, y_train, y_test = train_test_split(x,y, test_size= 0.2, random_state=42)

x_train = x_train.T
x_test = x_test.T
y_train = y_train.T
y_test = y_test.T

def initialize_weights_and_bias(dimension):
    
    w = np.full((dimension,1),0.01)
    b = 0.0
    return w,b

#w,b = initialize_weights_and_bias(30)
    
def sigmoid (z):
    
    y_head = 1 / (1 + np.exp(-z))
    return y_head
# %%
def forward_backward_propagation(w,b,x_train,y_train):
    #forward propagation
    z = np.dot(w.T,x_train) + b
    y_head = sigmoid(z)
    loss = -y_train * np.log(y_head)-(1-y_train)*np.log(1-y_head)
    cost = (np.sum(loss)) / x_train.shape[1] # x_train.shape[1] is for scaling
    
    #backward propagation
    derivative_weight = (np.dot(x_train,((y_head-y_train).T))) / x_train.shape[1]
    derivative_bias = np.sum(y_head - y_train) / x_train.shape[1]
    gradients = {'derivative_weight':derivative_weight, 'derivative_bias': derivative_bias}
    
    
    return cost,gradients