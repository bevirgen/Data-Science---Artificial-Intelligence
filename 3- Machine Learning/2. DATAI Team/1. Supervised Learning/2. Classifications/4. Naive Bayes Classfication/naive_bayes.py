# -*- coding: utf-8 -*-
"""
Created on Fri Jan  3 10:10:19 2020

@author: berka
"""

from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import warnings
warnings.filterwarnings('ignore')

data = pd.read_csv('data.csv')
data.drop(['id','Unnamed: 32'],axis=1, inplace=True)
data.head()
# %%
M = data[data.diagnosis == 'M']
B = data[data.diagnosis == 'B']
# %%
plt.scatter(M.radius_mean,M.texture_mean, c='red', label='Malignant' )
plt.scatter(B.radius_mean,B.texture_mean, c='green', label='Benign',alpha=0.3 )
plt.legend()
plt.xlabel('Radius Mean')
plt.ylabel('Texture Mean')
plt.show()
# %%
data['diagnosis'] = [1 if each == 'M' else 0 for each in data['diagnosis']]
y = data['diagnosis'].values
x_data = data.drop('diagnosis', axis=1)
x = (x_data - np.min(x_data)) / (np.max(x_data)-np.min(x_data)).values
# %%
x_train, x_test, y_train, y_test = train_test_split(x,y,test_size = 0.3,random_state=1)
nb = GaussianNB()
nb.fit(x_train,y_train)
print('naive bayes score :',nb.score(x_test,y_test))