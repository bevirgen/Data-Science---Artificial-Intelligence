# -*- coding: utf-8 -*-
"""
Created on Mon Dec 23 20:46:29 2019

@author: berka
"""

from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import r2_score
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

df = pd.read_csv('data.csv', sep=';')
# %%

x = df.iloc[:,0].values.reshape(-1,1)
y = df.iloc[:,1].values.reshape(-1,1)

rf = RandomForestRegressor(n_estimators = 100, random_state = 42)
rf.fit(x,y)
print(rf.predict([[10]]))

x_=np.arange(min(x),max(x),0.01).reshape(-1,1)

plt.scatter(x, y, color='red')
plt.plot(x_, rf.predict(x_), color='b')
plt.xlabel('Tribun Level',fontsize=13)
plt.ylabel('Price',fontsize=13)
plt.show()

# R Score
print('r_square_score= ',r2_score(y, rf.predict(x)))