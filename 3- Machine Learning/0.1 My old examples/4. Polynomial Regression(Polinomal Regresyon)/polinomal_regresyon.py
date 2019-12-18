import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

#veri yukleme

veri = pd.read_csv('maaslar.csv')

#linear regression

from sklearn.linear_model import LinearRegression
lr=LinearRegression()

edlv=veri.iloc[:,1:2]
slry=veri.iloc[:,2:]
Edlv=edlv.values
Slry=slry.values
lr.fit(Edlv,Slry)
plt.scatter(Edlv,Slry,color="red") #veriyi görselleştir (noktaları çıkarır)
plt.plot(edlv,lr.predict(Edlv),color="blue") #doğruyu çıkarır
plt.show()

#polynomial regression

from sklearn.preprocessing import PolynomialFeatures
lr2=LinearRegression()
pl=PolynomialFeatures(degree=5) #bu tabloda dereceyi artırdıkça başarı arttı

edlvpoly=pl.fit_transform(Edlv)
lr2.fit(edlvpoly,slry)
plt.scatter(Edlv,Slry,color="red")
plt.plot(Edlv,lr2.predict(edlvpoly),color="blue")
plt.show()

#tahminler

print(lr.predict([[11]]))
print(lr.predict([[6.5]]))


print(lr2.predict(pl.fit_transform([[11]])))
print(lr2.predict(pl.fit_transform([[6.9]])))





