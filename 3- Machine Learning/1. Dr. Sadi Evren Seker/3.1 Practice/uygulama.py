import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

#veri on isleme
from sklearn.preprocessing import LabelEncoder, OneHotEncoder

veri = pd.read_csv('odev_tenis.csv')
veri2=veri.apply(LabelEncoder().fit_transform) #tüm tabloyu LabelEncode etmek

ohe=OneHotEncoder(categorical_features="all")
a = veri2.iloc[:,:1].values
a=ohe.fit_transform(a).toarray()


havadurumu = pd.DataFrame(data = a, index=range(14), columns=["Overcast","Rainy","Sunny"])
sontablo=pd.concat([havadurumu,veri.iloc[:,1:3],veri2.iloc[:,-2:]],axis=1)

#temp predict

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

temp=sontablo.iloc[:,3:4]
sol=sontablo.iloc[:,:3]
sag=sontablo.iloc[:,4:]
tpt=pd.concat([sol,sag],axis=1)

x_train, x_test,y_train,y_test = train_test_split(tpt,temp,test_size=0.33, random_state=0)
lr=LinearRegression()
lr.fit(x_train,y_train)
temppred=lr.predict(x_test)
x_train=x_train.sort_index()
y_train=y_train.sort_index()
x_test=x_test.sort_index()
y_test=y_test.sort_index()
print(temppred)

#p value
    #tahmindeki hatalarımızın kontrolü için kullanılan algoritma
import statsmodels.formula.api as sm

X = np.append(arr = np.ones((14,1)).astype(int),values=tpt,axis=1) #14 tane 1 satırı içeren sütun ekle
X_l = tpt.iloc[:,[0,1,2,3,4,5]].values
r_ols = sm.OLS(endog=temp, exog=X_l) #p value kullandığımız satır
r=r_ols.fit()
print(r.summary())

X = np.append(arr = np.ones((14,1)).astype(int),values=tpt,axis=1)
X_l = tpt.iloc[:,[0,1,2,3]].values
r_ols = sm.OLS(endog=temp, exog=X_l)
r=r_ols.fit()
print(r.summary())

x_train=x_train.iloc[:,:-2]
x_test=x_test.iloc[:,:-2]
lr.fit(x_train,y_train)
temppred=lr.predict(x_test)
print(temppred)

X = np.append(arr = np.ones((14,1)).astype(int),values=tpt,axis=1)
X_l = tpt.iloc[:,[0,1,2]].values
r_ols = sm.OLS(endog=temp, exog=X_l)
r=r_ols.fit()
print(r.summary())

x_train=x_train.iloc[:,:-1]
x_test=x_test.iloc[:,:-1]
lr.fit(x_train,y_train)
temppred=lr.predict(x_test)
print(temppred)







