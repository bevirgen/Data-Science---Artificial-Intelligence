# -*- coding: utf-8 -*-
"""
Created on Tue Dec 24 08:52:38 2019

@author: berka
"""

from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np
import warnings
warnings.filterwarnings("ignore")
plt.style.use('ggplot')


data = pd.read_csv('column_2C_weka.csv')
# %%

print(data.info())
print(data.describe())

colors = ['red' if i=='Abnormal' else 'green' for i in data.loc[:,'class']]
pd.plotting.scatter_matrix(data.loc[:, data.columns!='class'],
                           color=colors,
                           figsize= [13,9.5],
                           diagonal='hist',
                           alpha=0.5,
                           marker='*',
                           s=150,
                           edgecolor='black')
plt.suptitle('Relations Between Features')
plt.show()
# %%
sns.countplot(data['class'])
print(data.loc[:,'class'].value_counts())
# %%

abnormals=data[data['class'] == 'Abnormal']
f, ax = plt.subplots(figsize=(15,9))
sns.heatmap(abnormals.corr(), annot=True, linewidths = .5, fmt = '.2f', ax=ax)
plt.title('Correlation')
plt.show()
# %%

x=np.array(abnormals.loc[:,'pelvic_incidence']).reshape(-1,1)
y=np.array(abnormals.loc[:,'sacral_slope']).reshape(-1,1)

lr=LinearRegression()
lr.fit(x,y)
print('r2_square_score',lr.score(x,y))

pred_space=np.linspace(min(x),max(x)).reshape(-1,1)

plt.figure(figsize=(13,8))
plt.scatter(x,y)
plt.plot(pred_space,lr.predict(pred_space),c='blue',linewidth=2)
plt.xlabel('Pelvic Incidence')
plt.ylabel('Sacral Slope')
plt.show()