# -*- coding: utf-8 -*-
"""
Created on Tue Dec 24 08:52:38 2019

@author: berka
"""

from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
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
normals=data[data['class'] == 'Normal']
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
# %%
plt.scatter(abnormals.pelvic_incidence,abnormals.lumbar_lordosis_angle, color='r',label='Abnormals',marker='X')
plt.scatter(normals.pelvic_incidence,normals.lumbar_lordosis_angle, color='green',label='Abnormals',marker='P',alpha=0.5)
plt.legend()
plt.xlabel('Abnormals',color='b')
plt.ylabel('Normals',color='b')
plt.show()
# %%
data['class'] = [1 if each == 'Abnormal' else 0 for each in data['class']]
y=data['class'].values
x_data=data.drop('class', axis=1)
x = (x_data - np.min(x_data)) / (np.max(x_data)-np.min(x_data)).values #normalization
# %%
x_train, x_test, y_train, y_test = train_test_split(x,y, test_size=0.3, random_state=1)
knn = KNeighborsClassifier(n_neighbors=19)
knn.fit(x_train,y_train)
pred = knn.predict(x_test)
print('{} Nearest Neighbor Score : {} '.format(19,knn.score(x_test,y_test)))
# %%
train_accuracy = []
test_accuracy = []
# Loop over different values of k
for each in range(1,25):
    knn2 = KNeighborsClassifier(n_neighbors=each)
    knn2.fit(x_train,y_train)
    train_accuracy.append(knn2.score(x_train, y_train))
    test_accuracy.append(knn2.score(x_test, y_test))

# Plot
plt.figure(figsize=[13,8])
plt.plot(range(1,25), test_accuracy, label = 'Testing Accuracy')
plt.plot(range(1,25), train_accuracy, label = 'Training Accuracy')
plt.legend()
plt.title('value VS Accuracy')
plt.xlabel('Number of Neighbors')
plt.ylabel('Accuracy')
plt.xticks(range(1,25))
plt.show()
print("Best accuracy is {} with K = {}".format(np.max(test_accuracy),1+test_accuracy.index(np.max(test_accuracy))))