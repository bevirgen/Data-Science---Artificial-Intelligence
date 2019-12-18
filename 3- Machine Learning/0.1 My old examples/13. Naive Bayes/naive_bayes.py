import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

#veri on isleme

veri = pd.read_csv('veriler.csv')

from sklearn.preprocessing import LabelEncoder , OneHotEncoder
le = LabelEncoder()
ohe = OneHotEncoder(categorical_features = "all")

ulke = veri.iloc[:,0:1].values
ulke[:,0] = le.fit_transform(ulke[:,0])
ulke = ohe.fit_transform(ulke).toarray()

ulkeler = pd.DataFrame(data = ulke, index = range(22), columns=["fr","tr","us"])
x = veri.iloc[:,1:4]
X = veri.iloc[:,1:4].values
y = veri.iloc[:,4:]
Y = veri.iloc[:,4:].values
s = pd.concat([ulkeler,x],axis=1)
S = s.values
# boy = veri.iloc[5:,1:2] 5.satırdan 5:,> 5.satırdan sonra - 1:2 veri tablosunun içinden 1.sütun için
print(s)
#veri kümesinin eğitim ve test olarak bölünmesi
    #x_train > ana verinin büyük kısmı(öğrenme yapmasını istediğimiz kısım)
    #x_test > kalan gerçek kısım(karşılaştırma için)
    #y_train > büyük kısım tahmin
    #y_test > kalan kısım tahmin
    #random state 0 olmasının sebebi verilerin rastgele öğrenimi için
    #kodun açıklaması : xtraini al, ytraini tahmin etmeyi öğren, xtesti al ytesti tahmin et
     
from sklearn.model_selection import train_test_split

x_train, x_test,y_train,y_test = train_test_split(S,Y,test_size=0.33, random_state=0)

"""
#sıralama

x_train=x_train.sort_index()
x_test=x_test.sort_index()
y_train=y_train.sort_index()
y_test=y_test.sort_index()

"""
#öznitelik ölçekleme
    #standardscaler > veriyi standartlaştır,standarda yakınlık oranını gösterir
    
from sklearn.preprocessing import StandardScaler

sc = StandardScaler()
X_train = sc.fit_transform(x_train)
X_test = sc.transform(x_test)

"""

#Eğer veri object kaldıysa

    for column in y_train.columns:
    if y_train[column].dtype==type(object):
        y_train[column]=le.fit_transform(y_train[column])

for column in y_test.columns:
    if y_test[column].dtype==type(object):
        y_test[column]=le.fit_transform(y_test[column])
        
"""

from sklearn.linear_model import LogisticRegression

logr=LogisticRegression(random_state=0)
logr.fit(X_train,y_train)

y_pred = logr.predict(X_test)
print("tahminler")
print("----------------")
print(y_pred)

#confusion matrix
    #tahmin-gerçekteki ilişkisini kurar örn: tahmin k gerçek e, tahmin k gerçek k gibi.
    
from sklearn.metrics import confusion_matrix

cm=confusion_matrix(y_test,y_pred)
print(cm)

#NaiveBayes
    #Gaussian , Bernoulli , Multinomial , Complement olarak çeşitleri vardır.
    #kullanılan NB yöntemleri başarıyı değiştirir.
    
from sklearn.naive_bayes import GaussianNB

gnb = GaussianNB()
gnb.fit(X_train,y_train)
y_pred = gnb.predict(X_test)

cm=confusion_matrix(y_test,y_pred)
print("GNB")
print(cm)

from sklearn.naive_bayes import BernoulliNB

bnb = BernoulliNB()
bnb.fit(X_train,y_train)
y_pred = bnb.predict(X_test)

cm = confusion_matrix(y_test,y_pred)
print("BNB")
print(cm)


from sklearn.naive_bayes import ComplementNB

cnb = ComplementNB()
cnb.fit(X_train,y_train)
y_pred = cnb.predict(X_test)

cm = confusion_matrix(y_test,y_pred)
print("CNB")
print(cm)














