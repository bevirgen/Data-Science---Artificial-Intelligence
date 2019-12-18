import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.metrics import r2_score
import statsmodels.formula.api as sm


veri = pd.read_csv('maaslar_yeni.csv')

datas=veri.iloc[:,2:5]
slry=veri.iloc[:,5:]
Datas=datas.values
Slry=slry.values

print(veri.corr())
#corr kategorilerin birbiri arasındaki bağlantısını gösterir
    # önemli : bağımsız değişkenlerin birbiri arasındaki ilişkisini gösterir

from sklearn.linear_model import LinearRegression

lr=LinearRegression()
lr.fit(Datas,Slry)

ols = sm.OLS(lr.predict(Datas),Datas)
olsf=ols.fit()
print("lr ols")
print(olsf.summary())

from sklearn.preprocessing import PolynomialFeatures

pl=PolynomialFeatures(degree=5)
datas_poly=pl.fit_transform(Datas)

lr2=LinearRegression()
lr2.fit(datas_poly,slry)

ols2 = sm.OLS(lr2.predict(datas_poly),Datas)
olsf2=ols.fit()
print("poly ols")
print(olsf2.summary())


