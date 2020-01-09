# -*- coding: utf-8 -*-
"""
Created on Fri Jan  3 10:10:19 2020

@author: berka
"""

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import confusion_matrix
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np
import warnings
warnings.filterwarnings('ignore')

data = pd.read_csv('data.csv')
data.drop(['id','Unnamed: 32'],axis=1, inplace=True)
data.head()
# %%
data['diagnosis'] = [1 if each == 'M' else 0 for each in data['diagnosis']]
y = data['diagnosis'].values
x_data = data.drop('diagnosis', axis=1)
x = (x_data - np.min(x_data)) / (np.max(x_data)-np.min(x_data)).values
# %%
x_train, x_test, y_train, y_test = train_test_split(x,y,test_size = 0.25, random_state=42)
dt= DecisionTreeClassifier(random_state=42)
dt.fit(x_train,y_train)
print('DT Classifier accuracy :',dt.score(x_test,y_test)) 
# %%
#random forest
rf = RandomForestClassifier(n_estimators=15, random_state=42)
rf.fit(x_train,y_train)
print('RF Classifier accuracy :',rf.score(x_test,y_test))
# %%
y_pred = rf.predict(x_test)
y_true = y_test
cm = confusion_matrix(y_true, y_pred)

f, ax = plt.subplots(figsize=(5,5))
sns.heatmap(cm, annot=True, linewidths=0.5, linecolor='red', fmt='.0f', ax=ax)
plt.xlabel('y_pred')
plt.ylabel('y_true')
plt.show()