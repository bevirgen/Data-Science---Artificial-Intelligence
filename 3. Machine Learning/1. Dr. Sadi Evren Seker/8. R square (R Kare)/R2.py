import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.metrics import r2_score

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

plt.scatter(Edlv,Slry,color="red")
plt.plot(Edlv,lr2.predict(edlvpoly),color="blue")
plt.show()

plt.scatter(Edlv,Slry,color="red") #veriyi görselleştir (noktaları çıkarır)
plt.plot(edlv,lr.predict(Edlv),color="blue") #doğruyu çıkarır
plt.show()

#tahminler linear ve polynomial

print(lr.predict([[11]]))
print(lr.predict([[6.5]]))
print("Linear Vector R2 Degeri")
print(r2_score(Slry,lr.predict(Edlv)))


print(lr2.predict(pl.fit_transform([[11]])))
print(lr2.predict(pl.fit_transform([[6.9]])))

print("Polynomial R2 Degeri")
print(r2_score(Slry,lr2.predict(pl.fit_transform(Edlv))))
#support vector regression

from sklearn.preprocessing import StandardScaler

sc1=StandardScaler()
sc2=StandardScaler()
edscaled=sc1.fit_transform(Edlv)
slscaled=sc2.fit_transform(Slry)

from sklearn.svm import SVR

svr=SVR(kernel="rbf")
svr.fit(edscaled,slscaled)

plt.scatter(edscaled,slscaled,color="red")
plt.plot(edscaled,svr.predict(edscaled),color="blue")
plt.show() #bu tablonun sonuna geldiğini ifade eder

print(svr.predict([[11]]))
print(svr.predict([[7]]))
print("Support Vector R2 Degeri")
print(r2_score(slscaled,svr.predict(edscaled)))

# decision tree regressor
#predict edilirken, 10 dan yukarısına her zaman 50bin,aşağısına en yakın değer verilir
#karar ağacı ona verilen verilerle eleme yaptığı için, o aralıkların dışına çıkamaz

from sklearn.tree import DecisionTreeRegressor

dtr=DecisionTreeRegressor(random_state=0)
dtr.fit(Edlv,Slry)
plt.scatter(Edlv,Slry,color="red")
plt.plot(edlv,dtr.predict(Edlv),color="blue")
plt.show()

print(dtr.predict([[6.6]]))
print("Decision Tree R2 Degeri")
print(r2_score(Slry,dtr.predict(Edlv)))

#random forest 
    #estimators , kaç adet karar ağacı uygulanacağının sayısıdır

from sklearn.ensemble import RandomForestRegressor

rfr=RandomForestRegressor(n_estimators=10, random_state=0)
rfr.fit(Edlv,Slry)

print(dtr.predict([[6.6]]))

plt.scatter(Edlv,Slry,color="red")
plt.plot(edlv,rfr.predict(Edlv),color="blue")
plt.show()

#R2 yöntemi
    # print(r2_score(Slry,rfr.predict(Edlv))) -> r2, y den x alınarak bulunur
from sklearn.metrics import r2_score

print("Random Forest R2 Degeri")
print(r2_score(Slry,rfr.predict(Edlv)))








