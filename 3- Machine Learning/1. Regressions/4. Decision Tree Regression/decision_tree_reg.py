# -*- coding: utf-8 -*-
"""
Created on Sun Dec 22 09:36:55 2019

@author: berka
"""
from sklearn.tree import DecisionTreeRegressor
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

df = pd.read_csv('data.csv', sep = ';',header = None)
# %%
# data preprocessing
x = df.iloc[:,0].values.reshape(-1,1)
y = df.iloc[:,1].values.reshape(-1,1)

tree_reg = DecisionTreeRegressor()
tree_reg.fit(x,y)

tree_reg.predict([[100]]) # predict for example
# %%
# data visualize
x_ = np.arange(min(x),max(x),0.1).reshape(-1,1)

plt.scatter(x,y, color='orange')
plt.plot(x_, tree_reg.predict(x_), color='blue')
plt.xlabel('Grandstand Class',color='purple')
plt.ylabel('Grandstand Cost',color='r')
plt.show()