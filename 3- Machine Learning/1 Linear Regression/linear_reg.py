# -*- coding: utf-8 -*-
"""
Created on Thu Dec 19 10:04:56 2019

@author: berka
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import r2_score
from sklearn.linear_model import LinearRegression # library for ML

df = pd.read_csv("data.csv",sep = ';')

plt.scatter(df.deneyim,df.maas)
plt.xlabel('deneyim')
plt.ylabel('maas')
plt.show()
# %% 
# linear regression > y = b0 + b1*x
lin_reg = LinearRegression()

x = df.deneyim.values.reshape(-1,1)
y = df.maas.values.reshape(-1,1)

lin_reg.fit(x,y)

# prediction

"""b0 = lin_reg.predict([[0]])
print("b0 : ",b0)"""

b0_ = lin_reg.intercept_ # (intercept) it's for determine b0
print("b0 : ",b0_)
b1 = lin_reg.coef_ #slope
print('b1 : ',b1)
salaryManuelPredict = 1663 + 1138*20
print("You'll get this for 20 years experience",salaryManuelPredict)
print(lin_reg.predict([[20]])) # same thing above line

array = np.arange(1,51,1).reshape(-1,1)

plt.scatter(array, lin_reg.predict(array), color='orange')
plt.plot(array,lin_reg.predict(array), color='blue')
plt.show()

print('r2_square_score',r2_score(y,lin_reg.predict(array)))