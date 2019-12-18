import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

#veri on isleme

veri = pd.read_csv('satislar.csv')
print(veri)
aylar = veri[["Aylar"]]
satislar = veri[["Satislar"]]

#veri kümesinin eğitim ve test olarak bölünmesi
    #x_train > ana verinin büyük kısmı(öğrenme yapmasını istediğimiz kısım)
    #x_test > kalan gerçek kısım(karşılaştırma için)
    #y_train > büyük kısım tahmin
    #y_test > kalan kısım tahmin
    #random state 0 olmasının sebebi verilerin rastgele öğrenimi için
    #kodun açıklaması : xtraini al, ytraini tahmin etmeyi öğren, xtesti al ytesti tahmin et
     
from sklearn.model_selection import train_test_split
x_train, x_test,y_train,y_test = train_test_split(aylar,satislar,test_size=0.33, random_state=0)

#verilerin ölçeklenmesi
    #standardscaler > veriyi standartlaştır,standarda yakınlık oranını gösterir


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





