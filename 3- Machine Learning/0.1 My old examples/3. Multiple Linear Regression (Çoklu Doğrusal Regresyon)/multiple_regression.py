import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

#veri on isleme

veri = pd.read_csv('veriler.csv')
boy = veri[['boy']]
boykilo = veri[['boy','kilo']]


#kategorik veriler
    #LabelEncoder > Verilen metinleri sayıya çevirir
    #OneHotEncoder > Etiketi kolon başlığına çevirir ardından
      #kolon altında olma durumunu 1 (değilse 0) ile yorumlar
      
from sklearn.preprocessing import LabelEncoder , OneHotEncoder

ulke = veri.iloc[:,0:1].values
print(ulke)
le = LabelEncoder()
ohe = OneHotEncoder(categorical_features = "all")
ulke[:,0] = le.fit_transform(ulke[:,0])
print(ulke)
ulke = ohe.fit_transform(ulke).toarray()
print(ulke)

c = veri.iloc[:,-1:].values
c[:,0]=le.fit_transform(c[:,0])
c=ohe.fit_transform(c).toarray()

#verilerin birleştirilmesi ve dataframe oluşturulması
    #dataframe > veriyi düzenleme
    #concat > düzenlediğimiz verileri birleştirme
    #axise 1 vermemizin sebebi birleştirmek istediğimiz verileri satır bazlı birleştirmek
    
sonuc = pd.DataFrame(data = ulke, index = range(22), columns=["fr","tr","us"])
print(sonuc)
sonuc2 = pd.DataFrame(data = Yas, index = range(22), columns=["boy","kilo","yas"])
print(sonuc2)
sonuc3 = pd.DataFrame(data = c[:,:1], index = range(22), columns=["cinsiyet"])
print(sonuc3)

s = pd.concat([sonuc,sonuc2,sonuc3],axis=1)
print(s)

#veri kümesinin eğitim ve test olarak bölünmesi
    #x_train > ana verinin büyük kısmı(öğrenme yapmasını istediğimiz kısım)
    #x_test > kalan gerçek kısım(karşılaştırma için)
    #y_train > büyük kısım tahmin
    #y_test > kalan kısım tahmin
    #random state 0 olmasının sebebi verilerin rastgele öğrenimi için
    #kodun açıklaması : xtraini al, ytraini tahmin etmeyi öğren, xtesti al ytesti tahmin et
     
#coklu regresyon islemleri
    
from sklearn.model_selection import train_test_split
x_train, x_test,y_train,y_test = train_test_split(s,sonuc3,test_size=0.33, random_state=0)

    
for column in x_train.columns:
    if x_train[column].dtype==type(object):
        x_train[column]=le.fit_transform(x_train[column])

for column in x_test.columns:
    if x_test[column].dtype==type(object):
        x_test[column]=le.fit_transform(x_test[column])

from sklearn.linear_model import LinearRegression
#cinsiyet tahmin

lr=LinearRegression()
lr.fit(x_train,y_train)
cthm=lr.predict(x_test)

#boy tahmin

boy=s.iloc[:,3:4].values
sol=s.iloc[:,:3]
sag=s.iloc[:,4:]
btt=pd.concat([sol,sag],axis=1)

x_train, x_test,y_train,y_test = train_test_split(btt,boy,test_size=0.33, random_state=0)

lr2=LinearRegression()
lr2.fit(x_train,y_train)
bthm=lr2.predict(x_test)