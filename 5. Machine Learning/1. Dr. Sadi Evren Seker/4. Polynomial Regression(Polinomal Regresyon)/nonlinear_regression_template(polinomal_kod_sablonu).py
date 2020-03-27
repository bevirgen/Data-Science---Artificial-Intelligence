import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

#veri yukleme

veri = pd.read_csv('maaslar.csv')

#dataframe dilimleme(slice)

edlv=veri.iloc[:,1:2]
slry=veri.iloc[:,2:]

#pandastan > numpye çevirme

Edlv=edlv.values
Slry=slry.values

#linear regression - dogrusal model olusturma

from sklearn.linear_model import LinearRegression
lr=LinearRegression()
lr.fit(Edlv,Slry)



#polynomial regression - nonlinear(dogrusal olmayan) model olusturma

from sklearn.preprocessing import PolynomialFeatures
lr2=LinearRegression()
pl=PolynomialFeatures(degree=5) #bu tabloda dereceyi artırdıkça başarı arttı

edlvpoly=pl.fit_transform(Edlv)
lr2.fit(edlvpoly,slry)

#data visualization - veriyi gorsellestirme

    #poly
plt.scatter(Edlv,Slry,color="red")
plt.plot(Edlv,lr2.predict(edlvpoly),color="blue")
plt.show()

    #linear
plt.scatter(Edlv,Slry,color="red") #veriyi görselleştir (noktaları çıkarır)
plt.plot(edlv,lr.predict(Edlv),color="blue") #doğruyu çıkarır
plt.show()

#tahminler

print(lr.predict([[11]]))
print(lr.predict([[6.5]]))


print(lr2.predict(pl.fit_transform([[11]])))
print(lr2.predict(pl.fit_transform([[6.9]])))






