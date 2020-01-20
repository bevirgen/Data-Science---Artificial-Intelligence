import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

from sklearn.preprocessing import LabelEncoder , OneHotEncoder

le = LabelEncoder()
ohe = OneHotEncoder(categorical_features = "all")

#veri on isleme


veri = pd.read_csv('eksikveriler.csv')
veri2=veri.apply(le.fit_transform) #tüm tabloyu LabelEncode etmek
boy = veri[['boy']]
boykilo = veri[['boy','kilo']]

class insan:
    boy=180
    def kosmak(self,b):
        return b+10

ali = insan()
print(ali.boy)
print(ali.kosmak(90))

#eksik veriler

    #sklearn sci-kit learn > bilimsel makine öğrenmesi
    #Import,imputation > eksik verilerin uygun bir şekilde doldurulması
    #iloc > veriyi almaya yarar
    #preprocessing > ön işleme
    #fit > istediğimizi uygulama
    #transform> istediğimizi içine yazdırma(dönüştürme)
    
from sklearn.preprocessing import Imputer 

imputer = Imputer(missing_values = "NaN", strategy = "mean", axis=0 )

Yas = veri.iloc[:,1:4]
print(Yas)
imputer = imputer.fit(Yas[:,1:4])
Yas[:,1:4] = imputer.transform(Yas[:,1:4])
print(Yas)

#kategorik veriler
    #LabelEncoder > Verilen metinleri sayıya çevirir
    #OneHotEncoder > Etiketi kolon başlığına çevirir ardından
      #kolon altında olma durumunu 1 (değilse 0) ile yorumlar

ulke = veri.iloc[:,0:1].values
print(ulke)
ulke[:,0] = le.fit_transform(ulke[:,0])
print(ulke)
ulke = ohe.fit_transform(ulke).toarray()
print(ulke)

#verilerin birleştirilmesi ve dataframe oluşturulması
    #dataframe > veriyi düzenleme
    #concat > düzenlediğimiz verileri birleştirme
    #axise 1 vermemizin sebebi birleştirmek istediğimiz verileri satır bazlı birleştirmek
    
sonuc = pd.DataFrame(data = ulke, index = range(22), columns=["fr","tr","us"])
print(sonuc)
sonuc2 = pd.DataFrame(data = Yas, index = range(22), columns=["boy","kilo","yas"])
print(sonuc2)

cinsiyet = veri.iloc[:,-1].values
print(cinsiyet)

sonuc3 = pd.DataFrame(data = cinsiyet, index = range(22), columns=["cinsiyet"])
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
     
from sklearn.model_selection import train_test_split
x_train, x_test,y_train,y_test = train_test_split(s,sonuc3,test_size=0.33, random_state=0)

#öznitelik ölçekleme
    #standardscaler > veriyi standartlaştır,standarda yakınlık oranını gösterir
    
for column in x_train.columns:
    if x_train[column].dtype==type(object):
        x_train[column]=le.fit_transform(x_train[column])

for column in x_test.columns:
    if x_test[column].dtype==type(object):
        x_test[column]=le.fit_transform(x_test[column])
        
from sklearn.preprocessing import StandardScaler

sc = StandardScaler()
X_train = sc.fit_transform(x_train)
X_test = sc.fit_transform(x_test)

#model inşası (doğrusal regresyon)
    #fit satırında x in içinden y yi öğrettik
    #predict satırında kalan kısmı tahmin ettirdik
    #sort ile sıralattık
    #plot ile tablo haline getirdik
    
from sklearn.linear_model import LinearRegression

lr=LinearRegression()
lr.fit(x_train,y_train)
thm = lr.predict(x_test)
x_train=x_train.sort_index()
y_train=y_train.sort_index()
plt.plot(x_train,y_train)
plt.plot(x_test,thm)
plt.title("Aylara Göre Satışlar")
plt.xlabel("Aylar")
plt.ylabel("Satışlar")







