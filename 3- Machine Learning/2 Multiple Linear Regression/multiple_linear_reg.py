# -*- coding: utf-8 -*-
"""
Created on Thu Dec 19 10:04:56 2019

@author: berka
"""

from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

df = pd.read_csv("data.csv",sep = ';')

# %% 

x = df.iloc[:,[0,2]].values
y = df.maas.values.reshape(-1,1)

ml_lin_reg = LinearRegression()
ml_lin_reg.fit(x,y)

# prediction
print("b0 : ",ml_lin_reg.intercept_)
print('b1, b2 : ',ml_lin_reg.coef_)
ml_lin_reg.predict([[10,35],[5,35]])

array = np.arange(1,51,1).reshape(-1,1)

plt.scatter(df.deneyim, y,color = 'orange')
plt.scatter(df.yas, y,color = 'blue')
plt.plot(x,ml_lin_reg.predict(x))
plt.show()