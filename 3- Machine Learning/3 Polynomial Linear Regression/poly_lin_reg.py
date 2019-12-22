# -*- coding: utf-8 -*-
"""
Created on Sat Dec 21 09:46:04 2019

@author: berka
"""

from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

df = pd.read_csv('data.csv', sep=';')
# %%
# linear
x = df.araba_fiyat.values.reshape(-1,1)
y = df.araba_max_hiz.values.reshape(-1,1)
plt.scatter(x,y)
plt.xlabel('Cost')
plt.ylabel('Max_Speed')
plt.show()

lr = LinearRegression()
lr.fit(x,y)

y_head = lr.predict(x)

plt.plot(x,y_head, color='blue', label='linear')
plt.show()
# %%
# polynomial linear regression> y = b0 + b1*x + b2 * x^2 +..+ bn * x^n

poly = PolynomialFeatures(degree = 4)
x_poly = poly.fit_transform(x)

t = poly.fit_transform([[1000]]) # predict for example
lr2.predict(t)

lr2 = LinearRegression()
lr2.fit(x_poly, y)

plt.plot(x, lr2.predict(x_poly), color='green', label='polynomial')
plt.legend()
plt.show()