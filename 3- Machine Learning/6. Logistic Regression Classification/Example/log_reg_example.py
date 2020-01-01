# -*- coding: utf-8 -*-
"""
Created on Wed Jan  1 11:30:04 2020

@author: berka
"""

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np
import warnings
warnings.filterwarnings('ignore')

data = pd.read_csv('voice.csv')
data.label = [1 if each == 'male' else 0 for each in data.label]
# %%
sns.countplot(data['label'])
print(data.loc[:,'label'].value_counts())
# %%
men = data[data['label']==1]
f, ax = plt.subplots(figsize=(15,9))
sns.heatmap(men.corr(), annot=True, linewidths = .5, fmt = '.2f', ax=ax)
plt.title("Men's Correlation")
plt.show()
# %%
women = data[data['label']==0]
f, ax = plt.subplots(figsize=(15,9))
sns.heatmap(women.corr(), annot=True, linewidths = .5, fmt = '.2f', ax=ax)
plt.title("Women's Correlation")
plt.show()
# %%
x=np.array(men.loc[:,'meanfreq']).reshape(-1,1)
y=np.array(men.loc[:,'Q25']).reshape(-1,1)

lr=LinearRegression()
lr.fit(x,y)
print('r2_square_score',lr.score(x,y))

pred_space=np.linspace(min(x),max(x)).reshape(-1,1)

plt.figure(figsize=(13,8))
plt.scatter(x,y)
plt.plot(pred_space,lr.predict(pred_space),c='blue',linewidth=2)
plt.xlabel('Mean Frequency')
plt.ylabel('Q25')
plt.show()
# %%
x=np.array(women.loc[:,'meanfreq']).reshape(-1,1)
y=np.array(women.loc[:,'Q25']).reshape(-1,1)

lr=LinearRegression()
lr.fit(x,y)
print('r2_square_score',lr.score(x,y))

pred_space=np.linspace(min(x),max(x)).reshape(-1,1)

plt.figure(figsize=(13,8))
plt.scatter(x,y)
plt.plot(pred_space,lr.predict(pred_space),c='blue',linewidth=2)
plt.xlabel('Mean Frequency')
plt.ylabel('Q25')
plt.show()
# %%
y = data.label.values
x_data = data.drop(['label'], axis=1)
x = (x_data - np.min(x_data)) / (np.max(x_data)-np.min(x_data)).values
print(data.info())
# %%
x_train, x_test, y_train, y_test = train_test_split(x,y, test_size= 0.2, random_state=42)

x_train = x_train.T
x_test = x_test.T
y_train = y_train.T
y_test = y_test.T
# %%
lr = LogisticRegression()
lr.fit(x_train.T, y_train.T)
print('Test Accuracy {}'.format(lr.score(x_test.T, y_test.T)))

























